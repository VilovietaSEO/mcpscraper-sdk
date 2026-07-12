from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ExportConnectedServiceDataInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    connection_id: str = Field(..., alias="connectionId", description="A tenant-owned connectionId from list_service_connections.")
    dataset: Literal["auto", "emails", "calendar_events", "zoom_recordings", "zoom_transcripts"] | None = Field(None, alias="dataset", description="Dataset to export. auto maps Gmail to emails, Google Calendar to calendar_events, and Zoom to zoom_transcripts.")
    last_days: int | None = Field(None, alias="lastDays", description="Relative range ending at to (or now). Defaults to 7 when from is omitted. Do not pass together with from.")
    from_: str | None = Field(None, alias="from", description="Inclusive RFC3339 range start. Use instead of lastDays.")
    to: str | None = Field(None, alias="to", description="Exclusive RFC3339 range end. Defaults to now.")
    max_items: int | None = Field(None, alias="maxItems", description="Maximum records to include in this export invocation. Pagination and detail retrieval happen server-side.")
    delivery: Literal["auto", "artifact"] | None = Field(None, alias="delivery", description="auto returns small results inline and stores larger results in private Blob. artifact always creates a private downloadable JSONL artifact.")
    continuation: dict[str, Any] | None = Field(None, alias="continuation", description="Preferred resume input. Pass the entire continuation object returned by a prior partial export unchanged; it preserves the exact original range and dataset.")
    cursor: str | None = Field(None, alias="cursor", description="Legacy resume input. When used, also pass the exact original from, to, and dataset. Prefer continuation.")


class ExportConnectedServiceDataOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
