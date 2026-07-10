from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class TableDropInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    table_name: str = Field(..., alias="tableName", description="Table name to permanently delete, from table-list.")


class TableDropOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True on success; false on auth/scope error.")
    dropped: bool | None = Field(None, alias="dropped", description="True if the table existed and was dropped; false if it did not exist.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
