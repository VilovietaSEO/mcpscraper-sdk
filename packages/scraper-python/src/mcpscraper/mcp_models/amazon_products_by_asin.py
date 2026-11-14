from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class AmazonProductsByAsinInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    amazon_domain: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='amazonDomain', description='Amazon marketplace domain to fetch products from.')
    asins: Annotated[list[Annotated[str, Field(min_length=1)]], Field(min_length=1, max_length=10)] = Field(..., alias='asins', description='Up to 10 Amazon ASINs to look up.')
    limit: Union[Annotated[int, Field(ge=1, le=10)], None] = Field(None, alias='limit', description='Maximum number of products to return (1-10); fewer costs less.')


class AmazonProductsByAsinOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    tool: str = Field(..., alias='tool', description='The tool that produced this result.')
    count: Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)] = Field(..., alias='count', description='Number of records returned.')
    items: list[dict[str, Any]] = Field(..., alias='items', description='Returned records. A lookup of one thing returns a single record.')
    charged_credits: Union[float, int] = Field(..., alias='chargedCredits', description='Credits charged for this call.')
    duration_ms: Union[Union[float, int], None] = Field(..., alias='durationMs', description='Time taken in milliseconds.')


AmazonProductsByAsinOutputVariant2DeliveryArtifactsItem = TypedDict('AmazonProductsByAsinOutputVariant2DeliveryArtifactsItem', {
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
AmazonProductsByAsinOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AmazonProductsByAsinOutputVariant2DeliveryAvailableExportsItem = TypedDict('AmazonProductsByAsinOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
AmazonProductsByAsinOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AmazonProductsByAsinOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AmazonProductsByAsinOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AmazonProductsByAsinOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AmazonProductsByAsinOutputVariant2Delivery = TypedDict('AmazonProductsByAsinOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AmazonProductsByAsinOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[AmazonProductsByAsinOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AmazonProductsByAsinOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AmazonProductsByAsinOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AmazonProductsByAsinOutputVariant2RecoveryOperation = TypedDict('AmazonProductsByAsinOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AmazonProductsByAsinOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AmazonProductsByAsinOutputVariant2Recovery = TypedDict('AmazonProductsByAsinOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AmazonProductsByAsinOutputVariant2RecoveryOperation],
})
AmazonProductsByAsinOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AmazonProductsByAsinOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AmazonProductsByAsinOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AmazonProductsByAsinOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AmazonProductsByAsinOutput).
AmazonProductsByAsinOutput = Union[AmazonProductsByAsinOutputVariant1, AmazonProductsByAsinOutputVariant2]

_AmazonProductsByAsinInputAdapter = TypeAdapter(AmazonProductsByAsinInput)
_AmazonProductsByAsinOutputAdapter = TypeAdapter(AmazonProductsByAsinOutput)