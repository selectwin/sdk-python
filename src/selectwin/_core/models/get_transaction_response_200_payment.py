from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.get_transaction_response_200_payment_provider import (
    GetTransactionResponse200PaymentProvider,
)
from ..models.get_transaction_response_200_payment_version import (
    GetTransactionResponse200PaymentVersion,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetTransactionResponse200Payment")


@_attrs_define
class GetTransactionResponse200Payment:
    """
    Attributes:
        provider (GetTransactionResponse200PaymentProvider):
        version (GetTransactionResponse200PaymentVersion):
        reusable (bool):
        billet_url (None | str):
        billet_barcode (None | str):
        billet_sequence (None | str):
        billet_document_number (None | str):
        billet_reference_number (None | str):
        pix_qr_code_emv (None | str):
        pix_qr_code_url (None | str):
        pix_qr_code_image (None | str):
        acquirer_transaction_number (None | str):
        card_first_digits (None | str):
        card_last_digits (None | str):
        card_brand (None | str):
        card_registered (bool):
        installments (int | None):
        expiration_date (None | str):
        paid_at (None | str):
        allow_renew_payment (bool):
        invoice_link (str):
        refused (Any | Unset):
    """

    provider: GetTransactionResponse200PaymentProvider
    version: GetTransactionResponse200PaymentVersion
    reusable: bool
    billet_url: None | str
    billet_barcode: None | str
    billet_sequence: None | str
    billet_document_number: None | str
    billet_reference_number: None | str
    pix_qr_code_emv: None | str
    pix_qr_code_url: None | str
    pix_qr_code_image: None | str
    acquirer_transaction_number: None | str
    card_first_digits: None | str
    card_last_digits: None | str
    card_brand: None | str
    card_registered: bool
    installments: int | None
    expiration_date: None | str
    paid_at: None | str
    allow_renew_payment: bool
    invoice_link: str
    refused: Any | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider.value

        version = self.version.value

        reusable = self.reusable

        billet_url: None | str
        billet_url = self.billet_url

        billet_barcode: None | str
        billet_barcode = self.billet_barcode

        billet_sequence: None | str
        billet_sequence = self.billet_sequence

        billet_document_number: None | str
        billet_document_number = self.billet_document_number

        billet_reference_number: None | str
        billet_reference_number = self.billet_reference_number

        pix_qr_code_emv: None | str
        pix_qr_code_emv = self.pix_qr_code_emv

        pix_qr_code_url: None | str
        pix_qr_code_url = self.pix_qr_code_url

        pix_qr_code_image: None | str
        pix_qr_code_image = self.pix_qr_code_image

        acquirer_transaction_number: None | str
        acquirer_transaction_number = self.acquirer_transaction_number

        card_first_digits: None | str
        card_first_digits = self.card_first_digits

        card_last_digits: None | str
        card_last_digits = self.card_last_digits

        card_brand: None | str
        card_brand = self.card_brand

        card_registered = self.card_registered

        installments: int | None
        installments = self.installments

        expiration_date: None | str
        expiration_date = self.expiration_date

        paid_at: None | str
        paid_at = self.paid_at

        allow_renew_payment = self.allow_renew_payment

        invoice_link = self.invoice_link

        refused = self.refused

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "provider": provider,
                "version": version,
                "reusable": reusable,
                "billetUrl": billet_url,
                "billetBarcode": billet_barcode,
                "billetSequence": billet_sequence,
                "billetDocumentNumber": billet_document_number,
                "billetReferenceNumber": billet_reference_number,
                "pixQrCodeEmv": pix_qr_code_emv,
                "pixQrCodeUrl": pix_qr_code_url,
                "pixQrCodeImage": pix_qr_code_image,
                "acquirerTransactionNumber": acquirer_transaction_number,
                "cardFirstDigits": card_first_digits,
                "cardLastDigits": card_last_digits,
                "cardBrand": card_brand,
                "cardRegistered": card_registered,
                "installments": installments,
                "expirationDate": expiration_date,
                "paidAt": paid_at,
                "allowRenewPayment": allow_renew_payment,
                "invoiceLink": invoice_link,
            }
        )
        if refused is not UNSET:
            field_dict["refused"] = refused

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        provider = GetTransactionResponse200PaymentProvider(d.pop("provider"))

        version = GetTransactionResponse200PaymentVersion(d.pop("version"))

        reusable = d.pop("reusable")

        def _parse_billet_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        billet_url = _parse_billet_url(d.pop("billetUrl"))

        def _parse_billet_barcode(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        billet_barcode = _parse_billet_barcode(d.pop("billetBarcode"))

        def _parse_billet_sequence(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        billet_sequence = _parse_billet_sequence(d.pop("billetSequence"))

        def _parse_billet_document_number(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        billet_document_number = _parse_billet_document_number(
            d.pop("billetDocumentNumber")
        )

        def _parse_billet_reference_number(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        billet_reference_number = _parse_billet_reference_number(
            d.pop("billetReferenceNumber")
        )

        def _parse_pix_qr_code_emv(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        pix_qr_code_emv = _parse_pix_qr_code_emv(d.pop("pixQrCodeEmv"))

        def _parse_pix_qr_code_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        pix_qr_code_url = _parse_pix_qr_code_url(d.pop("pixQrCodeUrl"))

        def _parse_pix_qr_code_image(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        pix_qr_code_image = _parse_pix_qr_code_image(d.pop("pixQrCodeImage"))

        def _parse_acquirer_transaction_number(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        acquirer_transaction_number = _parse_acquirer_transaction_number(
            d.pop("acquirerTransactionNumber")
        )

        def _parse_card_first_digits(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        card_first_digits = _parse_card_first_digits(d.pop("cardFirstDigits"))

        def _parse_card_last_digits(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        card_last_digits = _parse_card_last_digits(d.pop("cardLastDigits"))

        def _parse_card_brand(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        card_brand = _parse_card_brand(d.pop("cardBrand"))

        card_registered = d.pop("cardRegistered")

        def _parse_installments(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        installments = _parse_installments(d.pop("installments"))

        def _parse_expiration_date(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        expiration_date = _parse_expiration_date(d.pop("expirationDate"))

        def _parse_paid_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        paid_at = _parse_paid_at(d.pop("paidAt"))

        allow_renew_payment = d.pop("allowRenewPayment")

        invoice_link = d.pop("invoiceLink")

        refused = d.pop("refused", UNSET)

        get_transaction_response_200_payment = cls(
            provider=provider,
            version=version,
            reusable=reusable,
            billet_url=billet_url,
            billet_barcode=billet_barcode,
            billet_sequence=billet_sequence,
            billet_document_number=billet_document_number,
            billet_reference_number=billet_reference_number,
            pix_qr_code_emv=pix_qr_code_emv,
            pix_qr_code_url=pix_qr_code_url,
            pix_qr_code_image=pix_qr_code_image,
            acquirer_transaction_number=acquirer_transaction_number,
            card_first_digits=card_first_digits,
            card_last_digits=card_last_digits,
            card_brand=card_brand,
            card_registered=card_registered,
            installments=installments,
            expiration_date=expiration_date,
            paid_at=paid_at,
            allow_renew_payment=allow_renew_payment,
            invoice_link=invoice_link,
            refused=refused,
        )

        return get_transaction_response_200_payment
