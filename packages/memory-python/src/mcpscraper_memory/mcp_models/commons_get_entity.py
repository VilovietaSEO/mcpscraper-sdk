from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CommonsGetEntityInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_or_slug: str = Field(..., alias="idOrSlug", description="Transparent Public Wiki entity id such as TPW-Q... or a public /wiki/ slug.")
    include_wiki_page: bool | None = Field(None, alias="includeWikiPage", description="Include the Wikipedia-style page projection used by transparent-commons.cc/wiki/.")


class CommonsGetEntityOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
