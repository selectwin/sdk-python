from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.utils_corporate_document_check_response_200_type import (
    UtilsCorporateDocumentCheckResponse200Type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.utils_corporate_document_check_response_200_address_type_0 import (
        UtilsCorporateDocumentCheckResponse200AddressType0,
    )
    from ..models.utils_corporate_document_check_response_200_merchant import (
        UtilsCorporateDocumentCheckResponse200Merchant,
    )
    from ..models.utils_corporate_document_check_response_200_partners_item import (
        UtilsCorporateDocumentCheckResponse200PartnersItem,
    )
    from ..models.utils_corporate_document_check_response_200_secondary_cnaes_item import (
        UtilsCorporateDocumentCheckResponse200SecondaryCnaesItem,
    )


T = TypeVar("T", bound="UtilsCorporateDocumentCheckResponse200")


@_attrs_define
class UtilsCorporateDocumentCheckResponse200:
    """
    Attributes:
        valid (bool):
        document (str):
        type_ (UtilsCorporateDocumentCheckResponse200Type):
        name (None | str):
        fantasy_name (None | str):
        email (None | str):
        telephone (None | str):
        cnae (None | str):
        cnae_description (None | str):
        legal_nature (None | str):
        opening_date (None | str):
        registration_status (None | str):
        registration_status_date (None | str):
        active (bool | None):
        share_capital (float | None):
        size (None | str):
        simples_optant (bool | None):
        mei_optant (bool | None):
        address (None | UtilsCorporateDocumentCheckResponse200AddressType0):
        secondary_cnaes (list[UtilsCorporateDocumentCheckResponse200SecondaryCnaesItem]):
        partners (list[UtilsCorporateDocumentCheckResponse200PartnersItem]):
        merchant (UtilsCorporateDocumentCheckResponse200Merchant | Unset):
    """

    valid: bool
    document: str
    type_: UtilsCorporateDocumentCheckResponse200Type
    name: None | str
    fantasy_name: None | str
    email: None | str
    telephone: None | str
    cnae: None | str
    cnae_description: None | str
    legal_nature: None | str
    opening_date: None | str
    registration_status: None | str
    registration_status_date: None | str
    active: bool | None
    share_capital: float | None
    size: None | str
    simples_optant: bool | None
    mei_optant: bool | None
    address: None | UtilsCorporateDocumentCheckResponse200AddressType0
    secondary_cnaes: list[UtilsCorporateDocumentCheckResponse200SecondaryCnaesItem]
    partners: list[UtilsCorporateDocumentCheckResponse200PartnersItem]
    merchant: UtilsCorporateDocumentCheckResponse200Merchant | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.utils_corporate_document_check_response_200_address_type_0 import (
            UtilsCorporateDocumentCheckResponse200AddressType0,
        )

        valid = self.valid

        document = self.document

        type_ = self.type_.value

        name: None | str
        name = self.name

        fantasy_name: None | str
        fantasy_name = self.fantasy_name

        email: None | str
        email = self.email

        telephone: None | str
        telephone = self.telephone

        cnae: None | str
        cnae = self.cnae

        cnae_description: None | str
        cnae_description = self.cnae_description

        legal_nature: None | str
        legal_nature = self.legal_nature

        opening_date: None | str
        opening_date = self.opening_date

        registration_status: None | str
        registration_status = self.registration_status

        registration_status_date: None | str
        registration_status_date = self.registration_status_date

        active: bool | None
        active = self.active

        share_capital: float | None
        share_capital = self.share_capital

        size: None | str
        size = self.size

        simples_optant: bool | None
        simples_optant = self.simples_optant

        mei_optant: bool | None
        mei_optant = self.mei_optant

        address: dict[str, Any] | None
        if isinstance(self.address, UtilsCorporateDocumentCheckResponse200AddressType0):
            address = self.address.to_dict()
        else:
            address = self.address

        secondary_cnaes = []
        for secondary_cnaes_item_data in self.secondary_cnaes:
            secondary_cnaes_item = secondary_cnaes_item_data.to_dict()
            secondary_cnaes.append(secondary_cnaes_item)

        partners = []
        for partners_item_data in self.partners:
            partners_item = partners_item_data.to_dict()
            partners.append(partners_item)

        merchant: dict[str, Any] | Unset = UNSET
        if not isinstance(self.merchant, Unset):
            merchant = self.merchant.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "valid": valid,
                "document": document,
                "type": type_,
                "name": name,
                "fantasyName": fantasy_name,
                "email": email,
                "telephone": telephone,
                "cnae": cnae,
                "cnaeDescription": cnae_description,
                "legalNature": legal_nature,
                "openingDate": opening_date,
                "registrationStatus": registration_status,
                "registrationStatusDate": registration_status_date,
                "active": active,
                "shareCapital": share_capital,
                "size": size,
                "simplesOptant": simples_optant,
                "meiOptant": mei_optant,
                "address": address,
                "secondaryCnaes": secondary_cnaes,
                "partners": partners,
            }
        )
        if merchant is not UNSET:
            field_dict["merchant"] = merchant

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.utils_corporate_document_check_response_200_address_type_0 import (
            UtilsCorporateDocumentCheckResponse200AddressType0,
        )
        from ..models.utils_corporate_document_check_response_200_merchant import (
            UtilsCorporateDocumentCheckResponse200Merchant,
        )
        from ..models.utils_corporate_document_check_response_200_partners_item import (
            UtilsCorporateDocumentCheckResponse200PartnersItem,
        )
        from ..models.utils_corporate_document_check_response_200_secondary_cnaes_item import (
            UtilsCorporateDocumentCheckResponse200SecondaryCnaesItem,
        )

        d = dict(src_dict)
        valid = d.pop("valid")

        document = d.pop("document")

        type_ = UtilsCorporateDocumentCheckResponse200Type(d.pop("type"))

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        def _parse_fantasy_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        fantasy_name = _parse_fantasy_name(d.pop("fantasyName"))

        def _parse_email(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        email = _parse_email(d.pop("email"))

        def _parse_telephone(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        telephone = _parse_telephone(d.pop("telephone"))

        def _parse_cnae(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        cnae = _parse_cnae(d.pop("cnae"))

        def _parse_cnae_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        cnae_description = _parse_cnae_description(d.pop("cnaeDescription"))

        def _parse_legal_nature(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        legal_nature = _parse_legal_nature(d.pop("legalNature"))

        def _parse_opening_date(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        opening_date = _parse_opening_date(d.pop("openingDate"))

        def _parse_registration_status(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        registration_status = _parse_registration_status(d.pop("registrationStatus"))

        def _parse_registration_status_date(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        registration_status_date = _parse_registration_status_date(
            d.pop("registrationStatusDate")
        )

        def _parse_active(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        active = _parse_active(d.pop("active"))

        def _parse_share_capital(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        share_capital = _parse_share_capital(d.pop("shareCapital"))

        def _parse_size(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        size = _parse_size(d.pop("size"))

        def _parse_simples_optant(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        simples_optant = _parse_simples_optant(d.pop("simplesOptant"))

        def _parse_mei_optant(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        mei_optant = _parse_mei_optant(d.pop("meiOptant"))

        def _parse_address(
            data: object,
        ) -> None | UtilsCorporateDocumentCheckResponse200AddressType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                address_type_0 = (
                    UtilsCorporateDocumentCheckResponse200AddressType0.from_dict(data)
                )

                return address_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UtilsCorporateDocumentCheckResponse200AddressType0, data)

        address = _parse_address(d.pop("address"))

        secondary_cnaes = []
        _secondary_cnaes = d.pop("secondaryCnaes")
        for secondary_cnaes_item_data in _secondary_cnaes:
            secondary_cnaes_item = (
                UtilsCorporateDocumentCheckResponse200SecondaryCnaesItem.from_dict(
                    secondary_cnaes_item_data
                )
            )

            secondary_cnaes.append(secondary_cnaes_item)

        partners = []
        _partners = d.pop("partners")
        for partners_item_data in _partners:
            partners_item = (
                UtilsCorporateDocumentCheckResponse200PartnersItem.from_dict(
                    partners_item_data
                )
            )

            partners.append(partners_item)

        _merchant = d.pop("merchant", UNSET)
        merchant: UtilsCorporateDocumentCheckResponse200Merchant | Unset
        if isinstance(_merchant, Unset):
            merchant = UNSET
        else:
            merchant = UtilsCorporateDocumentCheckResponse200Merchant.from_dict(
                _merchant
            )

        utils_corporate_document_check_response_200 = cls(
            valid=valid,
            document=document,
            type_=type_,
            name=name,
            fantasy_name=fantasy_name,
            email=email,
            telephone=telephone,
            cnae=cnae,
            cnae_description=cnae_description,
            legal_nature=legal_nature,
            opening_date=opening_date,
            registration_status=registration_status,
            registration_status_date=registration_status_date,
            active=active,
            share_capital=share_capital,
            size=size,
            simples_optant=simples_optant,
            mei_optant=mei_optant,
            address=address,
            secondary_cnaes=secondary_cnaes,
            partners=partners,
            merchant=merchant,
        )

        return utils_corporate_document_check_response_200
