from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class RedditThreadInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    idempotency_key: str | None = Field(None, alias="idempotencyKey", description="One logical request identity. Retry identical inputs with the same key to replay or recover without repeating provider work. Omit for a fresh intent; use the key returned with the result or transport error for retries.")
    url: str = Field(..., alias="url", description="A known Reddit thread URL to open directly without searching; legacy Reddit hostnames are normalized to the current page.")
    max_comments: int | None = Field(None, alias="maxComments", description="Optional cap on comments returned. Omit to return the largest set captured within the bounded expansion window, up to 2,000.")


class RedditThreadOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    operation: dict[str, Any] | None = Field(None, alias="operation", description="")
    diagnostics: dict[str, Any] | None = Field(None, alias="diagnostics", description="")
    source_url: Any | None = Field(None, alias="sourceUrl", description="")
    canonical_url: Any | None = Field(None, alias="canonicalUrl", description="")
    old_reddit_url: Any | None = Field(None, alias="oldRedditUrl", description="")
    retrieval_source: Literal['www_reddit', 'old_reddit'] | None = Field(None, alias="retrievalSource", description="")
    title: Any | None = Field(None, alias="title", description="")
    author: Any | None = Field(None, alias="author", description="")
    score: Any | None = Field(None, alias="score", description="")
    post_body: Any | None = Field(None, alias="postBody", description="")
    published_at: Any | None = Field(None, alias="publishedAt", description="")
    num_comments: int | None = Field(None, alias="numComments", description="")
    comments: list[dict[str, Any]] | None = Field(None, alias="comments", description="")
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
