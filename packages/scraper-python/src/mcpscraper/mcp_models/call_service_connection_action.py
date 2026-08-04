from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CallServiceConnectionActionInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    confirmed: bool | None = Field(None, alias="confirmed", description="Set true only when the person explicitly authorized this exact external action. If omitted, a 2026-capable client may ask for confirmation through MCP multi-round input.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Required stable key for this intended external action. Reuse it only to retry the same action after a lost response; use a new key for a new action.")
    connection_id: str = Field(..., alias="connectionId", description="A connectionId from list_service_connections with actionsEnabled true.")
    tool: str = Field(..., alias="tool", description="One exact tool name from that connection's actionTools. Arbitrary provider action names and adminBlockedTools are rejected server-side.")
    args: dict[str, Any] = Field(..., alias="args", description="Arguments required by the selected action. The provider action validates its own typed input before execution.")


class CallServiceConnectionActionOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    result: Any | None = Field(None, alias="result", description="")
    error: Any = Field(..., alias="error", description="")
