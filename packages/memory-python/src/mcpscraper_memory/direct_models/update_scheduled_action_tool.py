from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class UpdateScheduledActionToolInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key (Bearer secret). Optional when the MCP session is already authenticated.")
    session_id: str | None = Field(None, alias="sessionId", description="Session identifier. Optional; defaults to the current MCP session.")
    id: str = Field(..., alias="id", description="The scheduled action id, from create-scheduled-action or list-scheduled-actions.")
    description: str | None = Field(None, alias="description", description="New free-text description of what this action should do each time it runs. Omit to keep the current one.")
    vault: str | None = Field(None, alias="vault", description="New vault this action writes its results into. You must already have write access to it. Omit to keep the current one.")
    cadence: Literal['once', 'daily', 'weekly', 'monthly'] | None = Field(None, alias="cadence", description="New cadence. Changing it recomputes the next run time fresh from now. Omit to keep the current one.")
    time_of_day: Any | None = Field(None, alias="timeOfDay", description="New 24-hour HH:MM clock time to run at, in the action's timezone. Pass null to clear it so the action runs at any time during the period. Omit to keep the current one.")
    timezone: str | None = Field(None, alias="timezone", description="New IANA timezone name, e.g. \"America/Denver\". Omit to keep the current one.")
    artifact_selection: Any | None = Field(None, alias="artifactSelection", description="Rich report selection. Use {mode:\"none\"} for no rendered artifact, or pin one saved template with {mode:\"saved_template\",templateId,templateVersionId}. This does not disable Memory-note or vault output. Omit to keep the current binding.")


class UpdateScheduledActionToolOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    ok: bool = Field(..., alias="ok", description="True when the scheduled action was updated.")
    action: dict[str, Any] | None = Field(None, alias="action", description="The updated scheduled action.")
    next_run_at: str | None = Field(None, alias="nextRunAt", description="When it will next run after this update.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
    code: str | None = Field(None, alias="code", description="Machine-readable denial code when the update is refused.")
