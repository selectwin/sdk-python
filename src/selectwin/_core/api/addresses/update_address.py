from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_address_body import UpdateAddressBody
from ...models.update_address_response_200 import UpdateAddressResponse200
from ...types import Response


def _get_kwargs(
    address_id: str,
    *,
    body: UpdateAddressBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/addresses/{address_id}".format(
            address_id=quote(str(address_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> UpdateAddressResponse200 | None:
    if response.status_code == 200:
        response_200 = UpdateAddressResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[UpdateAddressResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    address_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateAddressBody,
) -> Response[UpdateAddressResponse200]:
    """Update an address

    Args:
        address_id (str):
        body (UpdateAddressBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateAddressResponse200]
    """

    kwargs = _get_kwargs(
        address_id=address_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    address_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateAddressBody,
) -> UpdateAddressResponse200 | None:
    """Update an address

    Args:
        address_id (str):
        body (UpdateAddressBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateAddressResponse200
    """

    return sync_detailed(
        address_id=address_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    address_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateAddressBody,
) -> Response[UpdateAddressResponse200]:
    """Update an address

    Args:
        address_id (str):
        body (UpdateAddressBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateAddressResponse200]
    """

    kwargs = _get_kwargs(
        address_id=address_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    address_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateAddressBody,
) -> UpdateAddressResponse200 | None:
    """Update an address

    Args:
        address_id (str):
        body (UpdateAddressBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateAddressResponse200
    """

    return (
        await asyncio_detailed(
            address_id=address_id,
            client=client,
            body=body,
        )
    ).parsed
