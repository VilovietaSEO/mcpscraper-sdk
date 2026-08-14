from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class RouteMemoryInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    title: str = Field(..., alias="title", description="Human-readable title for the proposed record or authored content.")
    content: str = Field(..., alias="content", description="Complete content to route, validate, or store; do not substitute a partial excerpt when full content is required.")
    type: str | None = Field(None, alias="type", description="Governed content or record type used for routing and validation.")
    source: str | None = Field(None, alias="source", description="Optional source or provenance constraint appropriate to this tool; omit when no source restriction is intended.")


class RouteMemoryOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    vault: str | None = Field(None, alias="vault", description="")
    folder: str | None = Field(None, alias="folder", description="")
    reason: str | None = Field(None, alias="reason", description="")
    contract: dict[str, Any] | None = Field(None, alias="contract", description="")
    error: str | None = Field(None, alias="error", description="")
