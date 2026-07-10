from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class GetScheduleLinkInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")


class GetScheduleLinkOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True on success; false on auth error.")
    url: str | None = Field(None, alias="url", description="The schedule link. Present only the first time a link is minted for this identity.")
    already_exists: bool | None = Field(None, alias="alreadyExists", description="True when a link already exists and was NOT re-shown. Use revoke-schedule-link then call this again to get a fresh one.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
