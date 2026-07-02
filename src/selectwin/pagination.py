"""Auto-pagination over the API's list envelope (``{data, hasMore, offset, ...}``).

Works over the generated page models by reading ``.data`` and ``.has_more`` (the
snake_case attributes openapi-python-client produces), so it is model-agnostic.
"""

from __future__ import annotations

from typing import (
    Any,
    AsyncIterator,
    Awaitable,
    Callable,
    Generic,
    Iterator,
    List,
    Optional,
    TypeVar,
)

Item = TypeVar("Item")
Page = TypeVar("Page")

_DEFAULT_LIMIT = 20


def _page_items(page: Any) -> list:
    data = getattr(page, "data", None)
    if data is None and isinstance(page, dict):
        data = page.get("data")
    return list(data) if data else []


def _page_has_more(page: Any) -> bool:
    has_more = getattr(page, "has_more", None)
    if has_more is None and isinstance(page, dict):
        has_more = page.get("hasMore", page.get("has_more"))
    return bool(has_more)


class SyncPager(Generic[Item, Page]):
    """Return value of a sync ``list()``:

    - ``pager.first()``            -> the first page object (``{data, has_more, ...}``)
    - ``for item in pager``        -> iterate every item across all pages
    - ``pager.pages()``            -> iterate page objects
    - ``pager.to_list(max=None)``  -> collect items into a list (optionally capped)
    """

    def __init__(
        self,
        fetch_page: Callable[..., Page],
        params: Optional[dict] = None,
    ) -> None:
        self._fetch_page = fetch_page
        self._params = dict(params or {})

    def first(self) -> Page:
        return self._fetch_page(**self._params)

    def pages(self) -> Iterator[Page]:
        offset = self._params.get("offset", 0) or 0
        limit = self._params.get("limit", _DEFAULT_LIMIT) or _DEFAULT_LIMIT
        while True:
            page = self._fetch_page(**{**self._params, "offset": offset, "limit": limit})
            yield page
            items = _page_items(page)
            if not _page_has_more(page) or not items:
                return
            offset += len(items)

    def __iter__(self) -> Iterator[Item]:
        for page in self.pages():
            for item in _page_items(page):
                yield item

    def to_list(self, max: Optional[int] = None) -> List[Item]:
        out: List[Item] = []
        for item in self:
            out.append(item)
            if max is not None and len(out) >= max:
                break
        return out


class AsyncPager(Generic[Item, Page]):
    """Async counterpart of :class:`SyncPager`:

    - ``await pager.first()``
    - ``async for item in pager``
    - ``pager.pages()`` (async iterator)
    - ``await pager.to_list(max=None)``
    """

    def __init__(
        self,
        fetch_page: Callable[..., Awaitable[Page]],
        params: Optional[dict] = None,
    ) -> None:
        self._fetch_page = fetch_page
        self._params = dict(params or {})

    async def first(self) -> Page:
        return await self._fetch_page(**self._params)

    async def pages(self) -> AsyncIterator[Page]:
        offset = self._params.get("offset", 0) or 0
        limit = self._params.get("limit", _DEFAULT_LIMIT) or _DEFAULT_LIMIT
        while True:
            page = await self._fetch_page(**{**self._params, "offset": offset, "limit": limit})
            yield page
            items = _page_items(page)
            if not _page_has_more(page) or not items:
                return
            offset += len(items)

    async def __aiter__(self) -> AsyncIterator[Item]:
        async for page in self.pages():
            for item in _page_items(page):
                yield item

    async def to_list(self, max: Optional[int] = None) -> List[Item]:
        out: List[Item] = []
        async for item in self:
            out.append(item)
            if max is not None and len(out) >= max:
                break
        return out
