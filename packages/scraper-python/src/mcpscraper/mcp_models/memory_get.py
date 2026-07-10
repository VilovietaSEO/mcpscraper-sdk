from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class MemoryGetInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    vault: str | None = Field(None, alias="vault", description="Vault to read from. Optional; defaults to the session active vault, then the first vault the caller is entitled to. Ignored when shareId is given.")
    path: str | None = Field(None, alias="path", description="Exact vault-relative note path to read, e.g. projects/q3-plan (as returned by memory-list or recall). Required unless shareId is given.")
    share_id: str | None = Field(None, alias="shareId", description="Read a note shared with you and accepted, by its shareId (from note-inbox or list-shared-with-me), instead of vault+path.")


class MemoryGetOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True when the note was found and returned; false on error or not-found.")
    note: dict[str, Any] | None = Field(None, alias="note", description="The full note. Present when ok is true.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false (e.g. \"note not found\").")
