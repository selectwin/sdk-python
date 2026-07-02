from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.capture_transaction_body import CaptureTransactionBody
from ...models.capture_transaction_response_202 import CaptureTransactionResponse202
from ...types import Response


def _get_kwargs(
    transaction_id: str,
    *,
    body: CaptureTransactionBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/transactions/{transaction_id}/capture".format(
            transaction_id=quote(str(transaction_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CaptureTransactionResponse202 | None:
    if response.status_code == 202:
        response_202 = CaptureTransactionResponse202.from_dict(response.json())

        return response_202

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CaptureTransactionResponse202]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    transaction_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CaptureTransactionBody,
) -> Response[CaptureTransactionResponse202]:
    """Capture a pre-authorized transaction

    Args:
        transaction_id (str):
        body (CaptureTransactionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CaptureTransactionResponse202]
    """

    kwargs = _get_kwargs(
        transaction_id=transaction_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    transaction_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CaptureTransactionBody,
) -> CaptureTransactionResponse202 | None:
    """Capture a pre-authorized transaction

    Args:
        transaction_id (str):
        body (CaptureTransactionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CaptureTransactionResponse202
    """

    return sync_detailed(
        transaction_id=transaction_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    transaction_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CaptureTransactionBody,
) -> Response[CaptureTransactionResponse202]:
    """Capture a pre-authorized transaction

    Args:
        transaction_id (str):
        body (CaptureTransactionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CaptureTransactionResponse202]
    """

    kwargs = _get_kwargs(
        transaction_id=transaction_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    transaction_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CaptureTransactionBody,
) -> CaptureTransactionResponse202 | None:
    """Capture a pre-authorized transaction

    Args:
        transaction_id (str):
        body (CaptureTransactionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CaptureTransactionResponse202
    """

    return (
        await asyncio_detailed(
            transaction_id=transaction_id,
            client=client,
            body=body,
        )
    ).parsed
