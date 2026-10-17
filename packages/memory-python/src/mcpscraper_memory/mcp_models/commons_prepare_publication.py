from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class CommonsPreparePublicationInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    requested_subdomain: Annotated[str, Field(min_length=3, max_length=50)] = Field(..., alias='requestedSubdomain', description='Requested publication name under transparent-commons.cc. The server normalizes spaces to hyphens, rejects reserved names, and enforces one globally unique name per account.')
    title: Union[Annotated[str, Field(min_length=1, max_length=140)], None] = Field(None, alias='title', description='Reader-facing publication title. Omit to derive it from the chosen subdomain.')
    description: Union[Annotated[str, Field(max_length=500)], None] = Field(None, alias='description', description='Short description used on the publication archive and discovery surfaces.')


class CommonsPreparePublicationOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    data: Union[Any, None] = Field(None, alias='data', description='')
    error: Union[str, None] = Field(None, alias='error', description='')
    message: Union[str, None] = Field(None, alias='message', description='')


CommonsPreparePublicationOutputVariant2DeliveryArtifactsItem = TypedDict('CommonsPreparePublicationOutputVariant2DeliveryArtifactsItem', {
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
CommonsPreparePublicationOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsPreparePublicationOutputVariant2DeliveryAvailableExportsItem = TypedDict('CommonsPreparePublicationOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
CommonsPreparePublicationOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsPreparePublicationOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('CommonsPreparePublicationOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
CommonsPreparePublicationOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsPreparePublicationOutputVariant2Delivery = TypedDict('CommonsPreparePublicationOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[CommonsPreparePublicationOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[CommonsPreparePublicationOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[CommonsPreparePublicationOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
CommonsPreparePublicationOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsPreparePublicationOutputVariant2RecoveryOperation = TypedDict('CommonsPreparePublicationOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CommonsPreparePublicationOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsPreparePublicationOutputVariant2Recovery = TypedDict('CommonsPreparePublicationOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[CommonsPreparePublicationOutputVariant2RecoveryOperation],
})
CommonsPreparePublicationOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CommonsPreparePublicationOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: CommonsPreparePublicationOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: CommonsPreparePublicationOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(CommonsPreparePublicationOutput).
CommonsPreparePublicationOutput = Union[CommonsPreparePublicationOutputVariant2, CommonsPreparePublicationOutputVariant1]

_CommonsPreparePublicationInputAdapter = TypeAdapter(CommonsPreparePublicationInput)
_CommonsPreparePublicationOutputAdapter = TypeAdapter(CommonsPreparePublicationOutput)