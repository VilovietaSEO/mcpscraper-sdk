from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class RouteMemoryInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    title: str = Field(..., alias="title", description="Human-readable title for the proposed record or authored content.")
    content: str = Field(..., alias="content", description="Complete content to route, validate, or store; do not substitute a partial excerpt when full content is required.")
    type: str | None = Field(None, alias="type", description="Governed content or record type used for routing and validation.")
    source: str | None = Field(None, alias="source", description="Optional source or provenance constraint appropriate to this tool; omit when no source restriction is intended.")


class RouteMemoryOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="")
    vault: str | None = Field(None, alias="vault", description="")
    folder: str | None = Field(None, alias="folder", description="")
    reason: str | None = Field(None, alias="reason", description="")
    contract: dict[str, Any] | None = Field(None, alias="contract", description="")
    error: str | None = Field(None, alias="error", description="")
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
