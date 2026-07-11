from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class SetScheduledActionConnectionsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    schedule_action_id: str = Field(..., alias="scheduleActionId", description="A scheduled action id returned by create-scheduled-action or list-scheduled-actions.")
    connections: list[dict[str, Any]] = Field(..., alias="connections", description="Exact connection and tool grants for this schedule. Pass an empty array to remove every external-service grant.")


class SetScheduledActionConnectionsOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
