from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.pause_subscription_response_200_customer_document_type_0 import (
        PauseSubscriptionResponse200CustomerDocumentType0,
    )
    from ..models.pause_subscription_response_200_customer_metadata_type_0 import (
        PauseSubscriptionResponse200CustomerMetadataType0,
    )
    from ..models.pause_subscription_response_200_customer_telephone_type_0 import (
        PauseSubscriptionResponse200CustomerTelephoneType0,
    )


T = TypeVar("T", bound="PauseSubscriptionResponse200Customer")


@_attrs_define
class PauseSubscriptionResponse200Customer:
    """
    Attributes:
        id (None | str):
        first_name (None | str):
        last_name (None | str):
        email (None | str):
        birthdate (None | str):
        gender (None | str):
        document (None | PauseSubscriptionResponse200CustomerDocumentType0):
        telephone (None | PauseSubscriptionResponse200CustomerTelephoneType0):
        available (bool | None):
        delinquent (bool | None):
        external_reference (None | str):
        additional_emails (list[str] | None):
        metadata (None | PauseSubscriptionResponse200CustomerMetadataType0):
        updated_at (None | str):
        created_at (None | str):
    """

    id: None | str
    first_name: None | str
    last_name: None | str
    email: None | str
    birthdate: None | str
    gender: None | str
    document: None | PauseSubscriptionResponse200CustomerDocumentType0
    telephone: None | PauseSubscriptionResponse200CustomerTelephoneType0
    available: bool | None
    delinquent: bool | None
    external_reference: None | str
    additional_emails: list[str] | None
    metadata: None | PauseSubscriptionResponse200CustomerMetadataType0
    updated_at: None | str
    created_at: None | str

    def to_dict(self) -> dict[str, Any]:
        from ..models.pause_subscription_response_200_customer_document_type_0 import (
            PauseSubscriptionResponse200CustomerDocumentType0,
        )
        from ..models.pause_subscription_response_200_customer_metadata_type_0 import (
            PauseSubscriptionResponse200CustomerMetadataType0,
        )
        from ..models.pause_subscription_response_200_customer_telephone_type_0 import (
            PauseSubscriptionResponse200CustomerTelephoneType0,
        )

        id: None | str
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

        document: dict[str, Any] | None
        if isinstance(self.document, PauseSubscriptionResponse200CustomerDocumentType0):
            document = self.document.to_dict()
        else:
            document = self.document

        telephone: dict[str, Any] | None
        if isinstance(
            self.telephone, PauseSubscriptionResponse200CustomerTelephoneType0
        ):
            telephone = self.telephone.to_dict()
        else:
            telephone = self.telephone

        available: bool | None
        available = self.available

        delinquent: bool | None
        delinquent = self.delinquent

        external_reference: None | str
        external_reference = self.external_reference

        additional_emails: list[str] | None
        if isinstance(self.additional_emails, list):
            additional_emails = self.additional_emails

        else:
            additional_emails = self.additional_emails

        metadata: dict[str, Any] | None
        if isinstance(self.metadata, PauseSubscriptionResponse200CustomerMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        updated_at: None | str
        updated_at = self.updated_at

        created_at: None | str
        created_at = self.created_at

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
                "additionalEmails": additional_emails,
                "metadata": metadata,
                "updatedAt": updated_at,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pause_subscription_response_200_customer_document_type_0 import (
            PauseSubscriptionResponse200CustomerDocumentType0,
        )
        from ..models.pause_subscription_response_200_customer_metadata_type_0 import (
            PauseSubscriptionResponse200CustomerMetadataType0,
        )
        from ..models.pause_subscription_response_200_customer_telephone_type_0 import (
            PauseSubscriptionResponse200CustomerTelephoneType0,
        )

        d = dict(src_dict)

        def _parse_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        id = _parse_id(d.pop("id"))

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

        def _parse_document(
            data: object,
        ) -> None | PauseSubscriptionResponse200CustomerDocumentType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                document_type_0 = (
                    PauseSubscriptionResponse200CustomerDocumentType0.from_dict(data)
                )

                return document_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PauseSubscriptionResponse200CustomerDocumentType0, data)

        document = _parse_document(d.pop("document"))

        def _parse_telephone(
            data: object,
        ) -> None | PauseSubscriptionResponse200CustomerTelephoneType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                telephone_type_0 = (
                    PauseSubscriptionResponse200CustomerTelephoneType0.from_dict(data)
                )

                return telephone_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PauseSubscriptionResponse200CustomerTelephoneType0, data)

        telephone = _parse_telephone(d.pop("telephone"))

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

        def _parse_additional_emails(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                additional_emails_type_0 = cast(list[str], data)

                return additional_emails_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        additional_emails = _parse_additional_emails(d.pop("additionalEmails"))

        def _parse_metadata(
            data: object,
        ) -> None | PauseSubscriptionResponse200CustomerMetadataType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = (
                    PauseSubscriptionResponse200CustomerMetadataType0.from_dict(data)
                )

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PauseSubscriptionResponse200CustomerMetadataType0, data)

        metadata = _parse_metadata(d.pop("metadata"))

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

        pause_subscription_response_200_customer = cls(
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
            additional_emails=additional_emails,
            metadata=metadata,
            updated_at=updated_at,
            created_at=created_at,
        )

        return pause_subscription_response_200_customer
