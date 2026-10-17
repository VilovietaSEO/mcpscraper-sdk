from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class CommonsClaimPublicationInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    requested_subdomain: Annotated[str, Field(min_length=3, max_length=50)] = Field(..., alias='requestedSubdomain', description='Requested publication name under transparent-commons.cc. The server normalizes spaces to hyphens, rejects reserved names, and enforces one globally unique name per account.')
    title: Union[Annotated[str, Field(min_length=1, max_length=140)], None] = Field(None, alias='title', description='Reader-facing publication title. Omit to derive it from the chosen subdomain.')
    description: Union[Annotated[str, Field(max_length=500)], None] = Field(None, alias='description', description='Short description used on the publication archive and discovery surfaces.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=200)] = Field(..., alias='idempotencyKey', description='Unique key for this intended claim. Reuse it only when retrying the same claim.')


class CommonsClaimPublicationOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    data: Union[Any, None] = Field(None, alias='data', description='')
    error: Union[str, None] = Field(None, alias='error', description='')
    message: Union[str, None] = Field(None, alias='message', description='')


CommonsClaimPublicationOutputVariant2DeliveryArtifactsItem = TypedDict('CommonsClaimPublicationOutputVariant2DeliveryArtifactsItem', {
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
CommonsClaimPublicationOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsClaimPublicationOutputVariant2DeliveryAvailableExportsItem = TypedDict('CommonsClaimPublicationOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
CommonsClaimPublicationOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsClaimPublicationOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('CommonsClaimPublicationOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
CommonsClaimPublicationOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsClaimPublicationOutputVariant2Delivery = TypedDict('CommonsClaimPublicationOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[CommonsClaimPublicationOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[CommonsClaimPublicationOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[CommonsClaimPublicationOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
CommonsClaimPublicationOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsClaimPublicationOutputVariant2RecoveryOperation = TypedDict('CommonsClaimPublicationOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CommonsClaimPublicationOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsClaimPublicationOutputVariant2Recovery = TypedDict('CommonsClaimPublicationOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[CommonsClaimPublicationOutputVariant2RecoveryOperation],
})
CommonsClaimPublicationOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CommonsClaimPublicationOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: CommonsClaimPublicationOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: CommonsClaimPublicationOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(CommonsClaimPublicationOutput).
CommonsClaimPublicationOutput = Union[CommonsClaimPublicationOutputVariant2, CommonsClaimPublicationOutputVariant1]

_CommonsClaimPublicationInputAdapter = TypeAdapter(CommonsClaimPublicationInput)
_CommonsClaimPublicationOutputAdapter = TypeAdapter(CommonsClaimPublicationOutput)