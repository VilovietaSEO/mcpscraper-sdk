from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class VideoAnalyzeStatusInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    run_id: str = Field(..., alias="runId", description="The runId returned by video-analyze-start.")


class VideoAnalyzeStatusOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="")
    status: str | None = Field(None, alias="status", description="")
    progress: dict[str, Any] | None = Field(None, alias="progress", description="")
    frame_count: float | None = Field(None, alias="frameCount", description="")
    max_frames: float | None = Field(None, alias="maxFrames", description="")
    cost_usd: float | None = Field(None, alias="costUsd", description="")
    artifact_path: str | None = Field(None, alias="artifactPath", description="")
    report: str | None = Field(None, alias="report", description="")
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
