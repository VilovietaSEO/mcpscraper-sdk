from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CrmWorkSearchInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")


class CrmWorkSearchOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    ok: bool = Field(..., alias="ok", description="")
    message: str = Field(..., alias="message", description="")
    items: list[dict[str, Any]] | None = Field(None, alias="items", description="")
    page_info: dict[str, Any] | None = Field(None, alias="pageInfo", description="")
    code: str | None = Field(None, alias="code", description="")
    error: str | None = Field(None, alias="error", description="")
