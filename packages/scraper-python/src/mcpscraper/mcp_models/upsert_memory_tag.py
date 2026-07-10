from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class UpsertMemoryTagInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    tag: str = Field(..., alias="tag", description="")
    description: str | None = Field(None, alias="description", description="")
    aliases: list[str] | None = Field(None, alias="aliases", description="")
    status: Literal["active", "deprecated"] | None = Field(None, alias="status", description="")


class UpsertMemoryTagOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    tag: dict[str, Any] | None = Field(None, alias="tag", description="")
    error: str | None = Field(None, alias="error", description="")
