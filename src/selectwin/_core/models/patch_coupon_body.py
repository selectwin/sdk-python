from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.patch_coupon_body_scope import PatchCouponBodyScope
from ..models.patch_coupon_body_type import PatchCouponBodyType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchCouponBody")


@_attrs_define
class PatchCouponBody:
    """
    Attributes:
        name (str | Unset):
        code (str | Unset):
        type_ (PatchCouponBodyType | Unset):
        value (float | Unset):
        enabled (bool | Unset):
        min_cart_amount (int | Unset):
        max_cart_amount (int | Unset):
        min_cart_items (int | Unset):
        max_cart_items (int | Unset):
        usage_limit (int | Unset):
        usage_quantity (int | Unset):
        limit_one_use_per_customer (bool | Unset):
        is_cumulative (bool | Unset):
        init_date (datetime.datetime | Unset):
        end_date (datetime.datetime | Unset):
        allowed_item_ids (list[str] | Unset):
        allowed_customer_ids (list[str] | Unset):
        scope (PatchCouponBodyScope | Unset):
        recurring_cycles (int | None | Unset):
    """

    name: str | Unset = UNSET
    code: str | Unset = UNSET
    type_: PatchCouponBodyType | Unset = UNSET
    value: float | Unset = UNSET
    enabled: bool | Unset = UNSET
    min_cart_amount: int | Unset = UNSET
    max_cart_amount: int | Unset = UNSET
    min_cart_items: int | Unset = UNSET
    max_cart_items: int | Unset = UNSET
    usage_limit: int | Unset = UNSET
    usage_quantity: int | Unset = UNSET
    limit_one_use_per_customer: bool | Unset = UNSET
    is_cumulative: bool | Unset = UNSET
    init_date: datetime.datetime | Unset = UNSET
    end_date: datetime.datetime | Unset = UNSET
    allowed_item_ids: list[str] | Unset = UNSET
    allowed_customer_ids: list[str] | Unset = UNSET
    scope: PatchCouponBodyScope | Unset = UNSET
    recurring_cycles: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        code = self.code

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        value = self.value

        enabled = self.enabled

        min_cart_amount = self.min_cart_amount

        max_cart_amount = self.max_cart_amount

        min_cart_items = self.min_cart_items

        max_cart_items = self.max_cart_items

        usage_limit = self.usage_limit

        usage_quantity = self.usage_quantity

        limit_one_use_per_customer = self.limit_one_use_per_customer

        is_cumulative = self.is_cumulative

        init_date: str | Unset = UNSET
        if not isinstance(self.init_date, Unset):
            init_date = self.init_date.isoformat()

        end_date: str | Unset = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        allowed_item_ids: list[str] | Unset = UNSET
        if not isinstance(self.allowed_item_ids, Unset):
            allowed_item_ids = self.allowed_item_ids

        allowed_customer_ids: list[str] | Unset = UNSET
        if not isinstance(self.allowed_customer_ids, Unset):
            allowed_customer_ids = self.allowed_customer_ids

        scope: str | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.value

        recurring_cycles: int | None | Unset
        if isinstance(self.recurring_cycles, Unset):
            recurring_cycles = UNSET
        else:
            recurring_cycles = self.recurring_cycles

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if code is not UNSET:
            field_dict["code"] = code
        if type_ is not UNSET:
            field_dict["type"] = type_
        if value is not UNSET:
            field_dict["value"] = value
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if min_cart_amount is not UNSET:
            field_dict["minCartAmount"] = min_cart_amount
        if max_cart_amount is not UNSET:
            field_dict["maxCartAmount"] = max_cart_amount
        if min_cart_items is not UNSET:
            field_dict["minCartItems"] = min_cart_items
        if max_cart_items is not UNSET:
            field_dict["maxCartItems"] = max_cart_items
        if usage_limit is not UNSET:
            field_dict["usageLimit"] = usage_limit
        if usage_quantity is not UNSET:
            field_dict["usageQuantity"] = usage_quantity
        if limit_one_use_per_customer is not UNSET:
            field_dict["limitOneUsePerCustomer"] = limit_one_use_per_customer
        if is_cumulative is not UNSET:
            field_dict["isCumulative"] = is_cumulative
        if init_date is not UNSET:
            field_dict["initDate"] = init_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if allowed_item_ids is not UNSET:
            field_dict["allowedItemIds"] = allowed_item_ids
        if allowed_customer_ids is not UNSET:
            field_dict["allowedCustomerIds"] = allowed_customer_ids
        if scope is not UNSET:
            field_dict["scope"] = scope
        if recurring_cycles is not UNSET:
            field_dict["recurringCycles"] = recurring_cycles

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        code = d.pop("code", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: PatchCouponBodyType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = PatchCouponBodyType(_type_)

        value = d.pop("value", UNSET)

        enabled = d.pop("enabled", UNSET)

        min_cart_amount = d.pop("minCartAmount", UNSET)

        max_cart_amount = d.pop("maxCartAmount", UNSET)

        min_cart_items = d.pop("minCartItems", UNSET)

        max_cart_items = d.pop("maxCartItems", UNSET)

        usage_limit = d.pop("usageLimit", UNSET)

        usage_quantity = d.pop("usageQuantity", UNSET)

        limit_one_use_per_customer = d.pop("limitOneUsePerCustomer", UNSET)

        is_cumulative = d.pop("isCumulative", UNSET)

        _init_date = d.pop("initDate", UNSET)
        init_date: datetime.datetime | Unset
        if isinstance(_init_date, Unset):
            init_date = UNSET
        else:
            init_date = datetime.datetime.fromisoformat(_init_date)

        _end_date = d.pop("endDate", UNSET)
        end_date: datetime.datetime | Unset
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = datetime.datetime.fromisoformat(_end_date)

        allowed_item_ids = cast(list[str], d.pop("allowedItemIds", UNSET))

        allowed_customer_ids = cast(list[str], d.pop("allowedCustomerIds", UNSET))

        _scope = d.pop("scope", UNSET)
        scope: PatchCouponBodyScope | Unset
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = PatchCouponBodyScope(_scope)

        def _parse_recurring_cycles(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        recurring_cycles = _parse_recurring_cycles(d.pop("recurringCycles", UNSET))

        patch_coupon_body = cls(
            name=name,
            code=code,
            type_=type_,
            value=value,
            enabled=enabled,
            min_cart_amount=min_cart_amount,
            max_cart_amount=max_cart_amount,
            min_cart_items=min_cart_items,
            max_cart_items=max_cart_items,
            usage_limit=usage_limit,
            usage_quantity=usage_quantity,
            limit_one_use_per_customer=limit_one_use_per_customer,
            is_cumulative=is_cumulative,
            init_date=init_date,
            end_date=end_date,
            allowed_item_ids=allowed_item_ids,
            allowed_customer_ids=allowed_customer_ids,
            scope=scope,
            recurring_cycles=recurring_cycles,
        )

        return patch_coupon_body
