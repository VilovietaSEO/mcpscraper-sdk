from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class CommonsGetPublicationInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    include_articles: bool | None = Field(None, alias="includeArticles", description="Return every stored article’s Markdown source alongside each edition. Large payload; request it only when you intend to edit an article. Sources require an authenticated owner read, including when selecting by subdomain.")
    subdomain: str | None = Field(None, alias="subdomain", description="Public publication name to inspect. Omit only when the account owns exactly one publication; otherwise list and select a subdomain.")
    edition_slug: str | None = Field(None, alias="editionSlug", description="Restrict edition results to this slug.")
    article_slug: str | None = Field(None, alias="articleSlug", description="Restrict article source results to this slug; requires includeArticles.")
    include_editions: bool | None = Field(None, alias="includeEditions", description="Include the latest revision of every published edition.")


class CommonsGetPublicationOutput(BaseModel):
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
