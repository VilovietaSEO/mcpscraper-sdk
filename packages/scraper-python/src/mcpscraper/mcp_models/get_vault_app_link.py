from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class GetVaultAppLinkInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")


class GetVaultAppLinkOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True when the request succeeded.")
    url: str | None = Field(None, alias="url", description="Vault App link. Present only when the secret is first minted; anyone holding it can use the Vault App as this identity.")
    already_exists: bool | None = Field(None, alias="alreadyExists", description="True when an active Vault App link exists but its secret cannot be shown again.")
    error: str | None = Field(None, alias="error", description="Human-readable error when the request cannot be completed.")
