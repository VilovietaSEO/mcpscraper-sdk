from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class BrowserPressInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    session_id: str = Field(..., alias="session_id", description="The session id returned by browser_open or browser_list_sessions.")
    keys: list[str] = Field(..., alias="keys", description="Keys or combinations to press, e.g. [\"Return\"], [\"Ctrl+a\"], [\"Ctrl+Shift+Tab\"].")


class BrowserPressOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="Whether the browser-agent action succeeded.")
    tool: str | None = Field(None, alias="tool", description="Browser Agent MCP tool that produced this response.")
    session_id: Any | None = Field(None, alias="session_id", description="Browser session id when the response is scoped to a session.")
    result: dict[str, Any] | None = Field(None, alias="result", description="Provider action result. Check ok and follow with browser_screenshot/browser_read when page state matters.")
    next_recommended_tool: Any | None = Field(None, alias="nextRecommendedTool", description="")
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
