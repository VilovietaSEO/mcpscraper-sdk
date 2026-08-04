from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ValidateLocalSourcebookWriteInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    identity: dict[str, Any] | None = Field(None, alias="identity", description="New-listing identity returned by prepare-local-sourcebook-write.")
    listing: dict[str, Any] | None = Field(None, alias="listing", description="Complete replacement listing draft for an existing owner-scoped submission.")
    submission_id: str | None = Field(None, alias="submissionId", description="Existing owner-scoped submission being revised. Omit for a new capture.")
    base_revision: int | None = Field(None, alias="baseRevision", description="Required current draft revision for an edit, preventing silent overwrites.")
    tag_candidates: list[dict[str, Any]] | None = Field(None, alias="tagCandidates", description="")
    tag_decisions: list[dict[str, Any]] | None = Field(None, alias="tagDecisions", description="")


class ValidateLocalSourcebookWriteOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
