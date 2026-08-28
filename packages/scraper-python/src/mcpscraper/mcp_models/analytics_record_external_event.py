from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsRecordExternalEventInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    schema_version: float | None = Field(None, alias="schemaVersion", description="Canonical X-Ray event schema version; use version 1.")
    event_id: str = Field(..., alias="eventId", description="Caller-owned canonical event identifier used for end-to-end deduplication.")
    source: str = Field(..., alias="source", description="Optional source or provenance constraint appropriate to this tool; omit when no source restriction is intended.")
    source_account_ref: str = Field(..., alias="sourceAccountRef", description="Stable non-secret account identifier at the phone, CRM, or event source.")
    source_event_id: str = Field(..., alias="sourceEventId", description="Stable identifier assigned by the source system for idempotent ingestion.")
    event_kind: Literal['browser', 'form', 'call', 'crm', 'transaction', 'custom_server', 'conversion', 'delivery'] = Field(..., alias="eventKind", description="Canonical event family used for journey storage and conversion-rule evaluation.")
    event_name: str = Field(..., alias="eventName", description="Optional normalized analytics event-name filter.")
    occurred_at: str = Field(..., alias="occurredAt", description="ISO 8601 timestamp when the source event actually occurred.")
    visitor_id: str | None = Field(None, alias="visitorId", description="Consented first-party visitor identifier used for deterministic journey linking.")
    session_id: str | None = Field(None, alias="sessionId", description="First-party session identifier used for deterministic journey linking.")
    call_id: str | None = Field(None, alias="callId", description="Stable call identifier assigned by the phone provider.")
    deal_id: str | None = Field(None, alias="dealId", description="Stable CRM deal or opportunity identifier.")
    order_id: str | None = Field(None, alias="orderId", description="Stable order identifier used for conversion deduplication and reconciliation.")
    person_ref: str | None = Field(None, alias="personRef", description="Opaque source-system person reference; do not place raw contact data here.")
    path: str | None = Field(None, alias="path", description="Exact path value used by this tool; preserve its leading slash or vault-relative form as required.")
    canonical_url: str | None = Field(None, alias="canonicalUrl", description="Canonical public page URL associated with the event.")
    source_name: str | None = Field(None, alias="sourceName", description="Normalized acquisition-source name associated with the event.")
    medium: str | None = Field(None, alias="medium", description="Exact normalized campaign medium used to filter or label analytics data.")
    campaign: str | None = Field(None, alias="campaign", description="Exact normalized campaign value used to filter or label analytics data.")
    value_minor: int | None = Field(None, alias="valueMinor", description="Monetary event value in the smallest unit of the supplied currency.")
    currency: str | None = Field(None, alias="currency", description="Three-letter ISO currency code for the event value.")
    click_ids: dict[str, Any] | None = Field(None, alias="clickIds", description="Native advertising click identifiers preserved for deterministic offline conversion matching.")
    properties: dict[str, Any] | None = Field(None, alias="properties", description="Bounded non-secret event properties used for reporting and declarative rule evaluation.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Retry key; reuse only for this exact mutation.")


class AnalyticsRecordExternalEventOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    id: Any = Field(..., alias="id", description="")
    created: bool = Field(..., alias="created", description="")
    person_id: Any = Field(..., alias="personId", description="")
    identity_tier: Literal['confirmed', 'unlinked'] = Field(..., alias="identityTier", description="")
    namespace_id: Any = Field(..., alias="namespaceId", description="")
    conversion_ids: list[str] = Field(..., alias="conversionIds", description="")
    consent_eligibility: dict[str, Any] = Field(..., alias="consentEligibility", description="")
    value_provenance: dict[str, Any] = Field(..., alias="valueProvenance", description="")
    score_evaluation_ids: list[str] = Field(..., alias="scoreEvaluationIds", description="")
    prediction_evidence: Any = Field(..., alias="predictionEvidence", description="")
    candidate_promotion: Any = Field(..., alias="candidatePromotion", description="")
