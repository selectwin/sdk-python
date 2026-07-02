from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_customer_response_200_addresses_item import (
        GetCustomerResponse200AddressesItem,
    )
    from ..models.get_customer_response_200_cards_item import (
        GetCustomerResponse200CardsItem,
    )
    from ..models.get_customer_response_200_document_type_0 import (
        GetCustomerResponse200DocumentType0,
    )
    from ..models.get_customer_response_200_links import GetCustomerResponse200Links
    from ..models.get_customer_response_200_merchant import (
        GetCustomerResponse200Merchant,
    )
    from ..models.get_customer_response_200_metadata_type_0 import (
        GetCustomerResponse200MetadataType0,
    )
    from ..models.get_customer_response_200_subscriptions_item import (
        GetCustomerResponse200SubscriptionsItem,
    )
    from ..models.get_customer_response_200_telephone_type_0 import (
        GetCustomerResponse200TelephoneType0,
    )
    from ..models.get_customer_response_200_transactions_item import (
        GetCustomerResponse200TransactionsItem,
    )


T = TypeVar("T", bound="GetCustomerResponse200")


@_attrs_define
class GetCustomerResponse200:
    """
    Attributes:
        id (str): Public identifier (cus_…)
        first_name (str):
        last_name (str):
        email (None | str):
        document (GetCustomerResponse200DocumentType0 | None):
        telephone (GetCustomerResponse200TelephoneType0 | None):
        birthdate (None | str):
        gender (None | str):
        available (bool):
        delinquent (bool):
        external_reference (None | str):
        additional_emails (list[str] | None):
        metadata (GetCustomerResponse200MetadataType0 | None):
        created_at (str):
        updated_at (str):
        merchant (GetCustomerResponse200Merchant | Unset):
        field_links (GetCustomerResponse200Links | Unset):
        transactions (list[GetCustomerResponse200TransactionsItem] | Unset):
        subscriptions (list[GetCustomerResponse200SubscriptionsItem] | Unset):
        addresses (list[GetCustomerResponse200AddressesItem] | Unset):
        cards (list[GetCustomerResponse200CardsItem] | Unset):
    """

    id: str
    first_name: str
    last_name: str
    email: None | str
    document: GetCustomerResponse200DocumentType0 | None
    telephone: GetCustomerResponse200TelephoneType0 | None
    birthdate: None | str
    gender: None | str
    available: bool
    delinquent: bool
    external_reference: None | str
    additional_emails: list[str] | None
    metadata: GetCustomerResponse200MetadataType0 | None
    created_at: str
    updated_at: str
    merchant: GetCustomerResponse200Merchant | Unset = UNSET
    field_links: GetCustomerResponse200Links | Unset = UNSET
    transactions: list[GetCustomerResponse200TransactionsItem] | Unset = UNSET
    subscriptions: list[GetCustomerResponse200SubscriptionsItem] | Unset = UNSET
    addresses: list[GetCustomerResponse200AddressesItem] | Unset = UNSET
    cards: list[GetCustomerResponse200CardsItem] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_customer_response_200_document_type_0 import (
            GetCustomerResponse200DocumentType0,
        )
        from ..models.get_customer_response_200_metadata_type_0 import (
            GetCustomerResponse200MetadataType0,
        )
        from ..models.get_customer_response_200_telephone_type_0 import (
            GetCustomerResponse200TelephoneType0,
        )

        id = self.id

        first_name = self.first_name

        last_name = self.last_name

        email: None | str
        email = self.email

        document: dict[str, Any] | None
        if isinstance(self.document, GetCustomerResponse200DocumentType0):
            document = self.document.to_dict()
        else:
            document = self.document

        telephone: dict[str, Any] | None
        if isinstance(self.telephone, GetCustomerResponse200TelephoneType0):
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
        if isinstance(self.metadata, GetCustomerResponse200MetadataType0):
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

        transactions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.transactions, Unset):
            transactions = []
            for transactions_item_data in self.transactions:
                transactions_item = transactions_item_data.to_dict()
                transactions.append(transactions_item)

        subscriptions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.subscriptions, Unset):
            subscriptions = []
            for subscriptions_item_data in self.subscriptions:
                subscriptions_item = subscriptions_item_data.to_dict()
                subscriptions.append(subscriptions_item)

        addresses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.addresses, Unset):
            addresses = []
            for addresses_item_data in self.addresses:
                addresses_item = addresses_item_data.to_dict()
                addresses.append(addresses_item)

        cards: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.cards, Unset):
            cards = []
            for cards_item_data in self.cards:
                cards_item = cards_item_data.to_dict()
                cards.append(cards_item)

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
        if transactions is not UNSET:
            field_dict["transactions"] = transactions
        if subscriptions is not UNSET:
            field_dict["subscriptions"] = subscriptions
        if addresses is not UNSET:
            field_dict["addresses"] = addresses
        if cards is not UNSET:
            field_dict["cards"] = cards

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_customer_response_200_addresses_item import (
            GetCustomerResponse200AddressesItem,
        )
        from ..models.get_customer_response_200_cards_item import (
            GetCustomerResponse200CardsItem,
        )
        from ..models.get_customer_response_200_document_type_0 import (
            GetCustomerResponse200DocumentType0,
        )
        from ..models.get_customer_response_200_links import GetCustomerResponse200Links
        from ..models.get_customer_response_200_merchant import (
            GetCustomerResponse200Merchant,
        )
        from ..models.get_customer_response_200_metadata_type_0 import (
            GetCustomerResponse200MetadataType0,
        )
        from ..models.get_customer_response_200_subscriptions_item import (
            GetCustomerResponse200SubscriptionsItem,
        )
        from ..models.get_customer_response_200_telephone_type_0 import (
            GetCustomerResponse200TelephoneType0,
        )
        from ..models.get_customer_response_200_transactions_item import (
            GetCustomerResponse200TransactionsItem,
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

        def _parse_document(data: object) -> GetCustomerResponse200DocumentType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                document_type_0 = GetCustomerResponse200DocumentType0.from_dict(data)

                return document_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetCustomerResponse200DocumentType0 | None, data)

        document = _parse_document(d.pop("document"))

        def _parse_telephone(
            data: object,
        ) -> GetCustomerResponse200TelephoneType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                telephone_type_0 = GetCustomerResponse200TelephoneType0.from_dict(data)

                return telephone_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetCustomerResponse200TelephoneType0 | None, data)

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

        def _parse_metadata(data: object) -> GetCustomerResponse200MetadataType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = GetCustomerResponse200MetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetCustomerResponse200MetadataType0 | None, data)

        metadata = _parse_metadata(d.pop("metadata"))

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        _merchant = d.pop("merchant", UNSET)
        merchant: GetCustomerResponse200Merchant | Unset
        if isinstance(_merchant, Unset):
            merchant = UNSET
        else:
            merchant = GetCustomerResponse200Merchant.from_dict(_merchant)

        _field_links = d.pop("_links", UNSET)
        field_links: GetCustomerResponse200Links | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = GetCustomerResponse200Links.from_dict(_field_links)

        _transactions = d.pop("transactions", UNSET)
        transactions: list[GetCustomerResponse200TransactionsItem] | Unset = UNSET
        if _transactions is not UNSET:
            transactions = []
            for transactions_item_data in _transactions:
                transactions_item = GetCustomerResponse200TransactionsItem.from_dict(
                    transactions_item_data
                )

                transactions.append(transactions_item)

        _subscriptions = d.pop("subscriptions", UNSET)
        subscriptions: list[GetCustomerResponse200SubscriptionsItem] | Unset = UNSET
        if _subscriptions is not UNSET:
            subscriptions = []
            for subscriptions_item_data in _subscriptions:
                subscriptions_item = GetCustomerResponse200SubscriptionsItem.from_dict(
                    subscriptions_item_data
                )

                subscriptions.append(subscriptions_item)

        _addresses = d.pop("addresses", UNSET)
        addresses: list[GetCustomerResponse200AddressesItem] | Unset = UNSET
        if _addresses is not UNSET:
            addresses = []
            for addresses_item_data in _addresses:
                addresses_item = GetCustomerResponse200AddressesItem.from_dict(
                    addresses_item_data
                )

                addresses.append(addresses_item)

        _cards = d.pop("cards", UNSET)
        cards: list[GetCustomerResponse200CardsItem] | Unset = UNSET
        if _cards is not UNSET:
            cards = []
            for cards_item_data in _cards:
                cards_item = GetCustomerResponse200CardsItem.from_dict(cards_item_data)

                cards.append(cards_item)

        get_customer_response_200 = cls(
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
            transactions=transactions,
            subscriptions=subscriptions,
            addresses=addresses,
            cards=cards,
        )

        return get_customer_response_200
