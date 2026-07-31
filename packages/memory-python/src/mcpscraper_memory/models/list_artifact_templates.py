from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ListArtifactTemplatesInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="")
    session_id: str | None = Field(None, alias="sessionId", description="")
    status: Literal["active", "archived", "all"] | None = Field(None, alias="status", description="")


class ListArtifactTemplatesOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
