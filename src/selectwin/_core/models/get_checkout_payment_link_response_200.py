from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.get_checkout_payment_link_response_200_custom_inputs_type_0_item import (
        GetCheckoutPaymentLinkResponse200CustomInputsType0Item,
    )
    from ..models.get_checkout_payment_link_response_200_items_item import (
        GetCheckoutPaymentLinkResponse200ItemsItem,
    )
    from ..models.get_checkout_payment_link_response_200_metadata_type_0 import (
        GetCheckoutPaymentLinkResponse200MetadataType0,
    )


T = TypeVar("T", bound="GetCheckoutPaymentLinkResponse200")


@_attrs_define
class GetCheckoutPaymentLinkResponse200:
    """
    Attributes:
        id (str): Public identifier (link_…)
        name (str):
        type_ (None | str):
        enabled (bool):
        access_id (str):
        signature (str):
        access_full_url (None | str):
        session_id (None | str):
        editable (bool):
        items (list[GetCheckoutPaymentLinkResponse200ItemsItem]):
        discounts (list[Any] | None):
        custom_inputs (list[GetCheckoutPaymentLinkResponse200CustomInputsType0Item] | None):
        expires_at (None | str):
        available_at (None | str):
        template_id (None | str):
        integration_id (None | str):
        domain_id (None | str):
        metadata (GetCheckoutPaymentLinkResponse200MetadataType0 | None):
        created_at (str):
        updated_at (str):
    """

    id: str
    name: str
    type_: None | str
    enabled: bool
    access_id: str
    signature: str
    access_full_url: None | str
    session_id: None | str
    editable: bool
    items: list[GetCheckoutPaymentLinkResponse200ItemsItem]
    discounts: list[Any] | None
    custom_inputs: list[GetCheckoutPaymentLinkResponse200CustomInputsType0Item] | None
    expires_at: None | str
    available_at: None | str
    template_id: None | str
    integration_id: None | str
    domain_id: None | str
    metadata: GetCheckoutPaymentLinkResponse200MetadataType0 | None
    created_at: str
    updated_at: str

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_checkout_payment_link_response_200_metadata_type_0 import (
            GetCheckoutPaymentLinkResponse200MetadataType0,
        )

        id = self.id

        name = self.name

        type_: None | str
        type_ = self.type_

        enabled = self.enabled

        access_id = self.access_id

        signature = self.signature

        access_full_url: None | str
        access_full_url = self.access_full_url

        session_id: None | str
        session_id = self.session_id

        editable = self.editable

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        discounts: list[Any] | None
        if isinstance(self.discounts, list):
            discounts = self.discounts

        else:
            discounts = self.discounts

        custom_inputs: list[dict[str, Any]] | None
        if isinstance(self.custom_inputs, list):
            custom_inputs = []
            for custom_inputs_type_0_item_data in self.custom_inputs:
                custom_inputs_type_0_item = custom_inputs_type_0_item_data.to_dict()
                custom_inputs.append(custom_inputs_type_0_item)

        else:
            custom_inputs = self.custom_inputs

        expires_at: None | str
        expires_at = self.expires_at

        available_at: None | str
        available_at = self.available_at

        template_id: None | str
        template_id = self.template_id

        integration_id: None | str
        integration_id = self.integration_id

        domain_id: None | str
        domain_id = self.domain_id

        metadata: dict[str, Any] | None
        if isinstance(self.metadata, GetCheckoutPaymentLinkResponse200MetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "type": type_,
                "enabled": enabled,
                "accessId": access_id,
                "signature": signature,
                "accessFullUrl": access_full_url,
                "sessionId": session_id,
                "editable": editable,
                "items": items,
                "discounts": discounts,
                "customInputs": custom_inputs,
                "expiresAt": expires_at,
                "availableAt": available_at,
                "templateId": template_id,
                "integrationId": integration_id,
                "domainId": domain_id,
                "metadata": metadata,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_checkout_payment_link_response_200_custom_inputs_type_0_item import (
            GetCheckoutPaymentLinkResponse200CustomInputsType0Item,
        )
        from ..models.get_checkout_payment_link_response_200_items_item import (
            GetCheckoutPaymentLinkResponse200ItemsItem,
        )
        from ..models.get_checkout_payment_link_response_200_metadata_type_0 import (
            GetCheckoutPaymentLinkResponse200MetadataType0,
        )

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        def _parse_type_(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        type_ = _parse_type_(d.pop("type"))

        enabled = d.pop("enabled")

        access_id = d.pop("accessId")

        signature = d.pop("signature")

        def _parse_access_full_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        access_full_url = _parse_access_full_url(d.pop("accessFullUrl"))

        def _parse_session_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        session_id = _parse_session_id(d.pop("sessionId"))

        editable = d.pop("editable")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = GetCheckoutPaymentLinkResponse200ItemsItem.from_dict(
                items_item_data
            )

            items.append(items_item)

        def _parse_discounts(data: object) -> list[Any] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                discounts_type_0 = cast(list[Any], data)

                return discounts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Any] | None, data)

        discounts = _parse_discounts(d.pop("discounts"))

        def _parse_custom_inputs(
            data: object,
        ) -> list[GetCheckoutPaymentLinkResponse200CustomInputsType0Item] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                custom_inputs_type_0 = []
                _custom_inputs_type_0 = data
                for custom_inputs_type_0_item_data in _custom_inputs_type_0:
                    custom_inputs_type_0_item = GetCheckoutPaymentLinkResponse200CustomInputsType0Item.from_dict(
                        custom_inputs_type_0_item_data
                    )

                    custom_inputs_type_0.append(custom_inputs_type_0_item)

                return custom_inputs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[GetCheckoutPaymentLinkResponse200CustomInputsType0Item] | None,
                data,
            )

        custom_inputs = _parse_custom_inputs(d.pop("customInputs"))

        def _parse_expires_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        expires_at = _parse_expires_at(d.pop("expiresAt"))

        def _parse_available_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        available_at = _parse_available_at(d.pop("availableAt"))

        def _parse_template_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        template_id = _parse_template_id(d.pop("templateId"))

        def _parse_integration_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        integration_id = _parse_integration_id(d.pop("integrationId"))

        def _parse_domain_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        domain_id = _parse_domain_id(d.pop("domainId"))

        def _parse_metadata(
            data: object,
        ) -> GetCheckoutPaymentLinkResponse200MetadataType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = (
                    GetCheckoutPaymentLinkResponse200MetadataType0.from_dict(data)
                )

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetCheckoutPaymentLinkResponse200MetadataType0 | None, data)

        metadata = _parse_metadata(d.pop("metadata"))

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        get_checkout_payment_link_response_200 = cls(
            id=id,
            name=name,
            type_=type_,
            enabled=enabled,
            access_id=access_id,
            signature=signature,
            access_full_url=access_full_url,
            session_id=session_id,
            editable=editable,
            items=items,
            discounts=discounts,
            custom_inputs=custom_inputs,
            expires_at=expires_at,
            available_at=available_at,
            template_id=template_id,
            integration_id=integration_id,
            domain_id=domain_id,
            metadata=metadata,
            created_at=created_at,
            updated_at=updated_at,
        )

        return get_checkout_payment_link_response_200
