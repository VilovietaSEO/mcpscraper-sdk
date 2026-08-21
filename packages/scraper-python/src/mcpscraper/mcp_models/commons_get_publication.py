from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CommonsGetPublicationInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    include_articles: bool | None = Field(None, alias="includeArticles", description="Return every stored article’s Markdown source alongside each edition. Large payload; request it only when you intend to edit an article. Owner-only: a publication read by name never returns sources.")
    subdomain: str | None = Field(None, alias="subdomain", description="Public publication name to inspect. Omit to return the publication owned by the authenticated account.")
    include_editions: bool | None = Field(None, alias="includeEditions", description="Include the latest revision of every published edition.")


class CommonsGetPublicationOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    data: Any | None = Field(None, alias="data", description="")
    error: str | None = Field(None, alias="error", description="")
    message: str | None = Field(None, alias="message", description="")
