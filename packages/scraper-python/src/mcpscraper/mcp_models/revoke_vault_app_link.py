from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class RevokeVaultAppLinkInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")


class RevokeVaultAppLinkOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True when the request succeeded.")
    revoked: bool | None = Field(None, alias="revoked", description="True when an active Vault App link was revoked.")
    error: str | None = Field(None, alias="error", description="Human-readable error when the request cannot be completed.")
