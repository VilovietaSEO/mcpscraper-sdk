from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class RecordFactInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key (Bearer secret). Optional when the MCP session is already authenticated; the server resolves auth from the session.")
    session_id: str | None = Field(None, alias="sessionId", description="Session identifier used to resolve the active vault and per-session state. Optional; defaults to the current MCP session.")
    vault: str | None = Field(None, alias="vault", description="Vault to record the fact in. Optional; defaults to the session active vault, then the first vault the caller is entitled to.")
    subject: str = Field(..., alias="subject", description="The thing the fact is about (e.g. \"db preference\"). Canonicalized (lowercased/trimmed) to a stable key.")
    value: str = Field(..., alias="value", description="The current asserted value or conclusion for the subject (e.g. \"Postgres\").")
    source: str | None = Field(None, alias="source", description="Where the fact came from: user / tool / chat / library:… . Optional; drives the source-priority precedence policy.")
    confidence: float | None = Field(None, alias="confidence", description="Salience/confidence in 0..1 on write. Optional; defaults to 0.5.")
    reason: str | None = Field(None, alias="reason", description="Why this assertion replaces the previous one — the audit reason recorded on the superseded fact. Optional; a default is used.")


class RecordFactOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True when the fact was recorded (whether or not it superseded one); false on auth/scope/validation error.")
    fact: dict[str, Any] | None = Field(None, alias="fact", description="The new (or refreshed) active fact. Present when ok is true.")
    superseded: dict[str, Any] | None = Field(None, alias="superseded", description="The previously-active fact that this one replaced, with its resolution/precedence. Absent on an idempotent no-op or first assertion.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
