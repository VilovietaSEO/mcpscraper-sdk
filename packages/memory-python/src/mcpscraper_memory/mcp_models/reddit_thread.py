from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class RedditThreadInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    url: str = Field(..., alias="url", description="A reddit.com thread/post URL (www, old, new Reddit, or redd.it).")
    max_comments: int | None = Field(None, alias="maxComments", description="Optional cap on comments returned. Omit to return all captured comments.")


class RedditThreadOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
