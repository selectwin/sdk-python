from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_wallet_response_200 import GetWalletResponse200
from ...types import Response


def _get_kwargs(
    wallet_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/wallets/{wallet_id}".format(
            wallet_id=quote(str(wallet_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetWalletResponse200 | None:
    if response.status_code == 200:
        response_200 = GetWalletResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetWalletResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    wallet_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetWalletResponse200]:
    """Retrieve a payout wallet

    Args:
        wallet_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWalletResponse200]
    """

    kwargs = _get_kwargs(
        wallet_id=wallet_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    wallet_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetWalletResponse200 | None:
    """Retrieve a payout wallet

    Args:
        wallet_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWalletResponse200
    """

    return sync_detailed(
        wallet_id=wallet_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    wallet_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetWalletResponse200]:
    """Retrieve a payout wallet

    Args:
        wallet_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWalletResponse200]
    """

    kwargs = _get_kwargs(
        wallet_id=wallet_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    wallet_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetWalletResponse200 | None:
    """Retrieve a payout wallet

    Args:
        wallet_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWalletResponse200
    """

    return (
        await asyncio_detailed(
            wallet_id=wallet_id,
            client=client,
        )
    ).parsed
