from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ExportConnectedServiceDataInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    connection_id: str = Field(..., alias="connectionId", description="A tenant-owned connectionId from list_service_connections.")
    dataset: Literal["auto", "emails", "calendar_events", "zoom_recordings", "zoom_transcripts", "resend_data", "resend_emails", "resend_received_emails", "resend_logs", "resend_contacts", "resend_broadcasts", "resend_templates"] | None = Field(None, alias="dataset", description="Dataset to export. auto maps Gmail to emails, Google Calendar to calendar_events, Zoom to zoom_transcripts, and Resend to resend_data. The Resend aggregate walks 12 practical safe collections; six core collections are also individually selectable.")
    last_days: int | None = Field(None, alias="lastDays", description="Relative range ending at to (or now). Defaults to 7 when from is omitted. Do not pass together with from.")
    from_: str | None = Field(None, alias="from", description="Inclusive RFC3339 range start. Use instead of lastDays.")
    to: str | None = Field(None, alias="to", description="Exclusive RFC3339 range end. Defaults to now.")
    max_items: int | None = Field(None, alias="maxItems", description="Maximum records to include in this export invocation. Pagination and detail retrieval happen server-side.")
    delivery: Literal["auto", "artifact"] | None = Field(None, alias="delivery", description="auto returns small results inline and stores larger results in private Blob. artifact always creates a private downloadable JSONL artifact.")
    continuation: dict[str, Any] | None = Field(None, alias="continuation", description="Preferred resume input. Pass the entire continuation object returned by a prior partial export unchanged; it preserves the exact original range and dataset.")
    cursor: str | None = Field(None, alias="cursor", description="Legacy resume input. When used, also pass the exact original from, to, and dataset. Prefer continuation.")


class ExportConnectedServiceDataOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    export_id: str | None = Field(None, alias="exportId", description="")
    status: Literal["complete", "partial"] | None = Field(None, alias="status", description="")
    provider_config_key: str | None = Field(None, alias="providerConfigKey", description="")
    dataset: Literal["emails", "calendar_events", "zoom_recordings", "zoom_transcripts", "resend_data", "resend_emails", "resend_received_emails", "resend_logs", "resend_contacts", "resend_broadcasts", "resend_templates"] | None = Field(None, alias="dataset", description="")
    range: dict[str, Any] | None = Field(None, alias="range", description="")
    counts: dict[str, Any] | None = Field(None, alias="counts", description="")
    complete: bool | None = Field(None, alias="complete", description="")
    records: list[Any] | None = Field(None, alias="records", description="")
    preview: list[Any] | None = Field(None, alias="preview", description="")
    artifact: dict[str, Any] | None = Field(None, alias="artifact", description="")
    continuation: Any | None = Field(None, alias="continuation", description="")
    warnings: list[str] | None = Field(None, alias="warnings", description="")
    untrusted_content: bool | None = Field(None, alias="untrustedContent", description="")
    error: Any = Field(..., alias="error", description="")
