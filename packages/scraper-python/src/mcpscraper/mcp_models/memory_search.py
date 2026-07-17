from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class MemorySearchInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    vault: str | None = Field(None, alias="vault", description="Exact logical vault handle to search. Omit to search every entitled vault.")
    query: str = Field(..., alias="query", description="A focused semantic reformulation of the request.")
    user_message: str | None = Field(None, alias="userMessage", description="Original human wording. Used as a distinct query variant when useful and logged for quality review.")
    queries: list[str] | None = Field(None, alias="queries", description="Caller-provided focused query variants. The planner deduplicates these with query, original wording, and tag/entity terms.")
    entities: list[str] | None = Field(None, alias="entities", description="Named entities or exact terms used to form a focused query variant.")
    tags: list[str] | None = Field(None, alias="tags", description="Exact canonical tags used for tag-channel retrieval and filtering.")
    tag_mode: Literal["any", "all"] | None = Field(None, alias="tagMode", description="Whether a note must match any or all supplied tags. Default any.")
    kind: Literal["note", "library", "capture", "decision", "message"] | None = Field(None, alias="kind", description="Exact persisted note-kind filter.")
    type: str | None = Field(None, alias="type", description="Exact props.type filter.")
    date_from: str | None = Field(None, alias="dateFrom", description="Inclusive lower bound for note updatedAt.")
    date_to: str | None = Field(None, alias="dateTo", description="Inclusive upper bound for note updatedAt.")
    metadata: dict[str, Any] | None = Field(None, alias="metadata", description="Exact equality filters for primitive note props.")
    query_variant_count: int | None = Field(None, alias="queryVariantCount", description="Number of variants. Default 3.")
    candidate_pool: int | None = Field(None, alias="candidatePool", description="Total fused candidates before final reranking. Default 50.")
    graph_seed_count: int | None = Field(None, alias="graphSeedCount", description="Strong preliminary notes whose graph neighborhoods are considered. Default 8.")
    graph_depth: float | None = Field(None, alias="graphDepth", description="Graph expansion depth. Bounded to exactly one hop.")
    graph_neighbors_per_seed: int | None = Field(None, alias="graphNeighborsPerSeed", description="Maximum outgoing-link plus backlink neighbors per seed. Default 5.")
    rerank_top_n: int | None = Field(None, alias="rerankTopN", description="Final results retained after Jina reranking. Default 30.")
    top_k: int | None = Field(None, alias="topK", description="Deprecated compatibility alias for rerankTopN. Prefer rerankTopN; default remains 30.")
    include_shared: bool | None = Field(None, alias="includeShared", description="Also search individually accepted shares. Default true. Exact note metadata filters exclude shares without accessible metadata.")


class MemorySearchOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    vault: str | None = Field(None, alias="vault", description="")
    vaults_searched: list[str] | None = Field(None, alias="vaultsSearched", description="")
    planner: dict[str, Any] | None = Field(None, alias="planner", description="")
    rerank: dict[str, Any] | None = Field(None, alias="rerank", description="")
    results: list[dict[str, Any]] | None = Field(None, alias="results", description="")
    error: str | None = Field(None, alias="error", description="")
