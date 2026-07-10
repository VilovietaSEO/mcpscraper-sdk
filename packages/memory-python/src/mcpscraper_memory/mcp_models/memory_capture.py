from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class MemoryCaptureInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    vault: str = Field(..., alias="vault", description="")
    folder: str | None = Field(None, alias="folder", description="")
    path: str = Field(..., alias="path", description="")
    title: str = Field(..., alias="title", description="")
    content: str = Field(..., alias="content", description="")
    props: dict[str, Any] = Field(..., alias="props", description="")
    base_revision: float | None = Field(None, alias="baseRevision", description="")
    tag_decisions: list[dict[str, Any]] | None = Field(None, alias="tagDecisions", description="Required justification for any tag that does not already exist. Existing exact/alias/near tags are canonicalized automatically; a new tag is accepted only when its matching decision has central=true and reusable=true.")


class MemoryCaptureOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    valid: bool | None = Field(None, alias="valid", description="")
    errors: list[str] | None = Field(None, alias="errors", description="")
    warnings: list[str] | None = Field(None, alias="warnings", description="")
    tag_resolutions: list[dict[str, Any]] | None = Field(None, alias="tagResolutions", description="")
    note: dict[str, Any] | None = Field(None, alias="note", description="")
    indexed: float | None = Field(None, alias="indexed", description="")
    verified: dict[str, Any] | None = Field(None, alias="verified", description="")
    conflict: bool | None = Field(None, alias="conflict", description="")
    code: str | None = Field(None, alias="code", description="")
    error: str | None = Field(None, alias="error", description="")
