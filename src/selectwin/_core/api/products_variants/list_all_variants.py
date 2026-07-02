import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_all_variants_response_200_item import ListAllVariantsResponse200Item
from ...models.list_all_variants_sort import ListAllVariantsSort
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 999999,
    offset: int | Unset = 0,
    sort: ListAllVariantsSort | Unset = ListAllVariantsSort.ASCENDING,
    daterange: datetime.datetime | str | Unset = UNSET,
    daterangegt: datetime.datetime | Unset = UNSET,
    daterangegte: datetime.datetime | Unset = UNSET,
    daterangelt: datetime.datetime | Unset = UNSET,
    daterangelte: datetime.datetime | Unset = UNSET,
    id: str | Unset = UNSET,
    sku: str | Unset = UNSET,
    currency: str | Unset = UNSET,
    enabled: bool | Unset = UNSET,
    product_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

    json_daterange: str | Unset
    if isinstance(daterange, Unset):
        json_daterange = UNSET
    elif isinstance(daterange, datetime.datetime):
        json_daterange = daterange.isoformat()
    else:
        json_daterange = daterange
    params["daterange"] = json_daterange

    json_daterangegt: str | Unset = UNSET
    if not isinstance(daterangegt, Unset):
        json_daterangegt = daterangegt.isoformat()
    params["daterangegt"] = json_daterangegt

    json_daterangegte: str | Unset = UNSET
    if not isinstance(daterangegte, Unset):
        json_daterangegte = daterangegte.isoformat()
    params["daterangegte"] = json_daterangegte

    json_daterangelt: str | Unset = UNSET
    if not isinstance(daterangelt, Unset):
        json_daterangelt = daterangelt.isoformat()
    params["daterangelt"] = json_daterangelt

    json_daterangelte: str | Unset = UNSET
    if not isinstance(daterangelte, Unset):
        json_daterangelte = daterangelte.isoformat()
    params["daterangelte"] = json_daterangelte

    params["id"] = id

    params["sku"] = sku

    params["currency"] = currency

    params["enabled"] = enabled

    params["productId"] = product_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/variants",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[ListAllVariantsResponse200Item] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ListAllVariantsResponse200Item.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[ListAllVariantsResponse200Item]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 999999,
    offset: int | Unset = 0,
    sort: ListAllVariantsSort | Unset = ListAllVariantsSort.ASCENDING,
    daterange: datetime.datetime | str | Unset = UNSET,
    daterangegt: datetime.datetime | Unset = UNSET,
    daterangegte: datetime.datetime | Unset = UNSET,
    daterangelt: datetime.datetime | Unset = UNSET,
    daterangelte: datetime.datetime | Unset = UNSET,
    id: str | Unset = UNSET,
    sku: str | Unset = UNSET,
    currency: str | Unset = UNSET,
    enabled: bool | Unset = UNSET,
    product_id: str | Unset = UNSET,
) -> Response[list[ListAllVariantsResponse200Item]]:
    """List all product variants

    Args:
        limit (int | Unset):  Default: 999999.
        offset (int | Unset):  Default: 0.
        sort (ListAllVariantsSort | Unset):  Default: ListAllVariantsSort.ASCENDING.
        daterange (datetime.datetime | str | Unset):
        daterangegt (datetime.datetime | Unset):
        daterangegte (datetime.datetime | Unset):
        daterangelt (datetime.datetime | Unset):
        daterangelte (datetime.datetime | Unset):
        id (str | Unset):
        sku (str | Unset):
        currency (str | Unset):
        enabled (bool | Unset):
        product_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ListAllVariantsResponse200Item]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        sort=sort,
        daterange=daterange,
        daterangegt=daterangegt,
        daterangegte=daterangegte,
        daterangelt=daterangelt,
        daterangelte=daterangelte,
        id=id,
        sku=sku,
        currency=currency,
        enabled=enabled,
        product_id=product_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 999999,
    offset: int | Unset = 0,
    sort: ListAllVariantsSort | Unset = ListAllVariantsSort.ASCENDING,
    daterange: datetime.datetime | str | Unset = UNSET,
    daterangegt: datetime.datetime | Unset = UNSET,
    daterangegte: datetime.datetime | Unset = UNSET,
    daterangelt: datetime.datetime | Unset = UNSET,
    daterangelte: datetime.datetime | Unset = UNSET,
    id: str | Unset = UNSET,
    sku: str | Unset = UNSET,
    currency: str | Unset = UNSET,
    enabled: bool | Unset = UNSET,
    product_id: str | Unset = UNSET,
) -> list[ListAllVariantsResponse200Item] | None:
    """List all product variants

    Args:
        limit (int | Unset):  Default: 999999.
        offset (int | Unset):  Default: 0.
        sort (ListAllVariantsSort | Unset):  Default: ListAllVariantsSort.ASCENDING.
        daterange (datetime.datetime | str | Unset):
        daterangegt (datetime.datetime | Unset):
        daterangegte (datetime.datetime | Unset):
        daterangelt (datetime.datetime | Unset):
        daterangelte (datetime.datetime | Unset):
        id (str | Unset):
        sku (str | Unset):
        currency (str | Unset):
        enabled (bool | Unset):
        product_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ListAllVariantsResponse200Item]
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        sort=sort,
        daterange=daterange,
        daterangegt=daterangegt,
        daterangegte=daterangegte,
        daterangelt=daterangelt,
        daterangelte=daterangelte,
        id=id,
        sku=sku,
        currency=currency,
        enabled=enabled,
        product_id=product_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 999999,
    offset: int | Unset = 0,
    sort: ListAllVariantsSort | Unset = ListAllVariantsSort.ASCENDING,
    daterange: datetime.datetime | str | Unset = UNSET,
    daterangegt: datetime.datetime | Unset = UNSET,
    daterangegte: datetime.datetime | Unset = UNSET,
    daterangelt: datetime.datetime | Unset = UNSET,
    daterangelte: datetime.datetime | Unset = UNSET,
    id: str | Unset = UNSET,
    sku: str | Unset = UNSET,
    currency: str | Unset = UNSET,
    enabled: bool | Unset = UNSET,
    product_id: str | Unset = UNSET,
) -> Response[list[ListAllVariantsResponse200Item]]:
    """List all product variants

    Args:
        limit (int | Unset):  Default: 999999.
        offset (int | Unset):  Default: 0.
        sort (ListAllVariantsSort | Unset):  Default: ListAllVariantsSort.ASCENDING.
        daterange (datetime.datetime | str | Unset):
        daterangegt (datetime.datetime | Unset):
        daterangegte (datetime.datetime | Unset):
        daterangelt (datetime.datetime | Unset):
        daterangelte (datetime.datetime | Unset):
        id (str | Unset):
        sku (str | Unset):
        currency (str | Unset):
        enabled (bool | Unset):
        product_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ListAllVariantsResponse200Item]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        sort=sort,
        daterange=daterange,
        daterangegt=daterangegt,
        daterangegte=daterangegte,
        daterangelt=daterangelt,
        daterangelte=daterangelte,
        id=id,
        sku=sku,
        currency=currency,
        enabled=enabled,
        product_id=product_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 999999,
    offset: int | Unset = 0,
    sort: ListAllVariantsSort | Unset = ListAllVariantsSort.ASCENDING,
    daterange: datetime.datetime | str | Unset = UNSET,
    daterangegt: datetime.datetime | Unset = UNSET,
    daterangegte: datetime.datetime | Unset = UNSET,
    daterangelt: datetime.datetime | Unset = UNSET,
    daterangelte: datetime.datetime | Unset = UNSET,
    id: str | Unset = UNSET,
    sku: str | Unset = UNSET,
    currency: str | Unset = UNSET,
    enabled: bool | Unset = UNSET,
    product_id: str | Unset = UNSET,
) -> list[ListAllVariantsResponse200Item] | None:
    """List all product variants

    Args:
        limit (int | Unset):  Default: 999999.
        offset (int | Unset):  Default: 0.
        sort (ListAllVariantsSort | Unset):  Default: ListAllVariantsSort.ASCENDING.
        daterange (datetime.datetime | str | Unset):
        daterangegt (datetime.datetime | Unset):
        daterangegte (datetime.datetime | Unset):
        daterangelt (datetime.datetime | Unset):
        daterangelte (datetime.datetime | Unset):
        id (str | Unset):
        sku (str | Unset):
        currency (str | Unset):
        enabled (bool | Unset):
        product_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ListAllVariantsResponse200Item]
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            sort=sort,
            daterange=daterange,
            daterangegt=daterangegt,
            daterangegte=daterangegte,
            daterangelt=daterangelt,
            daterangelte=daterangelte,
            id=id,
            sku=sku,
            currency=currency,
            enabled=enabled,
            product_id=product_id,
        )
    ).parsed
