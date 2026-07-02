from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.update_customer_put_body_gender import UpdateCustomerPutBodyGender
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_customer_put_body_document import UpdateCustomerPutBodyDocument
    from ..models.update_customer_put_body_metadata import UpdateCustomerPutBodyMetadata
    from ..models.update_customer_put_body_telephone import (
        UpdateCustomerPutBodyTelephone,
    )


T = TypeVar("T", bound="UpdateCustomerPutBody")


@_attrs_define
class UpdateCustomerPutBody:
    """
    Attributes:
        first_name (str | Unset):
        last_name (str | Unset):
        email (str | Unset):
        document (UpdateCustomerPutBodyDocument | Unset):
        telephone (UpdateCustomerPutBodyTelephone | Unset):
        external_reference (str | Unset):
        gender (UpdateCustomerPutBodyGender | Unset):
        birthdate (str | Unset):
        additional_emails (list[str] | Unset):
        metadata (UpdateCustomerPutBodyMetadata | Unset):
    """

    first_name: str | Unset = UNSET
    last_name: str | Unset = UNSET
    email: str | Unset = UNSET
    document: UpdateCustomerPutBodyDocument | Unset = UNSET
    telephone: UpdateCustomerPutBodyTelephone | Unset = UNSET
    external_reference: str | Unset = UNSET
    gender: UpdateCustomerPutBodyGender | Unset = UNSET
    birthdate: str | Unset = UNSET
    additional_emails: list[str] | Unset = UNSET
    metadata: UpdateCustomerPutBodyMetadata | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        first_name = self.first_name

        last_name = self.last_name

        email = self.email

        document: dict[str, Any] | Unset = UNSET
        if not isinstance(self.document, Unset):
            document = self.document.to_dict()

        telephone: dict[str, Any] | Unset = UNSET
        if not isinstance(self.telephone, Unset):
            telephone = self.telephone.to_dict()

        external_reference = self.external_reference

        gender: str | Unset = UNSET
        if not isinstance(self.gender, Unset):
            gender = self.gender.value

        birthdate = self.birthdate

        additional_emails: list[str] | Unset = UNSET
        if not isinstance(self.additional_emails, Unset):
            additional_emails = self.additional_emails

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if email is not UNSET:
            field_dict["email"] = email
        if document is not UNSET:
            field_dict["document"] = document
        if telephone is not UNSET:
            field_dict["telephone"] = telephone
        if external_reference is not UNSET:
            field_dict["externalReference"] = external_reference
        if gender is not UNSET:
            field_dict["gender"] = gender
        if birthdate is not UNSET:
            field_dict["birthdate"] = birthdate
        if additional_emails is not UNSET:
            field_dict["additionalEmails"] = additional_emails
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_customer_put_body_document import (
            UpdateCustomerPutBodyDocument,
        )
        from ..models.update_customer_put_body_metadata import (
            UpdateCustomerPutBodyMetadata,
        )
        from ..models.update_customer_put_body_telephone import (
            UpdateCustomerPutBodyTelephone,
        )

        d = dict(src_dict)
        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        email = d.pop("email", UNSET)

        _document = d.pop("document", UNSET)
        document: UpdateCustomerPutBodyDocument | Unset
        if isinstance(_document, Unset):
            document = UNSET
        else:
            document = UpdateCustomerPutBodyDocument.from_dict(_document)

        _telephone = d.pop("telephone", UNSET)
        telephone: UpdateCustomerPutBodyTelephone | Unset
        if isinstance(_telephone, Unset):
            telephone = UNSET
        else:
            telephone = UpdateCustomerPutBodyTelephone.from_dict(_telephone)

        external_reference = d.pop("externalReference", UNSET)

        _gender = d.pop("gender", UNSET)
        gender: UpdateCustomerPutBodyGender | Unset
        if isinstance(_gender, Unset):
            gender = UNSET
        else:
            gender = UpdateCustomerPutBodyGender(_gender)

        birthdate = d.pop("birthdate", UNSET)

        additional_emails = cast(list[str], d.pop("additionalEmails", UNSET))

        _metadata = d.pop("metadata", UNSET)
        metadata: UpdateCustomerPutBodyMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = UpdateCustomerPutBodyMetadata.from_dict(_metadata)

        update_customer_put_body = cls(
            first_name=first_name,
            last_name=last_name,
            email=email,
            document=document,
            telephone=telephone,
            external_reference=external_reference,
            gender=gender,
            birthdate=birthdate,
            additional_emails=additional_emails,
            metadata=metadata,
        )

        return update_customer_put_body
