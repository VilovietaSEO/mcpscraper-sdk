from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ResearchPersonSearchInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    query: str | None = Field(None, alias="query", description="Text filter applied to the selected result inventory.")
    topic: str | None = Field(None, alias="topic", description="Research topic used to filter sourced records.")
    role: str | None = Field(None, alias="role", description="Optional sourced Research role to match on knowledge subjects; this is not a CRM relationship type.")
    cursor: str | None = Field(None, alias="cursor", description="Opaque continuation cursor returned by the previous page; omit for the first page.")
    limit: int | None = Field(None, alias="limit", description="Maximum rows or records to return on this page; use the returned cursor for more.")


class ResearchPersonSearchOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
