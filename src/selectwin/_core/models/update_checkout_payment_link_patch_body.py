from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_checkout_payment_link_patch_body_custom_inputs_item import (
        UpdateCheckoutPaymentLinkPatchBodyCustomInputsItem,
    )
    from ..models.update_checkout_payment_link_patch_body_items_item import (
        UpdateCheckoutPaymentLinkPatchBodyItemsItem,
    )
    from ..models.update_checkout_payment_link_patch_body_metadata import (
        UpdateCheckoutPaymentLinkPatchBodyMetadata,
    )


T = TypeVar("T", bound="UpdateCheckoutPaymentLinkPatchBody")


@_attrs_define
class UpdateCheckoutPaymentLinkPatchBody:
    """
    Attributes:
        name (str | Unset):
        items (list[UpdateCheckoutPaymentLinkPatchBodyItemsItem] | Unset):
        discounts (list[str] | Unset):
        custom_inputs (list[UpdateCheckoutPaymentLinkPatchBodyCustomInputsItem] | Unset):
        expires_at (datetime.datetime | Unset):
        available_at (datetime.datetime | Unset):
        editable (bool | Unset):
        template_id (str | Unset): Public identifier (tmpl_/ckt_…)
        metadata (UpdateCheckoutPaymentLinkPatchBodyMetadata | Unset):
    """

    name: str | Unset = UNSET
    items: list[UpdateCheckoutPaymentLinkPatchBodyItemsItem] | Unset = UNSET
    discounts: list[str] | Unset = UNSET
    custom_inputs: list[UpdateCheckoutPaymentLinkPatchBodyCustomInputsItem] | Unset = (
        UNSET
    )
    expires_at: datetime.datetime | Unset = UNSET
    available_at: datetime.datetime | Unset = UNSET
    editable: bool | Unset = UNSET
    template_id: str | Unset = UNSET
    metadata: UpdateCheckoutPaymentLinkPatchBodyMetadata | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        discounts: list[str] | Unset = UNSET
        if not isinstance(self.discounts, Unset):
            discounts = self.discounts

        custom_inputs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.custom_inputs, Unset):
            custom_inputs = []
            for custom_inputs_item_data in self.custom_inputs:
                custom_inputs_item = custom_inputs_item_data.to_dict()
                custom_inputs.append(custom_inputs_item)

        expires_at: str | Unset = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.isoformat()

        available_at: str | Unset = UNSET
        if not isinstance(self.available_at, Unset):
            available_at = self.available_at.isoformat()

        editable = self.editable

        template_id = self.template_id

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if items is not UNSET:
            field_dict["items"] = items
        if discounts is not UNSET:
            field_dict["discounts"] = discounts
        if custom_inputs is not UNSET:
            field_dict["customInputs"] = custom_inputs
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at
        if available_at is not UNSET:
            field_dict["availableAt"] = available_at
        if editable is not UNSET:
            field_dict["editable"] = editable
        if template_id is not UNSET:
            field_dict["templateId"] = template_id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_checkout_payment_link_patch_body_custom_inputs_item import (
            UpdateCheckoutPaymentLinkPatchBodyCustomInputsItem,
        )
        from ..models.update_checkout_payment_link_patch_body_items_item import (
            UpdateCheckoutPaymentLinkPatchBodyItemsItem,
        )
        from ..models.update_checkout_payment_link_patch_body_metadata import (
            UpdateCheckoutPaymentLinkPatchBodyMetadata,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _items = d.pop("items", UNSET)
        items: list[UpdateCheckoutPaymentLinkPatchBodyItemsItem] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = UpdateCheckoutPaymentLinkPatchBodyItemsItem.from_dict(
                    items_item_data
                )

                items.append(items_item)

        discounts = cast(list[str], d.pop("discounts", UNSET))

        _custom_inputs = d.pop("customInputs", UNSET)
        custom_inputs: (
            list[UpdateCheckoutPaymentLinkPatchBodyCustomInputsItem] | Unset
        ) = UNSET
        if _custom_inputs is not UNSET:
            custom_inputs = []
            for custom_inputs_item_data in _custom_inputs:
                custom_inputs_item = (
                    UpdateCheckoutPaymentLinkPatchBodyCustomInputsItem.from_dict(
                        custom_inputs_item_data
                    )
                )

                custom_inputs.append(custom_inputs_item)

        _expires_at = d.pop("expiresAt", UNSET)
        expires_at: datetime.datetime | Unset
        if isinstance(_expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = datetime.datetime.fromisoformat(_expires_at)

        _available_at = d.pop("availableAt", UNSET)
        available_at: datetime.datetime | Unset
        if isinstance(_available_at, Unset):
            available_at = UNSET
        else:
            available_at = datetime.datetime.fromisoformat(_available_at)

        editable = d.pop("editable", UNSET)

        template_id = d.pop("templateId", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: UpdateCheckoutPaymentLinkPatchBodyMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = UpdateCheckoutPaymentLinkPatchBodyMetadata.from_dict(_metadata)

        update_checkout_payment_link_patch_body = cls(
            name=name,
            items=items,
            discounts=discounts,
            custom_inputs=custom_inputs,
            expires_at=expires_at,
            available_at=available_at,
            editable=editable,
            template_id=template_id,
            metadata=metadata,
        )

        return update_checkout_payment_link_patch_body
