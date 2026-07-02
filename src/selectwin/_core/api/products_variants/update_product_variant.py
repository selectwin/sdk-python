from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_product_variant_body import UpdateProductVariantBody
from ...models.update_product_variant_response_200 import (
    UpdateProductVariantResponse200,
)
from ...types import Response


def _get_kwargs(
    product_id: str,
    variant_id: str,
    *,
    body: UpdateProductVariantBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/products/{product_id}/variants/{variant_id}".format(
            product_id=quote(str(product_id), safe=""),
            variant_id=quote(str(variant_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> UpdateProductVariantResponse200 | None:
    if response.status_code == 200:
        response_200 = UpdateProductVariantResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[UpdateProductVariantResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    product_id: str,
    variant_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateProductVariantBody,
) -> Response[UpdateProductVariantResponse200]:
    """Update a product variant

    Args:
        product_id (str):
        variant_id (str):
        body (UpdateProductVariantBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateProductVariantResponse200]
    """

    kwargs = _get_kwargs(
        product_id=product_id,
        variant_id=variant_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    product_id: str,
    variant_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateProductVariantBody,
) -> UpdateProductVariantResponse200 | None:
    """Update a product variant

    Args:
        product_id (str):
        variant_id (str):
        body (UpdateProductVariantBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateProductVariantResponse200
    """

    return sync_detailed(
        product_id=product_id,
        variant_id=variant_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    product_id: str,
    variant_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateProductVariantBody,
) -> Response[UpdateProductVariantResponse200]:
    """Update a product variant

    Args:
        product_id (str):
        variant_id (str):
        body (UpdateProductVariantBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateProductVariantResponse200]
    """

    kwargs = _get_kwargs(
        product_id=product_id,
        variant_id=variant_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    product_id: str,
    variant_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateProductVariantBody,
) -> UpdateProductVariantResponse200 | None:
    """Update a product variant

    Args:
        product_id (str):
        variant_id (str):
        body (UpdateProductVariantBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateProductVariantResponse200
    """

    return (
        await asyncio_detailed(
            product_id=product_id,
            variant_id=variant_id,
            client=client,
            body=body,
        )
    ).parsed
