from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class G2ReviewsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    product: Annotated[str, Field(min_length=1)] = Field(..., alias='product', description='The product\'s G2 URL slug, e.g. "notion" from g2.com/products/notion/reviews (also accepts a full g2.com product URL).')
    max_pages: Union[Annotated[int, Field(ge=1, le=50)], None] = Field(None, alias='maxPages', description='Review pages to fetch (~10 reviews per page). Default 5 (~50 reviews). Maximum 50 — this tool is for sampling, not full-corpus export.')


G2ReviewsOutputVariant1ReviewsItemReviewer = TypedDict('G2ReviewsOutputVariant1ReviewsItemReviewer', {
    'name': Required[Union[str, None]],
    'profileId': Required[Union[str, None]],
    'title': Required[Union[str, None]],
    'companySegment': Required[Union[str, None]],
})
G2ReviewsOutputVariant1ReviewsItemReviewer.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


G2ReviewsOutputVariant1ReviewsItemBodyItem = TypedDict('G2ReviewsOutputVariant1ReviewsItemBodyItem', {
    'question': Required[Union[str, None]],
    'answer': Required[str],
})
G2ReviewsOutputVariant1ReviewsItemBodyItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


G2ReviewsOutputVariant1ReviewsItemFlags = TypedDict('G2ReviewsOutputVariant1ReviewsItemFlags', {
    'origin': Required[Union[str, None]],
    'incentivized': Required[Union[bool, None]],
    'validated': Required[Union[bool, None]],
    'currentUser': Required[Union[bool, None]],
    'companyReplied': Required[Union[bool, None]],
})
G2ReviewsOutputVariant1ReviewsItemFlags.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


G2ReviewsOutputVariant1ReviewsItem = TypedDict('G2ReviewsOutputVariant1ReviewsItem', {
    'source': Required[Literal['trustpilot', 'g2']],
    'sourceReviewId': Required[Union[str, None]],
    'reviewUrl': Required[Union[str, None]],
    'reviewer': Required[G2ReviewsOutputVariant1ReviewsItemReviewer],
    'rating': Required[Union[Union[float, int], None]],
    'ratingScale': Required[Union[float, int]],
    'title': Required[Union[str, None]],
    'date': Required[Union[str, None]],
    'body': Required[list[G2ReviewsOutputVariant1ReviewsItemBodyItem]],
    'truncated': Required[bool],
    'flags': Required[G2ReviewsOutputVariant1ReviewsItemFlags],
})
G2ReviewsOutputVariant1ReviewsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class G2ReviewsOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    product: str = Field(..., alias='product', description='')
    review_url: str = Field(..., alias='reviewUrl', description='')
    extracted_at: str = Field(..., alias='extractedAt', description='')
    requested_max_pages: Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)] = Field(..., alias='requestedMaxPages', description='')
    pages_fetched: Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)] = Field(..., alias='pagesFetched', description='')
    review_count: Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)] = Field(..., alias='reviewCount', description='')
    reviews: list[G2ReviewsOutputVariant1ReviewsItem] = Field(..., alias='reviews', description='')
    duration_ms: Union[float, int] = Field(..., alias='durationMs', description='')


G2ReviewsOutputVariant2DeliveryArtifactsItem = TypedDict('G2ReviewsOutputVariant2DeliveryArtifactsItem', {
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
G2ReviewsOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


G2ReviewsOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('G2ReviewsOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
G2ReviewsOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


G2ReviewsOutputVariant2Delivery = TypedDict('G2ReviewsOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[G2ReviewsOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[G2ReviewsOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
G2ReviewsOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


G2ReviewsOutputVariant2RecoveryOperation = TypedDict('G2ReviewsOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
G2ReviewsOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


G2ReviewsOutputVariant2Recovery = TypedDict('G2ReviewsOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[G2ReviewsOutputVariant2RecoveryOperation],
})
G2ReviewsOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class G2ReviewsOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: G2ReviewsOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: G2ReviewsOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(G2ReviewsOutput).
G2ReviewsOutput = Union[G2ReviewsOutputVariant1, G2ReviewsOutputVariant2]

_G2ReviewsInputAdapter = TypeAdapter(G2ReviewsInput)
_G2ReviewsOutputAdapter = TypeAdapter(G2ReviewsOutput)