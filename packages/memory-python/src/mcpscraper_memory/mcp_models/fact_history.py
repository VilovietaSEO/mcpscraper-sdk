from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class FactHistoryInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    vault: str | None = Field(None, alias="vault", description="Vault to read from. Optional; defaults to the session active vault, then the first vault the caller is entitled to.")
    subject: str = Field(..., alias="subject", description="The subject whose history to read (e.g. \"db preference\"). Canonicalized to match how it was recorded.")


class FactHistoryOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True when the history was read; false on an auth/scope error.")
    current: Any | None = Field(None, alias="current", description="The current active fact for the subject, or null if none exists. Present when ok is true.")
    history: list[Any] | None = Field(None, alias="history", description="The superseded chain newest → oldest — the audit trail. Empty when nothing has been superseded. Present when ok is true.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
