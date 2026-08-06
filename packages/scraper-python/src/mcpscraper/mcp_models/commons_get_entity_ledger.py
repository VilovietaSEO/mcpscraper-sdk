from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CommonsGetEntityLedgerInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_or_slug: str = Field(..., alias="idOrSlug", description="Published entity id or /wiki/ slug whose contribution ledger should be read.")


class CommonsGetEntityLedgerOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    data: Any | None = Field(None, alias="data", description="")
    error: str | None = Field(None, alias="error", description="")
    message: str | None = Field(None, alias="message", description="")
