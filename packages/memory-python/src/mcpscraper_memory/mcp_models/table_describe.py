from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class TableDescribeInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    table_name: str = Field(..., alias="tableName", description="Table name, from table-list.")


class TableDescribeOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True on success; false on auth or not-found error.")
    table_name: str | None = Field(None, alias="tableName", description="The table name.")
    columns: list[dict[str, Any]] | None = Field(None, alias="columns", description="Column names and their Postgres types, in table order.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
