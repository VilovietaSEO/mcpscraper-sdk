from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CreateArtifactTemplateInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")


class CreateArtifactTemplateOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
