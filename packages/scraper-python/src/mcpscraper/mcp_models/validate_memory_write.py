from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ValidateMemoryWriteInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    vault: str = Field(..., alias="vault", description="Exact accessible Memory vault name; omit only when this tool documents a safe active-vault default.")
    title: str = Field(..., alias="title", description="Human-readable title for the proposed record or authored content.")
    content: str = Field(..., alias="content", description="Complete content to route, validate, or store; do not substitute a partial excerpt when full content is required.")
    props: dict[str, Any] = Field(..., alias="props", description="Complete governed note properties required by the target vault contract.")


class ValidateMemoryWriteOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    valid: bool | None = Field(None, alias="valid", description="")
    errors: list[str] | None = Field(None, alias="errors", description="")
    warnings: list[str] | None = Field(None, alias="warnings", description="")
    normalized_tags: list[str] | None = Field(None, alias="normalizedTags", description="")
    error: str | None = Field(None, alias="error", description="")
