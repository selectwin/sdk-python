from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.submit_checkout_payment_body import SubmitCheckoutPaymentBody
from ...models.submit_checkout_payment_response_202 import (
    SubmitCheckoutPaymentResponse202,
)
from ...types import Response


def _get_kwargs(
    session_id: str,
    *,
    body: SubmitCheckoutPaymentBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/checkouts/sessions/{session_id}/pay".format(
            session_id=quote(str(session_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> SubmitCheckoutPaymentResponse202 | None:
    if response.status_code == 202:
        response_202 = SubmitCheckoutPaymentResponse202.from_dict(response.json())

        return response_202

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[SubmitCheckoutPaymentResponse202]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SubmitCheckoutPaymentBody,
) -> Response[SubmitCheckoutPaymentResponse202]:
    """Submit a checkout session for payment (async)

    Args:
        session_id (str):
        body (SubmitCheckoutPaymentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SubmitCheckoutPaymentResponse202]
    """

    kwargs = _get_kwargs(
        session_id=session_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SubmitCheckoutPaymentBody,
) -> SubmitCheckoutPaymentResponse202 | None:
    """Submit a checkout session for payment (async)

    Args:
        session_id (str):
        body (SubmitCheckoutPaymentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SubmitCheckoutPaymentResponse202
    """

    return sync_detailed(
        session_id=session_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SubmitCheckoutPaymentBody,
) -> Response[SubmitCheckoutPaymentResponse202]:
    """Submit a checkout session for payment (async)

    Args:
        session_id (str):
        body (SubmitCheckoutPaymentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SubmitCheckoutPaymentResponse202]
    """

    kwargs = _get_kwargs(
        session_id=session_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SubmitCheckoutPaymentBody,
) -> SubmitCheckoutPaymentResponse202 | None:
    """Submit a checkout session for payment (async)

    Args:
        session_id (str):
        body (SubmitCheckoutPaymentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SubmitCheckoutPaymentResponse202
    """

    return (
        await asyncio_detailed(
            session_id=session_id,
            client=client,
            body=body,
        )
    ).parsed
