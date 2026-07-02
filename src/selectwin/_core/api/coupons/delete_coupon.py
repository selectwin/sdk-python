from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_coupon_response_200 import DeleteCouponResponse200
from ...types import Response


def _get_kwargs(
    coupon_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/coupons/{coupon_id}".format(
            coupon_id=quote(str(coupon_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DeleteCouponResponse200 | None:
    if response.status_code == 200:
        response_200 = DeleteCouponResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DeleteCouponResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    coupon_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DeleteCouponResponse200]:
    """Delete a coupon

    Args:
        coupon_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteCouponResponse200]
    """

    kwargs = _get_kwargs(
        coupon_id=coupon_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    coupon_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> DeleteCouponResponse200 | None:
    """Delete a coupon

    Args:
        coupon_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteCouponResponse200
    """

    return sync_detailed(
        coupon_id=coupon_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    coupon_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DeleteCouponResponse200]:
    """Delete a coupon

    Args:
        coupon_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteCouponResponse200]
    """

    kwargs = _get_kwargs(
        coupon_id=coupon_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    coupon_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> DeleteCouponResponse200 | None:
    """Delete a coupon

    Args:
        coupon_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteCouponResponse200
    """

    return (
        await asyncio_detailed(
            coupon_id=coupon_id,
            client=client,
        )
    ).parsed
