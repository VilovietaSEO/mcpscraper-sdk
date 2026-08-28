from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ValidateMemoryWriteInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="")
    session_id: str | None = Field(None, alias="sessionId", description="")
    vault: str = Field(..., alias="vault", description="")
    title: str = Field(..., alias="title", description="")
    content: str = Field(..., alias="content", description="")
    props: dict[str, Any] = Field(..., alias="props", description="")


class ValidateMemoryWriteOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    valid: bool | None = Field(None, alias="valid", description="")
    errors: list[str] | None = Field(None, alias="errors", description="")
    warnings: list[str] | None = Field(None, alias="warnings", description="")
    normalized_tags: list[str] | None = Field(None, alias="normalizedTags", description="")
    error: str | None = Field(None, alias="error", description="")
