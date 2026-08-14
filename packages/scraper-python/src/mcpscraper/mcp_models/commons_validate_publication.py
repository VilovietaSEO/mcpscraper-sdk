from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CommonsValidatePublicationInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

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

    ok: bool = Field(..., alias="ok", description="")
    data: Any | None = Field(None, alias="data", description="")
    error: str | None = Field(None, alias="error", description="")
    message: str | None = Field(None, alias="message", description="")
