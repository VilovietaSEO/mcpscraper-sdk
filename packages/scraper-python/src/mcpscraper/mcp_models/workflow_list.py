from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class WorkflowListInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    include_recipes: bool | None = Field(None, alias="includeRecipes", description="Include high-level AI-facing recipes (market analysis, ICP research, CRO audits, content gaps, etc).")


class WorkflowListOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
