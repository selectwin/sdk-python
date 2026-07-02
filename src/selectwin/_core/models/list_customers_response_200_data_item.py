from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_customers_response_200_data_item_document_type_0 import (
        ListCustomersResponse200DataItemDocumentType0,
    )
    from ..models.list_customers_response_200_data_item_links import (
        ListCustomersResponse200DataItemLinks,
    )
    from ..models.list_customers_response_200_data_item_merchant import (
        ListCustomersResponse200DataItemMerchant,
    )
    from ..models.list_customers_response_200_data_item_metadata_type_0 import (
        ListCustomersResponse200DataItemMetadataType0,
    )
    from ..models.list_customers_response_200_data_item_telephone_type_0 import (
        ListCustomersResponse200DataItemTelephoneType0,
    )


T = TypeVar("T", bound="ListCustomersResponse200DataItem")


@_attrs_define
class ListCustomersResponse200DataItem:
    """
    Attributes:
        id (str): Public identifier (cus_…)
        first_name (str):
        last_name (str):
        email (None | str):
        document (ListCustomersResponse200DataItemDocumentType0 | None):
        telephone (ListCustomersResponse200DataItemTelephoneType0 | None):
        birthdate (None | str):
        gender (None | str):
        available (bool):
        delinquent (bool):
        external_reference (None | str):
        additional_emails (list[str] | None):
        metadata (ListCustomersResponse200DataItemMetadataType0 | None):
        created_at (str):
        updated_at (str):
        merchant (ListCustomersResponse200DataItemMerchant | Unset):
        field_links (ListCustomersResponse200DataItemLinks | Unset):
    """

    id: str
    first_name: str
    last_name: str
    email: None | str
    document: ListCustomersResponse200DataItemDocumentType0 | None
    telephone: ListCustomersResponse200DataItemTelephoneType0 | None
    birthdate: None | str
    gender: None | str
    available: bool
    delinquent: bool
    external_reference: None | str
    additional_emails: list[str] | None
    metadata: ListCustomersResponse200DataItemMetadataType0 | None
    created_at: str
    updated_at: str
    merchant: ListCustomersResponse200DataItemMerchant | Unset = UNSET
    field_links: ListCustomersResponse200DataItemLinks | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.list_customers_response_200_data_item_document_type_0 import (
            ListCustomersResponse200DataItemDocumentType0,
        )
        from ..models.list_customers_response_200_data_item_metadata_type_0 import (
            ListCustomersResponse200DataItemMetadataType0,
        )
        from ..models.list_customers_response_200_data_item_telephone_type_0 import (
            ListCustomersResponse200DataItemTelephoneType0,
        )

        id = self.id

        first_name = self.first_name

        last_name = self.last_name

        email: None | str
        email = self.email

        document: dict[str, Any] | None
        if isinstance(self.document, ListCustomersResponse200DataItemDocumentType0):
            document = self.document.to_dict()
        else:
            document = self.document

        telephone: dict[str, Any] | None
        if isinstance(self.telephone, ListCustomersResponse200DataItemTelephoneType0):
            telephone = self.telephone.to_dict()
        else:
            telephone = self.telephone

        birthdate: None | str
        birthdate = self.birthdate

        gender: None | str
        gender = self.gender

        available = self.available

        delinquent = self.delinquent

        external_reference: None | str
        external_reference = self.external_reference

        additional_emails: list[str] | None
        if isinstance(self.additional_emails, list):
            additional_emails = self.additional_emails

        else:
            additional_emails = self.additional_emails

        metadata: dict[str, Any] | None
        if isinstance(self.metadata, ListCustomersResponse200DataItemMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        created_at = self.created_at

        updated_at = self.updated_at

        merchant: dict[str, Any] | Unset = UNSET
        if not isinstance(self.merchant, Unset):
            merchant = self.merchant.to_dict()

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "firstName": first_name,
                "lastName": last_name,
                "email": email,
                "document": document,
                "telephone": telephone,
                "birthdate": birthdate,
                "gender": gender,
                "available": available,
                "delinquent": delinquent,
                "externalReference": external_reference,
                "additionalEmails": additional_emails,
                "metadata": metadata,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if merchant is not UNSET:
            field_dict["merchant"] = merchant
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_customers_response_200_data_item_document_type_0 import (
            ListCustomersResponse200DataItemDocumentType0,
        )
        from ..models.list_customers_response_200_data_item_links import (
            ListCustomersResponse200DataItemLinks,
        )
        from ..models.list_customers_response_200_data_item_merchant import (
            ListCustomersResponse200DataItemMerchant,
        )
        from ..models.list_customers_response_200_data_item_metadata_type_0 import (
            ListCustomersResponse200DataItemMetadataType0,
        )
        from ..models.list_customers_response_200_data_item_telephone_type_0 import (
            ListCustomersResponse200DataItemTelephoneType0,
        )

        d = dict(src_dict)
        id = d.pop("id")

        first_name = d.pop("firstName")

        last_name = d.pop("lastName")

        def _parse_email(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        email = _parse_email(d.pop("email"))

        def _parse_document(
            data: object,
        ) -> ListCustomersResponse200DataItemDocumentType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                document_type_0 = (
                    ListCustomersResponse200DataItemDocumentType0.from_dict(data)
                )

                return document_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListCustomersResponse200DataItemDocumentType0 | None, data)

        document = _parse_document(d.pop("document"))

        def _parse_telephone(
            data: object,
        ) -> ListCustomersResponse200DataItemTelephoneType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                telephone_type_0 = (
                    ListCustomersResponse200DataItemTelephoneType0.from_dict(data)
                )

                return telephone_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListCustomersResponse200DataItemTelephoneType0 | None, data)

        telephone = _parse_telephone(d.pop("telephone"))

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

        available = d.pop("available")

        delinquent = d.pop("delinquent")

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
        ) -> ListCustomersResponse200DataItemMetadataType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = (
                    ListCustomersResponse200DataItemMetadataType0.from_dict(data)
                )

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListCustomersResponse200DataItemMetadataType0 | None, data)

        metadata = _parse_metadata(d.pop("metadata"))

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        _merchant = d.pop("merchant", UNSET)
        merchant: ListCustomersResponse200DataItemMerchant | Unset
        if isinstance(_merchant, Unset):
            merchant = UNSET
        else:
            merchant = ListCustomersResponse200DataItemMerchant.from_dict(_merchant)

        _field_links = d.pop("_links", UNSET)
        field_links: ListCustomersResponse200DataItemLinks | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = ListCustomersResponse200DataItemLinks.from_dict(_field_links)

        list_customers_response_200_data_item = cls(
            id=id,
            first_name=first_name,
            last_name=last_name,
            email=email,
            document=document,
            telephone=telephone,
            birthdate=birthdate,
            gender=gender,
            available=available,
            delinquent=delinquent,
            external_reference=external_reference,
            additional_emails=additional_emails,
            metadata=metadata,
            created_at=created_at,
            updated_at=updated_at,
            merchant=merchant,
            field_links=field_links,
        )

        return list_customers_response_200_data_item
