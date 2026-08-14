from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class UpsertMemoryTagInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    tag: str = Field(..., alias="tag", description="Canonical tag name to create or curate.")
    description: str | None = Field(None, alias="description", description="Human-readable summary that distinguishes this record from similarly named records.")
    aliases: list[str] | None = Field(None, alias="aliases", description="Alternative spellings that should resolve to this canonical value.")
    status: Literal['active', 'deprecated'] | None = Field(None, alias="status", description="Lifecycle status used to filter or update the selected records.")


class UpsertMemoryTagOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    tag: dict[str, Any] | None = Field(None, alias="tag", description="")
    error: str | None = Field(None, alias="error", description="")
