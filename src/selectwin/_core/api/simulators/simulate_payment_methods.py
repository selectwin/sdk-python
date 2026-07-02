from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.simulate_payment_methods_method import SimulatePaymentMethodsMethod
from ...models.simulate_payment_methods_response_200 import (
    SimulatePaymentMethodsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    amount: int,
    fee: float | Unset = UNSET,
    installment: int | Unset = UNSET,
    method: SimulatePaymentMethodsMethod,
    brand: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["amount"] = amount

    params["fee"] = fee

    params["installment"] = installment

    json_method = method.value
    params["method"] = json_method

    params["brand"] = brand

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/simulators/payment-methods",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> SimulatePaymentMethodsResponse200 | None:
    if response.status_code == 200:
        response_200 = SimulatePaymentMethodsResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[SimulatePaymentMethodsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    amount: int,
    fee: float | Unset = UNSET,
    installment: int | Unset = UNSET,
    method: SimulatePaymentMethodsMethod,
    brand: str | Unset = UNSET,
) -> Response[SimulatePaymentMethodsResponse200]:
    """Simulate the fees and totals for a single payment method

    Args:
        amount (int):
        fee (float | Unset):
        installment (int | Unset):
        method (SimulatePaymentMethodsMethod):
        brand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SimulatePaymentMethodsResponse200]
    """

    kwargs = _get_kwargs(
        amount=amount,
        fee=fee,
        installment=installment,
        method=method,
        brand=brand,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    amount: int,
    fee: float | Unset = UNSET,
    installment: int | Unset = UNSET,
    method: SimulatePaymentMethodsMethod,
    brand: str | Unset = UNSET,
) -> SimulatePaymentMethodsResponse200 | None:
    """Simulate the fees and totals for a single payment method

    Args:
        amount (int):
        fee (float | Unset):
        installment (int | Unset):
        method (SimulatePaymentMethodsMethod):
        brand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SimulatePaymentMethodsResponse200
    """

    return sync_detailed(
        client=client,
        amount=amount,
        fee=fee,
        installment=installment,
        method=method,
        brand=brand,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    amount: int,
    fee: float | Unset = UNSET,
    installment: int | Unset = UNSET,
    method: SimulatePaymentMethodsMethod,
    brand: str | Unset = UNSET,
) -> Response[SimulatePaymentMethodsResponse200]:
    """Simulate the fees and totals for a single payment method

    Args:
        amount (int):
        fee (float | Unset):
        installment (int | Unset):
        method (SimulatePaymentMethodsMethod):
        brand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SimulatePaymentMethodsResponse200]
    """

    kwargs = _get_kwargs(
        amount=amount,
        fee=fee,
        installment=installment,
        method=method,
        brand=brand,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    amount: int,
    fee: float | Unset = UNSET,
    installment: int | Unset = UNSET,
    method: SimulatePaymentMethodsMethod,
    brand: str | Unset = UNSET,
) -> SimulatePaymentMethodsResponse200 | None:
    """Simulate the fees and totals for a single payment method

    Args:
        amount (int):
        fee (float | Unset):
        installment (int | Unset):
        method (SimulatePaymentMethodsMethod):
        brand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SimulatePaymentMethodsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            amount=amount,
            fee=fee,
            installment=installment,
            method=method,
            brand=brand,
        )
    ).parsed
