from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.record_subscription_usage_body import RecordSubscriptionUsageBody
from ...models.record_subscription_usage_response_200 import (
    RecordSubscriptionUsageResponse200,
)
from ...models.record_subscription_usage_response_201 import (
    RecordSubscriptionUsageResponse201,
)
from ...types import Response


def _get_kwargs(
    subscription_id: str,
    item_id: str,
    *,
    body: RecordSubscriptionUsageBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/subscriptions/{subscription_id}/items/{item_id}/usage".format(
            subscription_id=quote(str(subscription_id), safe=""),
            item_id=quote(str(item_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RecordSubscriptionUsageResponse200 | RecordSubscriptionUsageResponse201 | None:
    if response.status_code == 200:
        response_200 = RecordSubscriptionUsageResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = RecordSubscriptionUsageResponse201.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RecordSubscriptionUsageResponse200 | RecordSubscriptionUsageResponse201]:
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
    body: RecordSubscriptionUsageBody,
) -> Response[RecordSubscriptionUsageResponse200 | RecordSubscriptionUsageResponse201]:
    """Report metered usage for a subscription item

    Args:
        subscription_id (str):
        item_id (str):
        body (RecordSubscriptionUsageBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RecordSubscriptionUsageResponse200 | RecordSubscriptionUsageResponse201]
    """

    kwargs = _get_kwargs(
        subscription_id=subscription_id,
        item_id=item_id,
        body=body,
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
    body: RecordSubscriptionUsageBody,
) -> RecordSubscriptionUsageResponse200 | RecordSubscriptionUsageResponse201 | None:
    """Report metered usage for a subscription item

    Args:
        subscription_id (str):
        item_id (str):
        body (RecordSubscriptionUsageBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RecordSubscriptionUsageResponse200 | RecordSubscriptionUsageResponse201
    """

    return sync_detailed(
        subscription_id=subscription_id,
        item_id=item_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    subscription_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RecordSubscriptionUsageBody,
) -> Response[RecordSubscriptionUsageResponse200 | RecordSubscriptionUsageResponse201]:
    """Report metered usage for a subscription item

    Args:
        subscription_id (str):
        item_id (str):
        body (RecordSubscriptionUsageBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RecordSubscriptionUsageResponse200 | RecordSubscriptionUsageResponse201]
    """

    kwargs = _get_kwargs(
        subscription_id=subscription_id,
        item_id=item_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    subscription_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RecordSubscriptionUsageBody,
) -> RecordSubscriptionUsageResponse200 | RecordSubscriptionUsageResponse201 | None:
    """Report metered usage for a subscription item

    Args:
        subscription_id (str):
        item_id (str):
        body (RecordSubscriptionUsageBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RecordSubscriptionUsageResponse200 | RecordSubscriptionUsageResponse201
    """

    return (
        await asyncio_detailed(
            subscription_id=subscription_id,
            item_id=item_id,
            client=client,
            body=body,
        )
    ).parsed
