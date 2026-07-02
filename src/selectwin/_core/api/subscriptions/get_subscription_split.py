from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_subscription_split_response_200 import (
    GetSubscriptionSplitResponse200,
)
from ...types import Response


def _get_kwargs(
    subscription_id: str,
    split_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/subscriptions/{subscription_id}/splits/{split_id}".format(
            subscription_id=quote(str(subscription_id), safe=""),
            split_id=quote(str(split_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetSubscriptionSplitResponse200 | None:
    if response.status_code == 200:
        response_200 = GetSubscriptionSplitResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetSubscriptionSplitResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    subscription_id: str,
    split_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetSubscriptionSplitResponse200]:
    """Retrieve a revenue split

    Args:
        subscription_id (str):
        split_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSubscriptionSplitResponse200]
    """

    kwargs = _get_kwargs(
        subscription_id=subscription_id,
        split_id=split_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    subscription_id: str,
    split_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetSubscriptionSplitResponse200 | None:
    """Retrieve a revenue split

    Args:
        subscription_id (str):
        split_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSubscriptionSplitResponse200
    """

    return sync_detailed(
        subscription_id=subscription_id,
        split_id=split_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    subscription_id: str,
    split_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetSubscriptionSplitResponse200]:
    """Retrieve a revenue split

    Args:
        subscription_id (str):
        split_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSubscriptionSplitResponse200]
    """

    kwargs = _get_kwargs(
        subscription_id=subscription_id,
        split_id=split_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    subscription_id: str,
    split_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetSubscriptionSplitResponse200 | None:
    """Retrieve a revenue split

    Args:
        subscription_id (str):
        split_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSubscriptionSplitResponse200
    """

    return (
        await asyncio_detailed(
            subscription_id=subscription_id,
            split_id=split_id,
            client=client,
        )
    ).parsed
