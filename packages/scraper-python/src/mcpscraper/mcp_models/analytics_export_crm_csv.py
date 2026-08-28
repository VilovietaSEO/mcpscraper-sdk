from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsExportCrmCsvInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    fields: list[Literal['person_id', 'crm_person_ref', 'journey_url', 'first_seen_at', 'last_seen_at', 'signal_count', 'form_submission_count', 'conversion_count', 'revenue_minor', 'currency', 'stage', 'outcome', 'gclid', 'gbraid', 'wbraid', 'fbclid']] | None = Field(None, alias="fields", description="Ordered form-field definitions to render and validate for submissions.")
    acknowledged_purpose: Literal['business_operations', 'advertising_measurement'] | None = Field(None, alias="acknowledgedPurpose", description="Explicit governed purpose acknowledgement required for advertising identifiers or activation exports.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Retry key; reuse only for this exact mutation.")


class AnalyticsExportCrmCsvOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    artifact: dict[str, Any] = Field(..., alias="artifact", description="")
