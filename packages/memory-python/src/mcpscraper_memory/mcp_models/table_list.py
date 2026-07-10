from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class TableListInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")


class TableListOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True on success; false on auth error.")
    tables: list[str] | None = Field(None, alias="tables", description="Table names owned by the caller. Present when ok is true; may be empty.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
