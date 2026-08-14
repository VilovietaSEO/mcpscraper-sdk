from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ValidateLocalSourcebookWriteInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    identity: dict[str, Any] = Field(..., alias="identity", description="New-listing identity returned by prepare-local-sourcebook-write. Evidence-bearing public fields are compiled by MCP Scraper and cannot be supplied here.")
    tag_candidates: list[dict[str, Any]] | None = Field(None, alias="tagCandidates", description="Proposed listing or memory tags to resolve against the live canonical vocabulary.")
    tag_decisions: list[dict[str, Any]] | None = Field(None, alias="tagDecisions", description="Explicit reuse, creation, or omission decisions for proposed non-canonical tags.")


class ValidateLocalSourcebookWriteOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
