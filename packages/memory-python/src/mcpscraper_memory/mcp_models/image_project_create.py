from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ImageProjectCreateInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    vault: str | None = Field(None, alias="vault", description="Writable logical Memory vault. Defaults to the active vault.")
    name: str = Field(..., alias="name", description="")
    description: str | None = Field(None, alias="description", description="")


class ImageProjectCreateOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
