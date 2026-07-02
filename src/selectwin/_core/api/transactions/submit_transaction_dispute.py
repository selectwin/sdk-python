from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.submit_transaction_dispute_body import SubmitTransactionDisputeBody
from ...models.submit_transaction_dispute_response_200 import (
    SubmitTransactionDisputeResponse200,
)
from ...types import Response


def _get_kwargs(
    transaction_id: str,
    *,
    body: SubmitTransactionDisputeBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/transactions/{transaction_id}/dispute".format(
            transaction_id=quote(str(transaction_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> SubmitTransactionDisputeResponse200 | None:
    if response.status_code == 200:
        response_200 = SubmitTransactionDisputeResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[SubmitTransactionDisputeResponse200]:
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
    body: SubmitTransactionDisputeBody,
) -> Response[SubmitTransactionDisputeResponse200]:
    """Submit dispute defense evidence

    Args:
        transaction_id (str):
        body (SubmitTransactionDisputeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SubmitTransactionDisputeResponse200]
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
    body: SubmitTransactionDisputeBody,
) -> SubmitTransactionDisputeResponse200 | None:
    """Submit dispute defense evidence

    Args:
        transaction_id (str):
        body (SubmitTransactionDisputeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SubmitTransactionDisputeResponse200
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
    body: SubmitTransactionDisputeBody,
) -> Response[SubmitTransactionDisputeResponse200]:
    """Submit dispute defense evidence

    Args:
        transaction_id (str):
        body (SubmitTransactionDisputeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SubmitTransactionDisputeResponse200]
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
    body: SubmitTransactionDisputeBody,
) -> SubmitTransactionDisputeResponse200 | None:
    """Submit dispute defense evidence

    Args:
        transaction_id (str):
        body (SubmitTransactionDisputeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SubmitTransactionDisputeResponse200
    """

    return (
        await asyncio_detailed(
            transaction_id=transaction_id,
            client=client,
            body=body,
        )
    ).parsed
