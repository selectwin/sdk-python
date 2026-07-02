from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_variant_response_200 import GetVariantResponse200
from ...types import Response


def _get_kwargs(
    variant_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/variants/{variant_id}".format(
            variant_id=quote(str(variant_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetVariantResponse200 | None:
    if response.status_code == 200:
        response_200 = GetVariantResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetVariantResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    variant_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetVariantResponse200]:
    """Retrieve a product variant

    Args:
        variant_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetVariantResponse200]
    """

    kwargs = _get_kwargs(
        variant_id=variant_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    variant_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetVariantResponse200 | None:
    """Retrieve a product variant

    Args:
        variant_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetVariantResponse200
    """

    return sync_detailed(
        variant_id=variant_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    variant_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetVariantResponse200]:
    """Retrieve a product variant

    Args:
        variant_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetVariantResponse200]
    """

    kwargs = _get_kwargs(
        variant_id=variant_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    variant_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetVariantResponse200 | None:
    """Retrieve a product variant

    Args:
        variant_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetVariantResponse200
    """

    return (
        await asyncio_detailed(
            variant_id=variant_id,
            client=client,
        )
    ).parsed
