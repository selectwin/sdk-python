"""Contains all the data models used in inputs/outputs"""

from .add_subscription_item_body import AddSubscriptionItemBody
from .add_subscription_item_body_metadata import AddSubscriptionItemBodyMetadata
from .add_subscription_item_response_201 import AddSubscriptionItemResponse201
from .add_subscription_item_response_201_images_type_0_item_type_1 import (
    AddSubscriptionItemResponse201ImagesType0ItemType1,
)
from .add_subscription_item_response_201_links import (
    AddSubscriptionItemResponse201Links,
)
from .add_subscription_item_response_201_links_additional_property import (
    AddSubscriptionItemResponse201LinksAdditionalProperty,
)
from .add_subscription_item_response_201_merchant import (
    AddSubscriptionItemResponse201Merchant,
)
from .add_subscription_item_response_201_metadata_type_0 import (
    AddSubscriptionItemResponse201MetadataType0,
)
from .add_subscription_split_body import AddSubscriptionSplitBody
from .add_subscription_split_body_type import AddSubscriptionSplitBodyType
from .add_subscription_split_response_201 import AddSubscriptionSplitResponse201
from .add_subscription_split_response_201_links import (
    AddSubscriptionSplitResponse201Links,
)
from .add_subscription_split_response_201_links_additional_property import (
    AddSubscriptionSplitResponse201LinksAdditionalProperty,
)
from .add_subscription_split_response_201_merchant import (
    AddSubscriptionSplitResponse201Merchant,
)
from .add_subscription_split_response_201_splits_item import (
    AddSubscriptionSplitResponse201SplitsItem,
)
from .add_subscription_split_response_201_splits_item_links import (
    AddSubscriptionSplitResponse201SplitsItemLinks,
)
from .add_subscription_split_response_201_splits_item_links_additional_property import (
    AddSubscriptionSplitResponse201SplitsItemLinksAdditionalProperty,
)
from .add_subscription_split_response_201_splits_item_merchant import (
    AddSubscriptionSplitResponse201SplitsItemMerchant,
)
from .add_subscription_threshold_body import AddSubscriptionThresholdBody
from .add_subscription_threshold_body_kind import AddSubscriptionThresholdBodyKind
from .add_subscription_threshold_response_201 import AddSubscriptionThresholdResponse201
from .add_subscription_threshold_response_201_kind import (
    AddSubscriptionThresholdResponse201Kind,
)
from .cancel_subscription_body import CancelSubscriptionBody
from .cancel_subscription_response_200 import CancelSubscriptionResponse200
from .cancel_subscription_response_200_billing import (
    CancelSubscriptionResponse200Billing,
)
from .cancel_subscription_response_200_billing_address import (
    CancelSubscriptionResponse200BillingAddress,
)
from .cancel_subscription_response_200_callback_type_0 import (
    CancelSubscriptionResponse200CallbackType0,
)
from .cancel_subscription_response_200_current_cycle_type_0 import (
    CancelSubscriptionResponse200CurrentCycleType0,
)
from .cancel_subscription_response_200_customer import (
    CancelSubscriptionResponse200Customer,
)
from .cancel_subscription_response_200_customer_document_type_0 import (
    CancelSubscriptionResponse200CustomerDocumentType0,
)
from .cancel_subscription_response_200_customer_metadata_type_0 import (
    CancelSubscriptionResponse200CustomerMetadataType0,
)
from .cancel_subscription_response_200_customer_telephone_type_0 import (
    CancelSubscriptionResponse200CustomerTelephoneType0,
)
from .cancel_subscription_response_200_discount_type_0 import (
    CancelSubscriptionResponse200DiscountType0,
)
from .cancel_subscription_response_200_geolocation_type_0 import (
    CancelSubscriptionResponse200GeolocationType0,
)
from .cancel_subscription_response_200_items_item import (
    CancelSubscriptionResponse200ItemsItem,
)
from .cancel_subscription_response_200_items_item_images_type_0_item_type_1 import (
    CancelSubscriptionResponse200ItemsItemImagesType0ItemType1,
)
from .cancel_subscription_response_200_items_item_metadata_type_0 import (
    CancelSubscriptionResponse200ItemsItemMetadataType0,
)
from .cancel_subscription_response_200_links import CancelSubscriptionResponse200Links
from .cancel_subscription_response_200_links_additional_property import (
    CancelSubscriptionResponse200LinksAdditionalProperty,
)
from .cancel_subscription_response_200_merchant import (
    CancelSubscriptionResponse200Merchant,
)
from .cancel_subscription_response_200_metadata_type_0 import (
    CancelSubscriptionResponse200MetadataType0,
)
from .cancel_subscription_response_200_shipping_type_0 import (
    CancelSubscriptionResponse200ShippingType0,
)
from .cancel_subscription_response_200_splits_type_0_item import (
    CancelSubscriptionResponse200SplitsType0Item,
)
from .cancel_subscription_response_200_status import CancelSubscriptionResponse200Status
from .capture_transaction_body import CaptureTransactionBody
from .capture_transaction_response_202 import CaptureTransactionResponse202
from .capture_transaction_response_202_status import CaptureTransactionResponse202Status
from .create_address_body import CreateAddressBody
from .create_address_body_metadata import CreateAddressBodyMetadata
from .create_address_response_201 import CreateAddressResponse201
from .create_address_response_201_links import CreateAddressResponse201Links
from .create_address_response_201_links_additional_property import (
    CreateAddressResponse201LinksAdditionalProperty,
)
from .create_address_response_201_merchant import CreateAddressResponse201Merchant
from .create_address_response_201_metadata_type_0 import (
    CreateAddressResponse201MetadataType0,
)
from .create_address_response_201_owner_type import CreateAddressResponse201OwnerType
from .create_card_body import CreateCardBody
from .create_card_body_expiration_year import CreateCardBodyExpirationYear
from .create_card_response_201 import CreateCardResponse201
from .create_card_response_201_links import CreateCardResponse201Links
from .create_card_response_201_links_additional_property import (
    CreateCardResponse201LinksAdditionalProperty,
)
from .create_card_response_201_merchant import CreateCardResponse201Merchant
from .create_checkout_payment_link_body import CreateCheckoutPaymentLinkBody
from .create_checkout_payment_link_body_custom_inputs_item import (
    CreateCheckoutPaymentLinkBodyCustomInputsItem,
)
from .create_checkout_payment_link_body_items_item import (
    CreateCheckoutPaymentLinkBodyItemsItem,
)
from .create_checkout_payment_link_body_metadata import (
    CreateCheckoutPaymentLinkBodyMetadata,
)
from .create_checkout_payment_link_response_201 import (
    CreateCheckoutPaymentLinkResponse201,
)
from .create_checkout_payment_link_response_201_custom_inputs_type_0_item import (
    CreateCheckoutPaymentLinkResponse201CustomInputsType0Item,
)
from .create_checkout_payment_link_response_201_items_item import (
    CreateCheckoutPaymentLinkResponse201ItemsItem,
)
from .create_checkout_payment_link_response_201_metadata_type_0 import (
    CreateCheckoutPaymentLinkResponse201MetadataType0,
)
from .create_checkout_session_body import CreateCheckoutSessionBody
from .create_checkout_session_body_address import CreateCheckoutSessionBodyAddress
from .create_checkout_session_body_ambient import CreateCheckoutSessionBodyAmbient
from .create_checkout_session_body_client import CreateCheckoutSessionBodyClient
from .create_checkout_session_body_cookies import CreateCheckoutSessionBodyCookies
from .create_checkout_session_body_coupons_item_type_1 import (
    CreateCheckoutSessionBodyCouponsItemType1,
)
from .create_checkout_session_body_customer import CreateCheckoutSessionBodyCustomer
from .create_checkout_session_body_items_item import CreateCheckoutSessionBodyItemsItem
from .create_checkout_session_body_line_items_item import (
    CreateCheckoutSessionBodyLineItemsItem,
)
from .create_checkout_session_body_metadata import CreateCheckoutSessionBodyMetadata
from .create_checkout_session_body_payment_methods_item_type_1 import (
    CreateCheckoutSessionBodyPaymentMethodsItemType1,
)
from .create_checkout_session_body_redirect_urls import (
    CreateCheckoutSessionBodyRedirectUrls,
)
from .create_checkout_session_body_shipping_delivery import (
    CreateCheckoutSessionBodyShippingDelivery,
)
from .create_checkout_session_body_utm import CreateCheckoutSessionBodyUtm
from .create_checkout_session_response_201 import CreateCheckoutSessionResponse201
from .create_checkout_session_response_201_address_type_0 import (
    CreateCheckoutSessionResponse201AddressType0,
)
from .create_checkout_session_response_201_coupons_item import (
    CreateCheckoutSessionResponse201CouponsItem,
)
from .create_checkout_session_response_201_currency import (
    CreateCheckoutSessionResponse201Currency,
)
from .create_checkout_session_response_201_custom_inputs import (
    CreateCheckoutSessionResponse201CustomInputs,
)
from .create_checkout_session_response_201_customer_type_0 import (
    CreateCheckoutSessionResponse201CustomerType0,
)
from .create_checkout_session_response_201_line_items_item import (
    CreateCheckoutSessionResponse201LineItemsItem,
)
from .create_checkout_session_response_201_line_items_item_metadata_type_0 import (
    CreateCheckoutSessionResponse201LineItemsItemMetadataType0,
)
from .create_checkout_session_response_201_metadata_type_0 import (
    CreateCheckoutSessionResponse201MetadataType0,
)
from .create_checkout_session_response_201_object import (
    CreateCheckoutSessionResponse201Object,
)
from .create_checkout_session_response_201_payment_methods_item_type_1 import (
    CreateCheckoutSessionResponse201PaymentMethodsItemType1,
)
from .create_checkout_session_response_201_payment_selection_type_0 import (
    CreateCheckoutSessionResponse201PaymentSelectionType0,
)
from .create_checkout_session_response_201_redirect_urls import (
    CreateCheckoutSessionResponse201RedirectUrls,
)
from .create_checkout_session_response_201_status import (
    CreateCheckoutSessionResponse201Status,
)
from .create_checkout_session_response_201_totals import (
    CreateCheckoutSessionResponse201Totals,
)
from .create_checkout_session_response_201_utm_type_0 import (
    CreateCheckoutSessionResponse201UtmType0,
)
from .create_coupon_body import CreateCouponBody
from .create_coupon_body_scope import CreateCouponBodyScope
from .create_coupon_body_type import CreateCouponBodyType
from .create_coupon_response_201 import CreateCouponResponse201
from .create_coupon_response_201_scope import CreateCouponResponse201Scope
from .create_coupon_response_201_type import CreateCouponResponse201Type
from .create_customer_body import CreateCustomerBody
from .create_customer_body_document import CreateCustomerBodyDocument
from .create_customer_body_document_type import CreateCustomerBodyDocumentType
from .create_customer_body_gender import CreateCustomerBodyGender
from .create_customer_body_metadata import CreateCustomerBodyMetadata
from .create_customer_body_telephone import CreateCustomerBodyTelephone
from .create_customer_response_201 import CreateCustomerResponse201
from .create_customer_response_201_document_type_0 import (
    CreateCustomerResponse201DocumentType0,
)
from .create_customer_response_201_document_type_0_type import (
    CreateCustomerResponse201DocumentType0Type,
)
from .create_customer_response_201_links import CreateCustomerResponse201Links
from .create_customer_response_201_links_additional_property import (
    CreateCustomerResponse201LinksAdditionalProperty,
)
from .create_customer_response_201_merchant import CreateCustomerResponse201Merchant
from .create_customer_response_201_metadata_type_0 import (
    CreateCustomerResponse201MetadataType0,
)
from .create_customer_response_201_telephone_type_0 import (
    CreateCustomerResponse201TelephoneType0,
)
from .create_product_body import CreateProductBody
from .create_product_body_images_item_type_1 import CreateProductBodyImagesItemType1
from .create_product_body_type import CreateProductBodyType
from .create_product_body_variants_item import CreateProductBodyVariantsItem
from .create_product_body_variants_item_attributes import (
    CreateProductBodyVariantsItemAttributes,
)
from .create_product_body_variants_item_images_item_type_1 import (
    CreateProductBodyVariantsItemImagesItemType1,
)
from .create_product_body_variants_item_metadata import (
    CreateProductBodyVariantsItemMetadata,
)
from .create_product_body_variants_item_pricing import (
    CreateProductBodyVariantsItemPricing,
)
from .create_product_body_variants_item_pricing_billing_frequency import (
    CreateProductBodyVariantsItemPricingBillingFrequency,
)
from .create_product_body_variants_item_pricing_billing_type import (
    CreateProductBodyVariantsItemPricingBillingType,
)
from .create_product_body_variants_item_pricing_schema import (
    CreateProductBodyVariantsItemPricingSchema,
)
from .create_product_body_variants_item_pricing_tiers_item import (
    CreateProductBodyVariantsItemPricingTiersItem,
)
from .create_product_body_variants_item_pricing_tiers_mode import (
    CreateProductBodyVariantsItemPricingTiersMode,
)
from .create_product_body_variants_item_pricing_transform_quantity import (
    CreateProductBodyVariantsItemPricingTransformQuantity,
)
from .create_product_body_variants_item_pricing_transform_quantity_round import (
    CreateProductBodyVariantsItemPricingTransformQuantityRound,
)
from .create_product_body_variants_item_pricing_trial_interval import (
    CreateProductBodyVariantsItemPricingTrialInterval,
)
from .create_product_body_variants_item_pricing_type import (
    CreateProductBodyVariantsItemPricingType,
)
from .create_product_body_variants_item_pricing_usage_aggregation import (
    CreateProductBodyVariantsItemPricingUsageAggregation,
)
from .create_product_body_variants_item_pricing_usage_type import (
    CreateProductBodyVariantsItemPricingUsageType,
)
from .create_product_response_201 import CreateProductResponse201
from .create_product_response_201_images_type_0_item_type_1 import (
    CreateProductResponse201ImagesType0ItemType1,
)
from .create_product_response_201_type import CreateProductResponse201Type
from .create_product_response_201_variants_item import (
    CreateProductResponse201VariantsItem,
)
from .create_product_response_201_variants_item_attributes_type_0 import (
    CreateProductResponse201VariantsItemAttributesType0,
)
from .create_product_response_201_variants_item_images_type_0_item_type_1 import (
    CreateProductResponse201VariantsItemImagesType0ItemType1,
)
from .create_product_response_201_variants_item_metadata_type_0 import (
    CreateProductResponse201VariantsItemMetadataType0,
)
from .create_product_response_201_variants_item_pricing import (
    CreateProductResponse201VariantsItemPricing,
)
from .create_product_response_201_variants_item_pricing_schema import (
    CreateProductResponse201VariantsItemPricingSchema,
)
from .create_product_response_201_variants_item_pricing_type import (
    CreateProductResponse201VariantsItemPricingType,
)
from .create_product_variant_body import CreateProductVariantBody
from .create_product_variant_body_attributes import CreateProductVariantBodyAttributes
from .create_product_variant_body_images_item_type_1 import (
    CreateProductVariantBodyImagesItemType1,
)
from .create_product_variant_body_metadata import CreateProductVariantBodyMetadata
from .create_product_variant_body_pricing import CreateProductVariantBodyPricing
from .create_product_variant_body_pricing_billing_frequency import (
    CreateProductVariantBodyPricingBillingFrequency,
)
from .create_product_variant_body_pricing_billing_type import (
    CreateProductVariantBodyPricingBillingType,
)
from .create_product_variant_body_pricing_schema import (
    CreateProductVariantBodyPricingSchema,
)
from .create_product_variant_body_pricing_tiers_item import (
    CreateProductVariantBodyPricingTiersItem,
)
from .create_product_variant_body_pricing_tiers_mode import (
    CreateProductVariantBodyPricingTiersMode,
)
from .create_product_variant_body_pricing_transform_quantity import (
    CreateProductVariantBodyPricingTransformQuantity,
)
from .create_product_variant_body_pricing_transform_quantity_round import (
    CreateProductVariantBodyPricingTransformQuantityRound,
)
from .create_product_variant_body_pricing_trial_interval import (
    CreateProductVariantBodyPricingTrialInterval,
)
from .create_product_variant_body_pricing_type import (
    CreateProductVariantBodyPricingType,
)
from .create_product_variant_body_pricing_usage_aggregation import (
    CreateProductVariantBodyPricingUsageAggregation,
)
from .create_product_variant_body_pricing_usage_type import (
    CreateProductVariantBodyPricingUsageType,
)
from .create_product_variant_response_201 import CreateProductVariantResponse201
from .create_product_variant_response_201_attributes_type_0 import (
    CreateProductVariantResponse201AttributesType0,
)
from .create_product_variant_response_201_images_type_0_item_type_1 import (
    CreateProductVariantResponse201ImagesType0ItemType1,
)
from .create_product_variant_response_201_metadata_type_0 import (
    CreateProductVariantResponse201MetadataType0,
)
from .create_product_variant_response_201_pricing import (
    CreateProductVariantResponse201Pricing,
)
from .create_product_variant_response_201_pricing_schema import (
    CreateProductVariantResponse201PricingSchema,
)
from .create_product_variant_response_201_pricing_type import (
    CreateProductVariantResponse201PricingType,
)
from .create_subscription_body import CreateSubscriptionBody
from .create_subscription_body_billing import CreateSubscriptionBodyBilling
from .create_subscription_body_billing_address import (
    CreateSubscriptionBodyBillingAddress,
)
from .create_subscription_body_callback import CreateSubscriptionBodyCallback
from .create_subscription_body_customer import CreateSubscriptionBodyCustomer
from .create_subscription_body_customer_document import (
    CreateSubscriptionBodyCustomerDocument,
)
from .create_subscription_body_customer_document_type import (
    CreateSubscriptionBodyCustomerDocumentType,
)
from .create_subscription_body_customer_gender import (
    CreateSubscriptionBodyCustomerGender,
)
from .create_subscription_body_customer_metadata import (
    CreateSubscriptionBodyCustomerMetadata,
)
from .create_subscription_body_customer_telephone import (
    CreateSubscriptionBodyCustomerTelephone,
)
from .create_subscription_body_discounts_item import CreateSubscriptionBodyDiscountsItem
from .create_subscription_body_free_trial import CreateSubscriptionBodyFreeTrial
from .create_subscription_body_frequency import CreateSubscriptionBodyFrequency
from .create_subscription_body_geolocation import CreateSubscriptionBodyGeolocation
from .create_subscription_body_items_item import CreateSubscriptionBodyItemsItem
from .create_subscription_body_items_item_metadata import (
    CreateSubscriptionBodyItemsItemMetadata,
)
from .create_subscription_body_metadata import CreateSubscriptionBodyMetadata
from .create_subscription_body_payment import CreateSubscriptionBodyPayment
from .create_subscription_body_payment_billet import CreateSubscriptionBodyPaymentBillet
from .create_subscription_body_payment_card import CreateSubscriptionBodyPaymentCard
from .create_subscription_body_payment_card_expiration_year import (
    CreateSubscriptionBodyPaymentCardExpirationYear,
)
from .create_subscription_body_payment_method import CreateSubscriptionBodyPaymentMethod
from .create_subscription_body_payment_pix import CreateSubscriptionBodyPaymentPix
from .create_subscription_body_shipping import CreateSubscriptionBodyShipping
from .create_subscription_body_splits_item import CreateSubscriptionBodySplitsItem
from .create_subscription_body_splits_item_type import (
    CreateSubscriptionBodySplitsItemType,
)
from .create_subscription_response_201 import CreateSubscriptionResponse201
from .create_subscription_response_201_billing import (
    CreateSubscriptionResponse201Billing,
)
from .create_subscription_response_201_billing_address import (
    CreateSubscriptionResponse201BillingAddress,
)
from .create_subscription_response_201_callback_type_0 import (
    CreateSubscriptionResponse201CallbackType0,
)
from .create_subscription_response_201_current_cycle_type_0 import (
    CreateSubscriptionResponse201CurrentCycleType0,
)
from .create_subscription_response_201_customer import (
    CreateSubscriptionResponse201Customer,
)
from .create_subscription_response_201_customer_document_type_0 import (
    CreateSubscriptionResponse201CustomerDocumentType0,
)
from .create_subscription_response_201_customer_metadata_type_0 import (
    CreateSubscriptionResponse201CustomerMetadataType0,
)
from .create_subscription_response_201_customer_telephone_type_0 import (
    CreateSubscriptionResponse201CustomerTelephoneType0,
)
from .create_subscription_response_201_discount_type_0 import (
    CreateSubscriptionResponse201DiscountType0,
)
from .create_subscription_response_201_geolocation_type_0 import (
    CreateSubscriptionResponse201GeolocationType0,
)
from .create_subscription_response_201_items_item import (
    CreateSubscriptionResponse201ItemsItem,
)
from .create_subscription_response_201_items_item_images_type_0_item_type_1 import (
    CreateSubscriptionResponse201ItemsItemImagesType0ItemType1,
)
from .create_subscription_response_201_items_item_metadata_type_0 import (
    CreateSubscriptionResponse201ItemsItemMetadataType0,
)
from .create_subscription_response_201_links import CreateSubscriptionResponse201Links
from .create_subscription_response_201_links_additional_property import (
    CreateSubscriptionResponse201LinksAdditionalProperty,
)
from .create_subscription_response_201_merchant import (
    CreateSubscriptionResponse201Merchant,
)
from .create_subscription_response_201_metadata_type_0 import (
    CreateSubscriptionResponse201MetadataType0,
)
from .create_subscription_response_201_shipping_type_0 import (
    CreateSubscriptionResponse201ShippingType0,
)
from .create_subscription_response_201_splits_type_0_item import (
    CreateSubscriptionResponse201SplitsType0Item,
)
from .create_subscription_response_201_status import CreateSubscriptionResponse201Status
from .create_transaction_body import CreateTransactionBody
from .create_transaction_body_billing import CreateTransactionBodyBilling
from .create_transaction_body_billing_address import CreateTransactionBodyBillingAddress
from .create_transaction_body_callback import CreateTransactionBodyCallback
from .create_transaction_body_customer import CreateTransactionBodyCustomer
from .create_transaction_body_customer_document import (
    CreateTransactionBodyCustomerDocument,
)
from .create_transaction_body_customer_document_type import (
    CreateTransactionBodyCustomerDocumentType,
)
from .create_transaction_body_customer_gender import CreateTransactionBodyCustomerGender
from .create_transaction_body_customer_metadata import (
    CreateTransactionBodyCustomerMetadata,
)
from .create_transaction_body_customer_telephone import (
    CreateTransactionBodyCustomerTelephone,
)
from .create_transaction_body_discounts_item import CreateTransactionBodyDiscountsItem
from .create_transaction_body_geolocation import CreateTransactionBodyGeolocation
from .create_transaction_body_items_item import CreateTransactionBodyItemsItem
from .create_transaction_body_items_item_metadata import (
    CreateTransactionBodyItemsItemMetadata,
)
from .create_transaction_body_items_item_pricing import (
    CreateTransactionBodyItemsItemPricing,
)
from .create_transaction_body_metadata import CreateTransactionBodyMetadata
from .create_transaction_body_payment import CreateTransactionBodyPayment
from .create_transaction_body_payment_billet import CreateTransactionBodyPaymentBillet
from .create_transaction_body_payment_billet_billing_instructions import (
    CreateTransactionBodyPaymentBilletBillingInstructions,
)
from .create_transaction_body_payment_billet_billing_instructions_discounts_item import (
    CreateTransactionBodyPaymentBilletBillingInstructionsDiscountsItem,
)
from .create_transaction_body_payment_billet_billing_instructions_discounts_item_mode import (
    CreateTransactionBodyPaymentBilletBillingInstructionsDiscountsItemMode,
)
from .create_transaction_body_payment_billet_billing_instructions_interest import (
    CreateTransactionBodyPaymentBilletBillingInstructionsInterest,
)
from .create_transaction_body_payment_billet_billing_instructions_interest_mode import (
    CreateTransactionBodyPaymentBilletBillingInstructionsInterestMode,
)
from .create_transaction_body_payment_billet_billing_instructions_late_fee import (
    CreateTransactionBodyPaymentBilletBillingInstructionsLateFee,
)
from .create_transaction_body_payment_billet_billing_instructions_late_fee_mode import (
    CreateTransactionBodyPaymentBilletBillingInstructionsLateFeeMode,
)
from .create_transaction_body_payment_card import CreateTransactionBodyPaymentCard
from .create_transaction_body_payment_card_expiration_year import (
    CreateTransactionBodyPaymentCardExpirationYear,
)
from .create_transaction_body_payment_method import CreateTransactionBodyPaymentMethod
from .create_transaction_body_payment_pix import CreateTransactionBodyPaymentPix
from .create_transaction_body_payment_pix_billing_instructions import (
    CreateTransactionBodyPaymentPixBillingInstructions,
)
from .create_transaction_body_payment_pix_billing_instructions_discounts_item import (
    CreateTransactionBodyPaymentPixBillingInstructionsDiscountsItem,
)
from .create_transaction_body_payment_pix_billing_instructions_discounts_item_mode import (
    CreateTransactionBodyPaymentPixBillingInstructionsDiscountsItemMode,
)
from .create_transaction_body_payment_pix_billing_instructions_interest import (
    CreateTransactionBodyPaymentPixBillingInstructionsInterest,
)
from .create_transaction_body_payment_pix_billing_instructions_interest_mode import (
    CreateTransactionBodyPaymentPixBillingInstructionsInterestMode,
)
from .create_transaction_body_payment_pix_billing_instructions_late_fee import (
    CreateTransactionBodyPaymentPixBillingInstructionsLateFee,
)
from .create_transaction_body_payment_pix_billing_instructions_late_fee_mode import (
    CreateTransactionBodyPaymentPixBillingInstructionsLateFeeMode,
)
from .create_transaction_body_shipping import CreateTransactionBodyShipping
from .create_transaction_body_splits_item import CreateTransactionBodySplitsItem
from .create_transaction_body_splits_item_type import (
    CreateTransactionBodySplitsItemType,
)
from .create_transaction_response_201 import CreateTransactionResponse201
from .create_transaction_response_201_billing import CreateTransactionResponse201Billing
from .create_transaction_response_201_billing_address import (
    CreateTransactionResponse201BillingAddress,
)
from .create_transaction_response_201_callback_type_0 import (
    CreateTransactionResponse201CallbackType0,
)
from .create_transaction_response_201_customer_type_0 import (
    CreateTransactionResponse201CustomerType0,
)
from .create_transaction_response_201_customer_type_0_document import (
    CreateTransactionResponse201CustomerType0Document,
)
from .create_transaction_response_201_customer_type_0_telephone import (
    CreateTransactionResponse201CustomerType0Telephone,
)
from .create_transaction_response_201_discount_type_0 import (
    CreateTransactionResponse201DiscountType0,
)
from .create_transaction_response_201_disputes_type_0_item import (
    CreateTransactionResponse201DisputesType0Item,
)
from .create_transaction_response_201_items_type_0_item import (
    CreateTransactionResponse201ItemsType0Item,
)
from .create_transaction_response_201_links import CreateTransactionResponse201Links
from .create_transaction_response_201_links_additional_property import (
    CreateTransactionResponse201LinksAdditionalProperty,
)
from .create_transaction_response_201_merchant import (
    CreateTransactionResponse201Merchant,
)
from .create_transaction_response_201_method import CreateTransactionResponse201Method
from .create_transaction_response_201_payment import CreateTransactionResponse201Payment
from .create_transaction_response_201_payment_provider import (
    CreateTransactionResponse201PaymentProvider,
)
from .create_transaction_response_201_payment_version import (
    CreateTransactionResponse201PaymentVersion,
)
from .create_transaction_response_201_receivables_type_0_item import (
    CreateTransactionResponse201ReceivablesType0Item,
)
from .create_transaction_response_201_refunds_type_0_item import (
    CreateTransactionResponse201RefundsType0Item,
)
from .create_transaction_response_201_splits_type_0_item import (
    CreateTransactionResponse201SplitsType0Item,
)
from .create_transaction_response_201_status import CreateTransactionResponse201Status
from .create_transaction_response_201_timeline_item import (
    CreateTransactionResponse201TimelineItem,
)
from .create_wallet_body import CreateWalletBody
from .create_wallet_response_201 import CreateWalletResponse201
from .create_wallet_response_201_links import CreateWalletResponse201Links
from .create_wallet_response_201_links_additional_property import (
    CreateWalletResponse201LinksAdditionalProperty,
)
from .create_wallet_response_201_merchant import CreateWalletResponse201Merchant
from .create_webhook_endpoint_body import CreateWebhookEndpointBody
from .create_webhook_endpoint_body_events_item import (
    CreateWebhookEndpointBodyEventsItem,
)
from .create_webhook_endpoint_body_metadata import CreateWebhookEndpointBodyMetadata
from .create_webhook_endpoint_response_201 import CreateWebhookEndpointResponse201
from .create_webhook_endpoint_response_201_links import (
    CreateWebhookEndpointResponse201Links,
)
from .create_webhook_endpoint_response_201_links_additional_property import (
    CreateWebhookEndpointResponse201LinksAdditionalProperty,
)
from .create_webhook_endpoint_response_201_merchant import (
    CreateWebhookEndpointResponse201Merchant,
)
from .create_webhook_endpoint_response_201_metadata_type_0 import (
    CreateWebhookEndpointResponse201MetadataType0,
)
from .create_withdrawal_body import CreateWithdrawalBody
from .create_withdrawal_response_201 import CreateWithdrawalResponse201
from .create_withdrawal_response_201_links import CreateWithdrawalResponse201Links
from .create_withdrawal_response_201_links_additional_property import (
    CreateWithdrawalResponse201LinksAdditionalProperty,
)
from .create_withdrawal_response_201_merchant import CreateWithdrawalResponse201Merchant
from .create_withdrawal_response_201_receiving_bank_account_type_0 import (
    CreateWithdrawalResponse201ReceivingBankAccountType0,
)
from .delete_address_response_200 import DeleteAddressResponse200
from .delete_address_response_200_links import DeleteAddressResponse200Links
from .delete_address_response_200_links_additional_property import (
    DeleteAddressResponse200LinksAdditionalProperty,
)
from .delete_address_response_200_merchant import DeleteAddressResponse200Merchant
from .delete_card_response_200 import DeleteCardResponse200
from .delete_card_response_200_links import DeleteCardResponse200Links
from .delete_card_response_200_links_additional_property import (
    DeleteCardResponse200LinksAdditionalProperty,
)
from .delete_card_response_200_merchant import DeleteCardResponse200Merchant
from .delete_checkout_payment_link_response_200 import (
    DeleteCheckoutPaymentLinkResponse200,
)
from .delete_checkout_payment_link_response_200_resource import (
    DeleteCheckoutPaymentLinkResponse200Resource,
)
from .delete_checkout_session_response_200 import DeleteCheckoutSessionResponse200
from .delete_checkout_session_response_200_resource import (
    DeleteCheckoutSessionResponse200Resource,
)
from .delete_coupon_response_200 import DeleteCouponResponse200
from .delete_coupon_response_200_resource import DeleteCouponResponse200Resource
from .delete_customer_response_200 import DeleteCustomerResponse200
from .delete_customer_response_200_links import DeleteCustomerResponse200Links
from .delete_customer_response_200_links_additional_property import (
    DeleteCustomerResponse200LinksAdditionalProperty,
)
from .delete_customer_response_200_merchant import DeleteCustomerResponse200Merchant
from .delete_product_response_200 import DeleteProductResponse200
from .delete_product_response_200_resource import DeleteProductResponse200Resource
from .delete_product_variant_response_200 import DeleteProductVariantResponse200
from .delete_product_variant_response_200_resource import (
    DeleteProductVariantResponse200Resource,
)
from .delete_variant_response_200 import DeleteVariantResponse200
from .delete_variant_response_200_resource import DeleteVariantResponse200Resource
from .delete_wallet_response_200 import DeleteWalletResponse200
from .delete_wallet_response_200_links import DeleteWalletResponse200Links
from .delete_wallet_response_200_links_additional_property import (
    DeleteWalletResponse200LinksAdditionalProperty,
)
from .delete_wallet_response_200_merchant import DeleteWalletResponse200Merchant
from .delete_webhook_endpoint_response_200 import DeleteWebhookEndpointResponse200
from .delete_webhook_endpoint_response_200_links import (
    DeleteWebhookEndpointResponse200Links,
)
from .delete_webhook_endpoint_response_200_links_additional_property import (
    DeleteWebhookEndpointResponse200LinksAdditionalProperty,
)
from .delete_webhook_endpoint_response_200_merchant import (
    DeleteWebhookEndpointResponse200Merchant,
)
from .get_address_response_200 import GetAddressResponse200
from .get_address_response_200_links import GetAddressResponse200Links
from .get_address_response_200_links_additional_property import (
    GetAddressResponse200LinksAdditionalProperty,
)
from .get_address_response_200_merchant import GetAddressResponse200Merchant
from .get_address_response_200_metadata_type_0 import GetAddressResponse200MetadataType0
from .get_address_response_200_owner_type import GetAddressResponse200OwnerType
from .get_balance_response_200 import GetBalanceResponse200
from .get_balance_response_200_merchant import GetBalanceResponse200Merchant
from .get_card_response_200 import GetCardResponse200
from .get_card_response_200_links import GetCardResponse200Links
from .get_card_response_200_links_additional_property import (
    GetCardResponse200LinksAdditionalProperty,
)
from .get_card_response_200_merchant import GetCardResponse200Merchant
from .get_checkout_payment_link_response_200 import GetCheckoutPaymentLinkResponse200
from .get_checkout_payment_link_response_200_custom_inputs_type_0_item import (
    GetCheckoutPaymentLinkResponse200CustomInputsType0Item,
)
from .get_checkout_payment_link_response_200_items_item import (
    GetCheckoutPaymentLinkResponse200ItemsItem,
)
from .get_checkout_payment_link_response_200_metadata_type_0 import (
    GetCheckoutPaymentLinkResponse200MetadataType0,
)
from .get_checkout_session_response_200 import GetCheckoutSessionResponse200
from .get_checkout_session_response_200_address_type_0 import (
    GetCheckoutSessionResponse200AddressType0,
)
from .get_checkout_session_response_200_coupons_item import (
    GetCheckoutSessionResponse200CouponsItem,
)
from .get_checkout_session_response_200_currency import (
    GetCheckoutSessionResponse200Currency,
)
from .get_checkout_session_response_200_custom_inputs import (
    GetCheckoutSessionResponse200CustomInputs,
)
from .get_checkout_session_response_200_customer_type_0 import (
    GetCheckoutSessionResponse200CustomerType0,
)
from .get_checkout_session_response_200_line_items_item import (
    GetCheckoutSessionResponse200LineItemsItem,
)
from .get_checkout_session_response_200_line_items_item_metadata_type_0 import (
    GetCheckoutSessionResponse200LineItemsItemMetadataType0,
)
from .get_checkout_session_response_200_metadata_type_0 import (
    GetCheckoutSessionResponse200MetadataType0,
)
from .get_checkout_session_response_200_object import (
    GetCheckoutSessionResponse200Object,
)
from .get_checkout_session_response_200_payment_methods_item_type_1 import (
    GetCheckoutSessionResponse200PaymentMethodsItemType1,
)
from .get_checkout_session_response_200_payment_selection_type_0 import (
    GetCheckoutSessionResponse200PaymentSelectionType0,
)
from .get_checkout_session_response_200_redirect_urls import (
    GetCheckoutSessionResponse200RedirectUrls,
)
from .get_checkout_session_response_200_status import (
    GetCheckoutSessionResponse200Status,
)
from .get_checkout_session_response_200_totals import (
    GetCheckoutSessionResponse200Totals,
)
from .get_checkout_session_response_200_utm_type_0 import (
    GetCheckoutSessionResponse200UtmType0,
)
from .get_coupon_response_200 import GetCouponResponse200
from .get_coupon_response_200_scope import GetCouponResponse200Scope
from .get_coupon_response_200_type import GetCouponResponse200Type
from .get_customer_response_200 import GetCustomerResponse200
from .get_customer_response_200_addresses_item import (
    GetCustomerResponse200AddressesItem,
)
from .get_customer_response_200_addresses_item_links import (
    GetCustomerResponse200AddressesItemLinks,
)
from .get_customer_response_200_addresses_item_links_additional_property import (
    GetCustomerResponse200AddressesItemLinksAdditionalProperty,
)
from .get_customer_response_200_addresses_item_merchant import (
    GetCustomerResponse200AddressesItemMerchant,
)
from .get_customer_response_200_addresses_item_metadata_type_0 import (
    GetCustomerResponse200AddressesItemMetadataType0,
)
from .get_customer_response_200_addresses_item_owner_type import (
    GetCustomerResponse200AddressesItemOwnerType,
)
from .get_customer_response_200_cards_item import GetCustomerResponse200CardsItem
from .get_customer_response_200_cards_item_links import (
    GetCustomerResponse200CardsItemLinks,
)
from .get_customer_response_200_cards_item_links_additional_property import (
    GetCustomerResponse200CardsItemLinksAdditionalProperty,
)
from .get_customer_response_200_cards_item_merchant import (
    GetCustomerResponse200CardsItemMerchant,
)
from .get_customer_response_200_document_type_0 import (
    GetCustomerResponse200DocumentType0,
)
from .get_customer_response_200_document_type_0_type import (
    GetCustomerResponse200DocumentType0Type,
)
from .get_customer_response_200_links import GetCustomerResponse200Links
from .get_customer_response_200_links_additional_property import (
    GetCustomerResponse200LinksAdditionalProperty,
)
from .get_customer_response_200_merchant import GetCustomerResponse200Merchant
from .get_customer_response_200_metadata_type_0 import (
    GetCustomerResponse200MetadataType0,
)
from .get_customer_response_200_subscriptions_item import (
    GetCustomerResponse200SubscriptionsItem,
)
from .get_customer_response_200_subscriptions_item_billing import (
    GetCustomerResponse200SubscriptionsItemBilling,
)
from .get_customer_response_200_subscriptions_item_billing_address import (
    GetCustomerResponse200SubscriptionsItemBillingAddress,
)
from .get_customer_response_200_subscriptions_item_callback_type_0 import (
    GetCustomerResponse200SubscriptionsItemCallbackType0,
)
from .get_customer_response_200_subscriptions_item_current_cycle_type_0 import (
    GetCustomerResponse200SubscriptionsItemCurrentCycleType0,
)
from .get_customer_response_200_subscriptions_item_customer import (
    GetCustomerResponse200SubscriptionsItemCustomer,
)
from .get_customer_response_200_subscriptions_item_customer_document_type_0 import (
    GetCustomerResponse200SubscriptionsItemCustomerDocumentType0,
)
from .get_customer_response_200_subscriptions_item_customer_metadata_type_0 import (
    GetCustomerResponse200SubscriptionsItemCustomerMetadataType0,
)
from .get_customer_response_200_subscriptions_item_customer_telephone_type_0 import (
    GetCustomerResponse200SubscriptionsItemCustomerTelephoneType0,
)
from .get_customer_response_200_subscriptions_item_discount_type_0 import (
    GetCustomerResponse200SubscriptionsItemDiscountType0,
)
from .get_customer_response_200_subscriptions_item_geolocation_type_0 import (
    GetCustomerResponse200SubscriptionsItemGeolocationType0,
)
from .get_customer_response_200_subscriptions_item_items_item import (
    GetCustomerResponse200SubscriptionsItemItemsItem,
)
from .get_customer_response_200_subscriptions_item_items_item_images_type_0_item_type_1 import (
    GetCustomerResponse200SubscriptionsItemItemsItemImagesType0ItemType1,
)
from .get_customer_response_200_subscriptions_item_items_item_metadata_type_0 import (
    GetCustomerResponse200SubscriptionsItemItemsItemMetadataType0,
)
from .get_customer_response_200_subscriptions_item_links import (
    GetCustomerResponse200SubscriptionsItemLinks,
)
from .get_customer_response_200_subscriptions_item_links_additional_property import (
    GetCustomerResponse200SubscriptionsItemLinksAdditionalProperty,
)
from .get_customer_response_200_subscriptions_item_merchant import (
    GetCustomerResponse200SubscriptionsItemMerchant,
)
from .get_customer_response_200_subscriptions_item_metadata_type_0 import (
    GetCustomerResponse200SubscriptionsItemMetadataType0,
)
from .get_customer_response_200_subscriptions_item_shipping_type_0 import (
    GetCustomerResponse200SubscriptionsItemShippingType0,
)
from .get_customer_response_200_subscriptions_item_splits_type_0_item import (
    GetCustomerResponse200SubscriptionsItemSplitsType0Item,
)
from .get_customer_response_200_subscriptions_item_status import (
    GetCustomerResponse200SubscriptionsItemStatus,
)
from .get_customer_response_200_telephone_type_0 import (
    GetCustomerResponse200TelephoneType0,
)
from .get_customer_response_200_transactions_item import (
    GetCustomerResponse200TransactionsItem,
)
from .get_product_response_200 import GetProductResponse200
from .get_product_response_200_images_type_0_item_type_1 import (
    GetProductResponse200ImagesType0ItemType1,
)
from .get_product_response_200_type import GetProductResponse200Type
from .get_product_response_200_variants_item import GetProductResponse200VariantsItem
from .get_product_response_200_variants_item_attributes_type_0 import (
    GetProductResponse200VariantsItemAttributesType0,
)
from .get_product_response_200_variants_item_images_type_0_item_type_1 import (
    GetProductResponse200VariantsItemImagesType0ItemType1,
)
from .get_product_response_200_variants_item_metadata_type_0 import (
    GetProductResponse200VariantsItemMetadataType0,
)
from .get_product_response_200_variants_item_pricing import (
    GetProductResponse200VariantsItemPricing,
)
from .get_product_response_200_variants_item_pricing_schema import (
    GetProductResponse200VariantsItemPricingSchema,
)
from .get_product_response_200_variants_item_pricing_type import (
    GetProductResponse200VariantsItemPricingType,
)
from .get_product_variant_response_200 import GetProductVariantResponse200
from .get_product_variant_response_200_attributes_type_0 import (
    GetProductVariantResponse200AttributesType0,
)
from .get_product_variant_response_200_images_type_0_item_type_1 import (
    GetProductVariantResponse200ImagesType0ItemType1,
)
from .get_product_variant_response_200_metadata_type_0 import (
    GetProductVariantResponse200MetadataType0,
)
from .get_product_variant_response_200_pricing import (
    GetProductVariantResponse200Pricing,
)
from .get_product_variant_response_200_pricing_schema import (
    GetProductVariantResponse200PricingSchema,
)
from .get_product_variant_response_200_pricing_type import (
    GetProductVariantResponse200PricingType,
)
from .get_receivable_response_200 import GetReceivableResponse200
from .get_receivable_response_200_links import GetReceivableResponse200Links
from .get_receivable_response_200_links_additional_property import (
    GetReceivableResponse200LinksAdditionalProperty,
)
from .get_receivable_response_200_merchant import GetReceivableResponse200Merchant
from .get_subscription_cycle_response_200 import GetSubscriptionCycleResponse200
from .get_subscription_cycle_response_200_links import (
    GetSubscriptionCycleResponse200Links,
)
from .get_subscription_cycle_response_200_links_additional_property import (
    GetSubscriptionCycleResponse200LinksAdditionalProperty,
)
from .get_subscription_cycle_response_200_merchant import (
    GetSubscriptionCycleResponse200Merchant,
)
from .get_subscription_cycle_usage_response_200 import (
    GetSubscriptionCycleUsageResponse200,
)
from .get_subscription_cycle_usage_response_200_aggregated_by_item_item import (
    GetSubscriptionCycleUsageResponse200AggregatedByItemItem,
)
from .get_subscription_item_response_200 import GetSubscriptionItemResponse200
from .get_subscription_item_response_200_images_type_0_item_type_1 import (
    GetSubscriptionItemResponse200ImagesType0ItemType1,
)
from .get_subscription_item_response_200_links import (
    GetSubscriptionItemResponse200Links,
)
from .get_subscription_item_response_200_links_additional_property import (
    GetSubscriptionItemResponse200LinksAdditionalProperty,
)
from .get_subscription_item_response_200_merchant import (
    GetSubscriptionItemResponse200Merchant,
)
from .get_subscription_item_response_200_metadata_type_0 import (
    GetSubscriptionItemResponse200MetadataType0,
)
from .get_subscription_response_200 import GetSubscriptionResponse200
from .get_subscription_response_200_billing import GetSubscriptionResponse200Billing
from .get_subscription_response_200_billing_address import (
    GetSubscriptionResponse200BillingAddress,
)
from .get_subscription_response_200_callback_type_0 import (
    GetSubscriptionResponse200CallbackType0,
)
from .get_subscription_response_200_current_cycle_type_0 import (
    GetSubscriptionResponse200CurrentCycleType0,
)
from .get_subscription_response_200_customer import GetSubscriptionResponse200Customer
from .get_subscription_response_200_customer_document_type_0 import (
    GetSubscriptionResponse200CustomerDocumentType0,
)
from .get_subscription_response_200_customer_metadata_type_0 import (
    GetSubscriptionResponse200CustomerMetadataType0,
)
from .get_subscription_response_200_customer_telephone_type_0 import (
    GetSubscriptionResponse200CustomerTelephoneType0,
)
from .get_subscription_response_200_discount_type_0 import (
    GetSubscriptionResponse200DiscountType0,
)
from .get_subscription_response_200_geolocation_type_0 import (
    GetSubscriptionResponse200GeolocationType0,
)
from .get_subscription_response_200_items_item import (
    GetSubscriptionResponse200ItemsItem,
)
from .get_subscription_response_200_items_item_images_type_0_item_type_1 import (
    GetSubscriptionResponse200ItemsItemImagesType0ItemType1,
)
from .get_subscription_response_200_items_item_metadata_type_0 import (
    GetSubscriptionResponse200ItemsItemMetadataType0,
)
from .get_subscription_response_200_links import GetSubscriptionResponse200Links
from .get_subscription_response_200_links_additional_property import (
    GetSubscriptionResponse200LinksAdditionalProperty,
)
from .get_subscription_response_200_merchant import GetSubscriptionResponse200Merchant
from .get_subscription_response_200_metadata_type_0 import (
    GetSubscriptionResponse200MetadataType0,
)
from .get_subscription_response_200_shipping_type_0 import (
    GetSubscriptionResponse200ShippingType0,
)
from .get_subscription_response_200_splits_type_0_item import (
    GetSubscriptionResponse200SplitsType0Item,
)
from .get_subscription_response_200_status import GetSubscriptionResponse200Status
from .get_subscription_split_response_200 import GetSubscriptionSplitResponse200
from .get_subscription_split_response_200_links import (
    GetSubscriptionSplitResponse200Links,
)
from .get_subscription_split_response_200_links_additional_property import (
    GetSubscriptionSplitResponse200LinksAdditionalProperty,
)
from .get_subscription_split_response_200_merchant import (
    GetSubscriptionSplitResponse200Merchant,
)
from .get_transaction_response_200 import GetTransactionResponse200
from .get_transaction_response_200_billing import GetTransactionResponse200Billing
from .get_transaction_response_200_billing_address import (
    GetTransactionResponse200BillingAddress,
)
from .get_transaction_response_200_callback_type_0 import (
    GetTransactionResponse200CallbackType0,
)
from .get_transaction_response_200_customer_type_0 import (
    GetTransactionResponse200CustomerType0,
)
from .get_transaction_response_200_customer_type_0_document import (
    GetTransactionResponse200CustomerType0Document,
)
from .get_transaction_response_200_customer_type_0_telephone import (
    GetTransactionResponse200CustomerType0Telephone,
)
from .get_transaction_response_200_discount_type_0 import (
    GetTransactionResponse200DiscountType0,
)
from .get_transaction_response_200_disputes_type_0_item import (
    GetTransactionResponse200DisputesType0Item,
)
from .get_transaction_response_200_items_type_0_item import (
    GetTransactionResponse200ItemsType0Item,
)
from .get_transaction_response_200_links import GetTransactionResponse200Links
from .get_transaction_response_200_links_additional_property import (
    GetTransactionResponse200LinksAdditionalProperty,
)
from .get_transaction_response_200_merchant import GetTransactionResponse200Merchant
from .get_transaction_response_200_method import GetTransactionResponse200Method
from .get_transaction_response_200_payment import GetTransactionResponse200Payment
from .get_transaction_response_200_payment_provider import (
    GetTransactionResponse200PaymentProvider,
)
from .get_transaction_response_200_payment_version import (
    GetTransactionResponse200PaymentVersion,
)
from .get_transaction_response_200_receivables_type_0_item import (
    GetTransactionResponse200ReceivablesType0Item,
)
from .get_transaction_response_200_refunds_type_0_item import (
    GetTransactionResponse200RefundsType0Item,
)
from .get_transaction_response_200_splits_type_0_item import (
    GetTransactionResponse200SplitsType0Item,
)
from .get_transaction_response_200_status import GetTransactionResponse200Status
from .get_transaction_response_200_timeline_item import (
    GetTransactionResponse200TimelineItem,
)
from .get_variant_response_200 import GetVariantResponse200
from .get_variant_response_200_attributes_type_0 import (
    GetVariantResponse200AttributesType0,
)
from .get_variant_response_200_images_type_0_item_type_1 import (
    GetVariantResponse200ImagesType0ItemType1,
)
from .get_variant_response_200_metadata_type_0 import GetVariantResponse200MetadataType0
from .get_variant_response_200_pricing import GetVariantResponse200Pricing
from .get_variant_response_200_pricing_schema import GetVariantResponse200PricingSchema
from .get_variant_response_200_pricing_type import GetVariantResponse200PricingType
from .get_wallet_response_200 import GetWalletResponse200
from .get_wallet_response_200_links import GetWalletResponse200Links
from .get_wallet_response_200_links_additional_property import (
    GetWalletResponse200LinksAdditionalProperty,
)
from .get_wallet_response_200_merchant import GetWalletResponse200Merchant
from .get_webhook_endpoint_response_200 import GetWebhookEndpointResponse200
from .get_webhook_endpoint_response_200_links import GetWebhookEndpointResponse200Links
from .get_webhook_endpoint_response_200_links_additional_property import (
    GetWebhookEndpointResponse200LinksAdditionalProperty,
)
from .get_webhook_endpoint_response_200_merchant import (
    GetWebhookEndpointResponse200Merchant,
)
from .get_webhook_endpoint_response_200_metadata_type_0 import (
    GetWebhookEndpointResponse200MetadataType0,
)
from .get_webhook_event_response_200 import GetWebhookEventResponse200
from .get_webhook_event_response_200_dispatches_item import (
    GetWebhookEventResponse200DispatchesItem,
)
from .get_webhook_event_response_200_dispatches_item_status import (
    GetWebhookEventResponse200DispatchesItemStatus,
)
from .get_webhook_event_response_200_links import GetWebhookEventResponse200Links
from .get_webhook_event_response_200_links_additional_property import (
    GetWebhookEventResponse200LinksAdditionalProperty,
)
from .get_webhook_event_response_200_merchant import GetWebhookEventResponse200Merchant
from .get_withdrawal_response_200 import GetWithdrawalResponse200
from .get_withdrawal_response_200_links import GetWithdrawalResponse200Links
from .get_withdrawal_response_200_links_additional_property import (
    GetWithdrawalResponse200LinksAdditionalProperty,
)
from .get_withdrawal_response_200_merchant import GetWithdrawalResponse200Merchant
from .get_withdrawal_response_200_receiving_bank_account_type_0 import (
    GetWithdrawalResponse200ReceivingBankAccountType0,
)
from .list_addresses_response_200 import ListAddressesResponse200
from .list_addresses_response_200_data_item import ListAddressesResponse200DataItem
from .list_addresses_response_200_data_item_links import (
    ListAddressesResponse200DataItemLinks,
)
from .list_addresses_response_200_data_item_links_additional_property import (
    ListAddressesResponse200DataItemLinksAdditionalProperty,
)
from .list_addresses_response_200_data_item_merchant import (
    ListAddressesResponse200DataItemMerchant,
)
from .list_addresses_response_200_data_item_metadata_type_0 import (
    ListAddressesResponse200DataItemMetadataType0,
)
from .list_addresses_response_200_data_item_owner_type import (
    ListAddressesResponse200DataItemOwnerType,
)
from .list_addresses_response_200_links import ListAddressesResponse200Links
from .list_addresses_response_200_links_additional_property import (
    ListAddressesResponse200LinksAdditionalProperty,
)
from .list_addresses_response_200_merchant import ListAddressesResponse200Merchant
from .list_addresses_response_200_page import ListAddressesResponse200Page
from .list_addresses_response_200_page_offset import ListAddressesResponse200PageOffset
from .list_addresses_sort import ListAddressesSort
from .list_all_variants_response_200_item import ListAllVariantsResponse200Item
from .list_all_variants_response_200_item_attributes_type_0 import (
    ListAllVariantsResponse200ItemAttributesType0,
)
from .list_all_variants_response_200_item_images_type_0_item_type_1 import (
    ListAllVariantsResponse200ItemImagesType0ItemType1,
)
from .list_all_variants_response_200_item_metadata_type_0 import (
    ListAllVariantsResponse200ItemMetadataType0,
)
from .list_all_variants_response_200_item_pricing import (
    ListAllVariantsResponse200ItemPricing,
)
from .list_all_variants_response_200_item_pricing_schema import (
    ListAllVariantsResponse200ItemPricingSchema,
)
from .list_all_variants_response_200_item_pricing_type import (
    ListAllVariantsResponse200ItemPricingType,
)
from .list_all_variants_sort import ListAllVariantsSort
from .list_balance_history_response_200 import ListBalanceHistoryResponse200
from .list_balance_history_response_200_data_item import (
    ListBalanceHistoryResponse200DataItem,
)
from .list_balance_history_response_200_data_item_new_balance import (
    ListBalanceHistoryResponse200DataItemNewBalance,
)
from .list_balance_history_response_200_data_item_old_balance import (
    ListBalanceHistoryResponse200DataItemOldBalance,
)
from .list_balance_history_response_200_links import ListBalanceHistoryResponse200Links
from .list_balance_history_response_200_links_additional_property import (
    ListBalanceHistoryResponse200LinksAdditionalProperty,
)
from .list_balance_history_response_200_merchant import (
    ListBalanceHistoryResponse200Merchant,
)
from .list_balance_history_response_200_page import ListBalanceHistoryResponse200Page
from .list_balance_history_response_200_page_offset import (
    ListBalanceHistoryResponse200PageOffset,
)
from .list_cards_response_200 import ListCardsResponse200
from .list_cards_response_200_data_item import ListCardsResponse200DataItem
from .list_cards_response_200_data_item_links import ListCardsResponse200DataItemLinks
from .list_cards_response_200_data_item_links_additional_property import (
    ListCardsResponse200DataItemLinksAdditionalProperty,
)
from .list_cards_response_200_data_item_merchant import (
    ListCardsResponse200DataItemMerchant,
)
from .list_cards_response_200_links import ListCardsResponse200Links
from .list_cards_response_200_links_additional_property import (
    ListCardsResponse200LinksAdditionalProperty,
)
from .list_cards_response_200_merchant import ListCardsResponse200Merchant
from .list_cards_response_200_page import ListCardsResponse200Page
from .list_cards_response_200_page_offset import ListCardsResponse200PageOffset
from .list_cards_sort import ListCardsSort
from .list_checkout_payment_links_response_200 import (
    ListCheckoutPaymentLinksResponse200,
)
from .list_checkout_payment_links_response_200_data_item import (
    ListCheckoutPaymentLinksResponse200DataItem,
)
from .list_checkout_payment_links_response_200_data_item_custom_inputs_type_0_item import (
    ListCheckoutPaymentLinksResponse200DataItemCustomInputsType0Item,
)
from .list_checkout_payment_links_response_200_data_item_items_item import (
    ListCheckoutPaymentLinksResponse200DataItemItemsItem,
)
from .list_checkout_payment_links_response_200_data_item_metadata_type_0 import (
    ListCheckoutPaymentLinksResponse200DataItemMetadataType0,
)
from .list_checkout_payment_links_response_200_page import (
    ListCheckoutPaymentLinksResponse200Page,
)
from .list_checkout_payment_links_response_200_page_offset import (
    ListCheckoutPaymentLinksResponse200PageOffset,
)
from .list_checkout_payment_links_status import ListCheckoutPaymentLinksStatus
from .list_checkout_sessions_response_200 import ListCheckoutSessionsResponse200
from .list_checkout_sessions_response_200_data_item import (
    ListCheckoutSessionsResponse200DataItem,
)
from .list_checkout_sessions_response_200_data_item_object import (
    ListCheckoutSessionsResponse200DataItemObject,
)
from .list_checkout_sessions_response_200_data_item_status import (
    ListCheckoutSessionsResponse200DataItemStatus,
)
from .list_checkout_sessions_response_200_page import (
    ListCheckoutSessionsResponse200Page,
)
from .list_checkout_sessions_response_200_page_offset import (
    ListCheckoutSessionsResponse200PageOffset,
)
from .list_checkout_sessions_status import ListCheckoutSessionsStatus
from .list_coupons_dir import ListCouponsDir
from .list_coupons_response_200 import ListCouponsResponse200
from .list_coupons_response_200_data_item import ListCouponsResponse200DataItem
from .list_coupons_response_200_data_item_scope import (
    ListCouponsResponse200DataItemScope,
)
from .list_coupons_response_200_data_item_type import ListCouponsResponse200DataItemType
from .list_coupons_response_200_page import ListCouponsResponse200Page
from .list_coupons_response_200_page_offset import ListCouponsResponse200PageOffset
from .list_coupons_status import ListCouponsStatus
from .list_coupons_type import ListCouponsType
from .list_customers_response_200 import ListCustomersResponse200
from .list_customers_response_200_data_item import ListCustomersResponse200DataItem
from .list_customers_response_200_data_item_document_type_0 import (
    ListCustomersResponse200DataItemDocumentType0,
)
from .list_customers_response_200_data_item_document_type_0_type import (
    ListCustomersResponse200DataItemDocumentType0Type,
)
from .list_customers_response_200_data_item_links import (
    ListCustomersResponse200DataItemLinks,
)
from .list_customers_response_200_data_item_links_additional_property import (
    ListCustomersResponse200DataItemLinksAdditionalProperty,
)
from .list_customers_response_200_data_item_merchant import (
    ListCustomersResponse200DataItemMerchant,
)
from .list_customers_response_200_data_item_metadata_type_0 import (
    ListCustomersResponse200DataItemMetadataType0,
)
from .list_customers_response_200_data_item_telephone_type_0 import (
    ListCustomersResponse200DataItemTelephoneType0,
)
from .list_customers_response_200_links import ListCustomersResponse200Links
from .list_customers_response_200_links_additional_property import (
    ListCustomersResponse200LinksAdditionalProperty,
)
from .list_customers_response_200_merchant import ListCustomersResponse200Merchant
from .list_customers_response_200_page import ListCustomersResponse200Page
from .list_customers_response_200_page_offset import ListCustomersResponse200PageOffset
from .list_product_variants_response_200 import ListProductVariantsResponse200
from .list_product_variants_response_200_data_item import (
    ListProductVariantsResponse200DataItem,
)
from .list_product_variants_response_200_data_item_attributes_type_0 import (
    ListProductVariantsResponse200DataItemAttributesType0,
)
from .list_product_variants_response_200_data_item_images_type_0_item_type_1 import (
    ListProductVariantsResponse200DataItemImagesType0ItemType1,
)
from .list_product_variants_response_200_data_item_metadata_type_0 import (
    ListProductVariantsResponse200DataItemMetadataType0,
)
from .list_product_variants_response_200_data_item_pricing import (
    ListProductVariantsResponse200DataItemPricing,
)
from .list_product_variants_response_200_data_item_pricing_schema import (
    ListProductVariantsResponse200DataItemPricingSchema,
)
from .list_product_variants_response_200_data_item_pricing_type import (
    ListProductVariantsResponse200DataItemPricingType,
)
from .list_product_variants_response_200_page import ListProductVariantsResponse200Page
from .list_product_variants_response_200_page_offset import (
    ListProductVariantsResponse200PageOffset,
)
from .list_products_response_200 import ListProductsResponse200
from .list_products_response_200_data_item import ListProductsResponse200DataItem
from .list_products_response_200_data_item_images_type_0_item_type_1 import (
    ListProductsResponse200DataItemImagesType0ItemType1,
)
from .list_products_response_200_data_item_type import (
    ListProductsResponse200DataItemType,
)
from .list_products_response_200_data_item_variants_item import (
    ListProductsResponse200DataItemVariantsItem,
)
from .list_products_response_200_data_item_variants_item_attributes_type_0 import (
    ListProductsResponse200DataItemVariantsItemAttributesType0,
)
from .list_products_response_200_data_item_variants_item_images_type_0_item_type_1 import (
    ListProductsResponse200DataItemVariantsItemImagesType0ItemType1,
)
from .list_products_response_200_data_item_variants_item_metadata_type_0 import (
    ListProductsResponse200DataItemVariantsItemMetadataType0,
)
from .list_products_response_200_data_item_variants_item_pricing import (
    ListProductsResponse200DataItemVariantsItemPricing,
)
from .list_products_response_200_data_item_variants_item_pricing_schema import (
    ListProductsResponse200DataItemVariantsItemPricingSchema,
)
from .list_products_response_200_data_item_variants_item_pricing_type import (
    ListProductsResponse200DataItemVariantsItemPricingType,
)
from .list_products_response_200_page import ListProductsResponse200Page
from .list_products_response_200_page_offset import ListProductsResponse200PageOffset
from .list_receivables_released import ListReceivablesReleased
from .list_receivables_response_200 import ListReceivablesResponse200
from .list_receivables_response_200_data_item import ListReceivablesResponse200DataItem
from .list_receivables_response_200_data_item_links import (
    ListReceivablesResponse200DataItemLinks,
)
from .list_receivables_response_200_data_item_links_additional_property import (
    ListReceivablesResponse200DataItemLinksAdditionalProperty,
)
from .list_receivables_response_200_data_item_merchant import (
    ListReceivablesResponse200DataItemMerchant,
)
from .list_receivables_response_200_links import ListReceivablesResponse200Links
from .list_receivables_response_200_links_additional_property import (
    ListReceivablesResponse200LinksAdditionalProperty,
)
from .list_receivables_response_200_merchant import ListReceivablesResponse200Merchant
from .list_receivables_response_200_page import ListReceivablesResponse200Page
from .list_receivables_response_200_page_offset import (
    ListReceivablesResponse200PageOffset,
)
from .list_subscription_cycles_response_200 import ListSubscriptionCyclesResponse200
from .list_subscription_cycles_response_200_data_item import (
    ListSubscriptionCyclesResponse200DataItem,
)
from .list_subscription_cycles_response_200_data_item_links import (
    ListSubscriptionCyclesResponse200DataItemLinks,
)
from .list_subscription_cycles_response_200_data_item_links_additional_property import (
    ListSubscriptionCyclesResponse200DataItemLinksAdditionalProperty,
)
from .list_subscription_cycles_response_200_data_item_merchant import (
    ListSubscriptionCyclesResponse200DataItemMerchant,
)
from .list_subscription_cycles_response_200_links import (
    ListSubscriptionCyclesResponse200Links,
)
from .list_subscription_cycles_response_200_links_additional_property import (
    ListSubscriptionCyclesResponse200LinksAdditionalProperty,
)
from .list_subscription_cycles_response_200_merchant import (
    ListSubscriptionCyclesResponse200Merchant,
)
from .list_subscription_cycles_response_200_page import (
    ListSubscriptionCyclesResponse200Page,
)
from .list_subscription_cycles_response_200_page_offset import (
    ListSubscriptionCyclesResponse200PageOffset,
)
from .list_subscription_cycles_status import ListSubscriptionCyclesStatus
from .list_subscription_items_response_200 import ListSubscriptionItemsResponse200
from .list_subscription_items_response_200_data_item import (
    ListSubscriptionItemsResponse200DataItem,
)
from .list_subscription_items_response_200_data_item_images_type_0_item_type_1 import (
    ListSubscriptionItemsResponse200DataItemImagesType0ItemType1,
)
from .list_subscription_items_response_200_data_item_links import (
    ListSubscriptionItemsResponse200DataItemLinks,
)
from .list_subscription_items_response_200_data_item_links_additional_property import (
    ListSubscriptionItemsResponse200DataItemLinksAdditionalProperty,
)
from .list_subscription_items_response_200_data_item_merchant import (
    ListSubscriptionItemsResponse200DataItemMerchant,
)
from .list_subscription_items_response_200_data_item_metadata_type_0 import (
    ListSubscriptionItemsResponse200DataItemMetadataType0,
)
from .list_subscription_items_response_200_links import (
    ListSubscriptionItemsResponse200Links,
)
from .list_subscription_items_response_200_links_additional_property import (
    ListSubscriptionItemsResponse200LinksAdditionalProperty,
)
from .list_subscription_items_response_200_merchant import (
    ListSubscriptionItemsResponse200Merchant,
)
from .list_subscription_items_response_200_page import (
    ListSubscriptionItemsResponse200Page,
)
from .list_subscription_items_response_200_page_offset import (
    ListSubscriptionItemsResponse200PageOffset,
)
from .list_subscription_splits_response_200 import ListSubscriptionSplitsResponse200
from .list_subscription_splits_response_200_data_item import (
    ListSubscriptionSplitsResponse200DataItem,
)
from .list_subscription_splits_response_200_data_item_links import (
    ListSubscriptionSplitsResponse200DataItemLinks,
)
from .list_subscription_splits_response_200_data_item_links_additional_property import (
    ListSubscriptionSplitsResponse200DataItemLinksAdditionalProperty,
)
from .list_subscription_splits_response_200_data_item_merchant import (
    ListSubscriptionSplitsResponse200DataItemMerchant,
)
from .list_subscription_splits_response_200_links import (
    ListSubscriptionSplitsResponse200Links,
)
from .list_subscription_splits_response_200_links_additional_property import (
    ListSubscriptionSplitsResponse200LinksAdditionalProperty,
)
from .list_subscription_splits_response_200_merchant import (
    ListSubscriptionSplitsResponse200Merchant,
)
from .list_subscription_splits_response_200_page import (
    ListSubscriptionSplitsResponse200Page,
)
from .list_subscription_splits_response_200_page_offset import (
    ListSubscriptionSplitsResponse200PageOffset,
)
from .list_subscription_thresholds_response_200 import (
    ListSubscriptionThresholdsResponse200,
)
from .list_subscription_thresholds_response_200_data_item import (
    ListSubscriptionThresholdsResponse200DataItem,
)
from .list_subscription_thresholds_response_200_data_item_kind import (
    ListSubscriptionThresholdsResponse200DataItemKind,
)
from .list_subscription_thresholds_response_200_links import (
    ListSubscriptionThresholdsResponse200Links,
)
from .list_subscription_thresholds_response_200_links_additional_property import (
    ListSubscriptionThresholdsResponse200LinksAdditionalProperty,
)
from .list_subscription_thresholds_response_200_merchant import (
    ListSubscriptionThresholdsResponse200Merchant,
)
from .list_subscription_thresholds_response_200_page import (
    ListSubscriptionThresholdsResponse200Page,
)
from .list_subscription_thresholds_response_200_page_offset import (
    ListSubscriptionThresholdsResponse200PageOffset,
)
from .list_subscription_usage_response_200 import ListSubscriptionUsageResponse200
from .list_subscription_usage_response_200_data_item import (
    ListSubscriptionUsageResponse200DataItem,
)
from .list_subscription_usage_response_200_links import (
    ListSubscriptionUsageResponse200Links,
)
from .list_subscription_usage_response_200_links_additional_property import (
    ListSubscriptionUsageResponse200LinksAdditionalProperty,
)
from .list_subscription_usage_response_200_merchant import (
    ListSubscriptionUsageResponse200Merchant,
)
from .list_subscription_usage_response_200_page import (
    ListSubscriptionUsageResponse200Page,
)
from .list_subscription_usage_response_200_page_offset import (
    ListSubscriptionUsageResponse200PageOffset,
)
from .list_subscriptions_response_200 import ListSubscriptionsResponse200
from .list_subscriptions_response_200_data_item import (
    ListSubscriptionsResponse200DataItem,
)
from .list_subscriptions_response_200_data_item_billing import (
    ListSubscriptionsResponse200DataItemBilling,
)
from .list_subscriptions_response_200_data_item_billing_address import (
    ListSubscriptionsResponse200DataItemBillingAddress,
)
from .list_subscriptions_response_200_data_item_callback_type_0 import (
    ListSubscriptionsResponse200DataItemCallbackType0,
)
from .list_subscriptions_response_200_data_item_current_cycle_type_0 import (
    ListSubscriptionsResponse200DataItemCurrentCycleType0,
)
from .list_subscriptions_response_200_data_item_customer import (
    ListSubscriptionsResponse200DataItemCustomer,
)
from .list_subscriptions_response_200_data_item_customer_document_type_0 import (
    ListSubscriptionsResponse200DataItemCustomerDocumentType0,
)
from .list_subscriptions_response_200_data_item_customer_metadata_type_0 import (
    ListSubscriptionsResponse200DataItemCustomerMetadataType0,
)
from .list_subscriptions_response_200_data_item_customer_telephone_type_0 import (
    ListSubscriptionsResponse200DataItemCustomerTelephoneType0,
)
from .list_subscriptions_response_200_data_item_discount_type_0 import (
    ListSubscriptionsResponse200DataItemDiscountType0,
)
from .list_subscriptions_response_200_data_item_geolocation_type_0 import (
    ListSubscriptionsResponse200DataItemGeolocationType0,
)
from .list_subscriptions_response_200_data_item_items_item import (
    ListSubscriptionsResponse200DataItemItemsItem,
)
from .list_subscriptions_response_200_data_item_items_item_images_type_0_item_type_1 import (
    ListSubscriptionsResponse200DataItemItemsItemImagesType0ItemType1,
)
from .list_subscriptions_response_200_data_item_items_item_metadata_type_0 import (
    ListSubscriptionsResponse200DataItemItemsItemMetadataType0,
)
from .list_subscriptions_response_200_data_item_links import (
    ListSubscriptionsResponse200DataItemLinks,
)
from .list_subscriptions_response_200_data_item_links_additional_property import (
    ListSubscriptionsResponse200DataItemLinksAdditionalProperty,
)
from .list_subscriptions_response_200_data_item_merchant import (
    ListSubscriptionsResponse200DataItemMerchant,
)
from .list_subscriptions_response_200_data_item_metadata_type_0 import (
    ListSubscriptionsResponse200DataItemMetadataType0,
)
from .list_subscriptions_response_200_data_item_shipping_type_0 import (
    ListSubscriptionsResponse200DataItemShippingType0,
)
from .list_subscriptions_response_200_data_item_splits_type_0_item import (
    ListSubscriptionsResponse200DataItemSplitsType0Item,
)
from .list_subscriptions_response_200_data_item_status import (
    ListSubscriptionsResponse200DataItemStatus,
)
from .list_subscriptions_response_200_links import ListSubscriptionsResponse200Links
from .list_subscriptions_response_200_links_additional_property import (
    ListSubscriptionsResponse200LinksAdditionalProperty,
)
from .list_subscriptions_response_200_merchant import (
    ListSubscriptionsResponse200Merchant,
)
from .list_subscriptions_response_200_page import ListSubscriptionsResponse200Page
from .list_subscriptions_response_200_page_offset import (
    ListSubscriptionsResponse200PageOffset,
)
from .list_subscriptions_status import ListSubscriptionsStatus
from .list_transactions_method import ListTransactionsMethod
from .list_transactions_response_200 import ListTransactionsResponse200
from .list_transactions_response_200_data_item import (
    ListTransactionsResponse200DataItem,
)
from .list_transactions_response_200_links import ListTransactionsResponse200Links
from .list_transactions_response_200_links_additional_property import (
    ListTransactionsResponse200LinksAdditionalProperty,
)
from .list_transactions_response_200_merchant import ListTransactionsResponse200Merchant
from .list_transactions_response_200_page import ListTransactionsResponse200Page
from .list_transactions_response_200_page_offset import (
    ListTransactionsResponse200PageOffset,
)
from .list_transactions_status import ListTransactionsStatus
from .list_wallets_response_200 import ListWalletsResponse200
from .list_wallets_response_200_data_item import ListWalletsResponse200DataItem
from .list_wallets_response_200_data_item_links import (
    ListWalletsResponse200DataItemLinks,
)
from .list_wallets_response_200_data_item_links_additional_property import (
    ListWalletsResponse200DataItemLinksAdditionalProperty,
)
from .list_wallets_response_200_data_item_merchant import (
    ListWalletsResponse200DataItemMerchant,
)
from .list_wallets_response_200_links import ListWalletsResponse200Links
from .list_wallets_response_200_links_additional_property import (
    ListWalletsResponse200LinksAdditionalProperty,
)
from .list_wallets_response_200_merchant import ListWalletsResponse200Merchant
from .list_wallets_response_200_page import ListWalletsResponse200Page
from .list_wallets_response_200_page_offset import ListWalletsResponse200PageOffset
from .list_webhook_dispatches_response_200 import ListWebhookDispatchesResponse200
from .list_webhook_dispatches_response_200_data_item import (
    ListWebhookDispatchesResponse200DataItem,
)
from .list_webhook_dispatches_response_200_data_item_status import (
    ListWebhookDispatchesResponse200DataItemStatus,
)
from .list_webhook_dispatches_response_200_links import (
    ListWebhookDispatchesResponse200Links,
)
from .list_webhook_dispatches_response_200_links_additional_property import (
    ListWebhookDispatchesResponse200LinksAdditionalProperty,
)
from .list_webhook_dispatches_response_200_merchant import (
    ListWebhookDispatchesResponse200Merchant,
)
from .list_webhook_dispatches_response_200_page import (
    ListWebhookDispatchesResponse200Page,
)
from .list_webhook_dispatches_response_200_page_offset import (
    ListWebhookDispatchesResponse200PageOffset,
)
from .list_webhook_dispatches_status import ListWebhookDispatchesStatus
from .list_webhook_endpoints_response_200 import ListWebhookEndpointsResponse200
from .list_webhook_endpoints_response_200_data_item import (
    ListWebhookEndpointsResponse200DataItem,
)
from .list_webhook_endpoints_response_200_data_item_links import (
    ListWebhookEndpointsResponse200DataItemLinks,
)
from .list_webhook_endpoints_response_200_data_item_links_additional_property import (
    ListWebhookEndpointsResponse200DataItemLinksAdditionalProperty,
)
from .list_webhook_endpoints_response_200_data_item_merchant import (
    ListWebhookEndpointsResponse200DataItemMerchant,
)
from .list_webhook_endpoints_response_200_data_item_metadata_type_0 import (
    ListWebhookEndpointsResponse200DataItemMetadataType0,
)
from .list_webhook_endpoints_response_200_links import (
    ListWebhookEndpointsResponse200Links,
)
from .list_webhook_endpoints_response_200_links_additional_property import (
    ListWebhookEndpointsResponse200LinksAdditionalProperty,
)
from .list_webhook_endpoints_response_200_merchant import (
    ListWebhookEndpointsResponse200Merchant,
)
from .list_webhook_endpoints_response_200_page import (
    ListWebhookEndpointsResponse200Page,
)
from .list_webhook_endpoints_response_200_page_offset import (
    ListWebhookEndpointsResponse200PageOffset,
)
from .list_webhook_events_response_200 import ListWebhookEventsResponse200
from .list_webhook_events_response_200_data_item import (
    ListWebhookEventsResponse200DataItem,
)
from .list_webhook_events_response_200_data_item_dispatches_item import (
    ListWebhookEventsResponse200DataItemDispatchesItem,
)
from .list_webhook_events_response_200_data_item_dispatches_item_status import (
    ListWebhookEventsResponse200DataItemDispatchesItemStatus,
)
from .list_webhook_events_response_200_data_item_links import (
    ListWebhookEventsResponse200DataItemLinks,
)
from .list_webhook_events_response_200_data_item_links_additional_property import (
    ListWebhookEventsResponse200DataItemLinksAdditionalProperty,
)
from .list_webhook_events_response_200_data_item_merchant import (
    ListWebhookEventsResponse200DataItemMerchant,
)
from .list_webhook_events_response_200_links import ListWebhookEventsResponse200Links
from .list_webhook_events_response_200_links_additional_property import (
    ListWebhookEventsResponse200LinksAdditionalProperty,
)
from .list_webhook_events_response_200_merchant import (
    ListWebhookEventsResponse200Merchant,
)
from .list_webhook_events_response_200_page import ListWebhookEventsResponse200Page
from .list_webhook_events_response_200_page_offset import (
    ListWebhookEventsResponse200PageOffset,
)
from .list_webhook_events_status import ListWebhookEventsStatus
from .list_webhook_events_type import ListWebhookEventsType
from .list_withdrawals_response_200 import ListWithdrawalsResponse200
from .list_withdrawals_response_200_data_item import ListWithdrawalsResponse200DataItem
from .list_withdrawals_response_200_data_item_links import (
    ListWithdrawalsResponse200DataItemLinks,
)
from .list_withdrawals_response_200_data_item_links_additional_property import (
    ListWithdrawalsResponse200DataItemLinksAdditionalProperty,
)
from .list_withdrawals_response_200_data_item_merchant import (
    ListWithdrawalsResponse200DataItemMerchant,
)
from .list_withdrawals_response_200_data_item_receiving_bank_account_type_0 import (
    ListWithdrawalsResponse200DataItemReceivingBankAccountType0,
)
from .list_withdrawals_response_200_links import ListWithdrawalsResponse200Links
from .list_withdrawals_response_200_links_additional_property import (
    ListWithdrawalsResponse200LinksAdditionalProperty,
)
from .list_withdrawals_response_200_merchant import ListWithdrawalsResponse200Merchant
from .list_withdrawals_response_200_page import ListWithdrawalsResponse200Page
from .list_withdrawals_response_200_page_offset import (
    ListWithdrawalsResponse200PageOffset,
)
from .patch_coupon_body import PatchCouponBody
from .patch_coupon_body_scope import PatchCouponBodyScope
from .patch_coupon_body_type import PatchCouponBodyType
from .patch_coupon_response_200 import PatchCouponResponse200
from .patch_coupon_response_200_scope import PatchCouponResponse200Scope
from .patch_coupon_response_200_type import PatchCouponResponse200Type
from .pause_subscription_response_200 import PauseSubscriptionResponse200
from .pause_subscription_response_200_billing import PauseSubscriptionResponse200Billing
from .pause_subscription_response_200_billing_address import (
    PauseSubscriptionResponse200BillingAddress,
)
from .pause_subscription_response_200_callback_type_0 import (
    PauseSubscriptionResponse200CallbackType0,
)
from .pause_subscription_response_200_current_cycle_type_0 import (
    PauseSubscriptionResponse200CurrentCycleType0,
)
from .pause_subscription_response_200_customer import (
    PauseSubscriptionResponse200Customer,
)
from .pause_subscription_response_200_customer_document_type_0 import (
    PauseSubscriptionResponse200CustomerDocumentType0,
)
from .pause_subscription_response_200_customer_metadata_type_0 import (
    PauseSubscriptionResponse200CustomerMetadataType0,
)
from .pause_subscription_response_200_customer_telephone_type_0 import (
    PauseSubscriptionResponse200CustomerTelephoneType0,
)
from .pause_subscription_response_200_discount_type_0 import (
    PauseSubscriptionResponse200DiscountType0,
)
from .pause_subscription_response_200_geolocation_type_0 import (
    PauseSubscriptionResponse200GeolocationType0,
)
from .pause_subscription_response_200_items_item import (
    PauseSubscriptionResponse200ItemsItem,
)
from .pause_subscription_response_200_items_item_images_type_0_item_type_1 import (
    PauseSubscriptionResponse200ItemsItemImagesType0ItemType1,
)
from .pause_subscription_response_200_items_item_metadata_type_0 import (
    PauseSubscriptionResponse200ItemsItemMetadataType0,
)
from .pause_subscription_response_200_links import PauseSubscriptionResponse200Links
from .pause_subscription_response_200_links_additional_property import (
    PauseSubscriptionResponse200LinksAdditionalProperty,
)
from .pause_subscription_response_200_merchant import (
    PauseSubscriptionResponse200Merchant,
)
from .pause_subscription_response_200_metadata_type_0 import (
    PauseSubscriptionResponse200MetadataType0,
)
from .pause_subscription_response_200_shipping_type_0 import (
    PauseSubscriptionResponse200ShippingType0,
)
from .pause_subscription_response_200_splits_type_0_item import (
    PauseSubscriptionResponse200SplitsType0Item,
)
from .pause_subscription_response_200_status import PauseSubscriptionResponse200Status
from .record_subscription_usage_body import RecordSubscriptionUsageBody
from .record_subscription_usage_body_action import RecordSubscriptionUsageBodyAction
from .record_subscription_usage_body_metadata import RecordSubscriptionUsageBodyMetadata
from .record_subscription_usage_response_200 import RecordSubscriptionUsageResponse200
from .record_subscription_usage_response_201 import RecordSubscriptionUsageResponse201
from .redispatch_webhook_response_202 import RedispatchWebhookResponse202
from .refund_transaction_body import RefundTransactionBody
from .refund_transaction_response_202 import RefundTransactionResponse202
from .refund_transaction_response_202_status import RefundTransactionResponse202Status
from .remove_subscription_item_response_200 import RemoveSubscriptionItemResponse200
from .remove_subscription_item_response_200_links import (
    RemoveSubscriptionItemResponse200Links,
)
from .remove_subscription_item_response_200_links_additional_property import (
    RemoveSubscriptionItemResponse200LinksAdditionalProperty,
)
from .remove_subscription_item_response_200_merchant import (
    RemoveSubscriptionItemResponse200Merchant,
)
from .remove_subscription_split_response_200 import RemoveSubscriptionSplitResponse200
from .remove_subscription_split_response_200_links import (
    RemoveSubscriptionSplitResponse200Links,
)
from .remove_subscription_split_response_200_links_additional_property import (
    RemoveSubscriptionSplitResponse200LinksAdditionalProperty,
)
from .remove_subscription_split_response_200_merchant import (
    RemoveSubscriptionSplitResponse200Merchant,
)
from .remove_subscription_split_response_200_splits_item import (
    RemoveSubscriptionSplitResponse200SplitsItem,
)
from .remove_subscription_split_response_200_splits_item_links import (
    RemoveSubscriptionSplitResponse200SplitsItemLinks,
)
from .remove_subscription_split_response_200_splits_item_links_additional_property import (
    RemoveSubscriptionSplitResponse200SplitsItemLinksAdditionalProperty,
)
from .remove_subscription_split_response_200_splits_item_merchant import (
    RemoveSubscriptionSplitResponse200SplitsItemMerchant,
)
from .remove_subscription_threshold_response_200 import (
    RemoveSubscriptionThresholdResponse200,
)
from .renew_subscription_cycle_response_201 import RenewSubscriptionCycleResponse201
from .renew_subscription_cycle_response_201_links import (
    RenewSubscriptionCycleResponse201Links,
)
from .renew_subscription_cycle_response_201_links_additional_property import (
    RenewSubscriptionCycleResponse201LinksAdditionalProperty,
)
from .renew_subscription_cycle_response_201_merchant import (
    RenewSubscriptionCycleResponse201Merchant,
)
from .resend_webhook_event_response_202 import ResendWebhookEventResponse202
from .resume_subscription_response_200 import ResumeSubscriptionResponse200
from .resume_subscription_response_200_billing import (
    ResumeSubscriptionResponse200Billing,
)
from .resume_subscription_response_200_billing_address import (
    ResumeSubscriptionResponse200BillingAddress,
)
from .resume_subscription_response_200_callback_type_0 import (
    ResumeSubscriptionResponse200CallbackType0,
)
from .resume_subscription_response_200_current_cycle_type_0 import (
    ResumeSubscriptionResponse200CurrentCycleType0,
)
from .resume_subscription_response_200_customer import (
    ResumeSubscriptionResponse200Customer,
)
from .resume_subscription_response_200_customer_document_type_0 import (
    ResumeSubscriptionResponse200CustomerDocumentType0,
)
from .resume_subscription_response_200_customer_metadata_type_0 import (
    ResumeSubscriptionResponse200CustomerMetadataType0,
)
from .resume_subscription_response_200_customer_telephone_type_0 import (
    ResumeSubscriptionResponse200CustomerTelephoneType0,
)
from .resume_subscription_response_200_discount_type_0 import (
    ResumeSubscriptionResponse200DiscountType0,
)
from .resume_subscription_response_200_geolocation_type_0 import (
    ResumeSubscriptionResponse200GeolocationType0,
)
from .resume_subscription_response_200_items_item import (
    ResumeSubscriptionResponse200ItemsItem,
)
from .resume_subscription_response_200_items_item_images_type_0_item_type_1 import (
    ResumeSubscriptionResponse200ItemsItemImagesType0ItemType1,
)
from .resume_subscription_response_200_items_item_metadata_type_0 import (
    ResumeSubscriptionResponse200ItemsItemMetadataType0,
)
from .resume_subscription_response_200_links import ResumeSubscriptionResponse200Links
from .resume_subscription_response_200_links_additional_property import (
    ResumeSubscriptionResponse200LinksAdditionalProperty,
)
from .resume_subscription_response_200_merchant import (
    ResumeSubscriptionResponse200Merchant,
)
from .resume_subscription_response_200_metadata_type_0 import (
    ResumeSubscriptionResponse200MetadataType0,
)
from .resume_subscription_response_200_shipping_type_0 import (
    ResumeSubscriptionResponse200ShippingType0,
)
from .resume_subscription_response_200_splits_type_0_item import (
    ResumeSubscriptionResponse200SplitsType0Item,
)
from .resume_subscription_response_200_status import ResumeSubscriptionResponse200Status
from .rotate_webhook_secret_response_200 import RotateWebhookSecretResponse200
from .rotate_webhook_secret_response_200_links import (
    RotateWebhookSecretResponse200Links,
)
from .rotate_webhook_secret_response_200_links_additional_property import (
    RotateWebhookSecretResponse200LinksAdditionalProperty,
)
from .rotate_webhook_secret_response_200_merchant import (
    RotateWebhookSecretResponse200Merchant,
)
from .rotate_webhook_secret_response_200_metadata_type_0 import (
    RotateWebhookSecretResponse200MetadataType0,
)
from .simulate_installment_resource import SimulateInstallmentResource
from .simulate_installment_response_200 import SimulateInstallmentResponse200
from .simulate_installment_response_200_amount import (
    SimulateInstallmentResponse200Amount,
)
from .simulate_installment_response_200_links import SimulateInstallmentResponse200Links
from .simulate_installment_response_200_links_installments import (
    SimulateInstallmentResponse200LinksInstallments,
)
from .simulate_installment_response_200_links_payment_methods import (
    SimulateInstallmentResponse200LinksPaymentMethods,
)
from .simulate_installment_response_200_links_self import (
    SimulateInstallmentResponse200LinksSelf,
)
from .simulate_installment_response_200_merchant import (
    SimulateInstallmentResponse200Merchant,
)
from .simulate_installment_response_200_original import (
    SimulateInstallmentResponse200Original,
)
from .simulate_installment_response_200_resource import (
    SimulateInstallmentResponse200Resource,
)
from .simulate_installment_response_200_total_fees import (
    SimulateInstallmentResponse200TotalFees,
)
from .simulate_installments_resource import SimulateInstallmentsResource
from .simulate_installments_response_200 import SimulateInstallmentsResponse200
from .simulate_installments_response_200_installments_item import (
    SimulateInstallmentsResponse200InstallmentsItem,
)
from .simulate_installments_response_200_links import (
    SimulateInstallmentsResponse200Links,
)
from .simulate_installments_response_200_links_installment import (
    SimulateInstallmentsResponse200LinksInstallment,
)
from .simulate_installments_response_200_links_payment_methods import (
    SimulateInstallmentsResponse200LinksPaymentMethods,
)
from .simulate_installments_response_200_links_self import (
    SimulateInstallmentsResponse200LinksSelf,
)
from .simulate_installments_response_200_merchant import (
    SimulateInstallmentsResponse200Merchant,
)
from .simulate_installments_response_200_resource import (
    SimulateInstallmentsResponse200Resource,
)
from .simulate_payment_methods_method import SimulatePaymentMethodsMethod
from .simulate_payment_methods_response_200 import SimulatePaymentMethodsResponse200
from .simulate_payment_methods_response_200_amount import (
    SimulatePaymentMethodsResponse200Amount,
)
from .simulate_payment_methods_response_200_links import (
    SimulatePaymentMethodsResponse200Links,
)
from .simulate_payment_methods_response_200_links_installment import (
    SimulatePaymentMethodsResponse200LinksInstallment,
)
from .simulate_payment_methods_response_200_links_installments import (
    SimulatePaymentMethodsResponse200LinksInstallments,
)
from .simulate_payment_methods_response_200_links_self import (
    SimulatePaymentMethodsResponse200LinksSelf,
)
from .simulate_payment_methods_response_200_merchant import (
    SimulatePaymentMethodsResponse200Merchant,
)
from .simulate_payment_methods_response_200_original import (
    SimulatePaymentMethodsResponse200Original,
)
from .simulate_payment_methods_response_200_resource import (
    SimulatePaymentMethodsResponse200Resource,
)
from .simulate_payment_methods_response_200_total_fees import (
    SimulatePaymentMethodsResponse200TotalFees,
)
from .submit_checkout_payment_body import SubmitCheckoutPaymentBody
from .submit_checkout_payment_body_payment import SubmitCheckoutPaymentBodyPayment
from .submit_checkout_payment_body_payment_method import (
    SubmitCheckoutPaymentBodyPaymentMethod,
)
from .submit_checkout_payment_response_202 import SubmitCheckoutPaymentResponse202
from .submit_checkout_payment_response_202_status import (
    SubmitCheckoutPaymentResponse202Status,
)
from .submit_transaction_dispute_body import SubmitTransactionDisputeBody
from .submit_transaction_dispute_body_documents_item import (
    SubmitTransactionDisputeBodyDocumentsItem,
)
from .submit_transaction_dispute_body_documents_item_authentication import (
    SubmitTransactionDisputeBodyDocumentsItemAuthentication,
)
from .submit_transaction_dispute_body_documents_item_type import (
    SubmitTransactionDisputeBodyDocumentsItemType,
)
from .submit_transaction_dispute_response_200 import SubmitTransactionDisputeResponse200
from .submit_transaction_dispute_response_200_billing import (
    SubmitTransactionDisputeResponse200Billing,
)
from .submit_transaction_dispute_response_200_billing_address import (
    SubmitTransactionDisputeResponse200BillingAddress,
)
from .submit_transaction_dispute_response_200_callback_type_0 import (
    SubmitTransactionDisputeResponse200CallbackType0,
)
from .submit_transaction_dispute_response_200_customer_type_0 import (
    SubmitTransactionDisputeResponse200CustomerType0,
)
from .submit_transaction_dispute_response_200_customer_type_0_document import (
    SubmitTransactionDisputeResponse200CustomerType0Document,
)
from .submit_transaction_dispute_response_200_customer_type_0_telephone import (
    SubmitTransactionDisputeResponse200CustomerType0Telephone,
)
from .submit_transaction_dispute_response_200_discount_type_0 import (
    SubmitTransactionDisputeResponse200DiscountType0,
)
from .submit_transaction_dispute_response_200_disputes_type_0_item import (
    SubmitTransactionDisputeResponse200DisputesType0Item,
)
from .submit_transaction_dispute_response_200_items_type_0_item import (
    SubmitTransactionDisputeResponse200ItemsType0Item,
)
from .submit_transaction_dispute_response_200_links import (
    SubmitTransactionDisputeResponse200Links,
)
from .submit_transaction_dispute_response_200_links_additional_property import (
    SubmitTransactionDisputeResponse200LinksAdditionalProperty,
)
from .submit_transaction_dispute_response_200_merchant import (
    SubmitTransactionDisputeResponse200Merchant,
)
from .submit_transaction_dispute_response_200_method import (
    SubmitTransactionDisputeResponse200Method,
)
from .submit_transaction_dispute_response_200_payment import (
    SubmitTransactionDisputeResponse200Payment,
)
from .submit_transaction_dispute_response_200_payment_provider import (
    SubmitTransactionDisputeResponse200PaymentProvider,
)
from .submit_transaction_dispute_response_200_payment_version import (
    SubmitTransactionDisputeResponse200PaymentVersion,
)
from .submit_transaction_dispute_response_200_receivables_type_0_item import (
    SubmitTransactionDisputeResponse200ReceivablesType0Item,
)
from .submit_transaction_dispute_response_200_refunds_type_0_item import (
    SubmitTransactionDisputeResponse200RefundsType0Item,
)
from .submit_transaction_dispute_response_200_splits_type_0_item import (
    SubmitTransactionDisputeResponse200SplitsType0Item,
)
from .submit_transaction_dispute_response_200_status import (
    SubmitTransactionDisputeResponse200Status,
)
from .submit_transaction_dispute_response_200_timeline_item import (
    SubmitTransactionDisputeResponse200TimelineItem,
)
from .test_webhook_endpoint_body_type_1 import TestWebhookEndpointBodyType1
from .test_webhook_endpoint_response_202 import TestWebhookEndpointResponse202
from .update_address_body import UpdateAddressBody
from .update_address_body_metadata import UpdateAddressBodyMetadata
from .update_address_patch_body import UpdateAddressPatchBody
from .update_address_patch_body_metadata import UpdateAddressPatchBodyMetadata
from .update_address_patch_response_200 import UpdateAddressPatchResponse200
from .update_address_patch_response_200_links import UpdateAddressPatchResponse200Links
from .update_address_patch_response_200_links_additional_property import (
    UpdateAddressPatchResponse200LinksAdditionalProperty,
)
from .update_address_patch_response_200_merchant import (
    UpdateAddressPatchResponse200Merchant,
)
from .update_address_patch_response_200_metadata_type_0 import (
    UpdateAddressPatchResponse200MetadataType0,
)
from .update_address_patch_response_200_owner_type import (
    UpdateAddressPatchResponse200OwnerType,
)
from .update_address_response_200 import UpdateAddressResponse200
from .update_address_response_200_links import UpdateAddressResponse200Links
from .update_address_response_200_links_additional_property import (
    UpdateAddressResponse200LinksAdditionalProperty,
)
from .update_address_response_200_merchant import UpdateAddressResponse200Merchant
from .update_address_response_200_metadata_type_0 import (
    UpdateAddressResponse200MetadataType0,
)
from .update_address_response_200_owner_type import UpdateAddressResponse200OwnerType
from .update_checkout_payment_link_body import UpdateCheckoutPaymentLinkBody
from .update_checkout_payment_link_body_custom_inputs_item import (
    UpdateCheckoutPaymentLinkBodyCustomInputsItem,
)
from .update_checkout_payment_link_body_items_item import (
    UpdateCheckoutPaymentLinkBodyItemsItem,
)
from .update_checkout_payment_link_body_metadata import (
    UpdateCheckoutPaymentLinkBodyMetadata,
)
from .update_checkout_payment_link_patch_body import UpdateCheckoutPaymentLinkPatchBody
from .update_checkout_payment_link_patch_body_custom_inputs_item import (
    UpdateCheckoutPaymentLinkPatchBodyCustomInputsItem,
)
from .update_checkout_payment_link_patch_body_items_item import (
    UpdateCheckoutPaymentLinkPatchBodyItemsItem,
)
from .update_checkout_payment_link_patch_body_metadata import (
    UpdateCheckoutPaymentLinkPatchBodyMetadata,
)
from .update_checkout_payment_link_patch_response_200 import (
    UpdateCheckoutPaymentLinkPatchResponse200,
)
from .update_checkout_payment_link_patch_response_200_custom_inputs_type_0_item import (
    UpdateCheckoutPaymentLinkPatchResponse200CustomInputsType0Item,
)
from .update_checkout_payment_link_patch_response_200_items_item import (
    UpdateCheckoutPaymentLinkPatchResponse200ItemsItem,
)
from .update_checkout_payment_link_patch_response_200_metadata_type_0 import (
    UpdateCheckoutPaymentLinkPatchResponse200MetadataType0,
)
from .update_checkout_payment_link_response_200 import (
    UpdateCheckoutPaymentLinkResponse200,
)
from .update_checkout_payment_link_response_200_custom_inputs_type_0_item import (
    UpdateCheckoutPaymentLinkResponse200CustomInputsType0Item,
)
from .update_checkout_payment_link_response_200_items_item import (
    UpdateCheckoutPaymentLinkResponse200ItemsItem,
)
from .update_checkout_payment_link_response_200_metadata_type_0 import (
    UpdateCheckoutPaymentLinkResponse200MetadataType0,
)
from .update_checkout_session_body import UpdateCheckoutSessionBody
from .update_checkout_session_body_address import UpdateCheckoutSessionBodyAddress
from .update_checkout_session_body_ambient import UpdateCheckoutSessionBodyAmbient
from .update_checkout_session_body_client import UpdateCheckoutSessionBodyClient
from .update_checkout_session_body_cookies import UpdateCheckoutSessionBodyCookies
from .update_checkout_session_body_coupons_item_type_1 import (
    UpdateCheckoutSessionBodyCouponsItemType1,
)
from .update_checkout_session_body_customer import UpdateCheckoutSessionBodyCustomer
from .update_checkout_session_body_items_item import UpdateCheckoutSessionBodyItemsItem
from .update_checkout_session_body_line_items_item import (
    UpdateCheckoutSessionBodyLineItemsItem,
)
from .update_checkout_session_body_metadata import UpdateCheckoutSessionBodyMetadata
from .update_checkout_session_body_payment_methods_item_type_1 import (
    UpdateCheckoutSessionBodyPaymentMethodsItemType1,
)
from .update_checkout_session_body_redirect_urls import (
    UpdateCheckoutSessionBodyRedirectUrls,
)
from .update_checkout_session_body_shipping_delivery import (
    UpdateCheckoutSessionBodyShippingDelivery,
)
from .update_checkout_session_body_status import UpdateCheckoutSessionBodyStatus
from .update_checkout_session_body_utm import UpdateCheckoutSessionBodyUtm
from .update_checkout_session_response_200 import UpdateCheckoutSessionResponse200
from .update_checkout_session_response_200_address_type_0 import (
    UpdateCheckoutSessionResponse200AddressType0,
)
from .update_checkout_session_response_200_coupons_item import (
    UpdateCheckoutSessionResponse200CouponsItem,
)
from .update_checkout_session_response_200_currency import (
    UpdateCheckoutSessionResponse200Currency,
)
from .update_checkout_session_response_200_custom_inputs import (
    UpdateCheckoutSessionResponse200CustomInputs,
)
from .update_checkout_session_response_200_customer_type_0 import (
    UpdateCheckoutSessionResponse200CustomerType0,
)
from .update_checkout_session_response_200_line_items_item import (
    UpdateCheckoutSessionResponse200LineItemsItem,
)
from .update_checkout_session_response_200_line_items_item_metadata_type_0 import (
    UpdateCheckoutSessionResponse200LineItemsItemMetadataType0,
)
from .update_checkout_session_response_200_metadata_type_0 import (
    UpdateCheckoutSessionResponse200MetadataType0,
)
from .update_checkout_session_response_200_object import (
    UpdateCheckoutSessionResponse200Object,
)
from .update_checkout_session_response_200_payment_methods_item_type_1 import (
    UpdateCheckoutSessionResponse200PaymentMethodsItemType1,
)
from .update_checkout_session_response_200_payment_selection_type_0 import (
    UpdateCheckoutSessionResponse200PaymentSelectionType0,
)
from .update_checkout_session_response_200_redirect_urls import (
    UpdateCheckoutSessionResponse200RedirectUrls,
)
from .update_checkout_session_response_200_status import (
    UpdateCheckoutSessionResponse200Status,
)
from .update_checkout_session_response_200_totals import (
    UpdateCheckoutSessionResponse200Totals,
)
from .update_checkout_session_response_200_utm_type_0 import (
    UpdateCheckoutSessionResponse200UtmType0,
)
from .update_coupon_body import UpdateCouponBody
from .update_coupon_body_scope import UpdateCouponBodyScope
from .update_coupon_body_type import UpdateCouponBodyType
from .update_coupon_response_200 import UpdateCouponResponse200
from .update_coupon_response_200_scope import UpdateCouponResponse200Scope
from .update_coupon_response_200_type import UpdateCouponResponse200Type
from .update_customer_body import UpdateCustomerBody
from .update_customer_body_document import UpdateCustomerBodyDocument
from .update_customer_body_document_type import UpdateCustomerBodyDocumentType
from .update_customer_body_gender import UpdateCustomerBodyGender
from .update_customer_body_metadata import UpdateCustomerBodyMetadata
from .update_customer_body_telephone import UpdateCustomerBodyTelephone
from .update_customer_put_body import UpdateCustomerPutBody
from .update_customer_put_body_document import UpdateCustomerPutBodyDocument
from .update_customer_put_body_document_type import UpdateCustomerPutBodyDocumentType
from .update_customer_put_body_gender import UpdateCustomerPutBodyGender
from .update_customer_put_body_metadata import UpdateCustomerPutBodyMetadata
from .update_customer_put_body_telephone import UpdateCustomerPutBodyTelephone
from .update_customer_put_response_200 import UpdateCustomerPutResponse200
from .update_customer_put_response_200_document_type_0 import (
    UpdateCustomerPutResponse200DocumentType0,
)
from .update_customer_put_response_200_document_type_0_type import (
    UpdateCustomerPutResponse200DocumentType0Type,
)
from .update_customer_put_response_200_links import UpdateCustomerPutResponse200Links
from .update_customer_put_response_200_links_additional_property import (
    UpdateCustomerPutResponse200LinksAdditionalProperty,
)
from .update_customer_put_response_200_merchant import (
    UpdateCustomerPutResponse200Merchant,
)
from .update_customer_put_response_200_metadata_type_0 import (
    UpdateCustomerPutResponse200MetadataType0,
)
from .update_customer_put_response_200_telephone_type_0 import (
    UpdateCustomerPutResponse200TelephoneType0,
)
from .update_customer_response_200 import UpdateCustomerResponse200
from .update_customer_response_200_document_type_0 import (
    UpdateCustomerResponse200DocumentType0,
)
from .update_customer_response_200_document_type_0_type import (
    UpdateCustomerResponse200DocumentType0Type,
)
from .update_customer_response_200_links import UpdateCustomerResponse200Links
from .update_customer_response_200_links_additional_property import (
    UpdateCustomerResponse200LinksAdditionalProperty,
)
from .update_customer_response_200_merchant import UpdateCustomerResponse200Merchant
from .update_customer_response_200_metadata_type_0 import (
    UpdateCustomerResponse200MetadataType0,
)
from .update_customer_response_200_telephone_type_0 import (
    UpdateCustomerResponse200TelephoneType0,
)
from .update_product_body import UpdateProductBody
from .update_product_body_images_item_type_1 import UpdateProductBodyImagesItemType1
from .update_product_body_type import UpdateProductBodyType
from .update_product_put_body import UpdateProductPutBody
from .update_product_put_body_images_item_type_1 import (
    UpdateProductPutBodyImagesItemType1,
)
from .update_product_put_body_type import UpdateProductPutBodyType
from .update_product_put_response_200 import UpdateProductPutResponse200
from .update_product_put_response_200_images_type_0_item_type_1 import (
    UpdateProductPutResponse200ImagesType0ItemType1,
)
from .update_product_put_response_200_type import UpdateProductPutResponse200Type
from .update_product_put_response_200_variants_item import (
    UpdateProductPutResponse200VariantsItem,
)
from .update_product_put_response_200_variants_item_attributes_type_0 import (
    UpdateProductPutResponse200VariantsItemAttributesType0,
)
from .update_product_put_response_200_variants_item_images_type_0_item_type_1 import (
    UpdateProductPutResponse200VariantsItemImagesType0ItemType1,
)
from .update_product_put_response_200_variants_item_metadata_type_0 import (
    UpdateProductPutResponse200VariantsItemMetadataType0,
)
from .update_product_put_response_200_variants_item_pricing import (
    UpdateProductPutResponse200VariantsItemPricing,
)
from .update_product_put_response_200_variants_item_pricing_schema import (
    UpdateProductPutResponse200VariantsItemPricingSchema,
)
from .update_product_put_response_200_variants_item_pricing_type import (
    UpdateProductPutResponse200VariantsItemPricingType,
)
from .update_product_response_200 import UpdateProductResponse200
from .update_product_response_200_images_type_0_item_type_1 import (
    UpdateProductResponse200ImagesType0ItemType1,
)
from .update_product_response_200_type import UpdateProductResponse200Type
from .update_product_response_200_variants_item import (
    UpdateProductResponse200VariantsItem,
)
from .update_product_response_200_variants_item_attributes_type_0 import (
    UpdateProductResponse200VariantsItemAttributesType0,
)
from .update_product_response_200_variants_item_images_type_0_item_type_1 import (
    UpdateProductResponse200VariantsItemImagesType0ItemType1,
)
from .update_product_response_200_variants_item_metadata_type_0 import (
    UpdateProductResponse200VariantsItemMetadataType0,
)
from .update_product_response_200_variants_item_pricing import (
    UpdateProductResponse200VariantsItemPricing,
)
from .update_product_response_200_variants_item_pricing_schema import (
    UpdateProductResponse200VariantsItemPricingSchema,
)
from .update_product_response_200_variants_item_pricing_type import (
    UpdateProductResponse200VariantsItemPricingType,
)
from .update_product_variant_body import UpdateProductVariantBody
from .update_product_variant_body_attributes import UpdateProductVariantBodyAttributes
from .update_product_variant_body_images_item_type_1 import (
    UpdateProductVariantBodyImagesItemType1,
)
from .update_product_variant_body_metadata import UpdateProductVariantBodyMetadata
from .update_product_variant_body_pricing import UpdateProductVariantBodyPricing
from .update_product_variant_body_pricing_billing_frequency import (
    UpdateProductVariantBodyPricingBillingFrequency,
)
from .update_product_variant_body_pricing_billing_type import (
    UpdateProductVariantBodyPricingBillingType,
)
from .update_product_variant_body_pricing_schema import (
    UpdateProductVariantBodyPricingSchema,
)
from .update_product_variant_body_pricing_tiers_item import (
    UpdateProductVariantBodyPricingTiersItem,
)
from .update_product_variant_body_pricing_tiers_mode import (
    UpdateProductVariantBodyPricingTiersMode,
)
from .update_product_variant_body_pricing_transform_quantity import (
    UpdateProductVariantBodyPricingTransformQuantity,
)
from .update_product_variant_body_pricing_transform_quantity_round import (
    UpdateProductVariantBodyPricingTransformQuantityRound,
)
from .update_product_variant_body_pricing_trial_interval import (
    UpdateProductVariantBodyPricingTrialInterval,
)
from .update_product_variant_body_pricing_type import (
    UpdateProductVariantBodyPricingType,
)
from .update_product_variant_body_pricing_usage_aggregation import (
    UpdateProductVariantBodyPricingUsageAggregation,
)
from .update_product_variant_body_pricing_usage_type import (
    UpdateProductVariantBodyPricingUsageType,
)
from .update_product_variant_put_body import UpdateProductVariantPutBody
from .update_product_variant_put_body_attributes import (
    UpdateProductVariantPutBodyAttributes,
)
from .update_product_variant_put_body_images_item_type_1 import (
    UpdateProductVariantPutBodyImagesItemType1,
)
from .update_product_variant_put_body_metadata import (
    UpdateProductVariantPutBodyMetadata,
)
from .update_product_variant_put_body_pricing import UpdateProductVariantPutBodyPricing
from .update_product_variant_put_body_pricing_billing_frequency import (
    UpdateProductVariantPutBodyPricingBillingFrequency,
)
from .update_product_variant_put_body_pricing_billing_type import (
    UpdateProductVariantPutBodyPricingBillingType,
)
from .update_product_variant_put_body_pricing_schema import (
    UpdateProductVariantPutBodyPricingSchema,
)
from .update_product_variant_put_body_pricing_tiers_item import (
    UpdateProductVariantPutBodyPricingTiersItem,
)
from .update_product_variant_put_body_pricing_tiers_mode import (
    UpdateProductVariantPutBodyPricingTiersMode,
)
from .update_product_variant_put_body_pricing_transform_quantity import (
    UpdateProductVariantPutBodyPricingTransformQuantity,
)
from .update_product_variant_put_body_pricing_transform_quantity_round import (
    UpdateProductVariantPutBodyPricingTransformQuantityRound,
)
from .update_product_variant_put_body_pricing_trial_interval import (
    UpdateProductVariantPutBodyPricingTrialInterval,
)
from .update_product_variant_put_body_pricing_type import (
    UpdateProductVariantPutBodyPricingType,
)
from .update_product_variant_put_body_pricing_usage_aggregation import (
    UpdateProductVariantPutBodyPricingUsageAggregation,
)
from .update_product_variant_put_body_pricing_usage_type import (
    UpdateProductVariantPutBodyPricingUsageType,
)
from .update_product_variant_put_response_200 import UpdateProductVariantPutResponse200
from .update_product_variant_put_response_200_attributes_type_0 import (
    UpdateProductVariantPutResponse200AttributesType0,
)
from .update_product_variant_put_response_200_images_type_0_item_type_1 import (
    UpdateProductVariantPutResponse200ImagesType0ItemType1,
)
from .update_product_variant_put_response_200_metadata_type_0 import (
    UpdateProductVariantPutResponse200MetadataType0,
)
from .update_product_variant_put_response_200_pricing import (
    UpdateProductVariantPutResponse200Pricing,
)
from .update_product_variant_put_response_200_pricing_schema import (
    UpdateProductVariantPutResponse200PricingSchema,
)
from .update_product_variant_put_response_200_pricing_type import (
    UpdateProductVariantPutResponse200PricingType,
)
from .update_product_variant_response_200 import UpdateProductVariantResponse200
from .update_product_variant_response_200_attributes_type_0 import (
    UpdateProductVariantResponse200AttributesType0,
)
from .update_product_variant_response_200_images_type_0_item_type_1 import (
    UpdateProductVariantResponse200ImagesType0ItemType1,
)
from .update_product_variant_response_200_metadata_type_0 import (
    UpdateProductVariantResponse200MetadataType0,
)
from .update_product_variant_response_200_pricing import (
    UpdateProductVariantResponse200Pricing,
)
from .update_product_variant_response_200_pricing_schema import (
    UpdateProductVariantResponse200PricingSchema,
)
from .update_product_variant_response_200_pricing_type import (
    UpdateProductVariantResponse200PricingType,
)
from .update_subscription_item_body import UpdateSubscriptionItemBody
from .update_subscription_item_put_body import UpdateSubscriptionItemPutBody
from .update_subscription_item_put_response_200 import (
    UpdateSubscriptionItemPutResponse200,
)
from .update_subscription_item_put_response_200_images_type_0_item_type_1 import (
    UpdateSubscriptionItemPutResponse200ImagesType0ItemType1,
)
from .update_subscription_item_put_response_200_links import (
    UpdateSubscriptionItemPutResponse200Links,
)
from .update_subscription_item_put_response_200_links_additional_property import (
    UpdateSubscriptionItemPutResponse200LinksAdditionalProperty,
)
from .update_subscription_item_put_response_200_merchant import (
    UpdateSubscriptionItemPutResponse200Merchant,
)
from .update_subscription_item_put_response_200_metadata_type_0 import (
    UpdateSubscriptionItemPutResponse200MetadataType0,
)
from .update_subscription_item_response_200 import UpdateSubscriptionItemResponse200
from .update_subscription_item_response_200_images_type_0_item_type_1 import (
    UpdateSubscriptionItemResponse200ImagesType0ItemType1,
)
from .update_subscription_item_response_200_links import (
    UpdateSubscriptionItemResponse200Links,
)
from .update_subscription_item_response_200_links_additional_property import (
    UpdateSubscriptionItemResponse200LinksAdditionalProperty,
)
from .update_subscription_item_response_200_merchant import (
    UpdateSubscriptionItemResponse200Merchant,
)
from .update_subscription_item_response_200_metadata_type_0 import (
    UpdateSubscriptionItemResponse200MetadataType0,
)
from .update_subscription_split_body import UpdateSubscriptionSplitBody
from .update_subscription_split_body_type import UpdateSubscriptionSplitBodyType
from .update_subscription_split_put_body import UpdateSubscriptionSplitPutBody
from .update_subscription_split_put_body_type import UpdateSubscriptionSplitPutBodyType
from .update_subscription_split_put_response_200 import (
    UpdateSubscriptionSplitPutResponse200,
)
from .update_subscription_split_put_response_200_links import (
    UpdateSubscriptionSplitPutResponse200Links,
)
from .update_subscription_split_put_response_200_links_additional_property import (
    UpdateSubscriptionSplitPutResponse200LinksAdditionalProperty,
)
from .update_subscription_split_put_response_200_merchant import (
    UpdateSubscriptionSplitPutResponse200Merchant,
)
from .update_subscription_split_response_200 import UpdateSubscriptionSplitResponse200
from .update_subscription_split_response_200_links import (
    UpdateSubscriptionSplitResponse200Links,
)
from .update_subscription_split_response_200_links_additional_property import (
    UpdateSubscriptionSplitResponse200LinksAdditionalProperty,
)
from .update_subscription_split_response_200_merchant import (
    UpdateSubscriptionSplitResponse200Merchant,
)
from .update_webhook_endpoint_body import UpdateWebhookEndpointBody
from .update_webhook_endpoint_body_events_item import (
    UpdateWebhookEndpointBodyEventsItem,
)
from .update_webhook_endpoint_body_metadata import UpdateWebhookEndpointBodyMetadata
from .update_webhook_endpoint_response_200 import UpdateWebhookEndpointResponse200
from .update_webhook_endpoint_response_200_links import (
    UpdateWebhookEndpointResponse200Links,
)
from .update_webhook_endpoint_response_200_links_additional_property import (
    UpdateWebhookEndpointResponse200LinksAdditionalProperty,
)
from .update_webhook_endpoint_response_200_merchant import (
    UpdateWebhookEndpointResponse200Merchant,
)
from .update_webhook_endpoint_response_200_metadata_type_0 import (
    UpdateWebhookEndpointResponse200MetadataType0,
)
from .utils_card_bin_validation_response_200 import UtilsCardBinValidationResponse200
from .utils_card_bin_validation_response_200_intel_type_0 import (
    UtilsCardBinValidationResponse200IntelType0,
)
from .utils_card_bin_validation_response_200_links import (
    UtilsCardBinValidationResponse200Links,
)
from .utils_card_bin_validation_response_200_links_additional_property import (
    UtilsCardBinValidationResponse200LinksAdditionalProperty,
)
from .utils_card_bin_validation_response_200_merchant import (
    UtilsCardBinValidationResponse200Merchant,
)
from .utils_company_types_response_200 import UtilsCompanyTypesResponse200
from .utils_company_types_response_200_data_item import (
    UtilsCompanyTypesResponse200DataItem,
)
from .utils_corporate_document_check_response_200 import (
    UtilsCorporateDocumentCheckResponse200,
)
from .utils_corporate_document_check_response_200_address_type_0 import (
    UtilsCorporateDocumentCheckResponse200AddressType0,
)
from .utils_corporate_document_check_response_200_merchant import (
    UtilsCorporateDocumentCheckResponse200Merchant,
)
from .utils_corporate_document_check_response_200_partners_item import (
    UtilsCorporateDocumentCheckResponse200PartnersItem,
)
from .utils_corporate_document_check_response_200_secondary_cnaes_item import (
    UtilsCorporateDocumentCheckResponse200SecondaryCnaesItem,
)
from .utils_corporate_document_check_response_200_type import (
    UtilsCorporateDocumentCheckResponse200Type,
)
from .utils_metadata_response_200 import UtilsMetadataResponse200
from .utils_metadata_response_200_data import UtilsMetadataResponse200Data
from .utils_postcode_validation_response_200 import UtilsPostcodeValidationResponse200
from .utils_postcode_validation_response_200_address_type_0 import (
    UtilsPostcodeValidationResponse200AddressType0,
)
from .utils_postcode_validation_response_200_merchant import (
    UtilsPostcodeValidationResponse200Merchant,
)
from .utils_roles_of_user_response_200 import UtilsRolesOfUserResponse200
from .utils_rules_of_recurrencies_response_200 import (
    UtilsRulesOfRecurrenciesResponse200,
)
from .utils_rules_of_recurrencies_response_200_data import (
    UtilsRulesOfRecurrenciesResponse200Data,
)
from .utils_rules_of_recurrencies_response_200_data_frequency_count import (
    UtilsRulesOfRecurrenciesResponse200DataFrequencyCount,
)
from .utils_types_of_bank_accounts_response_200 import (
    UtilsTypesOfBankAccountsResponse200,
)
from .utils_types_of_bank_accounts_response_200_data_item import (
    UtilsTypesOfBankAccountsResponse200DataItem,
)
from .utils_types_of_company_response_200 import UtilsTypesOfCompanyResponse200
from .utils_types_of_company_response_200_data_item import (
    UtilsTypesOfCompanyResponse200DataItem,
)
from .utils_types_of_refund_response_200 import UtilsTypesOfRefundResponse200
from .utils_types_of_refund_response_200_data_item import (
    UtilsTypesOfRefundResponse200DataItem,
)
from .utils_types_of_webhooks_response_200 import UtilsTypesOfWebhooksResponse200
from .validate_coupon_body import ValidateCouponBody
from .validate_coupon_response_200 import ValidateCouponResponse200
from .validate_coupon_response_200_discount_type_0 import (
    ValidateCouponResponse200DiscountType0,
)
from .validate_coupon_response_200_discount_type_0_type import (
    ValidateCouponResponse200DiscountType0Type,
)
from .webhook_event_payload import WebhookEventPayload
from .webhook_event_payload_payload import WebhookEventPayloadPayload
from .webhook_event_payload_payload_object import WebhookEventPayloadPayloadObject

__all__ = (
    "AddSubscriptionItemBody",
    "AddSubscriptionItemBodyMetadata",
    "AddSubscriptionItemResponse201",
    "AddSubscriptionItemResponse201ImagesType0ItemType1",
    "AddSubscriptionItemResponse201Links",
    "AddSubscriptionItemResponse201LinksAdditionalProperty",
    "AddSubscriptionItemResponse201Merchant",
    "AddSubscriptionItemResponse201MetadataType0",
    "AddSubscriptionSplitBody",
    "AddSubscriptionSplitBodyType",
    "AddSubscriptionSplitResponse201",
    "AddSubscriptionSplitResponse201Links",
    "AddSubscriptionSplitResponse201LinksAdditionalProperty",
    "AddSubscriptionSplitResponse201Merchant",
    "AddSubscriptionSplitResponse201SplitsItem",
    "AddSubscriptionSplitResponse201SplitsItemLinks",
    "AddSubscriptionSplitResponse201SplitsItemLinksAdditionalProperty",
    "AddSubscriptionSplitResponse201SplitsItemMerchant",
    "AddSubscriptionThresholdBody",
    "AddSubscriptionThresholdBodyKind",
    "AddSubscriptionThresholdResponse201",
    "AddSubscriptionThresholdResponse201Kind",
    "CancelSubscriptionBody",
    "CancelSubscriptionResponse200",
    "CancelSubscriptionResponse200Billing",
    "CancelSubscriptionResponse200BillingAddress",
    "CancelSubscriptionResponse200CallbackType0",
    "CancelSubscriptionResponse200CurrentCycleType0",
    "CancelSubscriptionResponse200Customer",
    "CancelSubscriptionResponse200CustomerDocumentType0",
    "CancelSubscriptionResponse200CustomerMetadataType0",
    "CancelSubscriptionResponse200CustomerTelephoneType0",
    "CancelSubscriptionResponse200DiscountType0",
    "CancelSubscriptionResponse200GeolocationType0",
    "CancelSubscriptionResponse200ItemsItem",
    "CancelSubscriptionResponse200ItemsItemImagesType0ItemType1",
    "CancelSubscriptionResponse200ItemsItemMetadataType0",
    "CancelSubscriptionResponse200Links",
    "CancelSubscriptionResponse200LinksAdditionalProperty",
    "CancelSubscriptionResponse200Merchant",
    "CancelSubscriptionResponse200MetadataType0",
    "CancelSubscriptionResponse200ShippingType0",
    "CancelSubscriptionResponse200SplitsType0Item",
    "CancelSubscriptionResponse200Status",
    "CaptureTransactionBody",
    "CaptureTransactionResponse202",
    "CaptureTransactionResponse202Status",
    "CreateAddressBody",
    "CreateAddressBodyMetadata",
    "CreateAddressResponse201",
    "CreateAddressResponse201Links",
    "CreateAddressResponse201LinksAdditionalProperty",
    "CreateAddressResponse201Merchant",
    "CreateAddressResponse201MetadataType0",
    "CreateAddressResponse201OwnerType",
    "CreateCardBody",
    "CreateCardBodyExpirationYear",
    "CreateCardResponse201",
    "CreateCardResponse201Links",
    "CreateCardResponse201LinksAdditionalProperty",
    "CreateCardResponse201Merchant",
    "CreateCheckoutPaymentLinkBody",
    "CreateCheckoutPaymentLinkBodyCustomInputsItem",
    "CreateCheckoutPaymentLinkBodyItemsItem",
    "CreateCheckoutPaymentLinkBodyMetadata",
    "CreateCheckoutPaymentLinkResponse201",
    "CreateCheckoutPaymentLinkResponse201CustomInputsType0Item",
    "CreateCheckoutPaymentLinkResponse201ItemsItem",
    "CreateCheckoutPaymentLinkResponse201MetadataType0",
    "CreateCheckoutSessionBody",
    "CreateCheckoutSessionBodyAddress",
    "CreateCheckoutSessionBodyAmbient",
    "CreateCheckoutSessionBodyClient",
    "CreateCheckoutSessionBodyCookies",
    "CreateCheckoutSessionBodyCouponsItemType1",
    "CreateCheckoutSessionBodyCustomer",
    "CreateCheckoutSessionBodyItemsItem",
    "CreateCheckoutSessionBodyLineItemsItem",
    "CreateCheckoutSessionBodyMetadata",
    "CreateCheckoutSessionBodyPaymentMethodsItemType1",
    "CreateCheckoutSessionBodyRedirectUrls",
    "CreateCheckoutSessionBodyShippingDelivery",
    "CreateCheckoutSessionBodyUtm",
    "CreateCheckoutSessionResponse201",
    "CreateCheckoutSessionResponse201AddressType0",
    "CreateCheckoutSessionResponse201CouponsItem",
    "CreateCheckoutSessionResponse201Currency",
    "CreateCheckoutSessionResponse201CustomerType0",
    "CreateCheckoutSessionResponse201CustomInputs",
    "CreateCheckoutSessionResponse201LineItemsItem",
    "CreateCheckoutSessionResponse201LineItemsItemMetadataType0",
    "CreateCheckoutSessionResponse201MetadataType0",
    "CreateCheckoutSessionResponse201Object",
    "CreateCheckoutSessionResponse201PaymentMethodsItemType1",
    "CreateCheckoutSessionResponse201PaymentSelectionType0",
    "CreateCheckoutSessionResponse201RedirectUrls",
    "CreateCheckoutSessionResponse201Status",
    "CreateCheckoutSessionResponse201Totals",
    "CreateCheckoutSessionResponse201UtmType0",
    "CreateCouponBody",
    "CreateCouponBodyScope",
    "CreateCouponBodyType",
    "CreateCouponResponse201",
    "CreateCouponResponse201Scope",
    "CreateCouponResponse201Type",
    "CreateCustomerBody",
    "CreateCustomerBodyDocument",
    "CreateCustomerBodyDocumentType",
    "CreateCustomerBodyGender",
    "CreateCustomerBodyMetadata",
    "CreateCustomerBodyTelephone",
    "CreateCustomerResponse201",
    "CreateCustomerResponse201DocumentType0",
    "CreateCustomerResponse201DocumentType0Type",
    "CreateCustomerResponse201Links",
    "CreateCustomerResponse201LinksAdditionalProperty",
    "CreateCustomerResponse201Merchant",
    "CreateCustomerResponse201MetadataType0",
    "CreateCustomerResponse201TelephoneType0",
    "CreateProductBody",
    "CreateProductBodyImagesItemType1",
    "CreateProductBodyType",
    "CreateProductBodyVariantsItem",
    "CreateProductBodyVariantsItemAttributes",
    "CreateProductBodyVariantsItemImagesItemType1",
    "CreateProductBodyVariantsItemMetadata",
    "CreateProductBodyVariantsItemPricing",
    "CreateProductBodyVariantsItemPricingBillingFrequency",
    "CreateProductBodyVariantsItemPricingBillingType",
    "CreateProductBodyVariantsItemPricingSchema",
    "CreateProductBodyVariantsItemPricingTiersItem",
    "CreateProductBodyVariantsItemPricingTiersMode",
    "CreateProductBodyVariantsItemPricingTransformQuantity",
    "CreateProductBodyVariantsItemPricingTransformQuantityRound",
    "CreateProductBodyVariantsItemPricingTrialInterval",
    "CreateProductBodyVariantsItemPricingType",
    "CreateProductBodyVariantsItemPricingUsageAggregation",
    "CreateProductBodyVariantsItemPricingUsageType",
    "CreateProductResponse201",
    "CreateProductResponse201ImagesType0ItemType1",
    "CreateProductResponse201Type",
    "CreateProductResponse201VariantsItem",
    "CreateProductResponse201VariantsItemAttributesType0",
    "CreateProductResponse201VariantsItemImagesType0ItemType1",
    "CreateProductResponse201VariantsItemMetadataType0",
    "CreateProductResponse201VariantsItemPricing",
    "CreateProductResponse201VariantsItemPricingSchema",
    "CreateProductResponse201VariantsItemPricingType",
    "CreateProductVariantBody",
    "CreateProductVariantBodyAttributes",
    "CreateProductVariantBodyImagesItemType1",
    "CreateProductVariantBodyMetadata",
    "CreateProductVariantBodyPricing",
    "CreateProductVariantBodyPricingBillingFrequency",
    "CreateProductVariantBodyPricingBillingType",
    "CreateProductVariantBodyPricingSchema",
    "CreateProductVariantBodyPricingTiersItem",
    "CreateProductVariantBodyPricingTiersMode",
    "CreateProductVariantBodyPricingTransformQuantity",
    "CreateProductVariantBodyPricingTransformQuantityRound",
    "CreateProductVariantBodyPricingTrialInterval",
    "CreateProductVariantBodyPricingType",
    "CreateProductVariantBodyPricingUsageAggregation",
    "CreateProductVariantBodyPricingUsageType",
    "CreateProductVariantResponse201",
    "CreateProductVariantResponse201AttributesType0",
    "CreateProductVariantResponse201ImagesType0ItemType1",
    "CreateProductVariantResponse201MetadataType0",
    "CreateProductVariantResponse201Pricing",
    "CreateProductVariantResponse201PricingSchema",
    "CreateProductVariantResponse201PricingType",
    "CreateSubscriptionBody",
    "CreateSubscriptionBodyBilling",
    "CreateSubscriptionBodyBillingAddress",
    "CreateSubscriptionBodyCallback",
    "CreateSubscriptionBodyCustomer",
    "CreateSubscriptionBodyCustomerDocument",
    "CreateSubscriptionBodyCustomerDocumentType",
    "CreateSubscriptionBodyCustomerGender",
    "CreateSubscriptionBodyCustomerMetadata",
    "CreateSubscriptionBodyCustomerTelephone",
    "CreateSubscriptionBodyDiscountsItem",
    "CreateSubscriptionBodyFreeTrial",
    "CreateSubscriptionBodyFrequency",
    "CreateSubscriptionBodyGeolocation",
    "CreateSubscriptionBodyItemsItem",
    "CreateSubscriptionBodyItemsItemMetadata",
    "CreateSubscriptionBodyMetadata",
    "CreateSubscriptionBodyPayment",
    "CreateSubscriptionBodyPaymentBillet",
    "CreateSubscriptionBodyPaymentCard",
    "CreateSubscriptionBodyPaymentCardExpirationYear",
    "CreateSubscriptionBodyPaymentMethod",
    "CreateSubscriptionBodyPaymentPix",
    "CreateSubscriptionBodyShipping",
    "CreateSubscriptionBodySplitsItem",
    "CreateSubscriptionBodySplitsItemType",
    "CreateSubscriptionResponse201",
    "CreateSubscriptionResponse201Billing",
    "CreateSubscriptionResponse201BillingAddress",
    "CreateSubscriptionResponse201CallbackType0",
    "CreateSubscriptionResponse201CurrentCycleType0",
    "CreateSubscriptionResponse201Customer",
    "CreateSubscriptionResponse201CustomerDocumentType0",
    "CreateSubscriptionResponse201CustomerMetadataType0",
    "CreateSubscriptionResponse201CustomerTelephoneType0",
    "CreateSubscriptionResponse201DiscountType0",
    "CreateSubscriptionResponse201GeolocationType0",
    "CreateSubscriptionResponse201ItemsItem",
    "CreateSubscriptionResponse201ItemsItemImagesType0ItemType1",
    "CreateSubscriptionResponse201ItemsItemMetadataType0",
    "CreateSubscriptionResponse201Links",
    "CreateSubscriptionResponse201LinksAdditionalProperty",
    "CreateSubscriptionResponse201Merchant",
    "CreateSubscriptionResponse201MetadataType0",
    "CreateSubscriptionResponse201ShippingType0",
    "CreateSubscriptionResponse201SplitsType0Item",
    "CreateSubscriptionResponse201Status",
    "CreateTransactionBody",
    "CreateTransactionBodyBilling",
    "CreateTransactionBodyBillingAddress",
    "CreateTransactionBodyCallback",
    "CreateTransactionBodyCustomer",
    "CreateTransactionBodyCustomerDocument",
    "CreateTransactionBodyCustomerDocumentType",
    "CreateTransactionBodyCustomerGender",
    "CreateTransactionBodyCustomerMetadata",
    "CreateTransactionBodyCustomerTelephone",
    "CreateTransactionBodyDiscountsItem",
    "CreateTransactionBodyGeolocation",
    "CreateTransactionBodyItemsItem",
    "CreateTransactionBodyItemsItemMetadata",
    "CreateTransactionBodyItemsItemPricing",
    "CreateTransactionBodyMetadata",
    "CreateTransactionBodyPayment",
    "CreateTransactionBodyPaymentBillet",
    "CreateTransactionBodyPaymentBilletBillingInstructions",
    "CreateTransactionBodyPaymentBilletBillingInstructionsDiscountsItem",
    "CreateTransactionBodyPaymentBilletBillingInstructionsDiscountsItemMode",
    "CreateTransactionBodyPaymentBilletBillingInstructionsInterest",
    "CreateTransactionBodyPaymentBilletBillingInstructionsInterestMode",
    "CreateTransactionBodyPaymentBilletBillingInstructionsLateFee",
    "CreateTransactionBodyPaymentBilletBillingInstructionsLateFeeMode",
    "CreateTransactionBodyPaymentCard",
    "CreateTransactionBodyPaymentCardExpirationYear",
    "CreateTransactionBodyPaymentMethod",
    "CreateTransactionBodyPaymentPix",
    "CreateTransactionBodyPaymentPixBillingInstructions",
    "CreateTransactionBodyPaymentPixBillingInstructionsDiscountsItem",
    "CreateTransactionBodyPaymentPixBillingInstructionsDiscountsItemMode",
    "CreateTransactionBodyPaymentPixBillingInstructionsInterest",
    "CreateTransactionBodyPaymentPixBillingInstructionsInterestMode",
    "CreateTransactionBodyPaymentPixBillingInstructionsLateFee",
    "CreateTransactionBodyPaymentPixBillingInstructionsLateFeeMode",
    "CreateTransactionBodyShipping",
    "CreateTransactionBodySplitsItem",
    "CreateTransactionBodySplitsItemType",
    "CreateTransactionResponse201",
    "CreateTransactionResponse201Billing",
    "CreateTransactionResponse201BillingAddress",
    "CreateTransactionResponse201CallbackType0",
    "CreateTransactionResponse201CustomerType0",
    "CreateTransactionResponse201CustomerType0Document",
    "CreateTransactionResponse201CustomerType0Telephone",
    "CreateTransactionResponse201DiscountType0",
    "CreateTransactionResponse201DisputesType0Item",
    "CreateTransactionResponse201ItemsType0Item",
    "CreateTransactionResponse201Links",
    "CreateTransactionResponse201LinksAdditionalProperty",
    "CreateTransactionResponse201Merchant",
    "CreateTransactionResponse201Method",
    "CreateTransactionResponse201Payment",
    "CreateTransactionResponse201PaymentProvider",
    "CreateTransactionResponse201PaymentVersion",
    "CreateTransactionResponse201ReceivablesType0Item",
    "CreateTransactionResponse201RefundsType0Item",
    "CreateTransactionResponse201SplitsType0Item",
    "CreateTransactionResponse201Status",
    "CreateTransactionResponse201TimelineItem",
    "CreateWalletBody",
    "CreateWalletResponse201",
    "CreateWalletResponse201Links",
    "CreateWalletResponse201LinksAdditionalProperty",
    "CreateWalletResponse201Merchant",
    "CreateWebhookEndpointBody",
    "CreateWebhookEndpointBodyEventsItem",
    "CreateWebhookEndpointBodyMetadata",
    "CreateWebhookEndpointResponse201",
    "CreateWebhookEndpointResponse201Links",
    "CreateWebhookEndpointResponse201LinksAdditionalProperty",
    "CreateWebhookEndpointResponse201Merchant",
    "CreateWebhookEndpointResponse201MetadataType0",
    "CreateWithdrawalBody",
    "CreateWithdrawalResponse201",
    "CreateWithdrawalResponse201Links",
    "CreateWithdrawalResponse201LinksAdditionalProperty",
    "CreateWithdrawalResponse201Merchant",
    "CreateWithdrawalResponse201ReceivingBankAccountType0",
    "DeleteAddressResponse200",
    "DeleteAddressResponse200Links",
    "DeleteAddressResponse200LinksAdditionalProperty",
    "DeleteAddressResponse200Merchant",
    "DeleteCardResponse200",
    "DeleteCardResponse200Links",
    "DeleteCardResponse200LinksAdditionalProperty",
    "DeleteCardResponse200Merchant",
    "DeleteCheckoutPaymentLinkResponse200",
    "DeleteCheckoutPaymentLinkResponse200Resource",
    "DeleteCheckoutSessionResponse200",
    "DeleteCheckoutSessionResponse200Resource",
    "DeleteCouponResponse200",
    "DeleteCouponResponse200Resource",
    "DeleteCustomerResponse200",
    "DeleteCustomerResponse200Links",
    "DeleteCustomerResponse200LinksAdditionalProperty",
    "DeleteCustomerResponse200Merchant",
    "DeleteProductResponse200",
    "DeleteProductResponse200Resource",
    "DeleteProductVariantResponse200",
    "DeleteProductVariantResponse200Resource",
    "DeleteVariantResponse200",
    "DeleteVariantResponse200Resource",
    "DeleteWalletResponse200",
    "DeleteWalletResponse200Links",
    "DeleteWalletResponse200LinksAdditionalProperty",
    "DeleteWalletResponse200Merchant",
    "DeleteWebhookEndpointResponse200",
    "DeleteWebhookEndpointResponse200Links",
    "DeleteWebhookEndpointResponse200LinksAdditionalProperty",
    "DeleteWebhookEndpointResponse200Merchant",
    "GetAddressResponse200",
    "GetAddressResponse200Links",
    "GetAddressResponse200LinksAdditionalProperty",
    "GetAddressResponse200Merchant",
    "GetAddressResponse200MetadataType0",
    "GetAddressResponse200OwnerType",
    "GetBalanceResponse200",
    "GetBalanceResponse200Merchant",
    "GetCardResponse200",
    "GetCardResponse200Links",
    "GetCardResponse200LinksAdditionalProperty",
    "GetCardResponse200Merchant",
    "GetCheckoutPaymentLinkResponse200",
    "GetCheckoutPaymentLinkResponse200CustomInputsType0Item",
    "GetCheckoutPaymentLinkResponse200ItemsItem",
    "GetCheckoutPaymentLinkResponse200MetadataType0",
    "GetCheckoutSessionResponse200",
    "GetCheckoutSessionResponse200AddressType0",
    "GetCheckoutSessionResponse200CouponsItem",
    "GetCheckoutSessionResponse200Currency",
    "GetCheckoutSessionResponse200CustomerType0",
    "GetCheckoutSessionResponse200CustomInputs",
    "GetCheckoutSessionResponse200LineItemsItem",
    "GetCheckoutSessionResponse200LineItemsItemMetadataType0",
    "GetCheckoutSessionResponse200MetadataType0",
    "GetCheckoutSessionResponse200Object",
    "GetCheckoutSessionResponse200PaymentMethodsItemType1",
    "GetCheckoutSessionResponse200PaymentSelectionType0",
    "GetCheckoutSessionResponse200RedirectUrls",
    "GetCheckoutSessionResponse200Status",
    "GetCheckoutSessionResponse200Totals",
    "GetCheckoutSessionResponse200UtmType0",
    "GetCouponResponse200",
    "GetCouponResponse200Scope",
    "GetCouponResponse200Type",
    "GetCustomerResponse200",
    "GetCustomerResponse200AddressesItem",
    "GetCustomerResponse200AddressesItemLinks",
    "GetCustomerResponse200AddressesItemLinksAdditionalProperty",
    "GetCustomerResponse200AddressesItemMerchant",
    "GetCustomerResponse200AddressesItemMetadataType0",
    "GetCustomerResponse200AddressesItemOwnerType",
    "GetCustomerResponse200CardsItem",
    "GetCustomerResponse200CardsItemLinks",
    "GetCustomerResponse200CardsItemLinksAdditionalProperty",
    "GetCustomerResponse200CardsItemMerchant",
    "GetCustomerResponse200DocumentType0",
    "GetCustomerResponse200DocumentType0Type",
    "GetCustomerResponse200Links",
    "GetCustomerResponse200LinksAdditionalProperty",
    "GetCustomerResponse200Merchant",
    "GetCustomerResponse200MetadataType0",
    "GetCustomerResponse200SubscriptionsItem",
    "GetCustomerResponse200SubscriptionsItemBilling",
    "GetCustomerResponse200SubscriptionsItemBillingAddress",
    "GetCustomerResponse200SubscriptionsItemCallbackType0",
    "GetCustomerResponse200SubscriptionsItemCurrentCycleType0",
    "GetCustomerResponse200SubscriptionsItemCustomer",
    "GetCustomerResponse200SubscriptionsItemCustomerDocumentType0",
    "GetCustomerResponse200SubscriptionsItemCustomerMetadataType0",
    "GetCustomerResponse200SubscriptionsItemCustomerTelephoneType0",
    "GetCustomerResponse200SubscriptionsItemDiscountType0",
    "GetCustomerResponse200SubscriptionsItemGeolocationType0",
    "GetCustomerResponse200SubscriptionsItemItemsItem",
    "GetCustomerResponse200SubscriptionsItemItemsItemImagesType0ItemType1",
    "GetCustomerResponse200SubscriptionsItemItemsItemMetadataType0",
    "GetCustomerResponse200SubscriptionsItemLinks",
    "GetCustomerResponse200SubscriptionsItemLinksAdditionalProperty",
    "GetCustomerResponse200SubscriptionsItemMerchant",
    "GetCustomerResponse200SubscriptionsItemMetadataType0",
    "GetCustomerResponse200SubscriptionsItemShippingType0",
    "GetCustomerResponse200SubscriptionsItemSplitsType0Item",
    "GetCustomerResponse200SubscriptionsItemStatus",
    "GetCustomerResponse200TelephoneType0",
    "GetCustomerResponse200TransactionsItem",
    "GetProductResponse200",
    "GetProductResponse200ImagesType0ItemType1",
    "GetProductResponse200Type",
    "GetProductResponse200VariantsItem",
    "GetProductResponse200VariantsItemAttributesType0",
    "GetProductResponse200VariantsItemImagesType0ItemType1",
    "GetProductResponse200VariantsItemMetadataType0",
    "GetProductResponse200VariantsItemPricing",
    "GetProductResponse200VariantsItemPricingSchema",
    "GetProductResponse200VariantsItemPricingType",
    "GetProductVariantResponse200",
    "GetProductVariantResponse200AttributesType0",
    "GetProductVariantResponse200ImagesType0ItemType1",
    "GetProductVariantResponse200MetadataType0",
    "GetProductVariantResponse200Pricing",
    "GetProductVariantResponse200PricingSchema",
    "GetProductVariantResponse200PricingType",
    "GetReceivableResponse200",
    "GetReceivableResponse200Links",
    "GetReceivableResponse200LinksAdditionalProperty",
    "GetReceivableResponse200Merchant",
    "GetSubscriptionCycleResponse200",
    "GetSubscriptionCycleResponse200Links",
    "GetSubscriptionCycleResponse200LinksAdditionalProperty",
    "GetSubscriptionCycleResponse200Merchant",
    "GetSubscriptionCycleUsageResponse200",
    "GetSubscriptionCycleUsageResponse200AggregatedByItemItem",
    "GetSubscriptionItemResponse200",
    "GetSubscriptionItemResponse200ImagesType0ItemType1",
    "GetSubscriptionItemResponse200Links",
    "GetSubscriptionItemResponse200LinksAdditionalProperty",
    "GetSubscriptionItemResponse200Merchant",
    "GetSubscriptionItemResponse200MetadataType0",
    "GetSubscriptionResponse200",
    "GetSubscriptionResponse200Billing",
    "GetSubscriptionResponse200BillingAddress",
    "GetSubscriptionResponse200CallbackType0",
    "GetSubscriptionResponse200CurrentCycleType0",
    "GetSubscriptionResponse200Customer",
    "GetSubscriptionResponse200CustomerDocumentType0",
    "GetSubscriptionResponse200CustomerMetadataType0",
    "GetSubscriptionResponse200CustomerTelephoneType0",
    "GetSubscriptionResponse200DiscountType0",
    "GetSubscriptionResponse200GeolocationType0",
    "GetSubscriptionResponse200ItemsItem",
    "GetSubscriptionResponse200ItemsItemImagesType0ItemType1",
    "GetSubscriptionResponse200ItemsItemMetadataType0",
    "GetSubscriptionResponse200Links",
    "GetSubscriptionResponse200LinksAdditionalProperty",
    "GetSubscriptionResponse200Merchant",
    "GetSubscriptionResponse200MetadataType0",
    "GetSubscriptionResponse200ShippingType0",
    "GetSubscriptionResponse200SplitsType0Item",
    "GetSubscriptionResponse200Status",
    "GetSubscriptionSplitResponse200",
    "GetSubscriptionSplitResponse200Links",
    "GetSubscriptionSplitResponse200LinksAdditionalProperty",
    "GetSubscriptionSplitResponse200Merchant",
    "GetTransactionResponse200",
    "GetTransactionResponse200Billing",
    "GetTransactionResponse200BillingAddress",
    "GetTransactionResponse200CallbackType0",
    "GetTransactionResponse200CustomerType0",
    "GetTransactionResponse200CustomerType0Document",
    "GetTransactionResponse200CustomerType0Telephone",
    "GetTransactionResponse200DiscountType0",
    "GetTransactionResponse200DisputesType0Item",
    "GetTransactionResponse200ItemsType0Item",
    "GetTransactionResponse200Links",
    "GetTransactionResponse200LinksAdditionalProperty",
    "GetTransactionResponse200Merchant",
    "GetTransactionResponse200Method",
    "GetTransactionResponse200Payment",
    "GetTransactionResponse200PaymentProvider",
    "GetTransactionResponse200PaymentVersion",
    "GetTransactionResponse200ReceivablesType0Item",
    "GetTransactionResponse200RefundsType0Item",
    "GetTransactionResponse200SplitsType0Item",
    "GetTransactionResponse200Status",
    "GetTransactionResponse200TimelineItem",
    "GetVariantResponse200",
    "GetVariantResponse200AttributesType0",
    "GetVariantResponse200ImagesType0ItemType1",
    "GetVariantResponse200MetadataType0",
    "GetVariantResponse200Pricing",
    "GetVariantResponse200PricingSchema",
    "GetVariantResponse200PricingType",
    "GetWalletResponse200",
    "GetWalletResponse200Links",
    "GetWalletResponse200LinksAdditionalProperty",
    "GetWalletResponse200Merchant",
    "GetWebhookEndpointResponse200",
    "GetWebhookEndpointResponse200Links",
    "GetWebhookEndpointResponse200LinksAdditionalProperty",
    "GetWebhookEndpointResponse200Merchant",
    "GetWebhookEndpointResponse200MetadataType0",
    "GetWebhookEventResponse200",
    "GetWebhookEventResponse200DispatchesItem",
    "GetWebhookEventResponse200DispatchesItemStatus",
    "GetWebhookEventResponse200Links",
    "GetWebhookEventResponse200LinksAdditionalProperty",
    "GetWebhookEventResponse200Merchant",
    "GetWithdrawalResponse200",
    "GetWithdrawalResponse200Links",
    "GetWithdrawalResponse200LinksAdditionalProperty",
    "GetWithdrawalResponse200Merchant",
    "GetWithdrawalResponse200ReceivingBankAccountType0",
    "ListAddressesResponse200",
    "ListAddressesResponse200DataItem",
    "ListAddressesResponse200DataItemLinks",
    "ListAddressesResponse200DataItemLinksAdditionalProperty",
    "ListAddressesResponse200DataItemMerchant",
    "ListAddressesResponse200DataItemMetadataType0",
    "ListAddressesResponse200DataItemOwnerType",
    "ListAddressesResponse200Links",
    "ListAddressesResponse200LinksAdditionalProperty",
    "ListAddressesResponse200Merchant",
    "ListAddressesResponse200Page",
    "ListAddressesResponse200PageOffset",
    "ListAddressesSort",
    "ListAllVariantsResponse200Item",
    "ListAllVariantsResponse200ItemAttributesType0",
    "ListAllVariantsResponse200ItemImagesType0ItemType1",
    "ListAllVariantsResponse200ItemMetadataType0",
    "ListAllVariantsResponse200ItemPricing",
    "ListAllVariantsResponse200ItemPricingSchema",
    "ListAllVariantsResponse200ItemPricingType",
    "ListAllVariantsSort",
    "ListBalanceHistoryResponse200",
    "ListBalanceHistoryResponse200DataItem",
    "ListBalanceHistoryResponse200DataItemNewBalance",
    "ListBalanceHistoryResponse200DataItemOldBalance",
    "ListBalanceHistoryResponse200Links",
    "ListBalanceHistoryResponse200LinksAdditionalProperty",
    "ListBalanceHistoryResponse200Merchant",
    "ListBalanceHistoryResponse200Page",
    "ListBalanceHistoryResponse200PageOffset",
    "ListCardsResponse200",
    "ListCardsResponse200DataItem",
    "ListCardsResponse200DataItemLinks",
    "ListCardsResponse200DataItemLinksAdditionalProperty",
    "ListCardsResponse200DataItemMerchant",
    "ListCardsResponse200Links",
    "ListCardsResponse200LinksAdditionalProperty",
    "ListCardsResponse200Merchant",
    "ListCardsResponse200Page",
    "ListCardsResponse200PageOffset",
    "ListCardsSort",
    "ListCheckoutPaymentLinksResponse200",
    "ListCheckoutPaymentLinksResponse200DataItem",
    "ListCheckoutPaymentLinksResponse200DataItemCustomInputsType0Item",
    "ListCheckoutPaymentLinksResponse200DataItemItemsItem",
    "ListCheckoutPaymentLinksResponse200DataItemMetadataType0",
    "ListCheckoutPaymentLinksResponse200Page",
    "ListCheckoutPaymentLinksResponse200PageOffset",
    "ListCheckoutPaymentLinksStatus",
    "ListCheckoutSessionsResponse200",
    "ListCheckoutSessionsResponse200DataItem",
    "ListCheckoutSessionsResponse200DataItemObject",
    "ListCheckoutSessionsResponse200DataItemStatus",
    "ListCheckoutSessionsResponse200Page",
    "ListCheckoutSessionsResponse200PageOffset",
    "ListCheckoutSessionsStatus",
    "ListCouponsDir",
    "ListCouponsResponse200",
    "ListCouponsResponse200DataItem",
    "ListCouponsResponse200DataItemScope",
    "ListCouponsResponse200DataItemType",
    "ListCouponsResponse200Page",
    "ListCouponsResponse200PageOffset",
    "ListCouponsStatus",
    "ListCouponsType",
    "ListCustomersResponse200",
    "ListCustomersResponse200DataItem",
    "ListCustomersResponse200DataItemDocumentType0",
    "ListCustomersResponse200DataItemDocumentType0Type",
    "ListCustomersResponse200DataItemLinks",
    "ListCustomersResponse200DataItemLinksAdditionalProperty",
    "ListCustomersResponse200DataItemMerchant",
    "ListCustomersResponse200DataItemMetadataType0",
    "ListCustomersResponse200DataItemTelephoneType0",
    "ListCustomersResponse200Links",
    "ListCustomersResponse200LinksAdditionalProperty",
    "ListCustomersResponse200Merchant",
    "ListCustomersResponse200Page",
    "ListCustomersResponse200PageOffset",
    "ListProductsResponse200",
    "ListProductsResponse200DataItem",
    "ListProductsResponse200DataItemImagesType0ItemType1",
    "ListProductsResponse200DataItemType",
    "ListProductsResponse200DataItemVariantsItem",
    "ListProductsResponse200DataItemVariantsItemAttributesType0",
    "ListProductsResponse200DataItemVariantsItemImagesType0ItemType1",
    "ListProductsResponse200DataItemVariantsItemMetadataType0",
    "ListProductsResponse200DataItemVariantsItemPricing",
    "ListProductsResponse200DataItemVariantsItemPricingSchema",
    "ListProductsResponse200DataItemVariantsItemPricingType",
    "ListProductsResponse200Page",
    "ListProductsResponse200PageOffset",
    "ListProductVariantsResponse200",
    "ListProductVariantsResponse200DataItem",
    "ListProductVariantsResponse200DataItemAttributesType0",
    "ListProductVariantsResponse200DataItemImagesType0ItemType1",
    "ListProductVariantsResponse200DataItemMetadataType0",
    "ListProductVariantsResponse200DataItemPricing",
    "ListProductVariantsResponse200DataItemPricingSchema",
    "ListProductVariantsResponse200DataItemPricingType",
    "ListProductVariantsResponse200Page",
    "ListProductVariantsResponse200PageOffset",
    "ListReceivablesReleased",
    "ListReceivablesResponse200",
    "ListReceivablesResponse200DataItem",
    "ListReceivablesResponse200DataItemLinks",
    "ListReceivablesResponse200DataItemLinksAdditionalProperty",
    "ListReceivablesResponse200DataItemMerchant",
    "ListReceivablesResponse200Links",
    "ListReceivablesResponse200LinksAdditionalProperty",
    "ListReceivablesResponse200Merchant",
    "ListReceivablesResponse200Page",
    "ListReceivablesResponse200PageOffset",
    "ListSubscriptionCyclesResponse200",
    "ListSubscriptionCyclesResponse200DataItem",
    "ListSubscriptionCyclesResponse200DataItemLinks",
    "ListSubscriptionCyclesResponse200DataItemLinksAdditionalProperty",
    "ListSubscriptionCyclesResponse200DataItemMerchant",
    "ListSubscriptionCyclesResponse200Links",
    "ListSubscriptionCyclesResponse200LinksAdditionalProperty",
    "ListSubscriptionCyclesResponse200Merchant",
    "ListSubscriptionCyclesResponse200Page",
    "ListSubscriptionCyclesResponse200PageOffset",
    "ListSubscriptionCyclesStatus",
    "ListSubscriptionItemsResponse200",
    "ListSubscriptionItemsResponse200DataItem",
    "ListSubscriptionItemsResponse200DataItemImagesType0ItemType1",
    "ListSubscriptionItemsResponse200DataItemLinks",
    "ListSubscriptionItemsResponse200DataItemLinksAdditionalProperty",
    "ListSubscriptionItemsResponse200DataItemMerchant",
    "ListSubscriptionItemsResponse200DataItemMetadataType0",
    "ListSubscriptionItemsResponse200Links",
    "ListSubscriptionItemsResponse200LinksAdditionalProperty",
    "ListSubscriptionItemsResponse200Merchant",
    "ListSubscriptionItemsResponse200Page",
    "ListSubscriptionItemsResponse200PageOffset",
    "ListSubscriptionSplitsResponse200",
    "ListSubscriptionSplitsResponse200DataItem",
    "ListSubscriptionSplitsResponse200DataItemLinks",
    "ListSubscriptionSplitsResponse200DataItemLinksAdditionalProperty",
    "ListSubscriptionSplitsResponse200DataItemMerchant",
    "ListSubscriptionSplitsResponse200Links",
    "ListSubscriptionSplitsResponse200LinksAdditionalProperty",
    "ListSubscriptionSplitsResponse200Merchant",
    "ListSubscriptionSplitsResponse200Page",
    "ListSubscriptionSplitsResponse200PageOffset",
    "ListSubscriptionsResponse200",
    "ListSubscriptionsResponse200DataItem",
    "ListSubscriptionsResponse200DataItemBilling",
    "ListSubscriptionsResponse200DataItemBillingAddress",
    "ListSubscriptionsResponse200DataItemCallbackType0",
    "ListSubscriptionsResponse200DataItemCurrentCycleType0",
    "ListSubscriptionsResponse200DataItemCustomer",
    "ListSubscriptionsResponse200DataItemCustomerDocumentType0",
    "ListSubscriptionsResponse200DataItemCustomerMetadataType0",
    "ListSubscriptionsResponse200DataItemCustomerTelephoneType0",
    "ListSubscriptionsResponse200DataItemDiscountType0",
    "ListSubscriptionsResponse200DataItemGeolocationType0",
    "ListSubscriptionsResponse200DataItemItemsItem",
    "ListSubscriptionsResponse200DataItemItemsItemImagesType0ItemType1",
    "ListSubscriptionsResponse200DataItemItemsItemMetadataType0",
    "ListSubscriptionsResponse200DataItemLinks",
    "ListSubscriptionsResponse200DataItemLinksAdditionalProperty",
    "ListSubscriptionsResponse200DataItemMerchant",
    "ListSubscriptionsResponse200DataItemMetadataType0",
    "ListSubscriptionsResponse200DataItemShippingType0",
    "ListSubscriptionsResponse200DataItemSplitsType0Item",
    "ListSubscriptionsResponse200DataItemStatus",
    "ListSubscriptionsResponse200Links",
    "ListSubscriptionsResponse200LinksAdditionalProperty",
    "ListSubscriptionsResponse200Merchant",
    "ListSubscriptionsResponse200Page",
    "ListSubscriptionsResponse200PageOffset",
    "ListSubscriptionsStatus",
    "ListSubscriptionThresholdsResponse200",
    "ListSubscriptionThresholdsResponse200DataItem",
    "ListSubscriptionThresholdsResponse200DataItemKind",
    "ListSubscriptionThresholdsResponse200Links",
    "ListSubscriptionThresholdsResponse200LinksAdditionalProperty",
    "ListSubscriptionThresholdsResponse200Merchant",
    "ListSubscriptionThresholdsResponse200Page",
    "ListSubscriptionThresholdsResponse200PageOffset",
    "ListSubscriptionUsageResponse200",
    "ListSubscriptionUsageResponse200DataItem",
    "ListSubscriptionUsageResponse200Links",
    "ListSubscriptionUsageResponse200LinksAdditionalProperty",
    "ListSubscriptionUsageResponse200Merchant",
    "ListSubscriptionUsageResponse200Page",
    "ListSubscriptionUsageResponse200PageOffset",
    "ListTransactionsMethod",
    "ListTransactionsResponse200",
    "ListTransactionsResponse200DataItem",
    "ListTransactionsResponse200Links",
    "ListTransactionsResponse200LinksAdditionalProperty",
    "ListTransactionsResponse200Merchant",
    "ListTransactionsResponse200Page",
    "ListTransactionsResponse200PageOffset",
    "ListTransactionsStatus",
    "ListWalletsResponse200",
    "ListWalletsResponse200DataItem",
    "ListWalletsResponse200DataItemLinks",
    "ListWalletsResponse200DataItemLinksAdditionalProperty",
    "ListWalletsResponse200DataItemMerchant",
    "ListWalletsResponse200Links",
    "ListWalletsResponse200LinksAdditionalProperty",
    "ListWalletsResponse200Merchant",
    "ListWalletsResponse200Page",
    "ListWalletsResponse200PageOffset",
    "ListWebhookDispatchesResponse200",
    "ListWebhookDispatchesResponse200DataItem",
    "ListWebhookDispatchesResponse200DataItemStatus",
    "ListWebhookDispatchesResponse200Links",
    "ListWebhookDispatchesResponse200LinksAdditionalProperty",
    "ListWebhookDispatchesResponse200Merchant",
    "ListWebhookDispatchesResponse200Page",
    "ListWebhookDispatchesResponse200PageOffset",
    "ListWebhookDispatchesStatus",
    "ListWebhookEndpointsResponse200",
    "ListWebhookEndpointsResponse200DataItem",
    "ListWebhookEndpointsResponse200DataItemLinks",
    "ListWebhookEndpointsResponse200DataItemLinksAdditionalProperty",
    "ListWebhookEndpointsResponse200DataItemMerchant",
    "ListWebhookEndpointsResponse200DataItemMetadataType0",
    "ListWebhookEndpointsResponse200Links",
    "ListWebhookEndpointsResponse200LinksAdditionalProperty",
    "ListWebhookEndpointsResponse200Merchant",
    "ListWebhookEndpointsResponse200Page",
    "ListWebhookEndpointsResponse200PageOffset",
    "ListWebhookEventsResponse200",
    "ListWebhookEventsResponse200DataItem",
    "ListWebhookEventsResponse200DataItemDispatchesItem",
    "ListWebhookEventsResponse200DataItemDispatchesItemStatus",
    "ListWebhookEventsResponse200DataItemLinks",
    "ListWebhookEventsResponse200DataItemLinksAdditionalProperty",
    "ListWebhookEventsResponse200DataItemMerchant",
    "ListWebhookEventsResponse200Links",
    "ListWebhookEventsResponse200LinksAdditionalProperty",
    "ListWebhookEventsResponse200Merchant",
    "ListWebhookEventsResponse200Page",
    "ListWebhookEventsResponse200PageOffset",
    "ListWebhookEventsStatus",
    "ListWebhookEventsType",
    "ListWithdrawalsResponse200",
    "ListWithdrawalsResponse200DataItem",
    "ListWithdrawalsResponse200DataItemLinks",
    "ListWithdrawalsResponse200DataItemLinksAdditionalProperty",
    "ListWithdrawalsResponse200DataItemMerchant",
    "ListWithdrawalsResponse200DataItemReceivingBankAccountType0",
    "ListWithdrawalsResponse200Links",
    "ListWithdrawalsResponse200LinksAdditionalProperty",
    "ListWithdrawalsResponse200Merchant",
    "ListWithdrawalsResponse200Page",
    "ListWithdrawalsResponse200PageOffset",
    "PatchCouponBody",
    "PatchCouponBodyScope",
    "PatchCouponBodyType",
    "PatchCouponResponse200",
    "PatchCouponResponse200Scope",
    "PatchCouponResponse200Type",
    "PauseSubscriptionResponse200",
    "PauseSubscriptionResponse200Billing",
    "PauseSubscriptionResponse200BillingAddress",
    "PauseSubscriptionResponse200CallbackType0",
    "PauseSubscriptionResponse200CurrentCycleType0",
    "PauseSubscriptionResponse200Customer",
    "PauseSubscriptionResponse200CustomerDocumentType0",
    "PauseSubscriptionResponse200CustomerMetadataType0",
    "PauseSubscriptionResponse200CustomerTelephoneType0",
    "PauseSubscriptionResponse200DiscountType0",
    "PauseSubscriptionResponse200GeolocationType0",
    "PauseSubscriptionResponse200ItemsItem",
    "PauseSubscriptionResponse200ItemsItemImagesType0ItemType1",
    "PauseSubscriptionResponse200ItemsItemMetadataType0",
    "PauseSubscriptionResponse200Links",
    "PauseSubscriptionResponse200LinksAdditionalProperty",
    "PauseSubscriptionResponse200Merchant",
    "PauseSubscriptionResponse200MetadataType0",
    "PauseSubscriptionResponse200ShippingType0",
    "PauseSubscriptionResponse200SplitsType0Item",
    "PauseSubscriptionResponse200Status",
    "RecordSubscriptionUsageBody",
    "RecordSubscriptionUsageBodyAction",
    "RecordSubscriptionUsageBodyMetadata",
    "RecordSubscriptionUsageResponse200",
    "RecordSubscriptionUsageResponse201",
    "RedispatchWebhookResponse202",
    "RefundTransactionBody",
    "RefundTransactionResponse202",
    "RefundTransactionResponse202Status",
    "RemoveSubscriptionItemResponse200",
    "RemoveSubscriptionItemResponse200Links",
    "RemoveSubscriptionItemResponse200LinksAdditionalProperty",
    "RemoveSubscriptionItemResponse200Merchant",
    "RemoveSubscriptionSplitResponse200",
    "RemoveSubscriptionSplitResponse200Links",
    "RemoveSubscriptionSplitResponse200LinksAdditionalProperty",
    "RemoveSubscriptionSplitResponse200Merchant",
    "RemoveSubscriptionSplitResponse200SplitsItem",
    "RemoveSubscriptionSplitResponse200SplitsItemLinks",
    "RemoveSubscriptionSplitResponse200SplitsItemLinksAdditionalProperty",
    "RemoveSubscriptionSplitResponse200SplitsItemMerchant",
    "RemoveSubscriptionThresholdResponse200",
    "RenewSubscriptionCycleResponse201",
    "RenewSubscriptionCycleResponse201Links",
    "RenewSubscriptionCycleResponse201LinksAdditionalProperty",
    "RenewSubscriptionCycleResponse201Merchant",
    "ResendWebhookEventResponse202",
    "ResumeSubscriptionResponse200",
    "ResumeSubscriptionResponse200Billing",
    "ResumeSubscriptionResponse200BillingAddress",
    "ResumeSubscriptionResponse200CallbackType0",
    "ResumeSubscriptionResponse200CurrentCycleType0",
    "ResumeSubscriptionResponse200Customer",
    "ResumeSubscriptionResponse200CustomerDocumentType0",
    "ResumeSubscriptionResponse200CustomerMetadataType0",
    "ResumeSubscriptionResponse200CustomerTelephoneType0",
    "ResumeSubscriptionResponse200DiscountType0",
    "ResumeSubscriptionResponse200GeolocationType0",
    "ResumeSubscriptionResponse200ItemsItem",
    "ResumeSubscriptionResponse200ItemsItemImagesType0ItemType1",
    "ResumeSubscriptionResponse200ItemsItemMetadataType0",
    "ResumeSubscriptionResponse200Links",
    "ResumeSubscriptionResponse200LinksAdditionalProperty",
    "ResumeSubscriptionResponse200Merchant",
    "ResumeSubscriptionResponse200MetadataType0",
    "ResumeSubscriptionResponse200ShippingType0",
    "ResumeSubscriptionResponse200SplitsType0Item",
    "ResumeSubscriptionResponse200Status",
    "RotateWebhookSecretResponse200",
    "RotateWebhookSecretResponse200Links",
    "RotateWebhookSecretResponse200LinksAdditionalProperty",
    "RotateWebhookSecretResponse200Merchant",
    "RotateWebhookSecretResponse200MetadataType0",
    "SimulateInstallmentResource",
    "SimulateInstallmentResponse200",
    "SimulateInstallmentResponse200Amount",
    "SimulateInstallmentResponse200Links",
    "SimulateInstallmentResponse200LinksInstallments",
    "SimulateInstallmentResponse200LinksPaymentMethods",
    "SimulateInstallmentResponse200LinksSelf",
    "SimulateInstallmentResponse200Merchant",
    "SimulateInstallmentResponse200Original",
    "SimulateInstallmentResponse200Resource",
    "SimulateInstallmentResponse200TotalFees",
    "SimulateInstallmentsResource",
    "SimulateInstallmentsResponse200",
    "SimulateInstallmentsResponse200InstallmentsItem",
    "SimulateInstallmentsResponse200Links",
    "SimulateInstallmentsResponse200LinksInstallment",
    "SimulateInstallmentsResponse200LinksPaymentMethods",
    "SimulateInstallmentsResponse200LinksSelf",
    "SimulateInstallmentsResponse200Merchant",
    "SimulateInstallmentsResponse200Resource",
    "SimulatePaymentMethodsMethod",
    "SimulatePaymentMethodsResponse200",
    "SimulatePaymentMethodsResponse200Amount",
    "SimulatePaymentMethodsResponse200Links",
    "SimulatePaymentMethodsResponse200LinksInstallment",
    "SimulatePaymentMethodsResponse200LinksInstallments",
    "SimulatePaymentMethodsResponse200LinksSelf",
    "SimulatePaymentMethodsResponse200Merchant",
    "SimulatePaymentMethodsResponse200Original",
    "SimulatePaymentMethodsResponse200Resource",
    "SimulatePaymentMethodsResponse200TotalFees",
    "SubmitCheckoutPaymentBody",
    "SubmitCheckoutPaymentBodyPayment",
    "SubmitCheckoutPaymentBodyPaymentMethod",
    "SubmitCheckoutPaymentResponse202",
    "SubmitCheckoutPaymentResponse202Status",
    "SubmitTransactionDisputeBody",
    "SubmitTransactionDisputeBodyDocumentsItem",
    "SubmitTransactionDisputeBodyDocumentsItemAuthentication",
    "SubmitTransactionDisputeBodyDocumentsItemType",
    "SubmitTransactionDisputeResponse200",
    "SubmitTransactionDisputeResponse200Billing",
    "SubmitTransactionDisputeResponse200BillingAddress",
    "SubmitTransactionDisputeResponse200CallbackType0",
    "SubmitTransactionDisputeResponse200CustomerType0",
    "SubmitTransactionDisputeResponse200CustomerType0Document",
    "SubmitTransactionDisputeResponse200CustomerType0Telephone",
    "SubmitTransactionDisputeResponse200DiscountType0",
    "SubmitTransactionDisputeResponse200DisputesType0Item",
    "SubmitTransactionDisputeResponse200ItemsType0Item",
    "SubmitTransactionDisputeResponse200Links",
    "SubmitTransactionDisputeResponse200LinksAdditionalProperty",
    "SubmitTransactionDisputeResponse200Merchant",
    "SubmitTransactionDisputeResponse200Method",
    "SubmitTransactionDisputeResponse200Payment",
    "SubmitTransactionDisputeResponse200PaymentProvider",
    "SubmitTransactionDisputeResponse200PaymentVersion",
    "SubmitTransactionDisputeResponse200ReceivablesType0Item",
    "SubmitTransactionDisputeResponse200RefundsType0Item",
    "SubmitTransactionDisputeResponse200SplitsType0Item",
    "SubmitTransactionDisputeResponse200Status",
    "SubmitTransactionDisputeResponse200TimelineItem",
    "TestWebhookEndpointBodyType1",
    "TestWebhookEndpointResponse202",
    "UpdateAddressBody",
    "UpdateAddressBodyMetadata",
    "UpdateAddressPatchBody",
    "UpdateAddressPatchBodyMetadata",
    "UpdateAddressPatchResponse200",
    "UpdateAddressPatchResponse200Links",
    "UpdateAddressPatchResponse200LinksAdditionalProperty",
    "UpdateAddressPatchResponse200Merchant",
    "UpdateAddressPatchResponse200MetadataType0",
    "UpdateAddressPatchResponse200OwnerType",
    "UpdateAddressResponse200",
    "UpdateAddressResponse200Links",
    "UpdateAddressResponse200LinksAdditionalProperty",
    "UpdateAddressResponse200Merchant",
    "UpdateAddressResponse200MetadataType0",
    "UpdateAddressResponse200OwnerType",
    "UpdateCheckoutPaymentLinkBody",
    "UpdateCheckoutPaymentLinkBodyCustomInputsItem",
    "UpdateCheckoutPaymentLinkBodyItemsItem",
    "UpdateCheckoutPaymentLinkBodyMetadata",
    "UpdateCheckoutPaymentLinkPatchBody",
    "UpdateCheckoutPaymentLinkPatchBodyCustomInputsItem",
    "UpdateCheckoutPaymentLinkPatchBodyItemsItem",
    "UpdateCheckoutPaymentLinkPatchBodyMetadata",
    "UpdateCheckoutPaymentLinkPatchResponse200",
    "UpdateCheckoutPaymentLinkPatchResponse200CustomInputsType0Item",
    "UpdateCheckoutPaymentLinkPatchResponse200ItemsItem",
    "UpdateCheckoutPaymentLinkPatchResponse200MetadataType0",
    "UpdateCheckoutPaymentLinkResponse200",
    "UpdateCheckoutPaymentLinkResponse200CustomInputsType0Item",
    "UpdateCheckoutPaymentLinkResponse200ItemsItem",
    "UpdateCheckoutPaymentLinkResponse200MetadataType0",
    "UpdateCheckoutSessionBody",
    "UpdateCheckoutSessionBodyAddress",
    "UpdateCheckoutSessionBodyAmbient",
    "UpdateCheckoutSessionBodyClient",
    "UpdateCheckoutSessionBodyCookies",
    "UpdateCheckoutSessionBodyCouponsItemType1",
    "UpdateCheckoutSessionBodyCustomer",
    "UpdateCheckoutSessionBodyItemsItem",
    "UpdateCheckoutSessionBodyLineItemsItem",
    "UpdateCheckoutSessionBodyMetadata",
    "UpdateCheckoutSessionBodyPaymentMethodsItemType1",
    "UpdateCheckoutSessionBodyRedirectUrls",
    "UpdateCheckoutSessionBodyShippingDelivery",
    "UpdateCheckoutSessionBodyStatus",
    "UpdateCheckoutSessionBodyUtm",
    "UpdateCheckoutSessionResponse200",
    "UpdateCheckoutSessionResponse200AddressType0",
    "UpdateCheckoutSessionResponse200CouponsItem",
    "UpdateCheckoutSessionResponse200Currency",
    "UpdateCheckoutSessionResponse200CustomerType0",
    "UpdateCheckoutSessionResponse200CustomInputs",
    "UpdateCheckoutSessionResponse200LineItemsItem",
    "UpdateCheckoutSessionResponse200LineItemsItemMetadataType0",
    "UpdateCheckoutSessionResponse200MetadataType0",
    "UpdateCheckoutSessionResponse200Object",
    "UpdateCheckoutSessionResponse200PaymentMethodsItemType1",
    "UpdateCheckoutSessionResponse200PaymentSelectionType0",
    "UpdateCheckoutSessionResponse200RedirectUrls",
    "UpdateCheckoutSessionResponse200Status",
    "UpdateCheckoutSessionResponse200Totals",
    "UpdateCheckoutSessionResponse200UtmType0",
    "UpdateCouponBody",
    "UpdateCouponBodyScope",
    "UpdateCouponBodyType",
    "UpdateCouponResponse200",
    "UpdateCouponResponse200Scope",
    "UpdateCouponResponse200Type",
    "UpdateCustomerBody",
    "UpdateCustomerBodyDocument",
    "UpdateCustomerBodyDocumentType",
    "UpdateCustomerBodyGender",
    "UpdateCustomerBodyMetadata",
    "UpdateCustomerBodyTelephone",
    "UpdateCustomerPutBody",
    "UpdateCustomerPutBodyDocument",
    "UpdateCustomerPutBodyDocumentType",
    "UpdateCustomerPutBodyGender",
    "UpdateCustomerPutBodyMetadata",
    "UpdateCustomerPutBodyTelephone",
    "UpdateCustomerPutResponse200",
    "UpdateCustomerPutResponse200DocumentType0",
    "UpdateCustomerPutResponse200DocumentType0Type",
    "UpdateCustomerPutResponse200Links",
    "UpdateCustomerPutResponse200LinksAdditionalProperty",
    "UpdateCustomerPutResponse200Merchant",
    "UpdateCustomerPutResponse200MetadataType0",
    "UpdateCustomerPutResponse200TelephoneType0",
    "UpdateCustomerResponse200",
    "UpdateCustomerResponse200DocumentType0",
    "UpdateCustomerResponse200DocumentType0Type",
    "UpdateCustomerResponse200Links",
    "UpdateCustomerResponse200LinksAdditionalProperty",
    "UpdateCustomerResponse200Merchant",
    "UpdateCustomerResponse200MetadataType0",
    "UpdateCustomerResponse200TelephoneType0",
    "UpdateProductBody",
    "UpdateProductBodyImagesItemType1",
    "UpdateProductBodyType",
    "UpdateProductPutBody",
    "UpdateProductPutBodyImagesItemType1",
    "UpdateProductPutBodyType",
    "UpdateProductPutResponse200",
    "UpdateProductPutResponse200ImagesType0ItemType1",
    "UpdateProductPutResponse200Type",
    "UpdateProductPutResponse200VariantsItem",
    "UpdateProductPutResponse200VariantsItemAttributesType0",
    "UpdateProductPutResponse200VariantsItemImagesType0ItemType1",
    "UpdateProductPutResponse200VariantsItemMetadataType0",
    "UpdateProductPutResponse200VariantsItemPricing",
    "UpdateProductPutResponse200VariantsItemPricingSchema",
    "UpdateProductPutResponse200VariantsItemPricingType",
    "UpdateProductResponse200",
    "UpdateProductResponse200ImagesType0ItemType1",
    "UpdateProductResponse200Type",
    "UpdateProductResponse200VariantsItem",
    "UpdateProductResponse200VariantsItemAttributesType0",
    "UpdateProductResponse200VariantsItemImagesType0ItemType1",
    "UpdateProductResponse200VariantsItemMetadataType0",
    "UpdateProductResponse200VariantsItemPricing",
    "UpdateProductResponse200VariantsItemPricingSchema",
    "UpdateProductResponse200VariantsItemPricingType",
    "UpdateProductVariantBody",
    "UpdateProductVariantBodyAttributes",
    "UpdateProductVariantBodyImagesItemType1",
    "UpdateProductVariantBodyMetadata",
    "UpdateProductVariantBodyPricing",
    "UpdateProductVariantBodyPricingBillingFrequency",
    "UpdateProductVariantBodyPricingBillingType",
    "UpdateProductVariantBodyPricingSchema",
    "UpdateProductVariantBodyPricingTiersItem",
    "UpdateProductVariantBodyPricingTiersMode",
    "UpdateProductVariantBodyPricingTransformQuantity",
    "UpdateProductVariantBodyPricingTransformQuantityRound",
    "UpdateProductVariantBodyPricingTrialInterval",
    "UpdateProductVariantBodyPricingType",
    "UpdateProductVariantBodyPricingUsageAggregation",
    "UpdateProductVariantBodyPricingUsageType",
    "UpdateProductVariantPutBody",
    "UpdateProductVariantPutBodyAttributes",
    "UpdateProductVariantPutBodyImagesItemType1",
    "UpdateProductVariantPutBodyMetadata",
    "UpdateProductVariantPutBodyPricing",
    "UpdateProductVariantPutBodyPricingBillingFrequency",
    "UpdateProductVariantPutBodyPricingBillingType",
    "UpdateProductVariantPutBodyPricingSchema",
    "UpdateProductVariantPutBodyPricingTiersItem",
    "UpdateProductVariantPutBodyPricingTiersMode",
    "UpdateProductVariantPutBodyPricingTransformQuantity",
    "UpdateProductVariantPutBodyPricingTransformQuantityRound",
    "UpdateProductVariantPutBodyPricingTrialInterval",
    "UpdateProductVariantPutBodyPricingType",
    "UpdateProductVariantPutBodyPricingUsageAggregation",
    "UpdateProductVariantPutBodyPricingUsageType",
    "UpdateProductVariantPutResponse200",
    "UpdateProductVariantPutResponse200AttributesType0",
    "UpdateProductVariantPutResponse200ImagesType0ItemType1",
    "UpdateProductVariantPutResponse200MetadataType0",
    "UpdateProductVariantPutResponse200Pricing",
    "UpdateProductVariantPutResponse200PricingSchema",
    "UpdateProductVariantPutResponse200PricingType",
    "UpdateProductVariantResponse200",
    "UpdateProductVariantResponse200AttributesType0",
    "UpdateProductVariantResponse200ImagesType0ItemType1",
    "UpdateProductVariantResponse200MetadataType0",
    "UpdateProductVariantResponse200Pricing",
    "UpdateProductVariantResponse200PricingSchema",
    "UpdateProductVariantResponse200PricingType",
    "UpdateSubscriptionItemBody",
    "UpdateSubscriptionItemPutBody",
    "UpdateSubscriptionItemPutResponse200",
    "UpdateSubscriptionItemPutResponse200ImagesType0ItemType1",
    "UpdateSubscriptionItemPutResponse200Links",
    "UpdateSubscriptionItemPutResponse200LinksAdditionalProperty",
    "UpdateSubscriptionItemPutResponse200Merchant",
    "UpdateSubscriptionItemPutResponse200MetadataType0",
    "UpdateSubscriptionItemResponse200",
    "UpdateSubscriptionItemResponse200ImagesType0ItemType1",
    "UpdateSubscriptionItemResponse200Links",
    "UpdateSubscriptionItemResponse200LinksAdditionalProperty",
    "UpdateSubscriptionItemResponse200Merchant",
    "UpdateSubscriptionItemResponse200MetadataType0",
    "UpdateSubscriptionSplitBody",
    "UpdateSubscriptionSplitBodyType",
    "UpdateSubscriptionSplitPutBody",
    "UpdateSubscriptionSplitPutBodyType",
    "UpdateSubscriptionSplitPutResponse200",
    "UpdateSubscriptionSplitPutResponse200Links",
    "UpdateSubscriptionSplitPutResponse200LinksAdditionalProperty",
    "UpdateSubscriptionSplitPutResponse200Merchant",
    "UpdateSubscriptionSplitResponse200",
    "UpdateSubscriptionSplitResponse200Links",
    "UpdateSubscriptionSplitResponse200LinksAdditionalProperty",
    "UpdateSubscriptionSplitResponse200Merchant",
    "UpdateWebhookEndpointBody",
    "UpdateWebhookEndpointBodyEventsItem",
    "UpdateWebhookEndpointBodyMetadata",
    "UpdateWebhookEndpointResponse200",
    "UpdateWebhookEndpointResponse200Links",
    "UpdateWebhookEndpointResponse200LinksAdditionalProperty",
    "UpdateWebhookEndpointResponse200Merchant",
    "UpdateWebhookEndpointResponse200MetadataType0",
    "UtilsCardBinValidationResponse200",
    "UtilsCardBinValidationResponse200IntelType0",
    "UtilsCardBinValidationResponse200Links",
    "UtilsCardBinValidationResponse200LinksAdditionalProperty",
    "UtilsCardBinValidationResponse200Merchant",
    "UtilsCompanyTypesResponse200",
    "UtilsCompanyTypesResponse200DataItem",
    "UtilsCorporateDocumentCheckResponse200",
    "UtilsCorporateDocumentCheckResponse200AddressType0",
    "UtilsCorporateDocumentCheckResponse200Merchant",
    "UtilsCorporateDocumentCheckResponse200PartnersItem",
    "UtilsCorporateDocumentCheckResponse200SecondaryCnaesItem",
    "UtilsCorporateDocumentCheckResponse200Type",
    "UtilsMetadataResponse200",
    "UtilsMetadataResponse200Data",
    "UtilsPostcodeValidationResponse200",
    "UtilsPostcodeValidationResponse200AddressType0",
    "UtilsPostcodeValidationResponse200Merchant",
    "UtilsRolesOfUserResponse200",
    "UtilsRulesOfRecurrenciesResponse200",
    "UtilsRulesOfRecurrenciesResponse200Data",
    "UtilsRulesOfRecurrenciesResponse200DataFrequencyCount",
    "UtilsTypesOfBankAccountsResponse200",
    "UtilsTypesOfBankAccountsResponse200DataItem",
    "UtilsTypesOfCompanyResponse200",
    "UtilsTypesOfCompanyResponse200DataItem",
    "UtilsTypesOfRefundResponse200",
    "UtilsTypesOfRefundResponse200DataItem",
    "UtilsTypesOfWebhooksResponse200",
    "ValidateCouponBody",
    "ValidateCouponResponse200",
    "ValidateCouponResponse200DiscountType0",
    "ValidateCouponResponse200DiscountType0Type",
    "WebhookEventPayload",
    "WebhookEventPayloadPayload",
    "WebhookEventPayloadPayloadObject",
)
