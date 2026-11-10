from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class CommonsUpdateEditorialArticleInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    source_label: str | None = Field(None, alias="sourceLabel", description="Replacement provenance label; omitted fields are preserved.")
    source_type: Any | None = Field(None, alias="sourceType", description="Replacement source class; null clears it.")
    revision: Any | None = Field(None, alias="revision", description="Replacement article revision label; null clears it.")
    updated_at: Any | None = Field(None, alias="updatedAt", description="Replacement source update label; null clears it.")
    image: Any | None = Field(None, alias="image", description="Replacement card and article image; null clears it.")
    og_image: Any | None = Field(None, alias="ogImage", description="Replacement social image; null clears it.")
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
