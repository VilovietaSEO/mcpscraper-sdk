from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class TableDeleteRowsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key (Bearer secret). Optional when the MCP session is already authenticated; the server resolves auth from the session.")
    session_id: str | None = Field(None, alias="sessionId", description="Session identifier. Optional; defaults to the current MCP session.")
    table_name: str = Field(..., alias="tableName", description="Table name, from table-list.")
    filters: list[dict[str, Any]] = Field(..., alias="filters", description="Filters to AND together; rows matching all of them are deleted.")


class TableDeleteRowsOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True on success; false on auth/scope/validation error.")
    deleted: float | None = Field(None, alias="deleted", description="Number of rows deleted.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
