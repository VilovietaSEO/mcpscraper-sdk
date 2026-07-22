from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ReadServiceConnectionInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    connection_id: str = Field(..., alias="connectionId", description="A connectionId from list_service_connections.")
    tool: str = Field(..., alias="tool", description="One of that connection's readTools (from list_service_connections). An unlisted tool name is rejected with the allowed list.")
    args: dict[str, Any] | None = Field(None, alias="args", description="Arguments for the tool, if it needs any (e.g. a channel id, a date filter).")


class ReadServiceConnectionOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    result: Any | None = Field(None, alias="result", description="")
    error: Any = Field(..., alias="error", description="")
