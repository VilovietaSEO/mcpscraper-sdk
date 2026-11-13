from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


AnalyticsRecordExternalEventInputClickIds = TypedDict('AnalyticsRecordExternalEventInputClickIds', {
    'gclid': NotRequired[Annotated[str, Field(max_length=500)]],
    'gbraid': NotRequired[Annotated[str, Field(max_length=500)]],
    'wbraid': NotRequired[Annotated[str, Field(max_length=500)]],
    'fbclid': NotRequired[Annotated[str, Field(max_length=500)]],
    'fbp': NotRequired[Annotated[str, Field(max_length=500)]],
    'fbc': NotRequired[Annotated[str, Field(max_length=500)]],
    'ttclid': NotRequired[Annotated[str, Field(max_length=500)]],
    'rdt_cid': NotRequired[Annotated[str, Field(max_length=500)]],
    'msclkid': NotRequired[Annotated[str, Field(max_length=500)]],
    'li_fat_id': NotRequired[Annotated[str, Field(max_length=500)]],
    'snapclid': NotRequired[Annotated[str, Field(max_length=500)]],
})
AnalyticsRecordExternalEventInputClickIds.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class AnalyticsRecordExternalEventInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    site_id: str = Field(..., alias='siteId', description='Analytics Site id returned by analytics_list_sites.')
    schema_version: Union[Literal[1], None] = Field(None, alias='schemaVersion', description='Canonical X-Ray event schema version; use version 1.')
    event_id: Annotated[str, Field(min_length=8, max_length=200)] = Field(..., alias='eventId', description='Caller-owned canonical event identifier used for end-to-end deduplication.')
    source: Annotated[str, Field(min_length=1, max_length=80)] = Field(..., alias='source', description='Required source-system name for the event being recorded; this is provenance, not a report filter.')
    source_account_ref: Annotated[str, Field(min_length=1, max_length=240)] = Field(..., alias='sourceAccountRef', description='Stable non-secret account identifier at the phone, CRM, or event source.')
    source_event_id: Annotated[str, Field(min_length=1, max_length=300)] = Field(..., alias='sourceEventId', description='Stable identifier assigned by the source system for idempotent ingestion.')
    event_kind: Literal['browser', 'form', 'call', 'crm', 'transaction', 'custom_server', 'conversion', 'delivery'] = Field(..., alias='eventKind', description='Canonical event family used for journey storage and conversion-rule evaluation.')
    event_name: str = Field(..., alias='eventName', description='Required canonical name for the event being recorded; use lowercase letters, digits, and underscores starting with a letter.')
    occurred_at: str = Field(..., alias='occurredAt', description='ISO 8601 timestamp when the source event actually occurred.')
    visitor_id: Union[Annotated[str, Field(max_length=160)], None] = Field(None, alias='visitorId', description='Consented first-party visitor identifier used for deterministic journey linking.')
    session_id: Union[Annotated[str, Field(max_length=160)], None] = Field(None, alias='sessionId', description='First-party session identifier used for deterministic journey linking.')
    call_id: Union[Annotated[str, Field(max_length=240)], None] = Field(None, alias='callId', description='Stable call identifier assigned by the phone provider.')
    deal_id: Union[Annotated[str, Field(max_length=240)], None] = Field(None, alias='dealId', description='Stable CRM deal or opportunity identifier.')
    order_id: Union[Annotated[str, Field(max_length=240)], None] = Field(None, alias='orderId', description='Stable order identifier used for conversion deduplication and reconciliation.')
    person_ref: Union[Annotated[str, Field(max_length=240)], None] = Field(None, alias='personRef', description='Opaque source-system person reference; do not place raw contact data here.')
    path: Union[Annotated[str, Field(max_length=2000)], None] = Field(None, alias='path', description='Exact path value used by this tool; preserve its leading slash or vault-relative form as required.')
    canonical_url: Union[Annotated[str, Field(max_length=3000)], None] = Field(None, alias='canonicalUrl', description='Canonical public page URL associated with the event.')
    source_name: Union[Annotated[str, Field(max_length=180)], None] = Field(None, alias='sourceName', description='Normalized acquisition-source name associated with the event.')
    medium: Union[Annotated[str, Field(max_length=180)], None] = Field(None, alias='medium', description='Exact normalized campaign medium used to filter or label analytics data.')
    campaign: Union[Annotated[str, Field(max_length=240)], None] = Field(None, alias='campaign', description='Exact normalized campaign value used to filter or label analytics data.')
    value_minor: Union[Annotated[int, Field(ge=0, le=2147483647)], None] = Field(None, alias='valueMinor', description='Monetary event value in the smallest unit of the supplied currency.')
    currency: Union[Annotated[str, Field(min_length=3, max_length=3)], None] = Field(None, alias='currency', description='Three-letter ISO currency code for the event value.')
    click_ids: Union[AnalyticsRecordExternalEventInputClickIds, None] = Field(None, alias='clickIds', description='Native advertising click identifiers preserved for deterministic offline conversion matching.')
    properties: Union[dict[str, Any], None] = Field(None, alias='properties', description='Bounded non-secret event properties used for reporting and declarative rule evaluation.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=160)] = Field(..., alias='idempotencyKey', description='Retry key; reuse only for this exact mutation.')


class AnalyticsRecordExternalEventOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    id: Union[str, None] = Field(..., alias='id', description='')
    created: bool = Field(..., alias='created', description='')
    person_id: Union[str, None] = Field(..., alias='personId', description='')
    identity_tier: Literal['confirmed', 'unlinked'] = Field(..., alias='identityTier', description='')
    namespace_id: Union[str, None] = Field(..., alias='namespaceId', description='')
    conversion_ids: Annotated[list[str], Field(max_length=500)] = Field(..., alias='conversionIds', description='')
    consent_eligibility: dict[str, Any] = Field(..., alias='consentEligibility', description='')
    value_provenance: dict[str, dict[str, Any]] = Field(..., alias='valueProvenance', description='')
    score_evaluation_ids: Annotated[list[Annotated[str, Field(min_length=1, max_length=240)]], Field(max_length=500)] = Field(..., alias='scoreEvaluationIds', description='')
    prediction_evidence: Any = Field(..., alias='predictionEvidence', description='')
    candidate_promotion: Union[dict[str, Any], None] = Field(..., alias='candidatePromotion', description='')


AnalyticsRecordExternalEventOutputVariant2DeliveryArtifactsItem = TypedDict('AnalyticsRecordExternalEventOutputVariant2DeliveryArtifactsItem', {
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
AnalyticsRecordExternalEventOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsRecordExternalEventOutputVariant2DeliveryAvailableExportsItem = TypedDict('AnalyticsRecordExternalEventOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
AnalyticsRecordExternalEventOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsRecordExternalEventOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AnalyticsRecordExternalEventOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AnalyticsRecordExternalEventOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsRecordExternalEventOutputVariant2Delivery = TypedDict('AnalyticsRecordExternalEventOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AnalyticsRecordExternalEventOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[AnalyticsRecordExternalEventOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AnalyticsRecordExternalEventOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AnalyticsRecordExternalEventOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsRecordExternalEventOutputVariant2RecoveryOperation = TypedDict('AnalyticsRecordExternalEventOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AnalyticsRecordExternalEventOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsRecordExternalEventOutputVariant2Recovery = TypedDict('AnalyticsRecordExternalEventOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AnalyticsRecordExternalEventOutputVariant2RecoveryOperation],
})
AnalyticsRecordExternalEventOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsRecordExternalEventOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AnalyticsRecordExternalEventOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AnalyticsRecordExternalEventOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AnalyticsRecordExternalEventOutput).
AnalyticsRecordExternalEventOutput = Union[AnalyticsRecordExternalEventOutputVariant1, AnalyticsRecordExternalEventOutputVariant2]

_AnalyticsRecordExternalEventInputAdapter = TypeAdapter(AnalyticsRecordExternalEventInput)
_AnalyticsRecordExternalEventOutputAdapter = TypeAdapter(AnalyticsRecordExternalEventOutput)