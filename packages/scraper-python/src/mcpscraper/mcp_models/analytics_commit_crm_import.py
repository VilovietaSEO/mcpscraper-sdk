from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsCommitCrmImportInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    source_system: Literal['hubspot', 'salesforce', 'gohighlevel', 'zoho', 'pipedrive', 'keap', 'other'] = Field(..., alias="sourceSystem", description="CRM system represented by the uploaded CSV.")
    filename: str = Field(..., alias="filename", description="Original CSV filename retained for the import receipt; this is not a local path.")
    csv: str = Field(..., alias="csv", description="Complete bounded CSV text to validate and stage; do not pass a local filesystem path.")
    mapping: dict[str, Any] = Field(..., alias="mapping", description="CSV-column mapping used to identify and protect supported CRM fields.")
    preview_fingerprint: str = Field(..., alias="previewFingerprint", description="Exact SHA-256 fingerprint returned by analytics_preview_crm_import.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Retry key; reuse only for this exact mutation.")


class AnalyticsCommitCrmImportOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    import_: dict[str, Any] = Field(..., alias="import", description="")
    receipt: dict[str, Any] = Field(..., alias="receipt", description="")
