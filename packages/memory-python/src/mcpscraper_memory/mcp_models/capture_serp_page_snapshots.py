from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class CaptureSerpPageSnapshotsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    urls: list[str] | None = Field(None, alias="urls", description="Public HTTP/HTTPS URLs to capture. Provide exactly one of urls or targets. Do not pass localhost, private IPs, file URLs, or internal admin URLs.")
    targets: list[dict[str, Any]] | None = Field(None, alias="targets", description="Structured targets. Provide exactly one of targets or urls; use targets when source kind or position should be preserved.")
    max_concurrency: int | None = Field(None, alias="maxConcurrency", description="Parallel page captures.")
    timeout_ms: int | None = Field(None, alias="timeoutMs", description="Per-page capture timeout in milliseconds; timeouts return as structured capture failures.")


class CaptureSerpPageSnapshotsOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    schema_version: str | None = Field(None, alias="schemaVersion", description="")
    status: str | None = Field(None, alias="status", description="")
    count: int | None = Field(None, alias="count", description="")
    captured_count: int | None = Field(None, alias="capturedCount", description="")
    failed_count: int | None = Field(None, alias="failedCount", description="")
    skipped_count: int | None = Field(None, alias="skippedCount", description="")
    captures: list[dict[str, Any]] | None = Field(None, alias="captures", description="")
    resolved_inputs: dict[str, Any] | None = Field(None, alias="resolvedInputs", description="")
    diagnostics: Any | None = Field(None, alias="diagnostics", description="")
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
