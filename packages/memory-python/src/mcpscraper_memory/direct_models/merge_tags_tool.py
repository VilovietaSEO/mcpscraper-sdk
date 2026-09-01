from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class MergeTagsToolInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    api_key: str | None = Field(None, alias="apiKey", description="")
    session_id: str | None = Field(None, alias="sessionId", description="")
    from_: str = Field(..., alias="from", description="The duplicate tag to retire.")
    into: str = Field(..., alias="into", description="The canonical tag to keep. Every note using \"from\" is retagged to this.")


class MergeTagsToolOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    ok: bool = Field(..., alias="ok", description="")
    from_: str | None = Field(None, alias="from", description="")
    into: str | None = Field(None, alias="into", description="")
    notes_retagged: float | None = Field(None, alias="notesRetagged", description="")
    aliases: list[str] | None = Field(None, alias="aliases", description="")
    description_copied: bool | None = Field(None, alias="descriptionCopied", description="")
    error: str | None = Field(None, alias="error", description="")
