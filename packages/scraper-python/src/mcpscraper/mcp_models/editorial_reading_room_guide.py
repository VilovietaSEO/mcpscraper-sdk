from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class EditorialReadingRoomGuideInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    focus: Literal['workflow', 'content_contract', 'example'] | None = Field(None, alias="focus", description="Which part of the reusable editorial-reading-room guide to return. Start with workflow; fetch the content contract or compact example only when needed.")


class EditorialReadingRoomGuideOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="")
    focus: Literal['workflow', 'content_contract', 'example'] | None = Field(None, alias="focus", description="")
    guide: str | None = Field(None, alias="guide", description="")
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
