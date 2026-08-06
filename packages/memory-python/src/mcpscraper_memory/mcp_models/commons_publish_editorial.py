from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CommonsPublishEditorialInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    publication_subdomain: str = Field(..., alias="publicationSubdomain", description="Publication owned by the authenticated account.")
    edition_slug: str | None = Field(None, alias="editionSlug", description="Stable public edition slug. Defaults to site.slug.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Unique key for this intended publish. Reuse it only when retrying the same revision.")
    base_revision: int | None = Field(None, alias="baseRevision", description="Required when revising an existing edition; use the current revision from commons_get_publication.")
    site: dict[str, Any] = Field(..., alias="site", description="")
    deck: str = Field(..., alias="deck", description="Two or three sentences that explain the collection’s value and scope without generic marketing language.")
    articles: list[dict[str, Any]] = Field(..., alias="articles", description="One to forty fully authored articles, with no more than 2,000,000 Markdown bytes combined. Read all in-scope source material before composing them; preserve distinctions, uncertainty, and provenance instead of flattening the corpus.")
    filename: str | None = Field(None, alias="filename", description="Optional download filename. The server always normalizes it to a safe .html filename.")


class CommonsPublishEditorialOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    data: Any | None = Field(None, alias="data", description="")
    error: str | None = Field(None, alias="error", description="")
    message: str | None = Field(None, alias="message", description="")
