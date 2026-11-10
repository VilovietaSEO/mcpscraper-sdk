from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class CommonsValidatePublicationInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    mode: Literal['merge', 'replace'] | None = Field(None, alias="mode", description="Merge preserves articles omitted from the payload; replace removes omitted articles from the current edition.")
    operation: Literal['claim', 'publish'] = Field(..., alias="operation", description="Validate either a new name claim or a finished editorial edition without writing.")
    requested_subdomain: str | None = Field(None, alias="requestedSubdomain", description="Publication name to validate when operation is claim.")
    publication_subdomain: str | None = Field(None, alias="publicationSubdomain", description="Already claimed publication name to validate when operation is publish.")
    title: str | None = Field(None, alias="title", description="Human-readable title for the proposed record or authored content.")
    description: str | None = Field(None, alias="description", description="Human-readable summary that distinguishes this record from similarly named records.")
    edition: dict[str, Any] | None = Field(None, alias="edition", description="Complete source-grounded reading-room payload to validate when operation is publish.")
    edition_slug: str | None = Field(None, alias="editionSlug", description="Stable public edition slug. Defaults to edition.site.slug.")
    base_revision: int | None = Field(None, alias="baseRevision", description="Current edition revision when validating an edit.")


class CommonsValidatePublicationOutput(BaseModel):
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
