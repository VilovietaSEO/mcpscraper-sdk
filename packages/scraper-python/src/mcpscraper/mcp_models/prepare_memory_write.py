from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class PrepareMemoryWriteInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    title: str = Field(..., alias="title", description="Human-readable title for the proposed record or authored content.")
    content: str = Field(..., alias="content", description="Complete content to route, validate, or store; do not substitute a partial excerpt when full content is required.")
    source: str | None = Field(None, alias="source", description="Optional source or provenance constraint appropriate to this tool; omit when no source restriction is intended.")
    type: str | None = Field(None, alias="type", description="Governed content or record type used for routing and validation.")
    vault: str | None = Field(None, alias="vault", description="Exact accessible Memory vault name; omit only when this tool documents a safe active-vault default.")
    tag_candidates: list[dict[str, Any]] | None = Field(None, alias="tagCandidates", description="Proposed listing or memory tags to resolve against the live canonical vocabulary.")
    max_links: int | None = Field(None, alias="maxLinks", description="Maximum related-note candidates to return from the planning pass.")


class PrepareMemoryWriteOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    route: dict[str, Any] | None = Field(None, alias="route", description="")
    contract: dict[str, Any] | None = Field(None, alias="contract", description="")
    tag_resolutions: list[dict[str, Any]] | None = Field(None, alias="tagResolutions", description="")
    link_opportunities: list[dict[str, Any]] | None = Field(None, alias="linkOpportunities", description="")
    instructions: list[str] | None = Field(None, alias="instructions", description="")
    error: str | None = Field(None, alias="error", description="")
