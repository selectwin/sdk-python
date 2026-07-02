from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_subscription_split_body import AddSubscriptionSplitBody
from ...models.add_subscription_split_response_201 import (
    AddSubscriptionSplitResponse201,
)
from ...types import Response


def _get_kwargs(
    subscription_id: str,
    *,
    body: AddSubscriptionSplitBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/subscriptions/{subscription_id}/splits".format(
            subscription_id=quote(str(subscription_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AddSubscriptionSplitResponse201 | None:
    if response.status_code == 201:
        response_201 = AddSubscriptionSplitResponse201.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AddSubscriptionSplitResponse201]:
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
    body: AddSubscriptionSplitBody,
) -> Response[AddSubscriptionSplitResponse201]:
    """Add a revenue split (recipient company)

    Args:
        subscription_id (str):
        body (AddSubscriptionSplitBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddSubscriptionSplitResponse201]
    """

    kwargs = _get_kwargs(
        subscription_id=subscription_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    subscription_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AddSubscriptionSplitBody,
) -> AddSubscriptionSplitResponse201 | None:
    """Add a revenue split (recipient company)

    Args:
        subscription_id (str):
        body (AddSubscriptionSplitBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddSubscriptionSplitResponse201
    """

    return sync_detailed(
        subscription_id=subscription_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    subscription_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AddSubscriptionSplitBody,
) -> Response[AddSubscriptionSplitResponse201]:
    """Add a revenue split (recipient company)

    Args:
        subscription_id (str):
        body (AddSubscriptionSplitBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddSubscriptionSplitResponse201]
    """

    kwargs = _get_kwargs(
        subscription_id=subscription_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    subscription_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AddSubscriptionSplitBody,
) -> AddSubscriptionSplitResponse201 | None:
    """Add a revenue split (recipient company)

    Args:
        subscription_id (str):
        body (AddSubscriptionSplitBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddSubscriptionSplitResponse201
    """

    return (
        await asyncio_detailed(
            subscription_id=subscription_id,
            client=client,
            body=body,
        )
    ).parsed
