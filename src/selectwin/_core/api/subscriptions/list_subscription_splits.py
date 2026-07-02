from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_subscription_splits_response_200 import (
    ListSubscriptionSplitsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    subscription_id: str,
    *,
    limit: int | Unset = 20,
    offset: int | Unset = 0,
    sort: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/subscriptions/{subscription_id}/splits".format(
            subscription_id=quote(str(subscription_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListSubscriptionSplitsResponse200 | None:
    if response.status_code == 200:
        response_200 = ListSubscriptionSplitsResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ListSubscriptionSplitsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    subscription_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 20,
    offset: int | Unset = 0,
    sort: str | Unset = UNSET,
) -> Response[ListSubscriptionSplitsResponse200]:
    """List a subscription's revenue splits

    Args:
        subscription_id (str):
        limit (int | Unset):  Default: 20.
        offset (int | Unset):  Default: 0.
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListSubscriptionSplitsResponse200]
    """

    kwargs = _get_kwargs(
        subscription_id=subscription_id,
        limit=limit,
        offset=offset,
        sort=sort,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    subscription_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 20,
    offset: int | Unset = 0,
    sort: str | Unset = UNSET,
) -> ListSubscriptionSplitsResponse200 | None:
    """List a subscription's revenue splits

    Args:
        subscription_id (str):
        limit (int | Unset):  Default: 20.
        offset (int | Unset):  Default: 0.
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListSubscriptionSplitsResponse200
    """

    return sync_detailed(
        subscription_id=subscription_id,
        client=client,
        limit=limit,
        offset=offset,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    subscription_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 20,
    offset: int | Unset = 0,
    sort: str | Unset = UNSET,
) -> Response[ListSubscriptionSplitsResponse200]:
    """List a subscription's revenue splits

    Args:
        subscription_id (str):
        limit (int | Unset):  Default: 20.
        offset (int | Unset):  Default: 0.
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListSubscriptionSplitsResponse200]
    """

    kwargs = _get_kwargs(
        subscription_id=subscription_id,
        limit=limit,
        offset=offset,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    subscription_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 20,
    offset: int | Unset = 0,
    sort: str | Unset = UNSET,
) -> ListSubscriptionSplitsResponse200 | None:
    """List a subscription's revenue splits

    Args:
        subscription_id (str):
        limit (int | Unset):  Default: 20.
        offset (int | Unset):  Default: 0.
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListSubscriptionSplitsResponse200
    """

    return (
        await asyncio_detailed(
            subscription_id=subscription_id,
            client=client,
            limit=limit,
            offset=offset,
            sort=sort,
        )
    ).parsed
