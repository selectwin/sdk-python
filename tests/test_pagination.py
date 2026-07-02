import pytest

from selectwin.pagination import AsyncPager, SyncPager


class Page:
    """Minimal stand-in for a generated list page model."""

    def __init__(self, data, has_more):
        self.data = data
        self.has_more = has_more


def make_pages():
    return [Page([1, 2], True), Page([3, 4], True), Page([5], False)]


def test_sync_first_returns_first_page():
    pages = make_pages()
    pager = SyncPager(lambda **p: pages[0], {"limit": 2})
    first = pager.first()
    assert first.data == [1, 2]
    assert first.has_more is True


def test_sync_iterates_every_item_and_advances_offset():
    pages = make_pages()
    seen_offsets = []

    def fetch(**p):
        seen_offsets.append(p.get("offset"))
        return pages[len(seen_offsets) - 1]

    pager = SyncPager(fetch, {"limit": 2})
    assert list(pager) == [1, 2, 3, 4, 5]
    assert seen_offsets == [0, 2, 4]


def test_sync_to_list_honours_cap():
    pages = make_pages()
    calls = {"n": 0}

    def fetch(**p):
        page = pages[calls["n"]]
        calls["n"] += 1
        return page

    assert SyncPager(fetch, {"limit": 2}).to_list(max=3) == [1, 2, 3]


def test_sync_stops_on_empty_page_even_if_has_more():
    pager = SyncPager(lambda **p: Page([], True), {})
    assert list(pager) == []


@pytest.mark.asyncio
async def test_async_iterates_every_item():
    pages = make_pages()
    calls = {"n": 0}

    async def fetch(**p):
        page = pages[calls["n"]]
        calls["n"] += 1
        return page

    pager = AsyncPager(fetch, {"limit": 2})
    out = [item async for item in pager]
    assert out == [1, 2, 3, 4, 5]


@pytest.mark.asyncio
async def test_async_first_and_to_list_cap():
    pages = make_pages()

    async def first_fetch(**p):
        return pages[0]

    assert (await AsyncPager(first_fetch, {}).first()).data == [1, 2]

    calls = {"n": 0}

    async def fetch(**p):
        page = pages[calls["n"]]
        calls["n"] += 1
        return page

    assert await AsyncPager(fetch, {"limit": 2}).to_list(max=2) == [1, 2]
