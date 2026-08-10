from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class MemoryListInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    vault: str | None = Field(None, alias="vault", description="Vault to list. Optional; defaults to the session active vault, then the first vault the caller is entitled to.")
    all_vaults: bool | None = Field(None, alias="allVaults", description="Set true for one complete account-wide inventory across every entitled vault. Omit or set false for one vault. When true, vault is ignored and reads run sequentially to avoid backend contention.")
    kind: Literal['note', 'library', 'capture', 'decision'] | None = Field(None, alias="kind", description="Filter to a single note kind. Optional; omit to list every kind in the vault.")
    tags: list[str] | None = Field(None, alias="tags", description="Filter to notes tagged with any of these tags (matches the note's tags primitive). Optional; omit to not filter by tag.")


class MemoryListOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True when the listing succeeded; false on an auth/scope/lookup error.")
    scope: Literal['vault', 'account'] | None = Field(None, alias="scope", description="Whether the result covers one logical vault or the whole entitled account.")
    partial: bool | None = Field(None, alias="partial", description="Account-wide mode only: true if one vault failed and vaultInventories contains only the completed prefix.")
    vault: str | None = Field(None, alias="vault", description="The vault that was actually listed (after defaulting).")
    notes: list[dict[str, Any]] | None = Field(None, alias="notes", description="The notes in the vault (metadata only, no content). Present when ok is true.")
    folders: list[str] | None = Field(None, alias="folders", description="Sorted complete folder inventory derived from note paths, including represented nested parent folders. Present when ok is true.")
    vaults: list[str] | None = Field(None, alias="vaults", description="All vaults the caller is entitled to, for choosing a different vault to list.")
    total_notes: int | None = Field(None, alias="totalNotes", description="Account-wide mode only: total notes across every completed vault inventory.")
    total_folders: int | None = Field(None, alias="totalFolders", description="Account-wide mode only: total represented folder instances across vaults.")
    vault_inventories: list[dict[str, Any]] | None = Field(None, alias="vaultInventories", description="Account-wide mode only: complete note and folder inventories grouped by vault so paths remain unambiguous.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
