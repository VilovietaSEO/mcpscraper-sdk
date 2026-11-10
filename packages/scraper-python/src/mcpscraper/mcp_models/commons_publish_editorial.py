from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class CommonsPublishEditorialInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    mode: Literal['merge', 'replace'] | None = Field(None, alias="mode", description="Merge preserves articles omitted from the payload; replace removes omitted articles from the current edition.")
    publication_subdomain: str = Field(..., alias="publicationSubdomain", description="Publication owned by the authenticated account.")
    edition_slug: str | None = Field(None, alias="editionSlug", description="Stable public edition slug. Defaults to site.slug.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Unique key for this intended publish. Reuse it only when retrying the same revision.")
    base_revision: int | None = Field(None, alias="baseRevision", description="Required when revising an existing edition; use the current revision from commons_get_publication.")
    site: dict[str, Any] = Field(..., alias="site", description="Complete editorial site payload containing the collection identity and authored articles.")
    deck: str = Field(..., alias="deck", description="Two or three sentences that explain the collection’s value and scope without generic marketing language.")
    articles: list[dict[str, Any]] = Field(..., alias="articles", description="One to one hundred fully authored articles, with no more than 2,000,000 Markdown bytes combined. Articles may include structured card/hero images, article-specific Open Graph images, and Markdown body images. Read all in-scope source material before composing them; preserve distinctions, uncertainty, image provenance, and rights context instead of flattening the corpus.")
    filename: str | None = Field(None, alias="filename", description="Optional download filename. The server always normalizes it to a safe .html filename.")


class CommonsPublishEditorialOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="")
    data: Any | None = Field(None, alias="data", description="")
    error: str | None = Field(None, alias="error", description="")
    message: str | None = Field(None, alias="message", description="")
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
