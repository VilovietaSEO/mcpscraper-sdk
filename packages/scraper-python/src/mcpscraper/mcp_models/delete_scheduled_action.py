from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class DeleteScheduledActionInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id: str = Field(..., alias="id", description="The scheduled action id.")


class DeleteScheduledActionOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    deleted: bool | None = Field(None, alias="deleted", description="")
    error: str | None = Field(None, alias="error", description="")
