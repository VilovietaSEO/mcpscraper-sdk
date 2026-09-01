from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ResearchPersonGetInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    entity_id: str = Field(..., alias="entityId", description="Existing governed entity identifier for this relation or edit.")


class ResearchPersonGetOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    message: str = Field(..., alias="message", description="")
    record: dict[str, Any] | None = Field(None, alias="record", description="")
    aliases: list[str] | None = Field(None, alias="aliases", description="")
    associations: list[dict[str, Any]] | None = Field(None, alias="associations", description="")
    counterpart_entity_id: Any | None = Field(None, alias="counterpartEntityId", description="")
    code: str | None = Field(None, alias="code", description="")
    error: str | None = Field(None, alias="error", description="")
