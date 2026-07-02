from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_subscription_cycle_usage_response_200 import (
    GetSubscriptionCycleUsageResponse200,
)
from ...types import Response


def _get_kwargs(
    subscription_id: str,
    cycle_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/subscriptions/{subscription_id}/cycles/{cycle_id}/usage".format(
            subscription_id=quote(str(subscription_id), safe=""),
            cycle_id=quote(str(cycle_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetSubscriptionCycleUsageResponse200 | None:
    if response.status_code == 200:
        response_200 = GetSubscriptionCycleUsageResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetSubscriptionCycleUsageResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    subscription_id: str,
    cycle_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetSubscriptionCycleUsageResponse200]:
    """Aggregated usage + computed line amounts for a cycle

    Args:
        subscription_id (str):
        cycle_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSubscriptionCycleUsageResponse200]
    """

    kwargs = _get_kwargs(
        subscription_id=subscription_id,
        cycle_id=cycle_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    subscription_id: str,
    cycle_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetSubscriptionCycleUsageResponse200 | None:
    """Aggregated usage + computed line amounts for a cycle

    Args:
        subscription_id (str):
        cycle_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSubscriptionCycleUsageResponse200
    """

    return sync_detailed(
        subscription_id=subscription_id,
        cycle_id=cycle_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    subscription_id: str,
    cycle_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetSubscriptionCycleUsageResponse200]:
    """Aggregated usage + computed line amounts for a cycle

    Args:
        subscription_id (str):
        cycle_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSubscriptionCycleUsageResponse200]
    """

    kwargs = _get_kwargs(
        subscription_id=subscription_id,
        cycle_id=cycle_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    subscription_id: str,
    cycle_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetSubscriptionCycleUsageResponse200 | None:
    """Aggregated usage + computed line amounts for a cycle

    Args:
        subscription_id (str):
        cycle_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSubscriptionCycleUsageResponse200
    """

    return (
        await asyncio_detailed(
            subscription_id=subscription_id,
            cycle_id=cycle_id,
            client=client,
        )
    ).parsed
