from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AccessRevokeShareInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    share_id: str = Field(..., alias="shareId", description="The shareId to revoke.")


class AccessRevokeShareOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True on success; false on auth/scope/lookup error.")
    share_id: str | None = Field(None, alias="shareId", description="The revoked share.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
