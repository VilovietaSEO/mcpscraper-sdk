from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class QueryFanoutWorkflowInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    session_id: str = Field(..., alias="session_id", description="Session id from browser_open. Must be on chatgpt.com or claude.ai, logged in via a saved hosted profile.")
    prompt: str | None = Field(None, alias="prompt", description="Optional prompt to type and submit before capturing. Omit to passively capture a prompt the user just ran. Must trigger web search to produce a fan-out.")
    wait_ms: int | None = Field(None, alias="wait_ms", description="How long to wait for the answer stream to finish. Defaults to 90000 when a prompt is sent, 8000 for passive capture.")
    first_party_domain: str | None = Field(None, alias="first_party_domain", description="The brand/site being researched, e.g. example.com — sources on this domain are tagged First-party/vendor.")
    reset: bool | None = Field(None, alias="reset", description="Clear any previously buffered stream for this page before capturing.")
    export: bool | None = Field(None, alias="export", description="When using the installed local MCP server, write JSON/CSV/TSV/HTML exports to MCP_SCRAPER_OUTPUT_DIR/fanout. Hosted clients such as ChatGPT always receive the complete structured result inline and leave exports null.")


class QueryFanoutWorkflowOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="Whether the browser-agent action succeeded.")
    tool: str | None = Field(None, alias="tool", description="")
    session_id: Any | None = Field(None, alias="session_id", description="Browser session id when the response is scoped to a session.")
    platform: Literal['ChatGPT', 'Claude'] | None = Field(None, alias="platform", description="Which AI-search surface the fan-out was captured from.")
    captured_at: str | None = Field(None, alias="captured_at", description="")
    prompt: str | None = Field(None, alias="prompt", description="The user prompt that triggered the captured fan-out, when recoverable.")
    meta: dict[str, Any] | None = Field(None, alias="meta", description="")
    queries: list[str] | None = Field(None, alias="queries", description="Every web-search sub-query issued, in capture order.")
    browsed_urls: list[dict[str, Any]] | None = Field(None, alias="browsed_urls", description="Every researched URL, cited first.")
    cited_urls: list[dict[str, Any]] | None = Field(None, alias="cited_urls", description="Researched URLs cited in the final answer.")
    browsed_only: list[dict[str, Any]] | None = Field(None, alias="browsed_only", description="Researched URLs pulled but not cited.")
    snippets: list[dict[str, Any]] | None = Field(None, alias="snippets", description="")
    counts: dict[str, Any] | None = Field(None, alias="counts", description="")
    aggregates: dict[str, Any] | None = Field(None, alias="aggregates", description="Objective aggregates: top sourced sites by frequency, citation order, and URL-category counts.")
    first_party_domain: Any | None = Field(None, alias="first_party_domain", description="")
    export_error: Any | None = Field(None, alias="export_error", description="Non-fatal local export failure. The inline capture remains complete when this is present.")
    exports: Any | None = Field(None, alias="exports", description="Local-only export paths when export=true, otherwise null. Hosted clients receive the complete structured result inline instead of inaccessible server paths.")
    debug: dict[str, Any] | None = Field(None, alias="debug", description="")
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
