from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.simulate_installment_resource import SimulateInstallmentResource
from ...models.simulate_installment_response_200 import SimulateInstallmentResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    amount: int,
    fee: float | Unset = UNSET,
    installment: int,
    resource: SimulateInstallmentResource | Unset = SimulateInstallmentResource.CREDIT,
    brand: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["amount"] = amount

    params["fee"] = fee

    params["installment"] = installment

    json_resource: str | Unset = UNSET
    if not isinstance(resource, Unset):
        json_resource = resource.value

    params["resource"] = json_resource

    params["brand"] = brand

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/simulators/installment",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> SimulateInstallmentResponse200 | None:
    if response.status_code == 200:
        response_200 = SimulateInstallmentResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[SimulateInstallmentResponse200]:
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
    installment: int,
    resource: SimulateInstallmentResource | Unset = SimulateInstallmentResource.CREDIT,
    brand: str | Unset = UNSET,
) -> Response[SimulateInstallmentResponse200]:
    """Simulate fees and totals for a single installment count (credit/nupay)

    Args:
        amount (int):
        fee (float | Unset):
        installment (int):
        resource (SimulateInstallmentResource | Unset):  Default:
            SimulateInstallmentResource.CREDIT.
        brand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SimulateInstallmentResponse200]
    """

    kwargs = _get_kwargs(
        amount=amount,
        fee=fee,
        installment=installment,
        resource=resource,
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
    installment: int,
    resource: SimulateInstallmentResource | Unset = SimulateInstallmentResource.CREDIT,
    brand: str | Unset = UNSET,
) -> SimulateInstallmentResponse200 | None:
    """Simulate fees and totals for a single installment count (credit/nupay)

    Args:
        amount (int):
        fee (float | Unset):
        installment (int):
        resource (SimulateInstallmentResource | Unset):  Default:
            SimulateInstallmentResource.CREDIT.
        brand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SimulateInstallmentResponse200
    """

    return sync_detailed(
        client=client,
        amount=amount,
        fee=fee,
        installment=installment,
        resource=resource,
        brand=brand,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    amount: int,
    fee: float | Unset = UNSET,
    installment: int,
    resource: SimulateInstallmentResource | Unset = SimulateInstallmentResource.CREDIT,
    brand: str | Unset = UNSET,
) -> Response[SimulateInstallmentResponse200]:
    """Simulate fees and totals for a single installment count (credit/nupay)

    Args:
        amount (int):
        fee (float | Unset):
        installment (int):
        resource (SimulateInstallmentResource | Unset):  Default:
            SimulateInstallmentResource.CREDIT.
        brand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SimulateInstallmentResponse200]
    """

    kwargs = _get_kwargs(
        amount=amount,
        fee=fee,
        installment=installment,
        resource=resource,
        brand=brand,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    amount: int,
    fee: float | Unset = UNSET,
    installment: int,
    resource: SimulateInstallmentResource | Unset = SimulateInstallmentResource.CREDIT,
    brand: str | Unset = UNSET,
) -> SimulateInstallmentResponse200 | None:
    """Simulate fees and totals for a single installment count (credit/nupay)

    Args:
        amount (int):
        fee (float | Unset):
        installment (int):
        resource (SimulateInstallmentResource | Unset):  Default:
            SimulateInstallmentResource.CREDIT.
        brand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SimulateInstallmentResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            amount=amount,
            fee=fee,
            installment=installment,
            resource=resource,
            brand=brand,
        )
    ).parsed
