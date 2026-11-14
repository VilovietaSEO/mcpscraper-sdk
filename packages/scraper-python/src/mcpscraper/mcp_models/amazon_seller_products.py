from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class AmazonSellerProductsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    page: Union[Annotated[int, Field(ge=1, le=9007199254740991)], None] = Field(None, alias='page', description="1-based page of the seller's storefront.")
    region: Union[Literal['amazon.com', 'amazon.co.uk', 'amazon.de', 'amazon.fr', 'amazon.it', 'amazon.es', 'amazon.nl', 'amazon.se', 'amazon.pl', 'amazon.ca', 'amazon.com.mx', 'amazon.com.br', 'amazon.co.jp', 'amazon.in', 'amazon.com.au', 'amazon.sg', 'amazon.ae', 'amazon.sa', 'amazon.com.tr', 'amazon.eg'], None] = Field(None, alias='region', description='Amazon marketplace to read, as its domain; omit it for amazon.com.')
    seller_id: Annotated[str, Field(min_length=1)] = Field(..., alias='sellerId', description='Amazon seller ID, the value after seller= in a seller page URL.')


class AmazonSellerProductsOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    tool: str = Field(..., alias='tool', description='The tool that produced this result.')
    count: Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)] = Field(..., alias='count', description='Number of records returned.')
    items: list[dict[str, Any]] = Field(..., alias='items', description='Returned records. A lookup of one thing returns a single record.')
    meta: Union[dict[str, Any], None] = Field(None, alias='meta', description='Values returned alongside the records, such as nextCursor for the next page, or totals.')
    charged_credits: Union[float, int] = Field(..., alias='chargedCredits', description='Credits charged for this call.')
    duration_ms: Union[Union[float, int], None] = Field(..., alias='durationMs', description='Time taken in milliseconds.')


AmazonSellerProductsOutputVariant2DeliveryArtifactsItem = TypedDict('AmazonSellerProductsOutputVariant2DeliveryArtifactsItem', {
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
AmazonSellerProductsOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AmazonSellerProductsOutputVariant2DeliveryAvailableExportsItem = TypedDict('AmazonSellerProductsOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
AmazonSellerProductsOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AmazonSellerProductsOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AmazonSellerProductsOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AmazonSellerProductsOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AmazonSellerProductsOutputVariant2Delivery = TypedDict('AmazonSellerProductsOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AmazonSellerProductsOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[AmazonSellerProductsOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AmazonSellerProductsOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AmazonSellerProductsOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AmazonSellerProductsOutputVariant2RecoveryOperation = TypedDict('AmazonSellerProductsOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AmazonSellerProductsOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AmazonSellerProductsOutputVariant2Recovery = TypedDict('AmazonSellerProductsOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AmazonSellerProductsOutputVariant2RecoveryOperation],
})
AmazonSellerProductsOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AmazonSellerProductsOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AmazonSellerProductsOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AmazonSellerProductsOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AmazonSellerProductsOutput).
AmazonSellerProductsOutput = Union[AmazonSellerProductsOutputVariant1, AmazonSellerProductsOutputVariant2]

_AmazonSellerProductsInputAdapter = TypeAdapter(AmazonSellerProductsInput)
_AmazonSellerProductsOutputAdapter = TypeAdapter(AmazonSellerProductsOutput)