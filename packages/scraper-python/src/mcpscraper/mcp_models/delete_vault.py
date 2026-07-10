from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class DeleteVaultInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    vault: str = Field(..., alias="vault", description="Exact name of the vault to delete. The caller must own this vault and hold admin scope on it.")


class DeleteVaultOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True when the vault was deleted; false on auth/scope/ownership error.")
    vault: str | None = Field(None, alias="vault", description="The deleted vault name. Present when ok is true.")
    deleted_notes: float | None = Field(None, alias="deletedNotes", description="Number of notes removed from the vault. Present when ok is true.")
    deleted_facts: float | None = Field(None, alias="deletedFacts", description="Number of facts (active + superseded) removed from the vault. Present when ok is true.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
