from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class RedditThreadInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    url: str = Field(..., alias="url", description="A reddit.com thread/post URL. Legacy reddit.com hostnames are normalized, but retrieval uses the current Reddit page only.")
    max_comments: int | None = Field(None, alias="maxComments", description="Optional cap on comments returned. Omit to return the largest set captured within the bounded expansion window, up to 2,000.")


class RedditThreadOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    source_url: Any = Field(..., alias="sourceUrl", description="")
    canonical_url: Any = Field(..., alias="canonicalUrl", description="")
    old_reddit_url: Any = Field(..., alias="oldRedditUrl", description="")
    retrieval_source: Literal['www_reddit', 'old_reddit'] = Field(..., alias="retrievalSource", description="")
    title: Any = Field(..., alias="title", description="")
    author: Any = Field(..., alias="author", description="")
    score: Any = Field(..., alias="score", description="")
    post_body: Any = Field(..., alias="postBody", description="")
    num_comments: int = Field(..., alias="numComments", description="")
    comments: list[dict[str, Any]] = Field(..., alias="comments", description="")
