from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AddVaultInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    vault: str = Field(..., alias="vault", description="Name of the vault to create. Must match ^[A-Za-z0-9 _-]{1,48}$ (letters, digits, space, _ or -, 1-48 chars).")
    owner: str | None = Field(None, alias="owner", description="Identity that should OWN the new vault (becomes the owner entitlement, so list-vaults reports role \"owner\" for them). Optional; defaults to the caller. Used when an admin bootstraps a personal vault on a user's behalf so the user owns it rather than receiving it as a share.")


class AddVaultOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True when the request succeeded (whether or not a new vault was created); false on auth/scope/validation error.")
    vault: str | None = Field(None, alias="vault", description="The vault name. Present when ok is true.")
    created: bool | None = Field(None, alias="created", description="True if a new vault was created; false if it already existed (idempotent no-op). Present when ok is true.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
