from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class TableInsertRowsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key (Bearer secret). Optional when the MCP session is already authenticated; the server resolves auth from the session.")
    session_id: str | None = Field(None, alias="sessionId", description="Session identifier. Optional; defaults to the current MCP session.")
    table_name: str = Field(..., alias="tableName", description="Table name, from table-list.")
    rows: list[dict[str, Any]] = Field(..., alias="rows", description="Rows to insert, each an object of column name to value.")


class TableInsertRowsOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True on success; false on auth/scope/validation error.")
    inserted: float | None = Field(None, alias="inserted", description="Number of rows inserted.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
