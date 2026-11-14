from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class AmazonReviewsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    end_date: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='endDate', description='Only return reviews on or before this date, inclusive, in YYYY-MM-DD format.')
    keyword: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='keyword', description='Only return reviews whose title or text contains this keyword, case-insensitively.')
    limit: Union[Annotated[int, Field(ge=1, le=50)], None] = Field(None, alias='limit', description='Maximum number of results to return (1-50, default 50).')
    product: Annotated[str, Field(min_length=1)] = Field(..., alias='product', description='Amazon product ASIN or a product link on one of the marketplaces listed under region, such as.')
    ratings: Union[list[Literal['1', '2', '3', '4', '5']], None] = Field(None, alias='ratings', description='Only return reviews whose star rating is in this set; omit for all ratings.')
    region: Union[Literal['amazon.com', 'amazon.ca', 'amazon.de', 'amazon.fr', 'amazon.co.uk', 'amazon.it', 'amazon.es', 'amazon.com.au', 'amazon.co.jp', 'amazon.com.br', 'amazon.com.mx', 'amazon.nl', 'amazon.ie', 'amazon.se', 'amazon.com.tr', 'amazon.ae', 'amazon.sg', 'amazon.sa', 'amazon.pl', 'amazon.com.be', 'amazon.eg', 'amazon.in'], None] = Field(None, alias='region', description='Amazon marketplace domain the product ASIN belongs to.')
    sort: Union[Literal['helpful', 'recent'], None] = Field(None, alias='sort', description='Review sort order: most helpful first or most recent first.')
    start_date: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='startDate', description='Only return reviews on or after this date, inclusive, in YYYY-MM-DD format.')
    verified_only: Union[bool, None] = Field(None, alias='verifiedOnly', description='Set true to return only verified-purchase reviews.')


class AmazonReviewsOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    tool: str = Field(..., alias='tool', description='The tool that produced this result.')
    count: Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)] = Field(..., alias='count', description='Number of records returned.')
    items: list[dict[str, Any]] = Field(..., alias='items', description='Returned records. A lookup of one thing returns a single record.')
    charged_credits: Union[float, int] = Field(..., alias='chargedCredits', description='Credits charged for this call.')
    duration_ms: Union[Union[float, int], None] = Field(..., alias='durationMs', description='Time taken in milliseconds.')


AmazonReviewsOutputVariant2DeliveryArtifactsItem = TypedDict('AmazonReviewsOutputVariant2DeliveryArtifactsItem', {
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
AmazonReviewsOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AmazonReviewsOutputVariant2DeliveryAvailableExportsItem = TypedDict('AmazonReviewsOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
AmazonReviewsOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AmazonReviewsOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AmazonReviewsOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AmazonReviewsOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AmazonReviewsOutputVariant2Delivery = TypedDict('AmazonReviewsOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AmazonReviewsOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[AmazonReviewsOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AmazonReviewsOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AmazonReviewsOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AmazonReviewsOutputVariant2RecoveryOperation = TypedDict('AmazonReviewsOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AmazonReviewsOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AmazonReviewsOutputVariant2Recovery = TypedDict('AmazonReviewsOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AmazonReviewsOutputVariant2RecoveryOperation],
})
AmazonReviewsOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AmazonReviewsOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AmazonReviewsOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AmazonReviewsOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AmazonReviewsOutput).
AmazonReviewsOutput = Union[AmazonReviewsOutputVariant1, AmazonReviewsOutputVariant2]

_AmazonReviewsInputAdapter = TypeAdapter(AmazonReviewsInput)
_AmazonReviewsOutputAdapter = TypeAdapter(AmazonReviewsOutput)