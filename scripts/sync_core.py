"""Copy the generated openapi-python-client core into src/selectwin/_core.

Source: selectwin-sdks/sdks/python-httpx (override with SELECTWIN_SDKS). The core
is committed (it's the vendored generated layer); the DX shell in src/selectwin
wraps it. Run scripts/gen_resources.py + scripts/gen_webhook_events.py after this.

Run: python scripts/sync_core.py
"""

from __future__ import annotations

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
DEST = REPO / "src" / "selectwin" / "_core"

sdks = os.environ.get("SELECTWIN_SDKS")
default = REPO.parent / "selectwin-sdks"
SRC = (Path(sdks) if sdks else default) / "sdks" / "python-httpx"


def main() -> None:
    if not SRC.is_dir():
        raise SystemExit(f"generated core not found: {SRC} (set SELECTWIN_SDKS)")
    if DEST.exists():
        shutil.rmtree(DEST)
    # Copy the package contents into _core (skip caches).
    shutil.copytree(SRC, DEST, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    # openapi-python-client marks the package typed; make sure it stays typed.
    (DEST / "py.typed").touch(exist_ok=True)
    n = sum(1 for _ in DEST.rglob("*.py"))
    print(f"synced core -> {DEST.relative_to(REPO)} ({n} .py files)")


if __name__ == "__main__":
    main()
