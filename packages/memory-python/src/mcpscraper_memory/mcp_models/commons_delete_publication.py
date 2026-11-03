from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class CommonsDeletePublicationInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    publication_subdomain: Annotated[str, Field(min_length=3, max_length=50)] = Field(..., alias='publicationSubdomain', description='Caller-owned publication whose stored editions will all be deleted.')
    base_revision: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='baseRevision', description='Publication revision from commons_get_publication, not an edition revision.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=200)] = Field(..., alias='idempotencyKey', description='Unique key for this deletion; reuse only for an exact retry.')


CommonsDeletePublicationOutputVariant1Data = TypedDict('CommonsDeletePublicationOutputVariant1Data', {
    'deleted': Required[Literal[True]],
    'subdomain': Required[str],
    'nameReserved': Required[Literal[True]],
    'revision': Required[Annotated[int, Field(ge=1, le=9007199254740991)]],
    'idempotentReplay': Required[bool],
})
CommonsDeletePublicationOutputVariant1Data.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CommonsDeletePublicationOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    data: Union[CommonsDeletePublicationOutputVariant1Data, None] = Field(None, alias='data', description='')
    error: Union[str, None] = Field(None, alias='error', description='')
    message: Union[str, None] = Field(None, alias='message', description='')


CommonsDeletePublicationOutputVariant2DeliveryArtifactsItem = TypedDict('CommonsDeletePublicationOutputVariant2DeliveryArtifactsItem', {
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
CommonsDeletePublicationOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsDeletePublicationOutputVariant2DeliveryAvailableExportsItem = TypedDict('CommonsDeletePublicationOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
CommonsDeletePublicationOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsDeletePublicationOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('CommonsDeletePublicationOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
CommonsDeletePublicationOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsDeletePublicationOutputVariant2Delivery = TypedDict('CommonsDeletePublicationOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[CommonsDeletePublicationOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[CommonsDeletePublicationOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[CommonsDeletePublicationOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
CommonsDeletePublicationOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsDeletePublicationOutputVariant2RecoveryOperation = TypedDict('CommonsDeletePublicationOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CommonsDeletePublicationOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsDeletePublicationOutputVariant2Recovery = TypedDict('CommonsDeletePublicationOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[CommonsDeletePublicationOutputVariant2RecoveryOperation],
})
CommonsDeletePublicationOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CommonsDeletePublicationOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: CommonsDeletePublicationOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: CommonsDeletePublicationOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(CommonsDeletePublicationOutput).
CommonsDeletePublicationOutput = Union[CommonsDeletePublicationOutputVariant2, CommonsDeletePublicationOutputVariant1]

_CommonsDeletePublicationInputAdapter = TypeAdapter(CommonsDeletePublicationInput)
_CommonsDeletePublicationOutputAdapter = TypeAdapter(CommonsDeletePublicationOutput)