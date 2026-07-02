from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.utils_corporate_document_check_response_200 import (
    UtilsCorporateDocumentCheckResponse200,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    document: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["document"] = document

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/utils/corporate-document-check",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> UtilsCorporateDocumentCheckResponse200 | None:
    if response.status_code == 200:
        response_200 = UtilsCorporateDocumentCheckResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[UtilsCorporateDocumentCheckResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    document: str,
) -> Response[UtilsCorporateDocumentCheckResponse200]:
    """Validate a CPF/CNPJ (checksum) and, for a CNPJ, enrich it with the company registration

    Args:
        document (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UtilsCorporateDocumentCheckResponse200]
    """

    kwargs = _get_kwargs(
        document=document,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    document: str,
) -> UtilsCorporateDocumentCheckResponse200 | None:
    """Validate a CPF/CNPJ (checksum) and, for a CNPJ, enrich it with the company registration

    Args:
        document (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UtilsCorporateDocumentCheckResponse200
    """

    return sync_detailed(
        client=client,
        document=document,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    document: str,
) -> Response[UtilsCorporateDocumentCheckResponse200]:
    """Validate a CPF/CNPJ (checksum) and, for a CNPJ, enrich it with the company registration

    Args:
        document (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UtilsCorporateDocumentCheckResponse200]
    """

    kwargs = _get_kwargs(
        document=document,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    document: str,
) -> UtilsCorporateDocumentCheckResponse200 | None:
    """Validate a CPF/CNPJ (checksum) and, for a CNPJ, enrich it with the company registration

    Args:
        document (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UtilsCorporateDocumentCheckResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            document=document,
        )
    ).parsed
