from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsUpsertCrmOutboundPolicyInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    provider: Literal['hubspot', 'salesforce', 'highlevel', 'zoho', 'pipedrive', 'keap'] = Field(..., alias="provider", description="Supported CRM provider.")
    connection_id: str = Field(..., alias="connectionId", description="Verified service connection reference.")
    kind: Literal['person_summary', 'pipeline_event'] = Field(..., alias="kind", description="Person summaries never create deals; pipeline events require an explicit versioned mapping.")
    enabled: bool = Field(..., alias="enabled", description="Policies are disabled by default and must be explicitly enabled after provisioning and consent checks.")
    version: int = Field(..., alias="version", description="Immutable policy version used for replay and conflict protection.")
    provisioning_receipt_id: str = Field(..., alias="provisioningReceiptId", description="Tested provisioning receipt authorizing the selected fields.")
    schema_fingerprint: str = Field(..., alias="schemaFingerprint", description="Tenant schema fingerprint bound to the provisioning receipt.")
    mapping_version: Any = Field(..., alias="mappingVersion", description="Pipeline mapping version, or null for a person-summary policy.")
    mapping: Any = Field(..., alias="mapping", description="Explicit pipeline mapping, or null for a person-summary policy.")
    allowed_fields: list[Literal['contact.email', 'contact.phone', 'contact.firstName', 'contact.lastName', 'attribution.firstTouch', 'attribution.lastNonDirectTouch', 'attribution.convertingTouch', 'attribution.landingPage', 'attribution.conversionPage', 'clickIds.gclid', 'clickIds.gbraid', 'clickIds.wbraid', 'events.selected', 'revenue.verified']] = Field(..., alias="allowedFields", description="Purpose-scoped CRM projection allowlist; raw device, IP, candidate evidence, and unrestricted journeys are unavailable.")
    selected_events: list[str] = Field(..., alias="selectedEvents", description="Canonical events eligible for this policy.")
    purpose: Literal['necessary_form_fulfillment', 'site_analytics', 'advertising_measurement'] = Field(..., alias="purpose", description="Declared processing purpose; this cannot grant visitor consent.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Caller-owned idempotency key. Reuse it only when retrying the same logical mutation.")


class AnalyticsUpsertCrmOutboundPolicyOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    policy: dict[str, Any] = Field(..., alias="policy", description="")
