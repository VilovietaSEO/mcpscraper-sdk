from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class MemoryUploadInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    vault: str | None = Field(None, alias="vault", description="Vault to upload into. Optional; defaults to the session active vault, then the first vault the caller is entitled to.")
    path: str = Field(..., alias="path", description="Vault-relative path to store the document at, e.g. docs/handbook. Writing an existing path replaces it.")
    content: str = Field(..., alias="content", description="Full text content of the file/document to store and index. Must be non-empty.")
    title: str | None = Field(None, alias="title", description="Optional human-readable title; defaults to the path when omitted.")
    source: str | None = Field(None, alias="source", description="Optional origin tag recorded with the note (e.g. a filename or URL); defaults to \"upload\".")


class MemoryUploadOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True when the document was stored and indexed; false on auth/scope error.")
    path: str | None = Field(None, alias="path", description="Vault-relative path the document was stored at.")
    indexed: float | None = Field(None, alias="indexed", description="Number of search chunks indexed for the content.")
    code: str | None = Field(None, alias="code", description="Machine-readable denial code when ok is false: quota_exceeded or free_cost_cap.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
