from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ZoomCreateMeetingInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    connection_id: str = Field(..., alias="connectionId", description="A Zoom connectionId from list_service_connections, with actionsEnabled true.")
    topic: str = Field(..., alias="topic", description="Meeting topic/title.")
    start_date_time: str = Field(..., alias="startDateTime", description="Start time, ISO 8601, e.g. \"2026-07-15T09:00:00-06:00\".")
    duration_minutes: int | None = Field(None, alias="durationMinutes", description="Meeting duration in minutes. Default 30.")
    timezone: str | None = Field(None, alias="timezone", description="IANA timezone, e.g. \"America/Denver\".")
    agenda: str = Field(..., alias="agenda", description="Required meeting description or agenda. Preserve the purpose and context supplied by the user.")


class ZoomCreateMeetingOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    result: Any | None = Field(None, alias="result", description="")
    error: Any = Field(..., alias="error", description="")
