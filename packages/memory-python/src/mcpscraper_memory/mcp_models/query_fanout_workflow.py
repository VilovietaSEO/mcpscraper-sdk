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
