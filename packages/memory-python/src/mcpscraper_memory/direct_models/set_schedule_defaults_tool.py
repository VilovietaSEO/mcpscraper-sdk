from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class SetScheduleDefaultsToolInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key (Bearer secret). Optional when the MCP session is already authenticated.")
    session_id: str | None = Field(None, alias="sessionId", description="Session identifier. Optional; defaults to the current MCP session.")
    default_timezone: Any = Field(..., alias="defaultTimezone", description="IANA timezone name, e.g. \"America/Denver\". null clears the default (new schedules fall back to UTC).")


class SetScheduleDefaultsToolOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    ok: bool = Field(..., alias="ok", description="")
    default_timezone: Any | None = Field(None, alias="defaultTimezone", description="The default timezone now in effect; null means UTC.")
    error: str | None = Field(None, alias="error", description="")
