from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ImageProjectListInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    vault: str | None = Field(None, alias="vault", description="")


class ImageProjectListOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
