from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_subscription_threshold_body import AddSubscriptionThresholdBody
from ...models.add_subscription_threshold_response_201 import (
    AddSubscriptionThresholdResponse201,
)
from ...types import Response


def _get_kwargs(
    subscription_id: str,
    *,
    body: AddSubscriptionThresholdBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/subscriptions/{subscription_id}/thresholds".format(
            subscription_id=quote(str(subscription_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AddSubscriptionThresholdResponse201 | None:
    if response.status_code == 201:
        response_201 = AddSubscriptionThresholdResponse201.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AddSubscriptionThresholdResponse201]:
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
    body: AddSubscriptionThresholdBody,
) -> Response[AddSubscriptionThresholdResponse201]:
    """Add a billing threshold

    Args:
        subscription_id (str):
        body (AddSubscriptionThresholdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddSubscriptionThresholdResponse201]
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
    body: AddSubscriptionThresholdBody,
) -> AddSubscriptionThresholdResponse201 | None:
    """Add a billing threshold

    Args:
        subscription_id (str):
        body (AddSubscriptionThresholdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddSubscriptionThresholdResponse201
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
    body: AddSubscriptionThresholdBody,
) -> Response[AddSubscriptionThresholdResponse201]:
    """Add a billing threshold

    Args:
        subscription_id (str):
        body (AddSubscriptionThresholdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddSubscriptionThresholdResponse201]
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
    body: AddSubscriptionThresholdBody,
) -> AddSubscriptionThresholdResponse201 | None:
    """Add a billing threshold

    Args:
        subscription_id (str):
        body (AddSubscriptionThresholdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddSubscriptionThresholdResponse201
    """

    return (
        await asyncio_detailed(
            subscription_id=subscription_id,
            client=client,
            body=body,
        )
    ).parsed
