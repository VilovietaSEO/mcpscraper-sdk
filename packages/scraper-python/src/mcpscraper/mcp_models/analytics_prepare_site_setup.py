from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class AnalyticsPrepareSiteSetupInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    site_id: str = Field(..., alias='siteId', description='Authorized Analytics Site id returned by analytics_list_sites.')
    start_url: Annotated[str, Field(max_length=3000)] = Field(..., alias='startUrl', description='Public same-origin URL from which X-Ray discovers bounded routes and rendering surfaces.')
    goal: Union[Annotated[str, Field(min_length=1, max_length=500)], None] = Field(None, alias='goal', description='Plain-language customer outcome to measure; do not paste credentials, source code, form contents, or visitor data.')
    business_model: Union[Literal['saas', 'lead_generation', 'ecommerce'], None] = Field(None, alias='businessModel', description='Optional user-confirmed model; omit to receive an evidence-backed recommendation.')
    scope: Union[Literal['same_origin', 'sitemap'], None] = Field(None, alias='scope', description='Bounded route discovery scope; neither mode authorizes third-party crawling.')
    max_pages: Union[Annotated[int, Field(ge=1, le=250)], None] = Field(None, alias='maxPages', description='Maximum pages inspected under the X-Ray entitlement; this consumes zero MCP Scraper Credits.')
    pixel_id: Union[str, None] = Field(None, alias='pixelId', description='Optional existing Pixel belonging to the Site; omit to let the service resolve the canonical Pixel.')
    consent_mode: Union[Literal['required', 'granted_test', 'unknown'], None] = Field(None, alias='consentMode', description='Consent expectation for non-delivering discovery. It never grants a visitor consent choice.')


AnalyticsPrepareSiteSetupOutputVariant1SetupReadinessDimensionsItem = TypedDict('AnalyticsPrepareSiteSetupOutputVariant1SetupReadinessDimensionsItem', {
    'dimension': Required[Literal['loader_coverage', 'route_coverage', 'pageview_integrity', 'semantic_action_coverage', 'terminal_outcome_coverage', 'destination_delivery', 'identity_value_coverage', 'data_sufficiency']],
    'state': Required[Literal['blocked', 'not_ready', 'partial', 'ready', 'not_required']],
    'numerator': Required[Annotated[Union[float, int], Field(ge=0)]],
    'denominator': Required[Annotated[Union[float, int], Field(ge=0)]],
    'readinessReason': Required[Literal['entitlement_required', 'connection_required', 'business_choice_required', 'surface_unreachable', 'adapter_unavailable', 'revision_stale', 'script_not_seen', 'duplicate_pageview', 'consent_blocked', 'only_pageview_seen', 'semantic_action_missing', 'definition_not_observed', 'terminal_outcome_missing', 'destination_not_connected', 'destination_delivery_failed', 'identity_value_missing', 'runtime_manifest_pending', 'events_processing', 'insufficient_data', 'ready']],
    'required': Required[bool],
})
AnalyticsPrepareSiteSetupOutputVariant1SetupReadinessDimensionsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsPrepareSiteSetupOutputVariant1SetupReadiness = TypedDict('AnalyticsPrepareSiteSetupOutputVariant1SetupReadiness', {
    'schemaVersion': Required[Literal[1]],
    'overallState': Required[Literal['blocked', 'not_ready', 'partial', 'ready']],
    'dimensions': Required[Annotated[list[AnalyticsPrepareSiteSetupOutputVariant1SetupReadinessDimensionsItem], Field(min_length=8, max_length=8)]],
})
AnalyticsPrepareSiteSetupOutputVariant1SetupReadiness.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsPrepareSiteSetupOutputVariant1Setup = TypedDict('AnalyticsPrepareSiteSetupOutputVariant1Setup', {
    'schemaVersion': Required[Literal[1]],
    'setupId': Required[str],
    'siteId': Required[str],
    'revision': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'status': Required[Literal['needs_business_choice', 'tag_required', 'prepared', 'publishing', 'awaiting_runtime_convergence', 'verifying', 'outcome_connection_required', 'collecting_data', 'answers_ready', 'partial', 'blocked']],
    'expiresAt': Required[str],
    'readiness': Required[AnalyticsPrepareSiteSetupOutputVariant1SetupReadiness],
})
AnalyticsPrepareSiteSetupOutputVariant1Setup.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsPrepareSiteSetupOutputVariant1BillingReceiptProviderCostsItem = TypedDict('AnalyticsPrepareSiteSetupOutputVariant1BillingReceiptProviderCostsItem', {
    'amountMinor': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'currency': NotRequired[str],
    'status': Required[Literal['none', 'estimated', 'incurred', 'unknown']],
})
AnalyticsPrepareSiteSetupOutputVariant1BillingReceiptProviderCostsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsPrepareSiteSetupOutputVariant1BillingReceipt = TypedDict('AnalyticsPrepareSiteSetupOutputVariant1BillingReceipt', {
    'billingClass': Required[Literal['xray_entitlement']],
    'mcpScraperCreditsCharged': Required[Literal[0]],
    'providerCosts': Required[Annotated[list[AnalyticsPrepareSiteSetupOutputVariant1BillingReceiptProviderCostsItem], Field(max_length=50)]],
})
AnalyticsPrepareSiteSetupOutputVariant1BillingReceipt.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsPrepareSiteSetupOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: Literal[True] = Field(..., alias='ok', description='')
    operation: Literal['prepare'] = Field(..., alias='operation', description='')
    setup: AnalyticsPrepareSiteSetupOutputVariant1Setup = Field(..., alias='setup', description='')
    next_action: Annotated[str, Field(min_length=1, max_length=500)] = Field(..., alias='nextAction', description='Exactly one safe next user or system action based on the current durable state.')
    billing_receipt: AnalyticsPrepareSiteSetupOutputVariant1BillingReceipt = Field(..., alias='billingReceipt', description='')


AnalyticsPrepareSiteSetupOutputVariant2DeliveryArtifactsItem = TypedDict('AnalyticsPrepareSiteSetupOutputVariant2DeliveryArtifactsItem', {
    'artifactId': Required[str],
    'filename': Required[str],
    'contentType': Required[str],
    'bytes': Required[Union[float, int]],
    'sha256': Required[str],
    'expiresAt': Required[str],
    'capabilities': Required[list[str]],
    'downloadUrl': Required[Union[str, None]],
    'downloadUrlExpiresAt': Required[Union[str, None]],
    'downloadState': Required[Literal['available', 'local', 'unavailable']],
})
AnalyticsPrepareSiteSetupOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsPrepareSiteSetupOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AnalyticsPrepareSiteSetupOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AnalyticsPrepareSiteSetupOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsPrepareSiteSetupOutputVariant2Delivery = TypedDict('AnalyticsPrepareSiteSetupOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AnalyticsPrepareSiteSetupOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AnalyticsPrepareSiteSetupOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AnalyticsPrepareSiteSetupOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsPrepareSiteSetupOutputVariant2RecoveryOperation = TypedDict('AnalyticsPrepareSiteSetupOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AnalyticsPrepareSiteSetupOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsPrepareSiteSetupOutputVariant2Recovery = TypedDict('AnalyticsPrepareSiteSetupOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AnalyticsPrepareSiteSetupOutputVariant2RecoveryOperation],
})
AnalyticsPrepareSiteSetupOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsPrepareSiteSetupOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AnalyticsPrepareSiteSetupOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AnalyticsPrepareSiteSetupOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AnalyticsPrepareSiteSetupOutput).
AnalyticsPrepareSiteSetupOutput = Union[AnalyticsPrepareSiteSetupOutputVariant1, AnalyticsPrepareSiteSetupOutputVariant2]

_AnalyticsPrepareSiteSetupInputAdapter = TypeAdapter(AnalyticsPrepareSiteSetupInput)
_AnalyticsPrepareSiteSetupOutputAdapter = TypeAdapter(AnalyticsPrepareSiteSetupOutput)