from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_checkout_payment_link_patch_body import (
    UpdateCheckoutPaymentLinkPatchBody,
)
from ...models.update_checkout_payment_link_patch_response_200 import (
    UpdateCheckoutPaymentLinkPatchResponse200,
)
from ...types import Response


def _get_kwargs(
    payment_link_id: str,
    *,
    body: UpdateCheckoutPaymentLinkPatchBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/checkouts/payment-links/{payment_link_id}".format(
            payment_link_id=quote(str(payment_link_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> UpdateCheckoutPaymentLinkPatchResponse200 | None:
    if response.status_code == 200:
        response_200 = UpdateCheckoutPaymentLinkPatchResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[UpdateCheckoutPaymentLinkPatchResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    payment_link_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateCheckoutPaymentLinkPatchBody,
) -> Response[UpdateCheckoutPaymentLinkPatchResponse200]:
    """Update a payment link

    Args:
        payment_link_id (str):
        body (UpdateCheckoutPaymentLinkPatchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateCheckoutPaymentLinkPatchResponse200]
    """

    kwargs = _get_kwargs(
        payment_link_id=payment_link_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    payment_link_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateCheckoutPaymentLinkPatchBody,
) -> UpdateCheckoutPaymentLinkPatchResponse200 | None:
    """Update a payment link

    Args:
        payment_link_id (str):
        body (UpdateCheckoutPaymentLinkPatchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateCheckoutPaymentLinkPatchResponse200
    """

    return sync_detailed(
        payment_link_id=payment_link_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    payment_link_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateCheckoutPaymentLinkPatchBody,
) -> Response[UpdateCheckoutPaymentLinkPatchResponse200]:
    """Update a payment link

    Args:
        payment_link_id (str):
        body (UpdateCheckoutPaymentLinkPatchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateCheckoutPaymentLinkPatchResponse200]
    """

    kwargs = _get_kwargs(
        payment_link_id=payment_link_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    payment_link_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateCheckoutPaymentLinkPatchBody,
) -> UpdateCheckoutPaymentLinkPatchResponse200 | None:
    """Update a payment link

    Args:
        payment_link_id (str):
        body (UpdateCheckoutPaymentLinkPatchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateCheckoutPaymentLinkPatchResponse200
    """

    return (
        await asyncio_detailed(
            payment_link_id=payment_link_id,
            client=client,
            body=body,
        )
    ).parsed
