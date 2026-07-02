from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubmitTransactionDisputeBodyDocumentsItemAuthentication")


@_attrs_define
class SubmitTransactionDisputeBodyDocumentsItemAuthentication:
    """
    Attributes:
        username (str | Unset):
        password (str | Unset):
        token (str | Unset):
    """

    username: str | Unset = UNSET
    password: str | Unset = UNSET
    token: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        password = self.password

        token = self.token

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if token is not UNSET:
            field_dict["token"] = token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        token = d.pop("token", UNSET)

        submit_transaction_dispute_body_documents_item_authentication = cls(
            username=username,
            password=password,
            token=token,
        )

        return submit_transaction_dispute_body_documents_item_authentication
