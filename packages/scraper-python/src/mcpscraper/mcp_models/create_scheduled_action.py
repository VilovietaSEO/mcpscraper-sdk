from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CreateScheduledActionInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    description: str = Field(..., alias="description", description="Free-text description of what this action should do each time it runs.")
    vault: str = Field(..., alias="vault", description="The vault this action writes its results into. You must already have write access to it.")
    cadence: Literal["once", "daily", "weekly", "monthly"] = Field(..., alias="cadence", description="How often this action runs. \"once\" fires a single time and then completes.")
    execution_mode: Literal["agent", "connection_sync"] | None = Field(None, alias="executionMode", description="How to execute each run. \"agent\" (default) lets an agent follow the description. \"connection_sync\" deterministically ingests data from the schedule's bound connections using only their approved read-only tools; bind at least one connection before it runs.")
    time_of_day: str | None = Field(None, alias="timeOfDay", description="24-hour HH:MM clock time to run at, in the given timezone. Optional — omit to run at any time during the period (matches prior default behavior).")
    timezone: str | None = Field(None, alias="timezone", description="IANA timezone name, e.g. \"America/Denver\". Only meaningful together with timeOfDay. Defaults to UTC.")
    deploy_date: str | None = Field(None, alias="deployDate", description="Calendar date (YYYY-MM-DD, in the given timezone) this action should first become eligible to run — its deployment/start date. For recurring cadences, the first occurrence lands on or after this date; every later occurrence still follows the normal cadence. For cadence \"once\", this (combined with timeOfDay if given) is exactly what day it fires. Omit to start immediately.")


class CreateScheduledActionOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True when the scheduled action was created.")
    id: str | None = Field(None, alias="id", description="The new scheduled action id.")
    next_run_at: str | None = Field(None, alias="nextRunAt", description="When it will first run.")
    execution_mode: Literal["agent", "connection_sync"] | None = Field(None, alias="executionMode", description="The stored execution mode. Defaults to agent when omitted from the request.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
    code: str | None = Field(None, alias="code", description="Machine-readable denial code when creation is refused.")
