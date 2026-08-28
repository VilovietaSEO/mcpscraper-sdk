from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class GmailImportStatusInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ingest_id: str = Field(..., alias="ingestId", description="Owner-scoped ingestId returned by gmail_import_to_memory; this status call never continues work.")


class GmailImportStatusOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    ingest: dict[str, Any] | None = Field(None, alias="ingest", description="")
    error: Any = Field(..., alias="error", description="")
