import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_customers_response_200 import ListCustomersResponse200
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
    email: str | Unset = UNSET,
    name: str | Unset = UNSET,
    telephoneline: str | Unset = UNSET,
    document: str | Unset = UNSET,
    externalreference: str | Unset = UNSET,
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

    params["email"] = email

    params["name"] = name

    params["telephoneline"] = telephoneline

    params["document"] = document

    params["externalreference"] = externalreference

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/customers",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListCustomersResponse200 | None:
    if response.status_code == 200:
        response_200 = ListCustomersResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ListCustomersResponse200]:
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
    email: str | Unset = UNSET,
    name: str | Unset = UNSET,
    telephoneline: str | Unset = UNSET,
    document: str | Unset = UNSET,
    externalreference: str | Unset = UNSET,
) -> Response[ListCustomersResponse200]:
    """List customers

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
        email (str | Unset):
        name (str | Unset):
        telephoneline (str | Unset):
        document (str | Unset):
        externalreference (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListCustomersResponse200]
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
        email=email,
        name=name,
        telephoneline=telephoneline,
        document=document,
        externalreference=externalreference,
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
    email: str | Unset = UNSET,
    name: str | Unset = UNSET,
    telephoneline: str | Unset = UNSET,
    document: str | Unset = UNSET,
    externalreference: str | Unset = UNSET,
) -> ListCustomersResponse200 | None:
    """List customers

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
        email (str | Unset):
        name (str | Unset):
        telephoneline (str | Unset):
        document (str | Unset):
        externalreference (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListCustomersResponse200
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
        email=email,
        name=name,
        telephoneline=telephoneline,
        document=document,
        externalreference=externalreference,
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
    email: str | Unset = UNSET,
    name: str | Unset = UNSET,
    telephoneline: str | Unset = UNSET,
    document: str | Unset = UNSET,
    externalreference: str | Unset = UNSET,
) -> Response[ListCustomersResponse200]:
    """List customers

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
        email (str | Unset):
        name (str | Unset):
        telephoneline (str | Unset):
        document (str | Unset):
        externalreference (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListCustomersResponse200]
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
        email=email,
        name=name,
        telephoneline=telephoneline,
        document=document,
        externalreference=externalreference,
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
    email: str | Unset = UNSET,
    name: str | Unset = UNSET,
    telephoneline: str | Unset = UNSET,
    document: str | Unset = UNSET,
    externalreference: str | Unset = UNSET,
) -> ListCustomersResponse200 | None:
    """List customers

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
        email (str | Unset):
        name (str | Unset):
        telephoneline (str | Unset):
        document (str | Unset):
        externalreference (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListCustomersResponse200
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
            email=email,
            name=name,
            telephoneline=telephoneline,
            document=document,
            externalreference=externalreference,
        )
    ).parsed
