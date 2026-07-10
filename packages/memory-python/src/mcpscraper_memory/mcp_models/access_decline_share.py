from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AccessDeclineShareInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    share_id: str = Field(..., alias="shareId", description="The shareId from note-inbox to decline.")


class AccessDeclineShareOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True on success; false on auth/scope/lookup error.")
    share_id: str | None = Field(None, alias="shareId", description="The declined share.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
