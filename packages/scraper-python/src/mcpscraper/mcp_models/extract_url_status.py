from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class ExtractUrlStatusInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    job_id: str = Field(..., alias="jobId", description="The jobId returned by extract_url. Polling never starts or bills another extraction.")


class ExtractUrlStatusOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    job_id: str | None = Field(None, alias="jobId", description="")
    status: Literal['pending', 'running', 'done', 'failed', 'cancelled'] | None = Field(None, alias="status", description="")
    status_tool: str | None = Field(None, alias="statusTool", description="")
    replayed: bool | None = Field(None, alias="replayed", description="")
    result: Any | None = Field(None, alias="result", description="")
    error: Any | None = Field(None, alias="error", description="")
    billing: dict[str, Any] | None = Field(None, alias="billing", description="")
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
