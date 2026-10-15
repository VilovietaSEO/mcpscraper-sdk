from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


AnalyticsSetupSiteInputAuthority = TypedDict('AnalyticsSetupSiteInputAuthority', {
    'confirmed': NotRequired[Literal[True]],
    'confirmedCanary': NotRequired[Literal[True]],
})
AnalyticsSetupSiteInputAuthority.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class AnalyticsSetupSiteInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    site_id: Union[str, None] = Field(None, alias='siteId', description='Authorized Analytics Site id. Supply siteId or startUrl on the first call.')
    start_url: Union[Annotated[str, Field(max_length=3000)], None] = Field(None, alias='startUrl', description='Public same-origin URL to set up. Supply only when siteId is not yet known.')
    goal: Union[Annotated[str, Field(min_length=1, max_length=500)], None] = Field(None, alias='goal', description='Plain-language customer outcome to measure; do not paste credentials, source code, form contents, or visitor data.')
    setup_id: Union[str, None] = Field(None, alias='setupId', description='Reuse to continue an existing durable setup after approval, deployment, or reconnecting.')
    revision: Union[Annotated[int, Field(le=9007199254740991, gt=0)], None] = Field(None, alias='revision', description='Exact current setup revision. Reload stale revisions before any mutation or canary.')
    business_model: Union[Literal['saas', 'lead_generation', 'ecommerce'], None] = Field(None, alias='businessModel', description='Optional explicit business model; omit to infer it from bounded site evidence.')
    goal_action: Union[Literal['continue', 'prepare', 'apply', 'verify', 'first_answers'], None] = Field(None, alias='goalAction', description='Desired lifecycle step. Continue lets the façade select the single safe next operation from durable state.')
    authority: Union[AnalyticsSetupSiteInputAuthority, None] = Field(None, alias='authority', description='Source authority or ownership context supporting this content.')
    idempotency_key: Union[Annotated[str, Field(min_length=8, max_length=160)], None] = Field(None, alias='idempotencyKey', description='Required only for apply or canary-capable verify; reuse for the exact same intent after an unknown result.')


AnalyticsSetupSiteOutputVariant1SetupReadinessDimensionsItem = TypedDict('AnalyticsSetupSiteOutputVariant1SetupReadinessDimensionsItem', {
    'dimension': Required[Literal['loader_coverage', 'route_coverage', 'pageview_integrity', 'semantic_action_coverage', 'terminal_outcome_coverage', 'destination_delivery', 'identity_value_coverage', 'data_sufficiency']],
    'state': Required[Literal['blocked', 'not_ready', 'partial', 'ready', 'not_required']],
    'numerator': Required[Annotated[Union[float, int], Field(ge=0)]],
    'denominator': Required[Annotated[Union[float, int], Field(ge=0)]],
    'readinessReason': Required[Literal['entitlement_required', 'connection_required', 'business_choice_required', 'surface_unreachable', 'adapter_unavailable', 'revision_stale', 'script_not_seen', 'duplicate_pageview', 'consent_blocked', 'only_pageview_seen', 'semantic_action_missing', 'definition_not_observed', 'terminal_outcome_missing', 'destination_not_connected', 'destination_delivery_failed', 'identity_value_missing', 'runtime_manifest_pending', 'events_processing', 'insufficient_data', 'ready']],
    'required': Required[bool],
})
AnalyticsSetupSiteOutputVariant1SetupReadinessDimensionsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsSetupSiteOutputVariant1SetupReadiness = TypedDict('AnalyticsSetupSiteOutputVariant1SetupReadiness', {
    'schemaVersion': Required[Literal[1]],
    'overallState': Required[Literal['blocked', 'not_ready', 'partial', 'ready']],
    'dimensions': Required[Annotated[list[AnalyticsSetupSiteOutputVariant1SetupReadinessDimensionsItem], Field(min_length=8, max_length=8)]],
})
AnalyticsSetupSiteOutputVariant1SetupReadiness.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsSetupSiteOutputVariant1Setup = TypedDict('AnalyticsSetupSiteOutputVariant1Setup', {
    'schemaVersion': Required[Literal[1]],
    'setupId': Required[str],
    'siteId': Required[str],
    'revision': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'status': Required[Literal['needs_business_choice', 'tag_required', 'prepared', 'publishing', 'awaiting_runtime_convergence', 'verifying', 'outcome_connection_required', 'collecting_data', 'answers_ready', 'partial', 'blocked']],
    'expiresAt': Required[str],
    'readiness': Required[AnalyticsSetupSiteOutputVariant1SetupReadiness],
})
AnalyticsSetupSiteOutputVariant1Setup.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsSetupSiteOutputVariant1BillingReceiptProviderCostsItem = TypedDict('AnalyticsSetupSiteOutputVariant1BillingReceiptProviderCostsItem', {
    'amountMinor': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'currency': NotRequired[str],
    'status': Required[Literal['none', 'estimated', 'incurred', 'unknown']],
})
AnalyticsSetupSiteOutputVariant1BillingReceiptProviderCostsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsSetupSiteOutputVariant1BillingReceipt = TypedDict('AnalyticsSetupSiteOutputVariant1BillingReceipt', {
    'billingClass': Required[Literal['xray_entitlement']],
    'mcpScraperCreditsCharged': Required[Literal[0]],
    'providerCosts': Required[Annotated[list[AnalyticsSetupSiteOutputVariant1BillingReceiptProviderCostsItem], Field(max_length=50)]],
})
AnalyticsSetupSiteOutputVariant1BillingReceipt.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsSetupSiteOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: Literal[True] = Field(..., alias='ok', description='')
    operation: Literal['facade'] = Field(..., alias='operation', description='')
    setup: AnalyticsSetupSiteOutputVariant1Setup = Field(..., alias='setup', description='')
    next_action: Annotated[str, Field(min_length=1, max_length=500)] = Field(..., alias='nextAction', description='Exactly one safe next user or system action based on the current durable state.')
    billing_receipt: AnalyticsSetupSiteOutputVariant1BillingReceipt = Field(..., alias='billingReceipt', description='')


AnalyticsSetupSiteOutputVariant2DeliveryArtifactsItem = TypedDict('AnalyticsSetupSiteOutputVariant2DeliveryArtifactsItem', {
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
AnalyticsSetupSiteOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsSetupSiteOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AnalyticsSetupSiteOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AnalyticsSetupSiteOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsSetupSiteOutputVariant2Delivery = TypedDict('AnalyticsSetupSiteOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AnalyticsSetupSiteOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AnalyticsSetupSiteOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AnalyticsSetupSiteOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsSetupSiteOutputVariant2RecoveryOperation = TypedDict('AnalyticsSetupSiteOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AnalyticsSetupSiteOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsSetupSiteOutputVariant2Recovery = TypedDict('AnalyticsSetupSiteOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AnalyticsSetupSiteOutputVariant2RecoveryOperation],
})
AnalyticsSetupSiteOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsSetupSiteOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AnalyticsSetupSiteOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AnalyticsSetupSiteOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AnalyticsSetupSiteOutput).
AnalyticsSetupSiteOutput = Union[AnalyticsSetupSiteOutputVariant1, AnalyticsSetupSiteOutputVariant2]

_AnalyticsSetupSiteInputAdapter = TypeAdapter(AnalyticsSetupSiteInput)
_AnalyticsSetupSiteOutputAdapter = TypeAdapter(AnalyticsSetupSiteOutput)