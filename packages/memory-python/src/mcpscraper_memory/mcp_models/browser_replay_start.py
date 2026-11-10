from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class BrowserReplayStartInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    session_id: str = Field(..., alias="session_id", description="The session id returned by browser_open or browser_list_sessions.")


class BrowserReplayStartOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="Whether the browser-agent action succeeded.")
    tool: str | None = Field(None, alias="tool", description="")
    session_id: Any | None = Field(None, alias="session_id", description="Browser session id when the response is scoped to a session.")
    replay_id: Any | None = Field(None, alias="replay_id", description="Replay id when the response is scoped to a replay.")
    view_url: Any | None = Field(None, alias="view_url", description="")
    download_url: Any | None = Field(None, alias="download_url", description="")
    raw: dict[str, Any] | None = Field(None, alias="raw", description="")
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
