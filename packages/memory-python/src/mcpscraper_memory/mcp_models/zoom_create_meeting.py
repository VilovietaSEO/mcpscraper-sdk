from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class ZoomCreateMeetingInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    confirmed: bool | None = Field(None, alias="confirmed", description="Set true only when the person explicitly authorized creating this exact meeting. If omitted, a 2026-capable client may ask for confirmation.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Required stable key for this intended meeting. Reuse it only when retrying the same creation after a lost response.")
    connection_id: str = Field(..., alias="connectionId", description="A Zoom connectionId from list_service_connections, with actionsEnabled true.")
    topic: str = Field(..., alias="topic", description="Meeting topic/title.")
    start_date_time: str = Field(..., alias="startDateTime", description="Start time, ISO 8601, e.g. \"2026-07-15T09:00:00-06:00\".")
    duration_minutes: int | None = Field(None, alias="durationMinutes", description="Meeting duration in minutes. Default 30.")
    timezone: str | None = Field(None, alias="timezone", description="IANA timezone, e.g. \"America/Denver\".")
    agenda: str = Field(..., alias="agenda", description="Required meeting description or agenda. Preserve the purpose and context supplied by the user.")


class ZoomCreateMeetingOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="")
    result: Any | None = Field(None, alias="result", description="")
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
