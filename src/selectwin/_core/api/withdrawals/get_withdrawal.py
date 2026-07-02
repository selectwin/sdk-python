from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_withdrawal_response_200 import GetWithdrawalResponse200
from ...types import Response


def _get_kwargs(
    withdrawal_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/withdrawals/{withdrawal_id}".format(
            withdrawal_id=quote(str(withdrawal_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetWithdrawalResponse200 | None:
    if response.status_code == 200:
        response_200 = GetWithdrawalResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetWithdrawalResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    withdrawal_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetWithdrawalResponse200]:
    """Retrieve a withdrawal

    Args:
        withdrawal_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWithdrawalResponse200]
    """

    kwargs = _get_kwargs(
        withdrawal_id=withdrawal_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    withdrawal_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetWithdrawalResponse200 | None:
    """Retrieve a withdrawal

    Args:
        withdrawal_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWithdrawalResponse200
    """

    return sync_detailed(
        withdrawal_id=withdrawal_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    withdrawal_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetWithdrawalResponse200]:
    """Retrieve a withdrawal

    Args:
        withdrawal_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWithdrawalResponse200]
    """

    kwargs = _get_kwargs(
        withdrawal_id=withdrawal_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    withdrawal_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetWithdrawalResponse200 | None:
    """Retrieve a withdrawal

    Args:
        withdrawal_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWithdrawalResponse200
    """

    return (
        await asyncio_detailed(
            withdrawal_id=withdrawal_id,
            client=client,
        )
    ).parsed
