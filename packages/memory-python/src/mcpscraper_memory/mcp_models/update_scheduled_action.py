from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class UpdateScheduledActionInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id: str = Field(..., alias="id", description="The scheduled action id.")
    description: str | None = Field(None, alias="description", description="")
    vault: str | None = Field(None, alias="vault", description="")
    cadence: Literal['once', 'daily', 'weekly', 'monthly'] | None = Field(None, alias="cadence", description="")
    time_of_day: Any | None = Field(None, alias="timeOfDay", description="")
    timezone: str | None = Field(None, alias="timezone", description="")
    artifact_selection: Any | None = Field(None, alias="artifactSelection", description="")


class UpdateScheduledActionOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    artifact_selection: Any | None = Field(None, alias="artifactSelection", description="")
    error: str | None = Field(None, alias="error", description="")
    error_code: str | None = Field(None, alias="errorCode", description="")
