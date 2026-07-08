from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class TableQueryInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key (Bearer secret). Optional when the MCP session is already authenticated; the server resolves auth from the session.")
    session_id: str | None = Field(None, alias="sessionId", description="Session identifier. Optional; defaults to the current MCP session.")
    table_name: str = Field(..., alias="tableName", description="Table name, from table-list.")
    filters: list[dict[str, Any]] | None = Field(None, alias="filters", description="Filters to AND together. Optional; omit to match every row.")
    sort: dict[str, Any] | None = Field(None, alias="sort", description="Column to sort by. Optional; defaults to id ascending (insertion order).")
    limit: int | None = Field(None, alias="limit", description="Max rows to return. Optional; default 100, max 2000.")
    offset: int | None = Field(None, alias="offset", description="Rows to skip, for pagination. Optional; default 0.")


class TableQueryOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True on success; false on auth/validation error.")
    table_name: str | None = Field(None, alias="tableName", description="The table name.")
    rows: list[dict[str, Any]] | None = Field(None, alias="rows", description="Matching rows, each an object of column name to value.")
    count: float | None = Field(None, alias="count", description="Total rows matching the filters, before limit/offset — use for pagination.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
