from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_receivable_response_200 import GetReceivableResponse200
from ...types import Response


def _get_kwargs(
    receivable_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/receivables/{receivable_id}".format(
            receivable_id=quote(str(receivable_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetReceivableResponse200 | None:
    if response.status_code == 200:
        response_200 = GetReceivableResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetReceivableResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    receivable_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetReceivableResponse200]:
    """Retrieve a receivable

    Args:
        receivable_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetReceivableResponse200]
    """

    kwargs = _get_kwargs(
        receivable_id=receivable_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    receivable_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetReceivableResponse200 | None:
    """Retrieve a receivable

    Args:
        receivable_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetReceivableResponse200
    """

    return sync_detailed(
        receivable_id=receivable_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    receivable_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetReceivableResponse200]:
    """Retrieve a receivable

    Args:
        receivable_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetReceivableResponse200]
    """

    kwargs = _get_kwargs(
        receivable_id=receivable_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    receivable_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetReceivableResponse200 | None:
    """Retrieve a receivable

    Args:
        receivable_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetReceivableResponse200
    """

    return (
        await asyncio_detailed(
            receivable_id=receivable_id,
            client=client,
        )
    ).parsed
