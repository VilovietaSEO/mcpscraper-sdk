from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class HarvestPaaStatusInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    job_id: str = Field(..., alias="jobId", description="The jobId returned by harvest_paa_start.")


class HarvestPaaStatusOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    job_id: str | None = Field(None, alias="jobId", description="")
    operation_id: str | None = Field(None, alias="operationId", description="")
    task_id: str | None = Field(None, alias="taskId", description="")
    status: Any | None = Field(None, alias="status", description="")
    execution: dict[str, Any] | None = Field(None, alias="execution", description="")
    replayed: bool | None = Field(None, alias="replayed", description="")
    progress: dict[str, Any] | None = Field(None, alias="progress", description="")
    result: Any | None = Field(None, alias="result", description="")
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
