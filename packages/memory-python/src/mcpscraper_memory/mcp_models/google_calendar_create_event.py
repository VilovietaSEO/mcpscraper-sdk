from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class GoogleCalendarCreateEventInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    connection_id: str = Field(..., alias="connectionId", description="A Google Calendar connectionId from list_service_connections, with actionsEnabled true.")
    calendar_id: str | None = Field(None, alias="calendarId", description="Calendar to create the event in. Default \"primary\".")
    summary: str = Field(..., alias="summary", description="Event title.")
    description: str | None = Field(None, alias="description", description="Event description.")
    location: str | None = Field(None, alias="location", description="Event location.")
    start_date_time: str = Field(..., alias="startDateTime", description="Start time, ISO 8601, e.g. \"2026-07-15T09:00:00-06:00\".")
    end_date_time: str = Field(..., alias="endDateTime", description="End time, ISO 8601, e.g. \"2026-07-15T10:00:00-06:00\".")
    time_zone: str | None = Field(None, alias="timeZone", description="IANA timezone, e.g. \"America/Denver\". Applies to both start and end.")


class GoogleCalendarCreateEventOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
