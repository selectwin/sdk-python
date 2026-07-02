from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.simulate_installments_resource import SimulateInstallmentsResource
from ...models.simulate_installments_response_200 import SimulateInstallmentsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    amount: int,
    fee: float | Unset = UNSET,
    resource: SimulateInstallmentsResource
    | Unset = SimulateInstallmentsResource.CREDIT,
    model: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["amount"] = amount

    params["fee"] = fee

    json_resource: str | Unset = UNSET
    if not isinstance(resource, Unset):
        json_resource = resource.value

    params["resource"] = json_resource

    params["model"] = model

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/simulators/installments",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> SimulateInstallmentsResponse200 | None:
    if response.status_code == 200:
        response_200 = SimulateInstallmentsResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[SimulateInstallmentsResponse200]:
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
    resource: SimulateInstallmentsResource
    | Unset = SimulateInstallmentsResource.CREDIT,
    model: str | Unset = UNSET,
) -> Response[SimulateInstallmentsResponse200]:
    """Simulate the installment table for an amount

    Args:
        amount (int):
        fee (float | Unset):
        resource (SimulateInstallmentsResource | Unset):  Default:
            SimulateInstallmentsResource.CREDIT.
        model (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SimulateInstallmentsResponse200]
    """

    kwargs = _get_kwargs(
        amount=amount,
        fee=fee,
        resource=resource,
        model=model,
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
    resource: SimulateInstallmentsResource
    | Unset = SimulateInstallmentsResource.CREDIT,
    model: str | Unset = UNSET,
) -> SimulateInstallmentsResponse200 | None:
    """Simulate the installment table for an amount

    Args:
        amount (int):
        fee (float | Unset):
        resource (SimulateInstallmentsResource | Unset):  Default:
            SimulateInstallmentsResource.CREDIT.
        model (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SimulateInstallmentsResponse200
    """

    return sync_detailed(
        client=client,
        amount=amount,
        fee=fee,
        resource=resource,
        model=model,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    amount: int,
    fee: float | Unset = UNSET,
    resource: SimulateInstallmentsResource
    | Unset = SimulateInstallmentsResource.CREDIT,
    model: str | Unset = UNSET,
) -> Response[SimulateInstallmentsResponse200]:
    """Simulate the installment table for an amount

    Args:
        amount (int):
        fee (float | Unset):
        resource (SimulateInstallmentsResource | Unset):  Default:
            SimulateInstallmentsResource.CREDIT.
        model (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SimulateInstallmentsResponse200]
    """

    kwargs = _get_kwargs(
        amount=amount,
        fee=fee,
        resource=resource,
        model=model,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    amount: int,
    fee: float | Unset = UNSET,
    resource: SimulateInstallmentsResource
    | Unset = SimulateInstallmentsResource.CREDIT,
    model: str | Unset = UNSET,
) -> SimulateInstallmentsResponse200 | None:
    """Simulate the installment table for an amount

    Args:
        amount (int):
        fee (float | Unset):
        resource (SimulateInstallmentsResource | Unset):  Default:
            SimulateInstallmentsResource.CREDIT.
        model (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SimulateInstallmentsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            amount=amount,
            fee=fee,
            resource=resource,
            model=model,
        )
    ).parsed
