from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CommonsGetEntityLinksetInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_or_slug: str = Field(..., alias="idOrSlug", description="Transparent Commons TPW-Q entity id or /wiki/ slug whose governed RFC 9264 linkset should be read.")


class CommonsGetEntityLinksetOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    data: Any | None = Field(None, alias="data", description="")
    error: str | None = Field(None, alias="error", description="")
    message: str | None = Field(None, alias="message", description="")
