from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyzeSiteSimilarityInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    url: str = Field(..., alias="url", description="Public live site to render and compare. Bare domains default to https://.")
    max_pages: int | None = Field(None, alias="maxPages", description="Maximum rendered pages to compare; default 100, maximum 500.")
    similarity_threshold: float | None = Field(None, alias="similarityThreshold", description="Minimum raw cosine score retained in the pair table; default 0.90.")
    similarity_max_pairs: int | None = Field(None, alias="similarityMaxPairs", description="Maximum scored pairs retained, highest first; default 10,000.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Required unique opaque ID for this intended analysis. Reuse only when retrying the same call; use a new value for an intentional rerun.")


class AnalyzeSiteSimilarityOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    url: str = Field(..., alias="url", description="")
    stopped_early: Any | None = Field(None, alias="stoppedEarly", description="Present when the crawl stopped before finishing. The returned pages are everything that was captured, and billing covers only those pages - treat the result as partial, not as the whole site.")
    page_count: int | None = Field(None, alias="pageCount", description="Absent when background is true — the crawl has not finished yet.")
    pages: list[dict[str, Any]] | None = Field(None, alias="pages", description="Absent when background is true — the crawl has not finished yet.")
    duration_ms: float | None = Field(None, alias="durationMs", description="Absent when background is true — the crawl has not finished yet.")
    truncated_count: int | None = Field(None, alias="truncatedCount", description="")
    artifact: dict[str, Any] | None = Field(None, alias="artifact", description="")
    job_id: str | None = Field(None, alias="jobId", description="Present when background (or downloadImages) was set — poll with check_site_export.")
    status: Literal['pending'] | None = Field(None, alias="status", description="Present when background (or downloadImages) was set.")
    status_url: str | None = Field(None, alias="statusUrl", description="Present when background (or downloadImages) was set — informational; use check_site_export with jobId, not this URL directly.")
    requested_max_pages: int | None = Field(None, alias="requestedMaxPages", description="")
    effective_max_pages: int | None = Field(None, alias="effectiveMaxPages", description="")
    credit_limited: bool | None = Field(None, alias="creditLimited", description="")
    credit_truncated: bool | None = Field(None, alias="creditTruncated", description="")
    delivery: dict[str, Any] | None = Field(None, alias="delivery", description="")
