from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CommonsListNeedsLinksInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    query: str | None = Field(None, alias="query", description="Optional text filter over unresolved concept title, summary, relationship, source page title, source description, and source tags.")
    entity_type: str | None = Field(None, alias="entityType", description="Only return unresolved concepts found on source entities of this type.")
    tag: str | None = Field(None, alias="tag", description="Only return unresolved concepts found on source entities with this tag.")
    tags: list[str] | None = Field(None, alias="tags", description="Only return unresolved concepts found on source entities matching all supplied tags.")
    source_entity_id: str | None = Field(None, alias="sourceEntityId", description="Only return unresolved concepts from one source entity id.")
    source_slug: str | None = Field(None, alias="sourceSlug", description="Only return unresolved concepts from one /wiki/ source slug.")
    limit: int | None = Field(None, alias="limit", description="")
    offset: int | None = Field(None, alias="offset", description="")


class CommonsListNeedsLinksOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    data: Any | None = Field(None, alias="data", description="")
    error: str | None = Field(None, alias="error", description="")
    message: str | None = Field(None, alias="message", description="")
