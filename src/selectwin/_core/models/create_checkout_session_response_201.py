from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.create_checkout_session_response_201_currency import (
    CreateCheckoutSessionResponse201Currency,
)
from ..models.create_checkout_session_response_201_custom_inputs import (
    CreateCheckoutSessionResponse201CustomInputs,
)
from ..models.create_checkout_session_response_201_object import (
    CreateCheckoutSessionResponse201Object,
)
from ..models.create_checkout_session_response_201_status import (
    CreateCheckoutSessionResponse201Status,
)

if TYPE_CHECKING:
    from ..models.create_checkout_session_response_201_address_type_0 import (
        CreateCheckoutSessionResponse201AddressType0,
    )
    from ..models.create_checkout_session_response_201_coupons_item import (
        CreateCheckoutSessionResponse201CouponsItem,
    )
    from ..models.create_checkout_session_response_201_customer_type_0 import (
        CreateCheckoutSessionResponse201CustomerType0,
    )
    from ..models.create_checkout_session_response_201_line_items_item import (
        CreateCheckoutSessionResponse201LineItemsItem,
    )
    from ..models.create_checkout_session_response_201_metadata_type_0 import (
        CreateCheckoutSessionResponse201MetadataType0,
    )
    from ..models.create_checkout_session_response_201_payment_methods_item_type_1 import (
        CreateCheckoutSessionResponse201PaymentMethodsItemType1,
    )
    from ..models.create_checkout_session_response_201_payment_selection_type_0 import (
        CreateCheckoutSessionResponse201PaymentSelectionType0,
    )
    from ..models.create_checkout_session_response_201_redirect_urls import (
        CreateCheckoutSessionResponse201RedirectUrls,
    )
    from ..models.create_checkout_session_response_201_totals import (
        CreateCheckoutSessionResponse201Totals,
    )
    from ..models.create_checkout_session_response_201_utm_type_0 import (
        CreateCheckoutSessionResponse201UtmType0,
    )


T = TypeVar("T", bound="CreateCheckoutSessionResponse201")


@_attrs_define
class CreateCheckoutSessionResponse201:
    """
    Attributes:
        object_ (CreateCheckoutSessionResponse201Object):
        id (str): Public identifier (sess_/ckts_/ses_…)
        url (None | str):
        status (CreateCheckoutSessionResponse201Status):
        ambient (str):
        source (None | str):
        currency (CreateCheckoutSessionResponse201Currency):
        line_items (list[CreateCheckoutSessionResponse201LineItemsItem]):
        totals (CreateCheckoutSessionResponse201Totals):
        coupons (list[CreateCheckoutSessionResponse201CouponsItem]):
        customer (CreateCheckoutSessionResponse201CustomerType0 | None):
        address (CreateCheckoutSessionResponse201AddressType0 | None):
        payment_methods (list[CreateCheckoutSessionResponse201PaymentMethodsItemType1 | str]):
        payment_selection (CreateCheckoutSessionResponse201PaymentSelectionType0 | None):
        redirect_urls (CreateCheckoutSessionResponse201RedirectUrls):
        utm (CreateCheckoutSessionResponse201UtmType0 | None):
        metadata (CreateCheckoutSessionResponse201MetadataType0 | None):
        custom_inputs (CreateCheckoutSessionResponse201CustomInputs):
        integration_type (None | str):
        integration_id (None | str):
        external_transaction_id (None | str):
        first_initialization (bool):
        online (bool):
        expires_at (None | str):
        created_at (str):
        updated_at (str):
    """

    object_: CreateCheckoutSessionResponse201Object
    id: str
    url: None | str
    status: CreateCheckoutSessionResponse201Status
    ambient: str
    source: None | str
    currency: CreateCheckoutSessionResponse201Currency
    line_items: list[CreateCheckoutSessionResponse201LineItemsItem]
    totals: CreateCheckoutSessionResponse201Totals
    coupons: list[CreateCheckoutSessionResponse201CouponsItem]
    customer: CreateCheckoutSessionResponse201CustomerType0 | None
    address: CreateCheckoutSessionResponse201AddressType0 | None
    payment_methods: list[CreateCheckoutSessionResponse201PaymentMethodsItemType1 | str]
    payment_selection: CreateCheckoutSessionResponse201PaymentSelectionType0 | None
    redirect_urls: CreateCheckoutSessionResponse201RedirectUrls
    utm: CreateCheckoutSessionResponse201UtmType0 | None
    metadata: CreateCheckoutSessionResponse201MetadataType0 | None
    custom_inputs: CreateCheckoutSessionResponse201CustomInputs
    integration_type: None | str
    integration_id: None | str
    external_transaction_id: None | str
    first_initialization: bool
    online: bool
    expires_at: None | str
    created_at: str
    updated_at: str

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_checkout_session_response_201_address_type_0 import (
            CreateCheckoutSessionResponse201AddressType0,
        )
        from ..models.create_checkout_session_response_201_customer_type_0 import (
            CreateCheckoutSessionResponse201CustomerType0,
        )
        from ..models.create_checkout_session_response_201_metadata_type_0 import (
            CreateCheckoutSessionResponse201MetadataType0,
        )
        from ..models.create_checkout_session_response_201_payment_methods_item_type_1 import (
            CreateCheckoutSessionResponse201PaymentMethodsItemType1,
        )
        from ..models.create_checkout_session_response_201_payment_selection_type_0 import (
            CreateCheckoutSessionResponse201PaymentSelectionType0,
        )
        from ..models.create_checkout_session_response_201_utm_type_0 import (
            CreateCheckoutSessionResponse201UtmType0,
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
        if isinstance(self.customer, CreateCheckoutSessionResponse201CustomerType0):
            customer = self.customer.to_dict()
        else:
            customer = self.customer

        address: dict[str, Any] | None
        if isinstance(self.address, CreateCheckoutSessionResponse201AddressType0):
            address = self.address.to_dict()
        else:
            address = self.address

        payment_methods = []
        for payment_methods_item_data in self.payment_methods:
            payment_methods_item: dict[str, Any] | str
            if isinstance(
                payment_methods_item_data,
                CreateCheckoutSessionResponse201PaymentMethodsItemType1,
            ):
                payment_methods_item = payment_methods_item_data.to_dict()
            else:
                payment_methods_item = payment_methods_item_data
            payment_methods.append(payment_methods_item)

        payment_selection: dict[str, Any] | None
        if isinstance(
            self.payment_selection,
            CreateCheckoutSessionResponse201PaymentSelectionType0,
        ):
            payment_selection = self.payment_selection.to_dict()
        else:
            payment_selection = self.payment_selection

        redirect_urls = self.redirect_urls.to_dict()

        utm: dict[str, Any] | None
        if isinstance(self.utm, CreateCheckoutSessionResponse201UtmType0):
            utm = self.utm.to_dict()
        else:
            utm = self.utm

        metadata: dict[str, Any] | None
        if isinstance(self.metadata, CreateCheckoutSessionResponse201MetadataType0):
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
        from ..models.create_checkout_session_response_201_address_type_0 import (
            CreateCheckoutSessionResponse201AddressType0,
        )
        from ..models.create_checkout_session_response_201_coupons_item import (
            CreateCheckoutSessionResponse201CouponsItem,
        )
        from ..models.create_checkout_session_response_201_customer_type_0 import (
            CreateCheckoutSessionResponse201CustomerType0,
        )
        from ..models.create_checkout_session_response_201_line_items_item import (
            CreateCheckoutSessionResponse201LineItemsItem,
        )
        from ..models.create_checkout_session_response_201_metadata_type_0 import (
            CreateCheckoutSessionResponse201MetadataType0,
        )
        from ..models.create_checkout_session_response_201_payment_methods_item_type_1 import (
            CreateCheckoutSessionResponse201PaymentMethodsItemType1,
        )
        from ..models.create_checkout_session_response_201_payment_selection_type_0 import (
            CreateCheckoutSessionResponse201PaymentSelectionType0,
        )
        from ..models.create_checkout_session_response_201_redirect_urls import (
            CreateCheckoutSessionResponse201RedirectUrls,
        )
        from ..models.create_checkout_session_response_201_totals import (
            CreateCheckoutSessionResponse201Totals,
        )
        from ..models.create_checkout_session_response_201_utm_type_0 import (
            CreateCheckoutSessionResponse201UtmType0,
        )

        d = dict(src_dict)
        object_ = CreateCheckoutSessionResponse201Object(d.pop("object"))

        id = d.pop("id")

        def _parse_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        url = _parse_url(d.pop("url"))

        status = CreateCheckoutSessionResponse201Status(d.pop("status"))

        ambient = d.pop("ambient")

        def _parse_source(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        source = _parse_source(d.pop("source"))

        currency = CreateCheckoutSessionResponse201Currency(d.pop("currency"))

        line_items = []
        _line_items = d.pop("lineItems")
        for line_items_item_data in _line_items:
            line_items_item = CreateCheckoutSessionResponse201LineItemsItem.from_dict(
                line_items_item_data
            )

            line_items.append(line_items_item)

        totals = CreateCheckoutSessionResponse201Totals.from_dict(d.pop("totals"))

        coupons = []
        _coupons = d.pop("coupons")
        for coupons_item_data in _coupons:
            coupons_item = CreateCheckoutSessionResponse201CouponsItem.from_dict(
                coupons_item_data
            )

            coupons.append(coupons_item)

        def _parse_customer(
            data: object,
        ) -> CreateCheckoutSessionResponse201CustomerType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                customer_type_0 = (
                    CreateCheckoutSessionResponse201CustomerType0.from_dict(data)
                )

                return customer_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateCheckoutSessionResponse201CustomerType0 | None, data)

        customer = _parse_customer(d.pop("customer"))

        def _parse_address(
            data: object,
        ) -> CreateCheckoutSessionResponse201AddressType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                address_type_0 = CreateCheckoutSessionResponse201AddressType0.from_dict(
                    data
                )

                return address_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateCheckoutSessionResponse201AddressType0 | None, data)

        address = _parse_address(d.pop("address"))

        payment_methods = []
        _payment_methods = d.pop("paymentMethods")
        for payment_methods_item_data in _payment_methods:

            def _parse_payment_methods_item(
                data: object,
            ) -> CreateCheckoutSessionResponse201PaymentMethodsItemType1 | str:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    payment_methods_item_type_1 = CreateCheckoutSessionResponse201PaymentMethodsItemType1.from_dict(
                        data
                    )

                    return payment_methods_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                return cast(
                    CreateCheckoutSessionResponse201PaymentMethodsItemType1 | str, data
                )

            payment_methods_item = _parse_payment_methods_item(
                payment_methods_item_data
            )

            payment_methods.append(payment_methods_item)

        def _parse_payment_selection(
            data: object,
        ) -> CreateCheckoutSessionResponse201PaymentSelectionType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                payment_selection_type_0 = (
                    CreateCheckoutSessionResponse201PaymentSelectionType0.from_dict(
                        data
                    )
                )

                return payment_selection_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CreateCheckoutSessionResponse201PaymentSelectionType0 | None, data
            )

        payment_selection = _parse_payment_selection(d.pop("paymentSelection"))

        redirect_urls = CreateCheckoutSessionResponse201RedirectUrls.from_dict(
            d.pop("redirectUrls")
        )

        def _parse_utm(data: object) -> CreateCheckoutSessionResponse201UtmType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                utm_type_0 = CreateCheckoutSessionResponse201UtmType0.from_dict(data)

                return utm_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateCheckoutSessionResponse201UtmType0 | None, data)

        utm = _parse_utm(d.pop("utm"))

        def _parse_metadata(
            data: object,
        ) -> CreateCheckoutSessionResponse201MetadataType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = (
                    CreateCheckoutSessionResponse201MetadataType0.from_dict(data)
                )

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateCheckoutSessionResponse201MetadataType0 | None, data)

        metadata = _parse_metadata(d.pop("metadata"))

        custom_inputs = CreateCheckoutSessionResponse201CustomInputs(
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

        create_checkout_session_response_201 = cls(
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

        return create_checkout_session_response_201
