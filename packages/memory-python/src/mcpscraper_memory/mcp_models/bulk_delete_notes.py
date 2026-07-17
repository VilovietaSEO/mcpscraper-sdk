from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class BulkDeleteNotesInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    vault: str | None = Field(None, alias="vault", description="Vault to delete from. Optional; defaults to the session active vault, then the first vault the caller is entitled to.")
    filters: list[dict[str, Any]] | None = Field(None, alias="filters", description="Filters to AND together. At least one of filters/tags is required.")
    tags: list[str] | None = Field(None, alias="tags", description="Match notes carrying ANY of these tags (ORed among themselves, ANDed with filters). At least one of filters/tags is required.")
    dry_run: bool | None = Field(None, alias="dryRun", description="When true (default), previews matches without deleting anything. Pass false to actually delete.")


class BulkDeleteNotesOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True on success; false on auth/scope/validation error.")
    vault: str | None = Field(None, alias="vault", description="The vault operated on (after defaulting). Present when ok is true.")
    dry_run: bool | None = Field(None, alias="dryRun", description="Echoes whether this call was a preview or a real delete.")
    match_count: float | None = Field(None, alias="matchCount", description="Number of notes matching the filters. Present on a dry run.")
    sample: list[dict[str, Any]] | None = Field(None, alias="sample", description="Up to 20 matching notes, most-recently-updated first. Present on a dry run.")
    deleted: float | None = Field(None, alias="deleted", description="Number of notes actually deleted. Present when dryRun is false.")
    deleted_paths: list[str] | None = Field(None, alias="deletedPaths", description="Paths of the deleted notes. Present when dryRun is false.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
