from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class SetScheduleDefaultsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    default_timezone: Any = Field(..., alias="defaultTimezone", description="IANA timezone name, e.g. \"America/Denver\". null clears the default (new schedules fall back to UTC).")


class SetScheduleDefaultsOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    default_timezone: Any | None = Field(None, alias="defaultTimezone", description="The default timezone now in effect; null means UTC.")
    error: str | None = Field(None, alias="error", description="")
