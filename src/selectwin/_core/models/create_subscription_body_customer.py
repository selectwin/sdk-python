from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.create_subscription_body_customer_gender import (
    CreateSubscriptionBodyCustomerGender,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_subscription_body_customer_document import (
        CreateSubscriptionBodyCustomerDocument,
    )
    from ..models.create_subscription_body_customer_metadata import (
        CreateSubscriptionBodyCustomerMetadata,
    )
    from ..models.create_subscription_body_customer_telephone import (
        CreateSubscriptionBodyCustomerTelephone,
    )


T = TypeVar("T", bound="CreateSubscriptionBodyCustomer")


@_attrs_define
class CreateSubscriptionBodyCustomer:
    """**Regra:** Obrigatório informar `id` (cliente salvo) **OU** os dados inline `firstName` + `lastName` + `email` (a
    API faz find-or-create). Enviar `customer: {}` é rejeitado.

        Attributes:
            id (str | Unset): Public identifier (cus_…)
            first_name (str | Unset):
            last_name (str | Unset):
            full_name (str | Unset):
            email (str | Unset):
            document (CreateSubscriptionBodyCustomerDocument | Unset):
            telephone (CreateSubscriptionBodyCustomerTelephone | Unset):
            external_reference (str | Unset):
            gender (CreateSubscriptionBodyCustomerGender | Unset):
            birthdate (str | Unset):
            additional_emails (list[str] | Unset):
            metadata (CreateSubscriptionBodyCustomerMetadata | Unset):
    """

    id: str | Unset = UNSET
    first_name: str | Unset = UNSET
    last_name: str | Unset = UNSET
    full_name: str | Unset = UNSET
    email: str | Unset = UNSET
    document: CreateSubscriptionBodyCustomerDocument | Unset = UNSET
    telephone: CreateSubscriptionBodyCustomerTelephone | Unset = UNSET
    external_reference: str | Unset = UNSET
    gender: CreateSubscriptionBodyCustomerGender | Unset = UNSET
    birthdate: str | Unset = UNSET
    additional_emails: list[str] | Unset = UNSET
    metadata: CreateSubscriptionBodyCustomerMetadata | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        first_name = self.first_name

        last_name = self.last_name

        full_name = self.full_name

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
        if id is not UNSET:
            field_dict["id"] = id
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if full_name is not UNSET:
            field_dict["fullName"] = full_name
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
        from ..models.create_subscription_body_customer_document import (
            CreateSubscriptionBodyCustomerDocument,
        )
        from ..models.create_subscription_body_customer_metadata import (
            CreateSubscriptionBodyCustomerMetadata,
        )
        from ..models.create_subscription_body_customer_telephone import (
            CreateSubscriptionBodyCustomerTelephone,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        full_name = d.pop("fullName", UNSET)

        email = d.pop("email", UNSET)

        _document = d.pop("document", UNSET)
        document: CreateSubscriptionBodyCustomerDocument | Unset
        if isinstance(_document, Unset):
            document = UNSET
        else:
            document = CreateSubscriptionBodyCustomerDocument.from_dict(_document)

        _telephone = d.pop("telephone", UNSET)
        telephone: CreateSubscriptionBodyCustomerTelephone | Unset
        if isinstance(_telephone, Unset):
            telephone = UNSET
        else:
            telephone = CreateSubscriptionBodyCustomerTelephone.from_dict(_telephone)

        external_reference = d.pop("externalReference", UNSET)

        _gender = d.pop("gender", UNSET)
        gender: CreateSubscriptionBodyCustomerGender | Unset
        if isinstance(_gender, Unset):
            gender = UNSET
        else:
            gender = CreateSubscriptionBodyCustomerGender(_gender)

        birthdate = d.pop("birthdate", UNSET)

        additional_emails = cast(list[str], d.pop("additionalEmails", UNSET))

        _metadata = d.pop("metadata", UNSET)
        metadata: CreateSubscriptionBodyCustomerMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CreateSubscriptionBodyCustomerMetadata.from_dict(_metadata)

        create_subscription_body_customer = cls(
            id=id,
            first_name=first_name,
            last_name=last_name,
            full_name=full_name,
            email=email,
            document=document,
            telephone=telephone,
            external_reference=external_reference,
            gender=gender,
            birthdate=birthdate,
            additional_emails=additional_emails,
            metadata=metadata,
        )

        return create_subscription_body_customer
