from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="CreateCheckoutSessionResponse201RedirectUrls")


@_attrs_define
class CreateCheckoutSessionResponse201RedirectUrls:
    """
    Attributes:
        paid (None | str):
        refused (None | str):
        pending (None | str):
    """

    paid: None | str
    refused: None | str
    pending: None | str

    def to_dict(self) -> dict[str, Any]:
        paid: None | str
        paid = self.paid

        refused: None | str
        refused = self.refused

        pending: None | str
        pending = self.pending

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "paid": paid,
                "refused": refused,
                "pending": pending,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_paid(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        paid = _parse_paid(d.pop("paid"))

        def _parse_refused(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        refused = _parse_refused(d.pop("refused"))

        def _parse_pending(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        pending = _parse_pending(d.pop("pending"))

        create_checkout_session_response_201_redirect_urls = cls(
            paid=paid,
            refused=refused,
            pending=pending,
        )

        return create_checkout_session_response_201_redirect_urls
