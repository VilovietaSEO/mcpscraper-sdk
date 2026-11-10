from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class GetVaultContractInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    vault: str = Field(..., alias="vault", description="One governed vault: Ideas, Examples and Inspirations, Knowledge, Library, People, Organizations, Deals, Communication, Calendar, Tasks, Projects, Issues, Improvement Log, Experiments, Sprint, or Skills. Former names Inspiration and Communications still resolve.")


class GetVaultContractOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="")
    vault: str | None = Field(None, alias="vault", description="")
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
