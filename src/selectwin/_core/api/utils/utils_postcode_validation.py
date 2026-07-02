from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.utils_postcode_validation_response_200 import (
    UtilsPostcodeValidationResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    postcode: str,
    country: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["postcode"] = postcode

    params["country"] = country

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/utils/postcode-validation",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> UtilsPostcodeValidationResponse200 | None:
    if response.status_code == 200:
        response_200 = UtilsPostcodeValidationResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[UtilsPostcodeValidationResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    postcode: str,
    country: str | Unset = UNSET,
) -> Response[UtilsPostcodeValidationResponse200]:
    """Validate a postal code (BR CEP format)

    Args:
        postcode (str):
        country (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UtilsPostcodeValidationResponse200]
    """

    kwargs = _get_kwargs(
        postcode=postcode,
        country=country,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    postcode: str,
    country: str | Unset = UNSET,
) -> UtilsPostcodeValidationResponse200 | None:
    """Validate a postal code (BR CEP format)

    Args:
        postcode (str):
        country (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UtilsPostcodeValidationResponse200
    """

    return sync_detailed(
        client=client,
        postcode=postcode,
        country=country,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    postcode: str,
    country: str | Unset = UNSET,
) -> Response[UtilsPostcodeValidationResponse200]:
    """Validate a postal code (BR CEP format)

    Args:
        postcode (str):
        country (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UtilsPostcodeValidationResponse200]
    """

    kwargs = _get_kwargs(
        postcode=postcode,
        country=country,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    postcode: str,
    country: str | Unset = UNSET,
) -> UtilsPostcodeValidationResponse200 | None:
    """Validate a postal code (BR CEP format)

    Args:
        postcode (str):
        country (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UtilsPostcodeValidationResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            postcode=postcode,
            country=country,
        )
    ).parsed
