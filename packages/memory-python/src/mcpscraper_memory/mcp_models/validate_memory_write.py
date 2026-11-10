from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class ValidateMemoryWriteInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    vault: str = Field(..., alias="vault", description="Exact accessible Memory vault name; omit only when this tool documents a safe active-vault default.")
    title: str = Field(..., alias="title", description="Human-readable title for the proposed record or authored content.")
    content: str = Field(..., alias="content", description="Complete content to route, validate, or store; do not substitute a partial excerpt when full content is required.")
    props: dict[str, Any] = Field(..., alias="props", description="Complete governed note properties required by the target vault contract.")


class ValidateMemoryWriteOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="")
    valid: bool | None = Field(None, alias="valid", description="")
    errors: list[str] | None = Field(None, alias="errors", description="")
    warnings: list[str] | None = Field(None, alias="warnings", description="")
    normalized_tags: list[str] | None = Field(None, alias="normalizedTags", description="")
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
