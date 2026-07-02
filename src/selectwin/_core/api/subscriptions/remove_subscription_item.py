from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.remove_subscription_item_response_200 import (
    RemoveSubscriptionItemResponse200,
)
from ...types import Response


def _get_kwargs(
    subscription_id: str,
    item_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/subscriptions/{subscription_id}/items/{item_id}".format(
            subscription_id=quote(str(subscription_id), safe=""),
            item_id=quote(str(item_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RemoveSubscriptionItemResponse200 | None:
    if response.status_code == 200:
        response_200 = RemoveSubscriptionItemResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RemoveSubscriptionItemResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    subscription_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RemoveSubscriptionItemResponse200]:
    """Remove a line item

    Args:
        subscription_id (str):
        item_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RemoveSubscriptionItemResponse200]
    """

    kwargs = _get_kwargs(
        subscription_id=subscription_id,
        item_id=item_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    subscription_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> RemoveSubscriptionItemResponse200 | None:
    """Remove a line item

    Args:
        subscription_id (str):
        item_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RemoveSubscriptionItemResponse200
    """

    return sync_detailed(
        subscription_id=subscription_id,
        item_id=item_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    subscription_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RemoveSubscriptionItemResponse200]:
    """Remove a line item

    Args:
        subscription_id (str):
        item_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RemoveSubscriptionItemResponse200]
    """

    kwargs = _get_kwargs(
        subscription_id=subscription_id,
        item_id=item_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    subscription_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> RemoveSubscriptionItemResponse200 | None:
    """Remove a line item

    Args:
        subscription_id (str):
        item_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RemoveSubscriptionItemResponse200
    """

    return (
        await asyncio_detailed(
            subscription_id=subscription_id,
            item_id=item_id,
            client=client,
        )
    ).parsed
