from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class PrepareMemoryWriteInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="")
    session_id: str | None = Field(None, alias="sessionId", description="")
    title: str = Field(..., alias="title", description="")
    content: str = Field(..., alias="content", description="")
    source: str | None = Field(None, alias="source", description="")
    type: str | None = Field(None, alias="type", description="")
    vault: str | None = Field(None, alias="vault", description="")
    tag_candidates: list[dict[str, Any]] | None = Field(None, alias="tagCandidates", description="")
    max_links: int | None = Field(None, alias="maxLinks", description="")


class PrepareMemoryWriteOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    route: dict[str, Any] | None = Field(None, alias="route", description="")
    contract: dict[str, Any] | None = Field(None, alias="contract", description="")
    tag_resolutions: list[dict[str, Any]] | None = Field(None, alias="tagResolutions", description="")
    link_opportunities: list[dict[str, Any]] | None = Field(None, alias="linkOpportunities", description="")
    instructions: list[str] | None = Field(None, alias="instructions", description="")
    error: str | None = Field(None, alias="error", description="")
