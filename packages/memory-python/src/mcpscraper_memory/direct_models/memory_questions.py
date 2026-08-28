from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class MemoryQuestionsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key (Bearer secret). Optional when the MCP session is already authenticated; the server resolves auth from the session.")
    session_id: str | None = Field(None, alias="sessionId", description="Session identifier used to resolve the active vault and per-session state. Optional; defaults to the current MCP session.")
    vault: str | None = Field(None, alias="vault", description="Vault to capture into. Optional; defaults to the session active vault, then the first vault the caller is entitled to.")
    answers: list[dict[str, Any]] | None = Field(None, alias="answers", description="Up to 5 question/answer pairs to ingest. Omit (or empty) to instead RECEIVE the day questions.")


class MemoryQuestionsOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True when questions were returned or answers were ingested; false on auth/scope error.")
    questions: list[str] | None = Field(None, alias="questions", description="The day capture questions. Present only when called with no answers.")
    ingested: float | None = Field(None, alias="ingested", description="Number of answers stored as captures. Present only when answers were supplied.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
