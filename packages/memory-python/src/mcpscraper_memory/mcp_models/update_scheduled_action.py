from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class UpdateScheduledActionInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id: str = Field(..., alias="id", description="The scheduled action id.")
    description: str | None = Field(None, alias="description", description="Human-readable summary that distinguishes this record from similarly named records.")
    vault: str | None = Field(None, alias="vault", description="Exact accessible Memory vault name; omit only when this tool documents a safe active-vault default.")
    cadence: Literal['once', 'daily', 'weekly', 'monthly'] | None = Field(None, alias="cadence", description="New execution cadence; omit to preserve the scheduled action cadence.")
    time_of_day: Any | None = Field(None, alias="timeOfDay", description="Local execution time in 24-hour HH:MM form; null clears the stored time.")
    timezone: str | None = Field(None, alias="timezone", description="IANA timezone for schedule evaluation; omit to preserve the current timezone.")
    artifact_selection: Any | None = Field(None, alias="artifactSelection", description="Explicit HTML artifact choice; omit to preserve the current selection.")


class UpdateScheduledActionOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    artifact_selection: Any | None = Field(None, alias="artifactSelection", description="")
    error: str | None = Field(None, alias="error", description="")
    error_code: str | None = Field(None, alias="errorCode", description="")
