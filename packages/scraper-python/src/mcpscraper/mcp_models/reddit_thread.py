from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class RedditThreadInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    idempotency_key: Union[Annotated[str, Field(min_length=1, max_length=512)], None] = Field(None, alias='idempotencyKey', description='One logical request identity. Retry identical inputs with the same key to replay or recover without repeating provider work. Omit for a fresh intent; use the key returned with the result or transport error for retries.')
    url: Annotated[str, Field(min_length=1)] = Field(..., alias='url', description='A reddit.com thread/post URL. Legacy reddit.com hostnames are normalized, but retrieval uses the current Reddit page only.')
    max_comments: Union[Annotated[int, Field(ge=1, le=2000)], None] = Field(None, alias='maxComments', description='Optional cap on comments returned. Omit to return the largest set captured within the bounded expansion window, up to 2,000.')


RedditThreadOutputVariant1Operation = TypedDict('RedditThreadOutputVariant1Operation', {
    'runId': Required[Union[str, None]],
    'idempotencyKey': Required[str],
    'state': Required[str],
})
RedditThreadOutputVariant1Operation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


RedditThreadOutputVariant1CommentsItem = TypedDict('RedditThreadOutputVariant1CommentsItem', {
    'author': Required[Union[str, None]],
    'score': Required[Union[str, None]],
    'depth': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'body': Required[str],
})
RedditThreadOutputVariant1CommentsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class RedditThreadOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    operation: Union[RedditThreadOutputVariant1Operation, None] = Field(None, alias='operation', description='')
    diagnostics: Union[dict[str, Any], None] = Field(None, alias='diagnostics', description='')
    source_url: Union[str, None] = Field(..., alias='sourceUrl', description='')
    canonical_url: Union[str, None] = Field(..., alias='canonicalUrl', description='')
    old_reddit_url: Union[str, None] = Field(..., alias='oldRedditUrl', description='')
    retrieval_source: Literal['www_reddit', 'old_reddit'] = Field(..., alias='retrievalSource', description='')
    title: Union[str, None] = Field(..., alias='title', description='')
    author: Union[str, None] = Field(..., alias='author', description='')
    score: Union[str, None] = Field(..., alias='score', description='')
    post_body: Union[str, None] = Field(..., alias='postBody', description='')
    num_comments: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='numComments', description='')
    comments: list[RedditThreadOutputVariant1CommentsItem] = Field(..., alias='comments', description='')


RedditThreadOutputVariant2DeliveryArtifactsItem = TypedDict('RedditThreadOutputVariant2DeliveryArtifactsItem', {
    'artifactId': Required[str],
    'filename': Required[str],
    'contentType': Required[str],
    'bytes': Required[Union[float, int]],
    'sha256': Required[str],
    'expiresAt': Required[str],
    'capabilities': Required[list[str]],
    'downloadUrl': Required[Union[str, None]],
    'downloadUrlExpiresAt': Required[Union[str, None]],
    'downloadState': Required[Literal['available', 'local', 'unavailable']],
})
RedditThreadOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


RedditThreadOutputVariant2DeliveryAvailableExportsItem = TypedDict('RedditThreadOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
RedditThreadOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


RedditThreadOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('RedditThreadOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
RedditThreadOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


RedditThreadOutputVariant2Delivery = TypedDict('RedditThreadOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[RedditThreadOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[RedditThreadOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[RedditThreadOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
RedditThreadOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


RedditThreadOutputVariant2RecoveryOperation = TypedDict('RedditThreadOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
RedditThreadOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


RedditThreadOutputVariant2Recovery = TypedDict('RedditThreadOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[RedditThreadOutputVariant2RecoveryOperation],
})
RedditThreadOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class RedditThreadOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: RedditThreadOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: RedditThreadOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(RedditThreadOutput).
RedditThreadOutput = Union[RedditThreadOutputVariant1, RedditThreadOutputVariant2]

_RedditThreadInputAdapter = TypeAdapter(RedditThreadInput)
_RedditThreadOutputAdapter = TypeAdapter(RedditThreadOutput)