from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CommonsSearchEntitiesInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    query: str | None = Field(None, alias="query", description="Search text matched against title, description, tags, keywords, JSON-LD, source metadata, citations, media, and article body.")
    entity_type: str | None = Field(None, alias="entityType", description="Optional entity type filter. \"Public Article\", \"PublicArticle\", \"Article\", and \"item\" normalize to PublicArticle.")
    tag: str | None = Field(None, alias="tag", description="Single canonical tag filter. Use tags for multiple tags.")
    tags: list[str] | None = Field(None, alias="tags", description="Multiple tag filters. All supplied tags are applied.")
    keyword: str | None = Field(None, alias="keyword", description="Single keyword filter. Use keywords for multiple keywords.")
    keywords: list[str] | None = Field(None, alias="keywords", description="Multiple keyword filters. All supplied keywords are applied.")
    related_entity_id: str | None = Field(None, alias="relatedEntityId", description="Return entities related to this Transparent Public Wiki entity id.")
    trail_id: str | None = Field(None, alias="trailId", description="Return entities collected into a specific reading trail entity.")
    source_domain: str | None = Field(None, alias="sourceDomain", description="Filter by original-source or canonical-source domain text.")
    has_media: bool | None = Field(None, alias="hasMedia", description="When true, only return entities with image, video, or audio media records.")
    has_video: bool | None = Field(None, alias="hasVideo", description="When true, only return entities with at least one video media record.")
    published_after: str | None = Field(None, alias="publishedAfter", description="Optional ISO-ish lower bound for publishedAt.")
    updated_after: str | None = Field(None, alias="updatedAfter", description="Optional ISO-ish lower bound for updatedAt.")
    filter_id: str | None = Field(None, alias="filterId", description="Optional saved filter id from commons_list_filters. The saved filter is merged with this call for this account.")
    limit: int | None = Field(None, alias="limit", description="Maximum entities to return. Default 20, maximum 100.")
    offset: int | None = Field(None, alias="offset", description="Pagination offset.")


class CommonsSearchEntitiesOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    data: Any | None = Field(None, alias="data", description="")
    error: str | None = Field(None, alias="error", description="")
    message: str | None = Field(None, alias="message", description="")
