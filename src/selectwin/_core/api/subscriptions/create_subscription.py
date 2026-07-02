from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_subscription_body import CreateSubscriptionBody
from ...models.create_subscription_response_201 import CreateSubscriptionResponse201
from ...types import Response


def _get_kwargs(
    *,
    body: CreateSubscriptionBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/subscriptions",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateSubscriptionResponse201 | None:
    if response.status_code == 201:
        response_201 = CreateSubscriptionResponse201.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateSubscriptionResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateSubscriptionBody,
) -> Response[CreateSubscriptionResponse201]:
    """Create a subscription

     Create a subscription

    **Catalog-only (Selectwin-strict):** the price/billing model comes from the product variant, never
    the request — the variant must have `pricingType=recurring` (else `422`). Metered/tiered
    subscriptions use the same request shape; the behavior is driven by the variant. A `freeTrial`
    subscription is born `trialing` and is NOT charged until the trial ends.

    Args:
        body (CreateSubscriptionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateSubscriptionResponse201]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CreateSubscriptionBody,
) -> CreateSubscriptionResponse201 | None:
    """Create a subscription

     Create a subscription

    **Catalog-only (Selectwin-strict):** the price/billing model comes from the product variant, never
    the request — the variant must have `pricingType=recurring` (else `422`). Metered/tiered
    subscriptions use the same request shape; the behavior is driven by the variant. A `freeTrial`
    subscription is born `trialing` and is NOT charged until the trial ends.

    Args:
        body (CreateSubscriptionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateSubscriptionResponse201
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateSubscriptionBody,
) -> Response[CreateSubscriptionResponse201]:
    """Create a subscription

     Create a subscription

    **Catalog-only (Selectwin-strict):** the price/billing model comes from the product variant, never
    the request — the variant must have `pricingType=recurring` (else `422`). Metered/tiered
    subscriptions use the same request shape; the behavior is driven by the variant. A `freeTrial`
    subscription is born `trialing` and is NOT charged until the trial ends.

    Args:
        body (CreateSubscriptionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateSubscriptionResponse201]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateSubscriptionBody,
) -> CreateSubscriptionResponse201 | None:
    """Create a subscription

     Create a subscription

    **Catalog-only (Selectwin-strict):** the price/billing model comes from the product variant, never
    the request — the variant must have `pricingType=recurring` (else `422`). Metered/tiered
    subscriptions use the same request shape; the behavior is driven by the variant. A `freeTrial`
    subscription is born `trialing` and is NOT charged until the trial ends.

    Args:
        body (CreateSubscriptionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateSubscriptionResponse201
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
