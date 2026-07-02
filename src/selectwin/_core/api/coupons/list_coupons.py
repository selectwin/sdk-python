import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_coupons_dir import ListCouponsDir
from ...models.list_coupons_response_200 import ListCouponsResponse200
from ...models.list_coupons_status import ListCouponsStatus
from ...models.list_coupons_type import ListCouponsType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 20,
    offset: int | Unset = 0,
    sort: str | Unset = UNSET,
    daterange: datetime.datetime | str | Unset = UNSET,
    daterangegt: datetime.datetime | Unset = UNSET,
    daterangegte: datetime.datetime | Unset = UNSET,
    daterangelt: datetime.datetime | Unset = UNSET,
    daterangelte: datetime.datetime | Unset = UNSET,
    id: str | Unset = UNSET,
    name: str | Unset = UNSET,
    code: str | Unset = UNSET,
    type_: ListCouponsType | Unset = UNSET,
    status: ListCouponsStatus | Unset = UNSET,
    dir_: ListCouponsDir | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params["sort"] = sort

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

    params["name"] = name

    params["code"] = code

    json_type_: str | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    json_dir_: str | Unset = UNSET
    if not isinstance(dir_, Unset):
        json_dir_ = dir_.value

    params["dir"] = json_dir_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/coupons",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListCouponsResponse200 | None:
    if response.status_code == 200:
        response_200 = ListCouponsResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ListCouponsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 20,
    offset: int | Unset = 0,
    sort: str | Unset = UNSET,
    daterange: datetime.datetime | str | Unset = UNSET,
    daterangegt: datetime.datetime | Unset = UNSET,
    daterangegte: datetime.datetime | Unset = UNSET,
    daterangelt: datetime.datetime | Unset = UNSET,
    daterangelte: datetime.datetime | Unset = UNSET,
    id: str | Unset = UNSET,
    name: str | Unset = UNSET,
    code: str | Unset = UNSET,
    type_: ListCouponsType | Unset = UNSET,
    status: ListCouponsStatus | Unset = UNSET,
    dir_: ListCouponsDir | Unset = UNSET,
) -> Response[ListCouponsResponse200]:
    """List coupons

    Args:
        limit (int | Unset):  Default: 20.
        offset (int | Unset):  Default: 0.
        sort (str | Unset):
        daterange (datetime.datetime | str | Unset):
        daterangegt (datetime.datetime | Unset):
        daterangegte (datetime.datetime | Unset):
        daterangelt (datetime.datetime | Unset):
        daterangelte (datetime.datetime | Unset):
        id (str | Unset):
        name (str | Unset):
        code (str | Unset):
        type_ (ListCouponsType | Unset):
        status (ListCouponsStatus | Unset):
        dir_ (ListCouponsDir | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListCouponsResponse200]
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
        name=name,
        code=code,
        type_=type_,
        status=status,
        dir_=dir_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 20,
    offset: int | Unset = 0,
    sort: str | Unset = UNSET,
    daterange: datetime.datetime | str | Unset = UNSET,
    daterangegt: datetime.datetime | Unset = UNSET,
    daterangegte: datetime.datetime | Unset = UNSET,
    daterangelt: datetime.datetime | Unset = UNSET,
    daterangelte: datetime.datetime | Unset = UNSET,
    id: str | Unset = UNSET,
    name: str | Unset = UNSET,
    code: str | Unset = UNSET,
    type_: ListCouponsType | Unset = UNSET,
    status: ListCouponsStatus | Unset = UNSET,
    dir_: ListCouponsDir | Unset = UNSET,
) -> ListCouponsResponse200 | None:
    """List coupons

    Args:
        limit (int | Unset):  Default: 20.
        offset (int | Unset):  Default: 0.
        sort (str | Unset):
        daterange (datetime.datetime | str | Unset):
        daterangegt (datetime.datetime | Unset):
        daterangegte (datetime.datetime | Unset):
        daterangelt (datetime.datetime | Unset):
        daterangelte (datetime.datetime | Unset):
        id (str | Unset):
        name (str | Unset):
        code (str | Unset):
        type_ (ListCouponsType | Unset):
        status (ListCouponsStatus | Unset):
        dir_ (ListCouponsDir | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListCouponsResponse200
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
        name=name,
        code=code,
        type_=type_,
        status=status,
        dir_=dir_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 20,
    offset: int | Unset = 0,
    sort: str | Unset = UNSET,
    daterange: datetime.datetime | str | Unset = UNSET,
    daterangegt: datetime.datetime | Unset = UNSET,
    daterangegte: datetime.datetime | Unset = UNSET,
    daterangelt: datetime.datetime | Unset = UNSET,
    daterangelte: datetime.datetime | Unset = UNSET,
    id: str | Unset = UNSET,
    name: str | Unset = UNSET,
    code: str | Unset = UNSET,
    type_: ListCouponsType | Unset = UNSET,
    status: ListCouponsStatus | Unset = UNSET,
    dir_: ListCouponsDir | Unset = UNSET,
) -> Response[ListCouponsResponse200]:
    """List coupons

    Args:
        limit (int | Unset):  Default: 20.
        offset (int | Unset):  Default: 0.
        sort (str | Unset):
        daterange (datetime.datetime | str | Unset):
        daterangegt (datetime.datetime | Unset):
        daterangegte (datetime.datetime | Unset):
        daterangelt (datetime.datetime | Unset):
        daterangelte (datetime.datetime | Unset):
        id (str | Unset):
        name (str | Unset):
        code (str | Unset):
        type_ (ListCouponsType | Unset):
        status (ListCouponsStatus | Unset):
        dir_ (ListCouponsDir | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListCouponsResponse200]
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
        name=name,
        code=code,
        type_=type_,
        status=status,
        dir_=dir_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 20,
    offset: int | Unset = 0,
    sort: str | Unset = UNSET,
    daterange: datetime.datetime | str | Unset = UNSET,
    daterangegt: datetime.datetime | Unset = UNSET,
    daterangegte: datetime.datetime | Unset = UNSET,
    daterangelt: datetime.datetime | Unset = UNSET,
    daterangelte: datetime.datetime | Unset = UNSET,
    id: str | Unset = UNSET,
    name: str | Unset = UNSET,
    code: str | Unset = UNSET,
    type_: ListCouponsType | Unset = UNSET,
    status: ListCouponsStatus | Unset = UNSET,
    dir_: ListCouponsDir | Unset = UNSET,
) -> ListCouponsResponse200 | None:
    """List coupons

    Args:
        limit (int | Unset):  Default: 20.
        offset (int | Unset):  Default: 0.
        sort (str | Unset):
        daterange (datetime.datetime | str | Unset):
        daterangegt (datetime.datetime | Unset):
        daterangegte (datetime.datetime | Unset):
        daterangelt (datetime.datetime | Unset):
        daterangelte (datetime.datetime | Unset):
        id (str | Unset):
        name (str | Unset):
        code (str | Unset):
        type_ (ListCouponsType | Unset):
        status (ListCouponsStatus | Unset):
        dir_ (ListCouponsDir | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListCouponsResponse200
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
            name=name,
            code=code,
            type_=type_,
            status=status,
            dir_=dir_,
        )
    ).parsed
