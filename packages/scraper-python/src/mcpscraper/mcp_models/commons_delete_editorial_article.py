from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class CommonsDeleteEditorialArticleInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    publication_subdomain: str = Field(..., alias="publicationSubdomain", description="Caller-owned publication containing the article.")
    edition_slug: str | None = Field(None, alias="editionSlug", description="Edition holding the article. Defaults to the publication’s latest edition.")
    article_slug: str = Field(..., alias="articleSlug", description="Slug of the article to delete; other articles are preserved.")
    base_revision: int = Field(..., alias="baseRevision", description="Current edition revision from commons_get_publication; stale deletes are rejected.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Unique key for this deletion; reuse only for an exact retry.")


class CommonsDeleteEditorialArticleOutput(BaseModel):
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
