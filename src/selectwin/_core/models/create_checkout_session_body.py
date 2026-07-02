from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.create_checkout_session_body_ambient import (
    CreateCheckoutSessionBodyAmbient,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_checkout_session_body_address import (
        CreateCheckoutSessionBodyAddress,
    )
    from ..models.create_checkout_session_body_client import (
        CreateCheckoutSessionBodyClient,
    )
    from ..models.create_checkout_session_body_cookies import (
        CreateCheckoutSessionBodyCookies,
    )
    from ..models.create_checkout_session_body_coupons_item_type_1 import (
        CreateCheckoutSessionBodyCouponsItemType1,
    )
    from ..models.create_checkout_session_body_customer import (
        CreateCheckoutSessionBodyCustomer,
    )
    from ..models.create_checkout_session_body_items_item import (
        CreateCheckoutSessionBodyItemsItem,
    )
    from ..models.create_checkout_session_body_line_items_item import (
        CreateCheckoutSessionBodyLineItemsItem,
    )
    from ..models.create_checkout_session_body_metadata import (
        CreateCheckoutSessionBodyMetadata,
    )
    from ..models.create_checkout_session_body_payment_methods_item_type_1 import (
        CreateCheckoutSessionBodyPaymentMethodsItemType1,
    )
    from ..models.create_checkout_session_body_redirect_urls import (
        CreateCheckoutSessionBodyRedirectUrls,
    )
    from ..models.create_checkout_session_body_shipping_delivery import (
        CreateCheckoutSessionBodyShippingDelivery,
    )
    from ..models.create_checkout_session_body_utm import CreateCheckoutSessionBodyUtm


T = TypeVar("T", bound="CreateCheckoutSessionBody")


@_attrs_define
class CreateCheckoutSessionBody:
    """
    Attributes:
        items (list[CreateCheckoutSessionBodyItemsItem] | Unset):
        line_items (list[CreateCheckoutSessionBodyLineItemsItem] | Unset):
        expires_at (datetime.datetime | Unset):
        customer (CreateCheckoutSessionBodyCustomer | Unset):
        address (CreateCheckoutSessionBodyAddress | Unset):
        client (CreateCheckoutSessionBodyClient | Unset):
        cookies (CreateCheckoutSessionBodyCookies | Unset):
        coupons (list[CreateCheckoutSessionBodyCouponsItemType1 | str] | Unset):
        payment_methods (list[CreateCheckoutSessionBodyPaymentMethodsItemType1 | str] | Unset):
        redirect_urls (CreateCheckoutSessionBodyRedirectUrls | Unset):
        shipping_delivery (CreateCheckoutSessionBodyShippingDelivery | Unset):
        source (str | Unset):
        language (str | Unset):
        timezone (str | Unset):
        total_amount (int | Unset):
        total_discount (int | Unset):
        total_shipping (int | Unset):
        total_tax (int | Unset):
        utm (CreateCheckoutSessionBodyUtm | Unset):
        metadata (CreateCheckoutSessionBodyMetadata | Unset):
        integration_type (str | Unset):
        integration_id (str | Unset):
        external_transaction_id (str | Unset):
        on_behalf_of (str | Unset): Public identifier (prefix_value)
        ambient (CreateCheckoutSessionBodyAmbient | Unset):
    """

    items: list[CreateCheckoutSessionBodyItemsItem] | Unset = UNSET
    line_items: list[CreateCheckoutSessionBodyLineItemsItem] | Unset = UNSET
    expires_at: datetime.datetime | Unset = UNSET
    customer: CreateCheckoutSessionBodyCustomer | Unset = UNSET
    address: CreateCheckoutSessionBodyAddress | Unset = UNSET
    client: CreateCheckoutSessionBodyClient | Unset = UNSET
    cookies: CreateCheckoutSessionBodyCookies | Unset = UNSET
    coupons: list[CreateCheckoutSessionBodyCouponsItemType1 | str] | Unset = UNSET
    payment_methods: (
        list[CreateCheckoutSessionBodyPaymentMethodsItemType1 | str] | Unset
    ) = UNSET
    redirect_urls: CreateCheckoutSessionBodyRedirectUrls | Unset = UNSET
    shipping_delivery: CreateCheckoutSessionBodyShippingDelivery | Unset = UNSET
    source: str | Unset = UNSET
    language: str | Unset = UNSET
    timezone: str | Unset = UNSET
    total_amount: int | Unset = UNSET
    total_discount: int | Unset = UNSET
    total_shipping: int | Unset = UNSET
    total_tax: int | Unset = UNSET
    utm: CreateCheckoutSessionBodyUtm | Unset = UNSET
    metadata: CreateCheckoutSessionBodyMetadata | Unset = UNSET
    integration_type: str | Unset = UNSET
    integration_id: str | Unset = UNSET
    external_transaction_id: str | Unset = UNSET
    on_behalf_of: str | Unset = UNSET
    ambient: CreateCheckoutSessionBodyAmbient | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_checkout_session_body_coupons_item_type_1 import (
            CreateCheckoutSessionBodyCouponsItemType1,
        )
        from ..models.create_checkout_session_body_payment_methods_item_type_1 import (
            CreateCheckoutSessionBodyPaymentMethodsItemType1,
        )

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        line_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.line_items, Unset):
            line_items = []
            for line_items_item_data in self.line_items:
                line_items_item = line_items_item_data.to_dict()
                line_items.append(line_items_item)

        expires_at: str | Unset = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.isoformat()

        customer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.customer, Unset):
            customer = self.customer.to_dict()

        address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        client: dict[str, Any] | Unset = UNSET
        if not isinstance(self.client, Unset):
            client = self.client.to_dict()

        cookies: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cookies, Unset):
            cookies = self.cookies.to_dict()

        coupons: list[dict[str, Any] | str] | Unset = UNSET
        if not isinstance(self.coupons, Unset):
            coupons = []
            for coupons_item_data in self.coupons:
                coupons_item: dict[str, Any] | str
                if isinstance(
                    coupons_item_data, CreateCheckoutSessionBodyCouponsItemType1
                ):
                    coupons_item = coupons_item_data.to_dict()
                else:
                    coupons_item = coupons_item_data
                coupons.append(coupons_item)

        payment_methods: list[dict[str, Any] | str] | Unset = UNSET
        if not isinstance(self.payment_methods, Unset):
            payment_methods = []
            for payment_methods_item_data in self.payment_methods:
                payment_methods_item: dict[str, Any] | str
                if isinstance(
                    payment_methods_item_data,
                    CreateCheckoutSessionBodyPaymentMethodsItemType1,
                ):
                    payment_methods_item = payment_methods_item_data.to_dict()
                else:
                    payment_methods_item = payment_methods_item_data
                payment_methods.append(payment_methods_item)

        redirect_urls: dict[str, Any] | Unset = UNSET
        if not isinstance(self.redirect_urls, Unset):
            redirect_urls = self.redirect_urls.to_dict()

        shipping_delivery: dict[str, Any] | Unset = UNSET
        if not isinstance(self.shipping_delivery, Unset):
            shipping_delivery = self.shipping_delivery.to_dict()

        source = self.source

        language = self.language

        timezone = self.timezone

        total_amount = self.total_amount

        total_discount = self.total_discount

        total_shipping = self.total_shipping

        total_tax = self.total_tax

        utm: dict[str, Any] | Unset = UNSET
        if not isinstance(self.utm, Unset):
            utm = self.utm.to_dict()

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        integration_type = self.integration_type

        integration_id = self.integration_id

        external_transaction_id = self.external_transaction_id

        on_behalf_of = self.on_behalf_of

        ambient: str | Unset = UNSET
        if not isinstance(self.ambient, Unset):
            ambient = self.ambient.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if items is not UNSET:
            field_dict["items"] = items
        if line_items is not UNSET:
            field_dict["lineItems"] = line_items
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at
        if customer is not UNSET:
            field_dict["customer"] = customer
        if address is not UNSET:
            field_dict["address"] = address
        if client is not UNSET:
            field_dict["client"] = client
        if cookies is not UNSET:
            field_dict["cookies"] = cookies
        if coupons is not UNSET:
            field_dict["coupons"] = coupons
        if payment_methods is not UNSET:
            field_dict["paymentMethods"] = payment_methods
        if redirect_urls is not UNSET:
            field_dict["redirectUrls"] = redirect_urls
        if shipping_delivery is not UNSET:
            field_dict["shippingDelivery"] = shipping_delivery
        if source is not UNSET:
            field_dict["source"] = source
        if language is not UNSET:
            field_dict["language"] = language
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if total_discount is not UNSET:
            field_dict["totalDiscount"] = total_discount
        if total_shipping is not UNSET:
            field_dict["totalShipping"] = total_shipping
        if total_tax is not UNSET:
            field_dict["totalTax"] = total_tax
        if utm is not UNSET:
            field_dict["utm"] = utm
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if integration_type is not UNSET:
            field_dict["integrationType"] = integration_type
        if integration_id is not UNSET:
            field_dict["integrationId"] = integration_id
        if external_transaction_id is not UNSET:
            field_dict["externalTransactionId"] = external_transaction_id
        if on_behalf_of is not UNSET:
            field_dict["onBehalfOf"] = on_behalf_of
        if ambient is not UNSET:
            field_dict["ambient"] = ambient

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_checkout_session_body_address import (
            CreateCheckoutSessionBodyAddress,
        )
        from ..models.create_checkout_session_body_client import (
            CreateCheckoutSessionBodyClient,
        )
        from ..models.create_checkout_session_body_cookies import (
            CreateCheckoutSessionBodyCookies,
        )
        from ..models.create_checkout_session_body_coupons_item_type_1 import (
            CreateCheckoutSessionBodyCouponsItemType1,
        )
        from ..models.create_checkout_session_body_customer import (
            CreateCheckoutSessionBodyCustomer,
        )
        from ..models.create_checkout_session_body_items_item import (
            CreateCheckoutSessionBodyItemsItem,
        )
        from ..models.create_checkout_session_body_line_items_item import (
            CreateCheckoutSessionBodyLineItemsItem,
        )
        from ..models.create_checkout_session_body_metadata import (
            CreateCheckoutSessionBodyMetadata,
        )
        from ..models.create_checkout_session_body_payment_methods_item_type_1 import (
            CreateCheckoutSessionBodyPaymentMethodsItemType1,
        )
        from ..models.create_checkout_session_body_redirect_urls import (
            CreateCheckoutSessionBodyRedirectUrls,
        )
        from ..models.create_checkout_session_body_shipping_delivery import (
            CreateCheckoutSessionBodyShippingDelivery,
        )
        from ..models.create_checkout_session_body_utm import (
            CreateCheckoutSessionBodyUtm,
        )

        d = dict(src_dict)
        _items = d.pop("items", UNSET)
        items: list[CreateCheckoutSessionBodyItemsItem] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = CreateCheckoutSessionBodyItemsItem.from_dict(
                    items_item_data
                )

                items.append(items_item)

        _line_items = d.pop("lineItems", UNSET)
        line_items: list[CreateCheckoutSessionBodyLineItemsItem] | Unset = UNSET
        if _line_items is not UNSET:
            line_items = []
            for line_items_item_data in _line_items:
                line_items_item = CreateCheckoutSessionBodyLineItemsItem.from_dict(
                    line_items_item_data
                )

                line_items.append(line_items_item)

        _expires_at = d.pop("expiresAt", UNSET)
        expires_at: datetime.datetime | Unset
        if isinstance(_expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = datetime.datetime.fromisoformat(_expires_at)

        _customer = d.pop("customer", UNSET)
        customer: CreateCheckoutSessionBodyCustomer | Unset
        if isinstance(_customer, Unset):
            customer = UNSET
        else:
            customer = CreateCheckoutSessionBodyCustomer.from_dict(_customer)

        _address = d.pop("address", UNSET)
        address: CreateCheckoutSessionBodyAddress | Unset
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = CreateCheckoutSessionBodyAddress.from_dict(_address)

        _client = d.pop("client", UNSET)
        client: CreateCheckoutSessionBodyClient | Unset
        if isinstance(_client, Unset):
            client = UNSET
        else:
            client = CreateCheckoutSessionBodyClient.from_dict(_client)

        _cookies = d.pop("cookies", UNSET)
        cookies: CreateCheckoutSessionBodyCookies | Unset
        if isinstance(_cookies, Unset):
            cookies = UNSET
        else:
            cookies = CreateCheckoutSessionBodyCookies.from_dict(_cookies)

        _coupons = d.pop("coupons", UNSET)
        coupons: list[CreateCheckoutSessionBodyCouponsItemType1 | str] | Unset = UNSET
        if _coupons is not UNSET:
            coupons = []
            for coupons_item_data in _coupons:

                def _parse_coupons_item(
                    data: object,
                ) -> CreateCheckoutSessionBodyCouponsItemType1 | str:
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        coupons_item_type_1 = (
                            CreateCheckoutSessionBodyCouponsItemType1.from_dict(data)
                        )

                        return coupons_item_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    return cast(CreateCheckoutSessionBodyCouponsItemType1 | str, data)

                coupons_item = _parse_coupons_item(coupons_item_data)

                coupons.append(coupons_item)

        _payment_methods = d.pop("paymentMethods", UNSET)
        payment_methods: (
            list[CreateCheckoutSessionBodyPaymentMethodsItemType1 | str] | Unset
        ) = UNSET
        if _payment_methods is not UNSET:
            payment_methods = []
            for payment_methods_item_data in _payment_methods:

                def _parse_payment_methods_item(
                    data: object,
                ) -> CreateCheckoutSessionBodyPaymentMethodsItemType1 | str:
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        payment_methods_item_type_1 = (
                            CreateCheckoutSessionBodyPaymentMethodsItemType1.from_dict(
                                data
                            )
                        )

                        return payment_methods_item_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    return cast(
                        CreateCheckoutSessionBodyPaymentMethodsItemType1 | str, data
                    )

                payment_methods_item = _parse_payment_methods_item(
                    payment_methods_item_data
                )

                payment_methods.append(payment_methods_item)

        _redirect_urls = d.pop("redirectUrls", UNSET)
        redirect_urls: CreateCheckoutSessionBodyRedirectUrls | Unset
        if isinstance(_redirect_urls, Unset):
            redirect_urls = UNSET
        else:
            redirect_urls = CreateCheckoutSessionBodyRedirectUrls.from_dict(
                _redirect_urls
            )

        _shipping_delivery = d.pop("shippingDelivery", UNSET)
        shipping_delivery: CreateCheckoutSessionBodyShippingDelivery | Unset
        if isinstance(_shipping_delivery, Unset):
            shipping_delivery = UNSET
        else:
            shipping_delivery = CreateCheckoutSessionBodyShippingDelivery.from_dict(
                _shipping_delivery
            )

        source = d.pop("source", UNSET)

        language = d.pop("language", UNSET)

        timezone = d.pop("timezone", UNSET)

        total_amount = d.pop("totalAmount", UNSET)

        total_discount = d.pop("totalDiscount", UNSET)

        total_shipping = d.pop("totalShipping", UNSET)

        total_tax = d.pop("totalTax", UNSET)

        _utm = d.pop("utm", UNSET)
        utm: CreateCheckoutSessionBodyUtm | Unset
        if isinstance(_utm, Unset):
            utm = UNSET
        else:
            utm = CreateCheckoutSessionBodyUtm.from_dict(_utm)

        _metadata = d.pop("metadata", UNSET)
        metadata: CreateCheckoutSessionBodyMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CreateCheckoutSessionBodyMetadata.from_dict(_metadata)

        integration_type = d.pop("integrationType", UNSET)

        integration_id = d.pop("integrationId", UNSET)

        external_transaction_id = d.pop("externalTransactionId", UNSET)

        on_behalf_of = d.pop("onBehalfOf", UNSET)

        _ambient = d.pop("ambient", UNSET)
        ambient: CreateCheckoutSessionBodyAmbient | Unset
        if isinstance(_ambient, Unset):
            ambient = UNSET
        else:
            ambient = CreateCheckoutSessionBodyAmbient(_ambient)

        create_checkout_session_body = cls(
            items=items,
            line_items=line_items,
            expires_at=expires_at,
            customer=customer,
            address=address,
            client=client,
            cookies=cookies,
            coupons=coupons,
            payment_methods=payment_methods,
            redirect_urls=redirect_urls,
            shipping_delivery=shipping_delivery,
            source=source,
            language=language,
            timezone=timezone,
            total_amount=total_amount,
            total_discount=total_discount,
            total_shipping=total_shipping,
            total_tax=total_tax,
            utm=utm,
            metadata=metadata,
            integration_type=integration_type,
            integration_id=integration_id,
            external_transaction_id=external_transaction_id,
            on_behalf_of=on_behalf_of,
            ambient=ambient,
        )

        return create_checkout_session_body
