from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class TableCreateInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key (Bearer secret). Optional when the MCP session is already authenticated; the server resolves auth from the session.")
    session_id: str | None = Field(None, alias="sessionId", description="Session identifier. Optional; defaults to the current MCP session.")
    table_name: str = Field(..., alias="tableName", description="Table name: lowercase letters, numbers, underscores, starting with a letter (e.g. rank_tracker).")
    columns: list[dict[str, Any]] = Field(..., alias="columns", description="Columns to create, in addition to the automatic id/created_at/updated_at.")


class TableCreateOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True on success; false on auth/scope/validation error.")
    table_name: str | None = Field(None, alias="tableName", description="The table name.")
    created: bool | None = Field(None, alias="created", description="True if the table was newly created; false if it already existed.")
    columns: list[dict[str, Any]] | None = Field(None, alias="columns", description="The columns requested (existing tables are not altered to match).")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
