from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AccessInboxSettingsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    allow_unapproved_senders: bool = Field(..., alias="allowUnapprovedSenders", description="Set true to accept invites/shares from anyone; false to require approval.")


class AccessInboxSettingsOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True on success; false on auth error.")
    allow_unapproved_senders: bool | None = Field(None, alias="allowUnapprovedSenders", description="The setting now in effect.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
