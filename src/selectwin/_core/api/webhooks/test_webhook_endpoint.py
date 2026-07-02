from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.test_webhook_endpoint_body_type_1 import TestWebhookEndpointBodyType1
from ...models.test_webhook_endpoint_response_202 import TestWebhookEndpointResponse202
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: Any | TestWebhookEndpointBodyType1,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/webhooks/{id}/test".format(
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, TestWebhookEndpointBodyType1):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> TestWebhookEndpointResponse202 | None:
    if response.status_code == 202:
        response_202 = TestWebhookEndpointResponse202.from_dict(response.json())

        return response_202

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[TestWebhookEndpointResponse202]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: Any | TestWebhookEndpointBodyType1,
) -> Response[TestWebhookEndpointResponse202]:
    """Send a synthetic ping to verify wiring

    Args:
        id (str):
        body (Any | TestWebhookEndpointBodyType1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TestWebhookEndpointResponse202]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: Any | TestWebhookEndpointBodyType1,
) -> TestWebhookEndpointResponse202 | None:
    """Send a synthetic ping to verify wiring

    Args:
        id (str):
        body (Any | TestWebhookEndpointBodyType1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TestWebhookEndpointResponse202
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: Any | TestWebhookEndpointBodyType1,
) -> Response[TestWebhookEndpointResponse202]:
    """Send a synthetic ping to verify wiring

    Args:
        id (str):
        body (Any | TestWebhookEndpointBodyType1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TestWebhookEndpointResponse202]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: Any | TestWebhookEndpointBodyType1,
) -> TestWebhookEndpointResponse202 | None:
    """Send a synthetic ping to verify wiring

    Args:
        id (str):
        body (Any | TestWebhookEndpointBodyType1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TestWebhookEndpointResponse202
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
