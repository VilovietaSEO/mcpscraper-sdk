from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CaptureSerpPageSnapshotsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    urls: list[str] | None = Field(None, alias="urls", description="Public HTTP/HTTPS URLs to capture. Provide exactly one of urls or targets. Do not pass localhost, private IPs, file URLs, or internal admin URLs.")
    targets: list[dict[str, Any]] | None = Field(None, alias="targets", description="Structured targets. Provide exactly one of targets or urls; use targets when source kind or position should be preserved.")
    max_concurrency: int | None = Field(None, alias="maxConcurrency", description="Parallel page captures.")
    timeout_ms: int | None = Field(None, alias="timeoutMs", description="Per-page capture timeout in milliseconds; timeouts return as structured capture failures.")
    debug: bool | None = Field(None, alias="debug", description="Include sanitized browser/proxy diagnostics.")


class CaptureSerpPageSnapshotsOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
