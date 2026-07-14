from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class QueryFanoutWorkflowInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    session_id: str = Field(..., alias="session_id", description="Session id from browser_open. Must be on chatgpt.com or claude.ai, logged in via a saved hosted profile.")
    prompt: str | None = Field(None, alias="prompt", description="Optional prompt to type and submit before capturing. Omit to passively capture a prompt the user just ran. Must trigger web search to produce a fan-out.")
    wait_ms: int | None = Field(None, alias="wait_ms", description="How long to wait for the answer stream to finish. Defaults to 90000 when a prompt is sent, 8000 for passive capture.")
    first_party_domain: str | None = Field(None, alias="first_party_domain", description="The brand/site being researched, e.g. example.com — sources on this domain are tagged First-party/vendor.")
    reset: bool | None = Field(None, alias="reset", description="Clear any previously buffered stream for this page before capturing.")
    export: bool | None = Field(None, alias="export", description="Write JSON/CSV/TSV/HTML exports to MCP_SCRAPER_OUTPUT_DIR/fanout, returning relative paths.")


class QueryFanoutWorkflowOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="Whether the browser-agent action succeeded.")
    tool: str = Field(..., alias="tool", description="")
    session_id: Any = Field(..., alias="session_id", description="Browser session id when the response is scoped to a session.")
    platform: Literal["ChatGPT", "Claude"] = Field(..., alias="platform", description="Which AI-search surface the fan-out was captured from.")
    captured_at: str = Field(..., alias="captured_at", description="")
    prompt: str = Field(..., alias="prompt", description="The user prompt that triggered the captured fan-out, when recoverable.")
    meta: dict[str, Any] = Field(..., alias="meta", description="")
    queries: list[str] = Field(..., alias="queries", description="Every web-search sub-query issued, in capture order.")
    browsed_urls: list[dict[str, Any]] = Field(..., alias="browsed_urls", description="Every researched URL, cited first.")
    cited_urls: list[Any] = Field(..., alias="cited_urls", description="Researched URLs cited in the final answer.")
    browsed_only: list[Any] = Field(..., alias="browsed_only", description="Researched URLs pulled but not cited.")
    snippets: list[dict[str, Any]] = Field(..., alias="snippets", description="")
    counts: dict[str, Any] = Field(..., alias="counts", description="")
    aggregates: dict[str, Any] = Field(..., alias="aggregates", description="Objective aggregates: top sourced sites by frequency, citation order, and URL-category counts.")
    first_party_domain: Any = Field(..., alias="first_party_domain", description="")
    exports: Any = Field(..., alias="exports", description="Relative export paths when export=true, otherwise null. Paths are relative to MCP_SCRAPER_OUTPUT_DIR, or ~/Downloads/mcp-scraper when that env var is not set.")
    debug: dict[str, Any] | None = Field(None, alias="debug", description="")
