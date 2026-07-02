from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_transaction_response_200_customer_type_0_document import (
        GetTransactionResponse200CustomerType0Document,
    )
    from ..models.get_transaction_response_200_customer_type_0_telephone import (
        GetTransactionResponse200CustomerType0Telephone,
    )


T = TypeVar("T", bound="GetTransactionResponse200CustomerType0")


@_attrs_define
class GetTransactionResponse200CustomerType0:
    """
    Attributes:
        id (str): Public identifier (cus_…)
        first_name (None | str):
        last_name (None | str):
        email (None | str):
        birthdate (None | str):
        gender (None | str):
        document (GetTransactionResponse200CustomerType0Document):
        telephone (GetTransactionResponse200CustomerType0Telephone):
        available (bool | None):
        delinquent (bool | None):
        external_reference (None | str):
        updated_at (None | str):
        created_at (None | str):
        additional_emails (Any | Unset):
        metadata (Any | Unset):
    """

    id: str
    first_name: None | str
    last_name: None | str
    email: None | str
    birthdate: None | str
    gender: None | str
    document: GetTransactionResponse200CustomerType0Document
    telephone: GetTransactionResponse200CustomerType0Telephone
    available: bool | None
    delinquent: bool | None
    external_reference: None | str
    updated_at: None | str
    created_at: None | str
    additional_emails: Any | Unset = UNSET
    metadata: Any | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        first_name: None | str
        first_name = self.first_name

        last_name: None | str
        last_name = self.last_name

        email: None | str
        email = self.email

        birthdate: None | str
        birthdate = self.birthdate

        gender: None | str
        gender = self.gender

        document = self.document.to_dict()

        telephone = self.telephone.to_dict()

        available: bool | None
        available = self.available

        delinquent: bool | None
        delinquent = self.delinquent

        external_reference: None | str
        external_reference = self.external_reference

        updated_at: None | str
        updated_at = self.updated_at

        created_at: None | str
        created_at = self.created_at

        additional_emails = self.additional_emails

        metadata = self.metadata

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "firstName": first_name,
                "lastName": last_name,
                "email": email,
                "birthdate": birthdate,
                "gender": gender,
                "document": document,
                "telephone": telephone,
                "available": available,
                "delinquent": delinquent,
                "externalReference": external_reference,
                "updatedAt": updated_at,
                "createdAt": created_at,
            }
        )
        if additional_emails is not UNSET:
            field_dict["additionalEmails"] = additional_emails
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_transaction_response_200_customer_type_0_document import (
            GetTransactionResponse200CustomerType0Document,
        )
        from ..models.get_transaction_response_200_customer_type_0_telephone import (
            GetTransactionResponse200CustomerType0Telephone,
        )

        d = dict(src_dict)
        id = d.pop("id")

        def _parse_first_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        first_name = _parse_first_name(d.pop("firstName"))

        def _parse_last_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_name = _parse_last_name(d.pop("lastName"))

        def _parse_email(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        email = _parse_email(d.pop("email"))

        def _parse_birthdate(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        birthdate = _parse_birthdate(d.pop("birthdate"))

        def _parse_gender(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        gender = _parse_gender(d.pop("gender"))

        document = GetTransactionResponse200CustomerType0Document.from_dict(
            d.pop("document")
        )

        telephone = GetTransactionResponse200CustomerType0Telephone.from_dict(
            d.pop("telephone")
        )

        def _parse_available(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        available = _parse_available(d.pop("available"))

        def _parse_delinquent(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        delinquent = _parse_delinquent(d.pop("delinquent"))

        def _parse_external_reference(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        external_reference = _parse_external_reference(d.pop("externalReference"))

        def _parse_updated_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        updated_at = _parse_updated_at(d.pop("updatedAt"))

        def _parse_created_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        created_at = _parse_created_at(d.pop("createdAt"))

        additional_emails = d.pop("additionalEmails", UNSET)

        metadata = d.pop("metadata", UNSET)

        get_transaction_response_200_customer_type_0 = cls(
            id=id,
            first_name=first_name,
            last_name=last_name,
            email=email,
            birthdate=birthdate,
            gender=gender,
            document=document,
            telephone=telephone,
            available=available,
            delinquent=delinquent,
            external_reference=external_reference,
            updated_at=updated_at,
            created_at=created_at,
            additional_emails=additional_emails,
            metadata=metadata,
        )

        return get_transaction_response_200_customer_type_0
