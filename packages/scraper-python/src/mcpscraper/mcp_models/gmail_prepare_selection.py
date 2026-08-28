from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class GmailPrepareSelectionInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    connection_id: str = Field(..., alias="connectionId", description="A tenant-owned Gmail connectionId returned by list_service_connections.")
    purpose: Literal['export', 'mailbox_action', 'memory_import'] = Field(..., alias="purpose", description="The one public downstream workflow this immutable selection authorizes. Scheduled export is reserved for the signed internal Scheduler contract.")
    source: Any = Field(..., alias="source", description="Choose exactly one query or explicit-message-ID source; invalid mixed modes are rejected.")


class GmailPrepareSelectionOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    selection: dict[str, Any] | None = Field(None, alias="selection", description="")
    error: Any = Field(..., alias="error", description="")
