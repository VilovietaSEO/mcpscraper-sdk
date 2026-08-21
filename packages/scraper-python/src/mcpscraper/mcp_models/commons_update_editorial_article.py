from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CommonsUpdateEditorialArticleInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    publication_subdomain: str = Field(..., alias="publicationSubdomain", description="Publication owned by the authenticated account.")
    edition_slug: str | None = Field(None, alias="editionSlug", description="Edition holding the article. Defaults to the publication’s latest edition.")
    article_slug: str = Field(..., alias="articleSlug", description="Slug of the one article to replace, from commons_get_publication with includeArticles.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Unique key for this intended edit. Reuse it only when retrying the same edit.")
    base_revision: int = Field(..., alias="baseRevision", description="Current edition revision from commons_get_publication. The edit is refused if the edition moved on.")
    markdown: str | None = Field(None, alias="markdown", description="Replacement Markdown body for this article. Omit to change only the metadata fields below.")
    title: str | None = Field(None, alias="title", description="Replacement article title.")
    summary: str | None = Field(None, alias="summary", description="Replacement one or two sentence summary.")
    category: str | None = Field(None, alias="category", description="Replacement section label.")
    kicker: str | None = Field(None, alias="kicker", description="Replacement framing line above the title.")
    order: int | None = Field(None, alias="order", description="Replacement reading-order position.")


class CommonsUpdateEditorialArticleOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    data: Any | None = Field(None, alias="data", description="")
    error: str | None = Field(None, alias="error", description="")
    message: str | None = Field(None, alias="message", description="")
