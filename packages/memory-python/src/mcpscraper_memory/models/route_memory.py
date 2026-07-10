from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class RouteMemoryInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="")
    session_id: str | None = Field(None, alias="sessionId", description="")
    title: str = Field(..., alias="title", description="")
    content: str = Field(..., alias="content", description="")
    type: str | None = Field(None, alias="type", description="")
    source: str | None = Field(None, alias="source", description="")


class RouteMemoryOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    vault: str | None = Field(None, alias="vault", description="")
    folder: str | None = Field(None, alias="folder", description="")
    reason: str | None = Field(None, alias="reason", description="")
    contract: dict[str, Any] | None = Field(None, alias="contract", description="")
    error: str | None = Field(None, alias="error", description="")
