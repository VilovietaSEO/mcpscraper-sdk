from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ListScheduledRunsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="")
    session_id: str | None = Field(None, alias="sessionId", description="")
    view: Literal["inbox", "all", "archived"] | None = Field(None, alias="view", description="")
    status: Literal["running", "succeeded", "no_output", "partial", "billing_stopped", "failed"] | None = Field(None, alias="status", description="")
    schedule_id: str | None = Field(None, alias="scheduleId", description="")
    template_id: str | None = Field(None, alias="templateId", description="")
    from_: str | None = Field(None, alias="from", description="")
    to: str | None = Field(None, alias="to", description="")
    query: str | None = Field(None, alias="query", description="")
    cursor: str | None = Field(None, alias="cursor", description="")
    limit: int | None = Field(None, alias="limit", description="")


class ListScheduledRunsOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
