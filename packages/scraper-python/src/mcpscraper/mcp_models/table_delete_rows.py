from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class TableDeleteRowsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    table_name: str = Field(..., alias="tableName", description="Table name, from table-list.")
    filters: list[dict[str, Any]] = Field(..., alias="filters", description="Filters to AND together; rows matching all of them are deleted.")


class TableDeleteRowsOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True on success; false on auth/scope/validation error.")
    deleted: float | None = Field(None, alias="deleted", description="Number of rows deleted.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
