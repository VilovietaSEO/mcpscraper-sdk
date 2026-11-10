from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class GmailImportToMemoryInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    idempotency_key: str = Field(..., alias="idempotencyKey", description="Stable retry key bound to the immutable import plan; reuse resumes and conflicting input fails before a write.")
    import_plan_id: str = Field(..., alias="importPlanId", description="Reviewed, unexpired importPlanId returned by gmail_prepare_memory_import.")


class GmailImportToMemoryOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="")
    ingest: dict[str, Any] | None = Field(None, alias="ingest", description="")
    error: Any | None = Field(None, alias="error", description="")
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
