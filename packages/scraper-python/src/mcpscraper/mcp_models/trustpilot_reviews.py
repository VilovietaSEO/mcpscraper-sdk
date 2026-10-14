from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class TrustpilotReviewsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    domain: Annotated[str, Field(min_length=1)] = Field(..., alias='domain', description='The business\'s domain as it appears in its Trustpilot URL, e.g. "www.bhphotovideo.com" (include the www. if the site uses it — pass the domain as-is, do not guess).')
    max_pages: Union[Annotated[int, Field(ge=1, le=50)], None] = Field(None, alias='maxPages', description='Review pages to fetch (~20 reviews per page). Default 5 (~100 reviews). Maximum 50 — large companies can have 1,000+ pages; this tool is for sampling, not full-corpus export.')


TrustpilotReviewsOutputVariant1ReviewsItemReviewer = TypedDict('TrustpilotReviewsOutputVariant1ReviewsItemReviewer', {
    'name': Required[Union[str, None]],
    'profileId': Required[Union[str, None]],
    'title': Required[Union[str, None]],
    'companySegment': Required[Union[str, None]],
})
TrustpilotReviewsOutputVariant1ReviewsItemReviewer.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TrustpilotReviewsOutputVariant1ReviewsItemBodyItem = TypedDict('TrustpilotReviewsOutputVariant1ReviewsItemBodyItem', {
    'question': Required[Union[str, None]],
    'answer': Required[str],
})
TrustpilotReviewsOutputVariant1ReviewsItemBodyItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TrustpilotReviewsOutputVariant1ReviewsItemFlags = TypedDict('TrustpilotReviewsOutputVariant1ReviewsItemFlags', {
    'origin': Required[Union[str, None]],
    'incentivized': Required[Union[bool, None]],
    'validated': Required[Union[bool, None]],
    'currentUser': Required[Union[bool, None]],
    'companyReplied': Required[Union[bool, None]],
})
TrustpilotReviewsOutputVariant1ReviewsItemFlags.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TrustpilotReviewsOutputVariant1ReviewsItem = TypedDict('TrustpilotReviewsOutputVariant1ReviewsItem', {
    'source': Required[Literal['trustpilot', 'g2']],
    'sourceReviewId': Required[Union[str, None]],
    'reviewUrl': Required[Union[str, None]],
    'reviewer': Required[TrustpilotReviewsOutputVariant1ReviewsItemReviewer],
    'rating': Required[Union[Union[float, int], None]],
    'ratingScale': Required[Union[float, int]],
    'title': Required[Union[str, None]],
    'date': Required[Union[str, None]],
    'body': Required[list[TrustpilotReviewsOutputVariant1ReviewsItemBodyItem]],
    'truncated': Required[bool],
    'flags': Required[TrustpilotReviewsOutputVariant1ReviewsItemFlags],
})
TrustpilotReviewsOutputVariant1ReviewsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class TrustpilotReviewsOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    domain: str = Field(..., alias='domain', description='')
    review_url: str = Field(..., alias='reviewUrl', description='')
    extracted_at: str = Field(..., alias='extractedAt', description='')
    requested_max_pages: Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)] = Field(..., alias='requestedMaxPages', description='')
    pages_fetched: Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)] = Field(..., alias='pagesFetched', description='')
    review_count: Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)] = Field(..., alias='reviewCount', description='')
    reviews: list[TrustpilotReviewsOutputVariant1ReviewsItem] = Field(..., alias='reviews', description='')
    duration_ms: Union[float, int] = Field(..., alias='durationMs', description='')


TrustpilotReviewsOutputVariant2DeliveryArtifactsItem = TypedDict('TrustpilotReviewsOutputVariant2DeliveryArtifactsItem', {
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
TrustpilotReviewsOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TrustpilotReviewsOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('TrustpilotReviewsOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
TrustpilotReviewsOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TrustpilotReviewsOutputVariant2Delivery = TypedDict('TrustpilotReviewsOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[TrustpilotReviewsOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[TrustpilotReviewsOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
TrustpilotReviewsOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TrustpilotReviewsOutputVariant2RecoveryOperation = TypedDict('TrustpilotReviewsOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
TrustpilotReviewsOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TrustpilotReviewsOutputVariant2Recovery = TypedDict('TrustpilotReviewsOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[TrustpilotReviewsOutputVariant2RecoveryOperation],
})
TrustpilotReviewsOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class TrustpilotReviewsOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: TrustpilotReviewsOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: TrustpilotReviewsOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(TrustpilotReviewsOutput).
TrustpilotReviewsOutput = Union[TrustpilotReviewsOutputVariant1, TrustpilotReviewsOutputVariant2]

_TrustpilotReviewsInputAdapter = TypeAdapter(TrustpilotReviewsInput)
_TrustpilotReviewsOutputAdapter = TypeAdapter(TrustpilotReviewsOutput)