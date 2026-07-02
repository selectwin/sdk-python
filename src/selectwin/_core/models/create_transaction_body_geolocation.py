from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateTransactionBodyGeolocation")


@_attrs_define
class CreateTransactionBodyGeolocation:
    """
    Attributes:
        ip_address (Any | Unset):
        latitude (float | Unset):
        longitude (float | Unset):
        device_fingerprint (str | Unset):
        user_agent (str | Unset):
        accept_language (str | Unset):
    """

    ip_address: Any | Unset = UNSET
    latitude: float | Unset = UNSET
    longitude: float | Unset = UNSET
    device_fingerprint: str | Unset = UNSET
    user_agent: str | Unset = UNSET
    accept_language: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        ip_address: Any | Unset
        if isinstance(self.ip_address, Unset):
            ip_address = UNSET
        else:
            ip_address = self.ip_address

        latitude = self.latitude

        longitude = self.longitude

        device_fingerprint = self.device_fingerprint

        user_agent = self.user_agent

        accept_language = self.accept_language

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if ip_address is not UNSET:
            field_dict["ipAddress"] = ip_address
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if device_fingerprint is not UNSET:
            field_dict["deviceFingerprint"] = device_fingerprint
        if user_agent is not UNSET:
            field_dict["userAgent"] = user_agent
        if accept_language is not UNSET:
            field_dict["acceptLanguage"] = accept_language

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_ip_address(data: object) -> Any | Unset:
            if isinstance(data, Unset):
                return data
            return cast(Any | Unset, data)

        ip_address = _parse_ip_address(d.pop("ipAddress", UNSET))

        latitude = d.pop("latitude", UNSET)

        longitude = d.pop("longitude", UNSET)

        device_fingerprint = d.pop("deviceFingerprint", UNSET)

        user_agent = d.pop("userAgent", UNSET)

        accept_language = d.pop("acceptLanguage", UNSET)

        create_transaction_body_geolocation = cls(
            ip_address=ip_address,
            latitude=latitude,
            longitude=longitude,
            device_fingerprint=device_fingerprint,
            user_agent=user_agent,
            accept_language=accept_language,
        )

        return create_transaction_body_geolocation
