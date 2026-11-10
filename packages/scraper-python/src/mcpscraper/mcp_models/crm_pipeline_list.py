from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CrmPipelineListInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")


class CrmPipelineListOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
