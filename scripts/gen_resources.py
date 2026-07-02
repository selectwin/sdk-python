"""Generate src/selectwin/resources.py — Sync + async namespaces.

Parses each generated op module (``_core/api/<tag>/<op>.py``) for its ``sync``
signature, derives a friendly alias (get->retrieve, strip the resource noun),
classifies the shape (paginated list / create-body / id / id+body / passthrough)
and emits one sync class + one async class per tag, delegating to the generated
``.sync`` / ``.asyncio`` functions with the shared client bound.

Run: python scripts/gen_resources.py   (after scripts/sync_core.py)
"""

from __future__ import annotations

import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
API_DIR = REPO / "src" / "selectwin" / "_core" / "api"
OUT = REPO / "src" / "selectwin" / "resources.py"

VERB_ALIAS = {"get": "retrieve"}
RESERVED = {"raw", "client"}
# Friendly attribute names on the client for a few tags.
ATTR_OVERRIDE = {"products_variants": "variants"}


def singular(w: str) -> str:
    return w[:-1] if w.endswith("s") else w


def pascal(tag: str) -> str:
    return "".join(part.capitalize() for part in tag.split("_"))


def derive_alias(op: str, noun_words: set) -> str:
    words = op.split("_")
    if not words:
        return op
    verb = VERB_ALIAS.get(words[0], words[0])
    rest = [w for w in words[1:] if w.lower() not in noun_words and singular(w.lower()) not in noun_words]
    return "_".join([verb] + rest) or verb


def parse_sync_params(src: str):
    m = re.search(r"\ndef sync\(\n(.*?)\n\) ->", src, re.DOTALL)
    if not m:
        return None
    params = []
    for raw in m.group(1).split("\n"):
        line = raw.strip().rstrip(",")
        if not line or line.startswith("*") or line.startswith("client:"):
            continue
        mm = re.match(r"^([A-Za-z_]\w*)\s*:\s*(.+)$", line)
        if not mm:
            continue
        name, rest = mm.group(1), mm.group(2)
        if "=" in rest:
            ann = rest.split("=", 1)[0].strip()
            required = False
        else:
            ann = rest.strip()
            required = True
        params.append((name, ann, required))
    return params


def body_model(ann: str):
    for tok in re.split(r"[|\[\], ]+", ann or ""):
        if re.match(r"^[A-Z]\w+$", tok) and tok not in ("Unset", "Any", "None"):
            return tok
    return None


def classify(params):
    required = [p for p in params if p[2]]
    names = {p[0] for p in params}
    has_paging = "offset" in names and "limit" in names
    ids = [p for p in required if p[0].endswith("_id") and p[1].strip() == "str"]
    bodies = [p for p in required if p[0] == "body"]
    any_body = next((p[1] for p in params if p[0] == "body"), None)
    if has_paging and not required:
        return {"kind": "list"}
    if len(required) == 1 and bodies:
        return {"kind": "body", "model": body_model(bodies[0][1])}
    if len(required) == 1 and len(ids) == 1:
        return {"kind": "id", "id": ids[0][0]}
    if len(required) == 2 and len(ids) == 1 and len(bodies) == 1:
        return {"kind": "id_body", "id": ids[0][0], "model": body_model(bodies[0][1])}
    return {"kind": "passthrough", "model": body_model(any_body) if any_body else None}


def emit_method(alias, opref, shape, is_async):
    d = "async def" if is_async else "def"
    aw = "await " if is_async else ""
    caller = "acall" if is_async else "call"
    fn = f"{opref}.asyncio" if is_async else f"{opref}.sync"
    Pager = "AsyncPager" if is_async else "SyncPager"
    kind = shape["kind"]
    if kind == "list":
        # The pager fetch binds the client; call/acall normalises transport errors.
        lam = f"lambda **p: {caller}({fn}, client=self._c, **p)"
        return [
            f"    def {alias}(self, **params):",
            f'        """`{opref.split(".")[-1]}` — paginated ({("async" if is_async else "sync")})."""',
            f"        return {Pager}({lam}, params)",
        ]
    if kind == "body":
        return [
            f"    {d} {alias}(self, body):",
            f"        return {aw}{caller}({fn}, client=self._c, body=as_model(body, {shape['model']}))",
        ]
    if kind == "id":
        return [
            f"    {d} {alias}(self, id):",
            f"        return {aw}{caller}({fn}, client=self._c, {shape['id']}=id)",
        ]
    if kind == "id_body":
        return [
            f"    {d} {alias}(self, id, body):",
            f"        return {aw}{caller}({fn}, client=self._c, {shape['id']}=id, body=as_model(body, {shape['model']}))",
        ]
    # passthrough
    lines = [f"    {d} {alias}(self, **kwargs):"]
    if shape.get("model"):
        lines.append('        if isinstance(kwargs.get("body"), dict):')
        lines.append(f"            kwargs['body'] = as_model(kwargs['body'], {shape['model']})")
    lines.append(f"        return {aw}{caller}({fn}, client=self._c, **kwargs)")
    return lines


def main() -> None:
    tags = sorted(p.name for p in API_DIR.iterdir() if p.is_dir() and p.name != "__pycache__")
    op_imports = {}   # import-alias -> (tag, op)
    model_imports = set()
    tag_imports = []  # tag names
    sync_classes, async_classes, registry = [], [], []
    total_ops = 0

    for tag in tags:
        tag_dir = API_DIR / tag
        ops = sorted(f.stem for f in tag_dir.glob("*.py") if f.stem != "__init__")
        if not ops:
            continue
        noun_words = set()
        for w in tag.split("_"):
            noun_words.add(w.lower())
            noun_words.add(singular(w.lower()))

        tag_imports.append(tag)
        sync_methods, async_methods = [], []
        used = {}
        for op in ops:
            src = (tag_dir / op).with_suffix(".py").read_text(encoding="utf-8")
            params = parse_sync_params(src)
            if params is None:
                continue
            total_ops += 1
            alias = derive_alias(op, noun_words)
            if alias in RESERVED or (alias in used and used[alias] != op):
                alias = op  # collision / reserved -> fall back to the raw op name
            used[alias] = op
            shape = classify(params)
            if shape.get("model"):
                model_imports.add(shape["model"])
            opref = f"_op_{tag}__{op}"
            op_imports[opref] = (tag, op)
            sync_methods += emit_method(alias, opref, shape, is_async=False) + [""]
            async_methods += emit_method(alias, opref, shape, is_async=True) + [""]

        cls = pascal(tag)
        header = [
            f"class {cls}Namespace:",
            f"    raw = _tag_{tag}",
            "    def __init__(self, client):",
            "        self._c = client",
            "    @property",
            "    def client(self):",
            "        return self._c",
            "",
        ]
        aheader = [
            f"class Async{cls}Namespace:",
            f"    raw = _tag_{tag}",
            "    def __init__(self, client):",
            "        self._c = client",
            "    @property",
            "    def client(self):",
            "        return self._c",
            "",
        ]
        sync_classes.append("\n".join(header + sync_methods))
        async_classes.append("\n".join(aheader + async_methods))
        attr = ATTR_OVERRIDE.get(tag, tag)
        registry.append((attr, f"{cls}Namespace", f"Async{cls}Namespace"))

    # Assemble imports.
    lines = [
        '"""GENERATED by scripts/gen_resources.py — DO NOT EDIT.',
        "",
        "Sync + async resource namespaces delegating to the generated core.",
        "Regenerate after scripts/sync_core.py with scripts/gen_resources.py.",
        '"""',
        "# ruff: noqa",
        "from __future__ import annotations",
        "",
        "from .pagination import SyncPager, AsyncPager",
        "from ._support import call, acall, as_model",
    ]
    for tag in tag_imports:
        lines.append(f"from ._core.api import {tag} as _tag_{tag}")
    for opref, (tag, op) in sorted(op_imports.items()):
        lines.append(f"from ._core.api.{tag} import {op} as {opref}")
    if model_imports:
        lines.append("from ._core.models import (")
        for m in sorted(model_imports):
            lines.append(f"    {m},")
        lines.append(")")
    lines.append("")
    lines.append("")
    lines.append("\n\n".join(sync_classes))
    lines.append("")
    lines.append("\n\n".join(async_classes))
    lines.append("")
    lines.append("#: (attribute, sync namespace class, async namespace class) for each resource.")
    lines.append("NAMESPACES = [")
    for attr, sc, ac in registry:
        lines.append(f"    ({attr!r}, {sc}, {ac}),")
    lines.append("]")
    lines.append("")

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(
        f"wrote {OUT.relative_to(REPO)} — {len(registry)} resources, {total_ops} ops, "
        f"{len(model_imports)} body models"
    )


if __name__ == "__main__":
    main()
