from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.create_customer_body_gender import CreateCustomerBodyGender
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_customer_body_document import CreateCustomerBodyDocument
    from ..models.create_customer_body_metadata import CreateCustomerBodyMetadata
    from ..models.create_customer_body_telephone import CreateCustomerBodyTelephone


T = TypeVar("T", bound="CreateCustomerBody")


@_attrs_define
class CreateCustomerBody:
    """
    Attributes:
        first_name (str):
        last_name (str):
        email (str):
        document (CreateCustomerBodyDocument | Unset):
        telephone (CreateCustomerBodyTelephone | Unset):
        external_reference (str | Unset):
        gender (CreateCustomerBodyGender | Unset):
        birthdate (str | Unset):
        additional_emails (list[str] | Unset):
        metadata (CreateCustomerBodyMetadata | Unset):
    """

    first_name: str
    last_name: str
    email: str
    document: CreateCustomerBodyDocument | Unset = UNSET
    telephone: CreateCustomerBodyTelephone | Unset = UNSET
    external_reference: str | Unset = UNSET
    gender: CreateCustomerBodyGender | Unset = UNSET
    birthdate: str | Unset = UNSET
    additional_emails: list[str] | Unset = UNSET
    metadata: CreateCustomerBodyMetadata | Unset = UNSET

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

        field_dict.update(
            {
                "firstName": first_name,
                "lastName": last_name,
                "email": email,
            }
        )
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
        from ..models.create_customer_body_document import CreateCustomerBodyDocument
        from ..models.create_customer_body_metadata import CreateCustomerBodyMetadata
        from ..models.create_customer_body_telephone import CreateCustomerBodyTelephone

        d = dict(src_dict)
        first_name = d.pop("firstName")

        last_name = d.pop("lastName")

        email = d.pop("email")

        _document = d.pop("document", UNSET)
        document: CreateCustomerBodyDocument | Unset
        if isinstance(_document, Unset):
            document = UNSET
        else:
            document = CreateCustomerBodyDocument.from_dict(_document)

        _telephone = d.pop("telephone", UNSET)
        telephone: CreateCustomerBodyTelephone | Unset
        if isinstance(_telephone, Unset):
            telephone = UNSET
        else:
            telephone = CreateCustomerBodyTelephone.from_dict(_telephone)

        external_reference = d.pop("externalReference", UNSET)

        _gender = d.pop("gender", UNSET)
        gender: CreateCustomerBodyGender | Unset
        if isinstance(_gender, Unset):
            gender = UNSET
        else:
            gender = CreateCustomerBodyGender(_gender)

        birthdate = d.pop("birthdate", UNSET)

        additional_emails = cast(list[str], d.pop("additionalEmails", UNSET))

        _metadata = d.pop("metadata", UNSET)
        metadata: CreateCustomerBodyMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CreateCustomerBodyMetadata.from_dict(_metadata)

        create_customer_body = cls(
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

        return create_customer_body
