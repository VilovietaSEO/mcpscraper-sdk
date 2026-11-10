from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class WorkflowListInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    include_recipes: bool | None = Field(None, alias="includeRecipes", description="Include high-level AI-facing recipes (market analysis, ICP research, CRO audits, content gaps, etc).")


class WorkflowListOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    workflows: list[dict[str, Any]] | None = Field(None, alias="workflows", description="")
    recipes: list[dict[str, Any]] | None = Field(None, alias="recipes", description="")
    delivery: dict[str, Any] | None = Field(None, alias="delivery", description="")
    preview: str | None = Field(None, alias="preview", description="")
    scope: dict[str, Any] | None = Field(None, alias="scope", description="")
    recovery: dict[str, Any] | None = Field(None, alias="recovery", description="")

    @model_serializer(mode="wrap")
    def _serialize_response(self, handler, info):
        data = handler(self)
        for name, field in type(self).model_fields.items():
            if name not in self.model_fields_set:
                key = field.alias if info.by_alias and field.alias else name
                data.pop(key, None)
        return data
