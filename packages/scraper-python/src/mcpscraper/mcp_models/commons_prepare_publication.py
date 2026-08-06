from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CommonsPreparePublicationInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    requested_subdomain: str = Field(..., alias="requestedSubdomain", description="Requested publication name under transparent-commons.cc. The server normalizes spaces to hyphens, rejects reserved names, and enforces one globally unique name per account.")
    title: str | None = Field(None, alias="title", description="Reader-facing publication title. Omit to derive it from the chosen subdomain.")
    description: str | None = Field(None, alias="description", description="Short description used on the publication archive and discovery surfaces.")


class CommonsPreparePublicationOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    data: Any | None = Field(None, alias="data", description="")
    error: str | None = Field(None, alias="error", description="")
    message: str | None = Field(None, alias="message", description="")
