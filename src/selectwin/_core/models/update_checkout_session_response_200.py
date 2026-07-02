from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.update_checkout_session_response_200_currency import (
    UpdateCheckoutSessionResponse200Currency,
)
from ..models.update_checkout_session_response_200_custom_inputs import (
    UpdateCheckoutSessionResponse200CustomInputs,
)
from ..models.update_checkout_session_response_200_object import (
    UpdateCheckoutSessionResponse200Object,
)
from ..models.update_checkout_session_response_200_status import (
    UpdateCheckoutSessionResponse200Status,
)

if TYPE_CHECKING:
    from ..models.update_checkout_session_response_200_address_type_0 import (
        UpdateCheckoutSessionResponse200AddressType0,
    )
    from ..models.update_checkout_session_response_200_coupons_item import (
        UpdateCheckoutSessionResponse200CouponsItem,
    )
    from ..models.update_checkout_session_response_200_customer_type_0 import (
        UpdateCheckoutSessionResponse200CustomerType0,
    )
    from ..models.update_checkout_session_response_200_line_items_item import (
        UpdateCheckoutSessionResponse200LineItemsItem,
    )
    from ..models.update_checkout_session_response_200_metadata_type_0 import (
        UpdateCheckoutSessionResponse200MetadataType0,
    )
    from ..models.update_checkout_session_response_200_payment_methods_item_type_1 import (
        UpdateCheckoutSessionResponse200PaymentMethodsItemType1,
    )
    from ..models.update_checkout_session_response_200_payment_selection_type_0 import (
        UpdateCheckoutSessionResponse200PaymentSelectionType0,
    )
    from ..models.update_checkout_session_response_200_redirect_urls import (
        UpdateCheckoutSessionResponse200RedirectUrls,
    )
    from ..models.update_checkout_session_response_200_totals import (
        UpdateCheckoutSessionResponse200Totals,
    )
    from ..models.update_checkout_session_response_200_utm_type_0 import (
        UpdateCheckoutSessionResponse200UtmType0,
    )


T = TypeVar("T", bound="UpdateCheckoutSessionResponse200")


@_attrs_define
class UpdateCheckoutSessionResponse200:
    """
    Attributes:
        object_ (UpdateCheckoutSessionResponse200Object):
        id (str): Public identifier (sess_/ckts_/ses_…)
        url (None | str):
        status (UpdateCheckoutSessionResponse200Status):
        ambient (str):
        source (None | str):
        currency (UpdateCheckoutSessionResponse200Currency):
        line_items (list[UpdateCheckoutSessionResponse200LineItemsItem]):
        totals (UpdateCheckoutSessionResponse200Totals):
        coupons (list[UpdateCheckoutSessionResponse200CouponsItem]):
        customer (None | UpdateCheckoutSessionResponse200CustomerType0):
        address (None | UpdateCheckoutSessionResponse200AddressType0):
        payment_methods (list[str | UpdateCheckoutSessionResponse200PaymentMethodsItemType1]):
        payment_selection (None | UpdateCheckoutSessionResponse200PaymentSelectionType0):
        redirect_urls (UpdateCheckoutSessionResponse200RedirectUrls):
        utm (None | UpdateCheckoutSessionResponse200UtmType0):
        metadata (None | UpdateCheckoutSessionResponse200MetadataType0):
        custom_inputs (UpdateCheckoutSessionResponse200CustomInputs):
        integration_type (None | str):
        integration_id (None | str):
        external_transaction_id (None | str):
        first_initialization (bool):
        online (bool):
        expires_at (None | str):
        created_at (str):
        updated_at (str):
    """

    object_: UpdateCheckoutSessionResponse200Object
    id: str
    url: None | str
    status: UpdateCheckoutSessionResponse200Status
    ambient: str
    source: None | str
    currency: UpdateCheckoutSessionResponse200Currency
    line_items: list[UpdateCheckoutSessionResponse200LineItemsItem]
    totals: UpdateCheckoutSessionResponse200Totals
    coupons: list[UpdateCheckoutSessionResponse200CouponsItem]
    customer: None | UpdateCheckoutSessionResponse200CustomerType0
    address: None | UpdateCheckoutSessionResponse200AddressType0
    payment_methods: list[str | UpdateCheckoutSessionResponse200PaymentMethodsItemType1]
    payment_selection: None | UpdateCheckoutSessionResponse200PaymentSelectionType0
    redirect_urls: UpdateCheckoutSessionResponse200RedirectUrls
    utm: None | UpdateCheckoutSessionResponse200UtmType0
    metadata: None | UpdateCheckoutSessionResponse200MetadataType0
    custom_inputs: UpdateCheckoutSessionResponse200CustomInputs
    integration_type: None | str
    integration_id: None | str
    external_transaction_id: None | str
    first_initialization: bool
    online: bool
    expires_at: None | str
    created_at: str
    updated_at: str

    def to_dict(self) -> dict[str, Any]:
        from ..models.update_checkout_session_response_200_address_type_0 import (
            UpdateCheckoutSessionResponse200AddressType0,
        )
        from ..models.update_checkout_session_response_200_customer_type_0 import (
            UpdateCheckoutSessionResponse200CustomerType0,
        )
        from ..models.update_checkout_session_response_200_metadata_type_0 import (
            UpdateCheckoutSessionResponse200MetadataType0,
        )
        from ..models.update_checkout_session_response_200_payment_methods_item_type_1 import (
            UpdateCheckoutSessionResponse200PaymentMethodsItemType1,
        )
        from ..models.update_checkout_session_response_200_payment_selection_type_0 import (
            UpdateCheckoutSessionResponse200PaymentSelectionType0,
        )
        from ..models.update_checkout_session_response_200_utm_type_0 import (
            UpdateCheckoutSessionResponse200UtmType0,
        )

        object_ = self.object_.value

        id = self.id

        url: None | str
        url = self.url

        status = self.status.value

        ambient = self.ambient

        source: None | str
        source = self.source

        currency = self.currency.value

        line_items = []
        for line_items_item_data in self.line_items:
            line_items_item = line_items_item_data.to_dict()
            line_items.append(line_items_item)

        totals = self.totals.to_dict()

        coupons = []
        for coupons_item_data in self.coupons:
            coupons_item = coupons_item_data.to_dict()
            coupons.append(coupons_item)

        customer: dict[str, Any] | None
        if isinstance(self.customer, UpdateCheckoutSessionResponse200CustomerType0):
            customer = self.customer.to_dict()
        else:
            customer = self.customer

        address: dict[str, Any] | None
        if isinstance(self.address, UpdateCheckoutSessionResponse200AddressType0):
            address = self.address.to_dict()
        else:
            address = self.address

        payment_methods = []
        for payment_methods_item_data in self.payment_methods:
            payment_methods_item: dict[str, Any] | str
            if isinstance(
                payment_methods_item_data,
                UpdateCheckoutSessionResponse200PaymentMethodsItemType1,
            ):
                payment_methods_item = payment_methods_item_data.to_dict()
            else:
                payment_methods_item = payment_methods_item_data
            payment_methods.append(payment_methods_item)

        payment_selection: dict[str, Any] | None
        if isinstance(
            self.payment_selection,
            UpdateCheckoutSessionResponse200PaymentSelectionType0,
        ):
            payment_selection = self.payment_selection.to_dict()
        else:
            payment_selection = self.payment_selection

        redirect_urls = self.redirect_urls.to_dict()

        utm: dict[str, Any] | None
        if isinstance(self.utm, UpdateCheckoutSessionResponse200UtmType0):
            utm = self.utm.to_dict()
        else:
            utm = self.utm

        metadata: dict[str, Any] | None
        if isinstance(self.metadata, UpdateCheckoutSessionResponse200MetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        custom_inputs = self.custom_inputs.value

        integration_type: None | str
        integration_type = self.integration_type

        integration_id: None | str
        integration_id = self.integration_id

        external_transaction_id: None | str
        external_transaction_id = self.external_transaction_id

        first_initialization = self.first_initialization

        online = self.online

        expires_at: None | str
        expires_at = self.expires_at

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "object": object_,
                "id": id,
                "url": url,
                "status": status,
                "ambient": ambient,
                "source": source,
                "currency": currency,
                "lineItems": line_items,
                "totals": totals,
                "coupons": coupons,
                "customer": customer,
                "address": address,
                "paymentMethods": payment_methods,
                "paymentSelection": payment_selection,
                "redirectUrls": redirect_urls,
                "utm": utm,
                "metadata": metadata,
                "customInputs": custom_inputs,
                "integrationType": integration_type,
                "integrationId": integration_id,
                "externalTransactionId": external_transaction_id,
                "firstInitialization": first_initialization,
                "online": online,
                "expiresAt": expires_at,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_checkout_session_response_200_address_type_0 import (
            UpdateCheckoutSessionResponse200AddressType0,
        )
        from ..models.update_checkout_session_response_200_coupons_item import (
            UpdateCheckoutSessionResponse200CouponsItem,
        )
        from ..models.update_checkout_session_response_200_customer_type_0 import (
            UpdateCheckoutSessionResponse200CustomerType0,
        )
        from ..models.update_checkout_session_response_200_line_items_item import (
            UpdateCheckoutSessionResponse200LineItemsItem,
        )
        from ..models.update_checkout_session_response_200_metadata_type_0 import (
            UpdateCheckoutSessionResponse200MetadataType0,
        )
        from ..models.update_checkout_session_response_200_payment_methods_item_type_1 import (
            UpdateCheckoutSessionResponse200PaymentMethodsItemType1,
        )
        from ..models.update_checkout_session_response_200_payment_selection_type_0 import (
            UpdateCheckoutSessionResponse200PaymentSelectionType0,
        )
        from ..models.update_checkout_session_response_200_redirect_urls import (
            UpdateCheckoutSessionResponse200RedirectUrls,
        )
        from ..models.update_checkout_session_response_200_totals import (
            UpdateCheckoutSessionResponse200Totals,
        )
        from ..models.update_checkout_session_response_200_utm_type_0 import (
            UpdateCheckoutSessionResponse200UtmType0,
        )

        d = dict(src_dict)
        object_ = UpdateCheckoutSessionResponse200Object(d.pop("object"))

        id = d.pop("id")

        def _parse_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        url = _parse_url(d.pop("url"))

        status = UpdateCheckoutSessionResponse200Status(d.pop("status"))

        ambient = d.pop("ambient")

        def _parse_source(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        source = _parse_source(d.pop("source"))

        currency = UpdateCheckoutSessionResponse200Currency(d.pop("currency"))

        line_items = []
        _line_items = d.pop("lineItems")
        for line_items_item_data in _line_items:
            line_items_item = UpdateCheckoutSessionResponse200LineItemsItem.from_dict(
                line_items_item_data
            )

            line_items.append(line_items_item)

        totals = UpdateCheckoutSessionResponse200Totals.from_dict(d.pop("totals"))

        coupons = []
        _coupons = d.pop("coupons")
        for coupons_item_data in _coupons:
            coupons_item = UpdateCheckoutSessionResponse200CouponsItem.from_dict(
                coupons_item_data
            )

            coupons.append(coupons_item)

        def _parse_customer(
            data: object,
        ) -> None | UpdateCheckoutSessionResponse200CustomerType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                customer_type_0 = (
                    UpdateCheckoutSessionResponse200CustomerType0.from_dict(data)
                )

                return customer_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UpdateCheckoutSessionResponse200CustomerType0, data)

        customer = _parse_customer(d.pop("customer"))

        def _parse_address(
            data: object,
        ) -> None | UpdateCheckoutSessionResponse200AddressType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                address_type_0 = UpdateCheckoutSessionResponse200AddressType0.from_dict(
                    data
                )

                return address_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UpdateCheckoutSessionResponse200AddressType0, data)

        address = _parse_address(d.pop("address"))

        payment_methods = []
        _payment_methods = d.pop("paymentMethods")
        for payment_methods_item_data in _payment_methods:

            def _parse_payment_methods_item(
                data: object,
            ) -> str | UpdateCheckoutSessionResponse200PaymentMethodsItemType1:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    payment_methods_item_type_1 = UpdateCheckoutSessionResponse200PaymentMethodsItemType1.from_dict(
                        data
                    )

                    return payment_methods_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                return cast(
                    str | UpdateCheckoutSessionResponse200PaymentMethodsItemType1, data
                )

            payment_methods_item = _parse_payment_methods_item(
                payment_methods_item_data
            )

            payment_methods.append(payment_methods_item)

        def _parse_payment_selection(
            data: object,
        ) -> None | UpdateCheckoutSessionResponse200PaymentSelectionType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                payment_selection_type_0 = (
                    UpdateCheckoutSessionResponse200PaymentSelectionType0.from_dict(
                        data
                    )
                )

                return payment_selection_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | UpdateCheckoutSessionResponse200PaymentSelectionType0, data
            )

        payment_selection = _parse_payment_selection(d.pop("paymentSelection"))

        redirect_urls = UpdateCheckoutSessionResponse200RedirectUrls.from_dict(
            d.pop("redirectUrls")
        )

        def _parse_utm(data: object) -> None | UpdateCheckoutSessionResponse200UtmType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                utm_type_0 = UpdateCheckoutSessionResponse200UtmType0.from_dict(data)

                return utm_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UpdateCheckoutSessionResponse200UtmType0, data)

        utm = _parse_utm(d.pop("utm"))

        def _parse_metadata(
            data: object,
        ) -> None | UpdateCheckoutSessionResponse200MetadataType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = (
                    UpdateCheckoutSessionResponse200MetadataType0.from_dict(data)
                )

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UpdateCheckoutSessionResponse200MetadataType0, data)

        metadata = _parse_metadata(d.pop("metadata"))

        custom_inputs = UpdateCheckoutSessionResponse200CustomInputs(
            d.pop("customInputs")
        )

        def _parse_integration_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        integration_type = _parse_integration_type(d.pop("integrationType"))

        def _parse_integration_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        integration_id = _parse_integration_id(d.pop("integrationId"))

        def _parse_external_transaction_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        external_transaction_id = _parse_external_transaction_id(
            d.pop("externalTransactionId")
        )

        first_initialization = d.pop("firstInitialization")

        online = d.pop("online")

        def _parse_expires_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        expires_at = _parse_expires_at(d.pop("expiresAt"))

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        update_checkout_session_response_200 = cls(
            object_=object_,
            id=id,
            url=url,
            status=status,
            ambient=ambient,
            source=source,
            currency=currency,
            line_items=line_items,
            totals=totals,
            coupons=coupons,
            customer=customer,
            address=address,
            payment_methods=payment_methods,
            payment_selection=payment_selection,
            redirect_urls=redirect_urls,
            utm=utm,
            metadata=metadata,
            custom_inputs=custom_inputs,
            integration_type=integration_type,
            integration_id=integration_id,
            external_transaction_id=external_transaction_id,
            first_initialization=first_initialization,
            online=online,
            expires_at=expires_at,
            created_at=created_at,
            updated_at=updated_at,
        )

        return update_checkout_session_response_200
