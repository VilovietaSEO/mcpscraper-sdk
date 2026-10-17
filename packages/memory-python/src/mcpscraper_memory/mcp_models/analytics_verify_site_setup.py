from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class AnalyticsVerifySiteSetupInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    site_id: str = Field(..., alias='siteId', description='Authorized Analytics Site id owning the setup.')
    setup_id: str = Field(..., alias='setupId', description='Durable owner-bound setup id returned by an X-Ray setup operation; it is not a browser session id.')
    revision: Annotated[int, Field(le=9007199254740991, gt=0)] = Field(..., alias='revision', description='Exact current setup revision. Reload stale revisions before any mutation or canary.')
    confirmed_canary: Union[Literal[True], None] = Field(None, alias='confirmedCanary', description='Omit for non-delivering interception. True separately authorizes only labeled, bounded canaries; it does not authorize merge or deploy.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=160)] = Field(..., alias='idempotencyKey', description='Retry key; reuse only for this exact mutation.')


AnalyticsVerifySiteSetupOutputVariant1SetupReadinessDimensionsItem = TypedDict('AnalyticsVerifySiteSetupOutputVariant1SetupReadinessDimensionsItem', {
    'dimension': Required[Literal['loader_coverage', 'route_coverage', 'pageview_integrity', 'semantic_action_coverage', 'terminal_outcome_coverage', 'destination_delivery', 'identity_value_coverage', 'data_sufficiency']],
    'state': Required[Literal['blocked', 'not_ready', 'partial', 'ready', 'not_required']],
    'numerator': Required[Annotated[Union[float, int], Field(ge=0)]],
    'denominator': Required[Annotated[Union[float, int], Field(ge=0)]],
    'readinessReason': Required[Literal['entitlement_required', 'connection_required', 'business_choice_required', 'surface_unreachable', 'adapter_unavailable', 'revision_stale', 'script_not_seen', 'duplicate_pageview', 'consent_blocked', 'only_pageview_seen', 'semantic_action_missing', 'definition_not_observed', 'terminal_outcome_missing', 'destination_not_connected', 'destination_delivery_failed', 'identity_value_missing', 'runtime_manifest_pending', 'events_processing', 'insufficient_data', 'ready']],
    'required': Required[bool],
})
AnalyticsVerifySiteSetupOutputVariant1SetupReadinessDimensionsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsVerifySiteSetupOutputVariant1SetupReadiness = TypedDict('AnalyticsVerifySiteSetupOutputVariant1SetupReadiness', {
    'schemaVersion': Required[Literal[1]],
    'overallState': Required[Literal['blocked', 'not_ready', 'partial', 'ready']],
    'dimensions': Required[Annotated[list[AnalyticsVerifySiteSetupOutputVariant1SetupReadinessDimensionsItem], Field(min_length=8, max_length=8)]],
})
AnalyticsVerifySiteSetupOutputVariant1SetupReadiness.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsVerifySiteSetupOutputVariant1Setup = TypedDict('AnalyticsVerifySiteSetupOutputVariant1Setup', {
    'schemaVersion': Required[Literal[1]],
    'setupId': Required[str],
    'siteId': Required[str],
    'revision': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'status': Required[Literal['needs_business_choice', 'tag_required', 'prepared', 'publishing', 'awaiting_runtime_convergence', 'verifying', 'outcome_connection_required', 'collecting_data', 'answers_ready', 'partial', 'blocked']],
    'expiresAt': Required[str],
    'readiness': Required[AnalyticsVerifySiteSetupOutputVariant1SetupReadiness],
})
AnalyticsVerifySiteSetupOutputVariant1Setup.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsVerifySiteSetupOutputVariant1BillingReceiptProviderCostsItem = TypedDict('AnalyticsVerifySiteSetupOutputVariant1BillingReceiptProviderCostsItem', {
    'amountMinor': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'currency': NotRequired[str],
    'status': Required[Literal['none', 'estimated', 'incurred', 'unknown']],
})
AnalyticsVerifySiteSetupOutputVariant1BillingReceiptProviderCostsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsVerifySiteSetupOutputVariant1BillingReceipt = TypedDict('AnalyticsVerifySiteSetupOutputVariant1BillingReceipt', {
    'billingClass': Required[Literal['xray_entitlement']],
    'mcpScraperCreditsCharged': Required[Literal[0]],
    'providerCosts': Required[Annotated[list[AnalyticsVerifySiteSetupOutputVariant1BillingReceiptProviderCostsItem], Field(max_length=50)]],
})
AnalyticsVerifySiteSetupOutputVariant1BillingReceipt.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsVerifySiteSetupOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: Literal[True] = Field(..., alias='ok', description='')
    operation: Literal['verify'] = Field(..., alias='operation', description='')
    setup: AnalyticsVerifySiteSetupOutputVariant1Setup = Field(..., alias='setup', description='')
    next_action: Annotated[str, Field(min_length=1, max_length=500)] = Field(..., alias='nextAction', description='Exactly one safe next user or system action based on the current durable state.')
    billing_receipt: AnalyticsVerifySiteSetupOutputVariant1BillingReceipt = Field(..., alias='billingReceipt', description='')


AnalyticsVerifySiteSetupOutputVariant2DeliveryArtifactsItem = TypedDict('AnalyticsVerifySiteSetupOutputVariant2DeliveryArtifactsItem', {
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
AnalyticsVerifySiteSetupOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsVerifySiteSetupOutputVariant2DeliveryAvailableExportsItem = TypedDict('AnalyticsVerifySiteSetupOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
AnalyticsVerifySiteSetupOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsVerifySiteSetupOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AnalyticsVerifySiteSetupOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AnalyticsVerifySiteSetupOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsVerifySiteSetupOutputVariant2Delivery = TypedDict('AnalyticsVerifySiteSetupOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AnalyticsVerifySiteSetupOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[AnalyticsVerifySiteSetupOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AnalyticsVerifySiteSetupOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AnalyticsVerifySiteSetupOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsVerifySiteSetupOutputVariant2RecoveryOperation = TypedDict('AnalyticsVerifySiteSetupOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AnalyticsVerifySiteSetupOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsVerifySiteSetupOutputVariant2Recovery = TypedDict('AnalyticsVerifySiteSetupOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AnalyticsVerifySiteSetupOutputVariant2RecoveryOperation],
})
AnalyticsVerifySiteSetupOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsVerifySiteSetupOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AnalyticsVerifySiteSetupOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AnalyticsVerifySiteSetupOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AnalyticsVerifySiteSetupOutput).
AnalyticsVerifySiteSetupOutput = Union[AnalyticsVerifySiteSetupOutputVariant1, AnalyticsVerifySiteSetupOutputVariant2]

_AnalyticsVerifySiteSetupInputAdapter = TypeAdapter(AnalyticsVerifySiteSetupInput)
_AnalyticsVerifySiteSetupOutputAdapter = TypeAdapter(AnalyticsVerifySiteSetupOutput)