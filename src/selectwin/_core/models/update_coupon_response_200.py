from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.update_coupon_response_200_scope import UpdateCouponResponse200Scope
from ..models.update_coupon_response_200_type import UpdateCouponResponse200Type

T = TypeVar("T", bound="UpdateCouponResponse200")


@_attrs_define
class UpdateCouponResponse200:
    """
    Attributes:
        id (str): Public identifier (dis_/coup_…)
        name (None | str):
        code (None | str):
        type_ (UpdateCouponResponse200Type):
        value (float):
        enabled (bool):
        min_cart_amount (int | None):
        max_cart_amount (int | None):
        min_cart_items (int | None):
        max_cart_items (int | None):
        usage_limit (int | None):
        usage_quantity (int | None):
        limit_one_use_per_customer (bool):
        is_cumulative (bool):
        init_date (None | str):
        end_date (None | str):
        allowed_item_ids (list[Any] | None):
        allowed_customer_ids (list[Any] | None):
        scope (UpdateCouponResponse200Scope):
        recurring_cycles (int | None):
        created_at (str):
        updated_at (str):
    """

    id: str
    name: None | str
    code: None | str
    type_: UpdateCouponResponse200Type
    value: float
    enabled: bool
    min_cart_amount: int | None
    max_cart_amount: int | None
    min_cart_items: int | None
    max_cart_items: int | None
    usage_limit: int | None
    usage_quantity: int | None
    limit_one_use_per_customer: bool
    is_cumulative: bool
    init_date: None | str
    end_date: None | str
    allowed_item_ids: list[Any] | None
    allowed_customer_ids: list[Any] | None
    scope: UpdateCouponResponse200Scope
    recurring_cycles: int | None
    created_at: str
    updated_at: str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name: None | str
        name = self.name

        code: None | str
        code = self.code

        type_ = self.type_.value

        value = self.value

        enabled = self.enabled

        min_cart_amount: int | None
        min_cart_amount = self.min_cart_amount

        max_cart_amount: int | None
        max_cart_amount = self.max_cart_amount

        min_cart_items: int | None
        min_cart_items = self.min_cart_items

        max_cart_items: int | None
        max_cart_items = self.max_cart_items

        usage_limit: int | None
        usage_limit = self.usage_limit

        usage_quantity: int | None
        usage_quantity = self.usage_quantity

        limit_one_use_per_customer = self.limit_one_use_per_customer

        is_cumulative = self.is_cumulative

        init_date: None | str
        init_date = self.init_date

        end_date: None | str
        end_date = self.end_date

        allowed_item_ids: list[Any] | None
        if isinstance(self.allowed_item_ids, list):
            allowed_item_ids = self.allowed_item_ids

        else:
            allowed_item_ids = self.allowed_item_ids

        allowed_customer_ids: list[Any] | None
        if isinstance(self.allowed_customer_ids, list):
            allowed_customer_ids = self.allowed_customer_ids

        else:
            allowed_customer_ids = self.allowed_customer_ids

        scope = self.scope.value

        recurring_cycles: int | None
        recurring_cycles = self.recurring_cycles

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "code": code,
                "type": type_,
                "value": value,
                "enabled": enabled,
                "minCartAmount": min_cart_amount,
                "maxCartAmount": max_cart_amount,
                "minCartItems": min_cart_items,
                "maxCartItems": max_cart_items,
                "usageLimit": usage_limit,
                "usageQuantity": usage_quantity,
                "limitOneUsePerCustomer": limit_one_use_per_customer,
                "isCumulative": is_cumulative,
                "initDate": init_date,
                "endDate": end_date,
                "allowedItemIds": allowed_item_ids,
                "allowedCustomerIds": allowed_customer_ids,
                "scope": scope,
                "recurringCycles": recurring_cycles,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        def _parse_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        code = _parse_code(d.pop("code"))

        type_ = UpdateCouponResponse200Type(d.pop("type"))

        value = d.pop("value")

        enabled = d.pop("enabled")

        def _parse_min_cart_amount(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        min_cart_amount = _parse_min_cart_amount(d.pop("minCartAmount"))

        def _parse_max_cart_amount(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        max_cart_amount = _parse_max_cart_amount(d.pop("maxCartAmount"))

        def _parse_min_cart_items(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        min_cart_items = _parse_min_cart_items(d.pop("minCartItems"))

        def _parse_max_cart_items(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        max_cart_items = _parse_max_cart_items(d.pop("maxCartItems"))

        def _parse_usage_limit(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        usage_limit = _parse_usage_limit(d.pop("usageLimit"))

        def _parse_usage_quantity(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        usage_quantity = _parse_usage_quantity(d.pop("usageQuantity"))

        limit_one_use_per_customer = d.pop("limitOneUsePerCustomer")

        is_cumulative = d.pop("isCumulative")

        def _parse_init_date(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        init_date = _parse_init_date(d.pop("initDate"))

        def _parse_end_date(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        end_date = _parse_end_date(d.pop("endDate"))

        def _parse_allowed_item_ids(data: object) -> list[Any] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                allowed_item_ids_type_0 = cast(list[Any], data)

                return allowed_item_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Any] | None, data)

        allowed_item_ids = _parse_allowed_item_ids(d.pop("allowedItemIds"))

        def _parse_allowed_customer_ids(data: object) -> list[Any] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                allowed_customer_ids_type_0 = cast(list[Any], data)

                return allowed_customer_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Any] | None, data)

        allowed_customer_ids = _parse_allowed_customer_ids(d.pop("allowedCustomerIds"))

        scope = UpdateCouponResponse200Scope(d.pop("scope"))

        def _parse_recurring_cycles(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        recurring_cycles = _parse_recurring_cycles(d.pop("recurringCycles"))

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        update_coupon_response_200 = cls(
            id=id,
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
            created_at=created_at,
            updated_at=updated_at,
        )

        return update_coupon_response_200
