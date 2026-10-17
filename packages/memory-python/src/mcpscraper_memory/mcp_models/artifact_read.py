from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class ArtifactReadInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    artifact_id: Annotated[str, Field(min_length=1, max_length=1024)] = Field(..., alias='artifactId', description='Artifact ID returned by a completed MCP result. Access remains bound to this authenticated caller.')
    offset: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(None, alias='offset', description='UTF-8 byte offset; use the exact nextOffset from the previous read.')
    max_bytes: Union[Annotated[int, Field(ge=4, le=100000)], None] = Field(None, alias='maxBytes', description='Requested maximum bytes. The common serialized response budget may return a smaller window; follow nextOffset until null for the complete file.')


class ArtifactReadOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    artifact_id: str = Field(..., alias='artifactId', description='')
    text: str = Field(..., alias='text', description='')
    total_bytes: Union[float, int] = Field(..., alias='totalBytes', description='')
    offset: Union[float, int] = Field(..., alias='offset', description='')
    consumed_bytes: Union[float, int] = Field(..., alias='consumedBytes', description='')
    next_offset: Union[Union[float, int], None] = Field(..., alias='nextOffset', description='')
    content_type: str = Field(..., alias='contentType', description='')
    sha256: Union[str, None] = Field(..., alias='sha256', description='')


ArtifactReadOutputVariant2DeliveryArtifactsItem = TypedDict('ArtifactReadOutputVariant2DeliveryArtifactsItem', {
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
ArtifactReadOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ArtifactReadOutputVariant2DeliveryAvailableExportsItem = TypedDict('ArtifactReadOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
ArtifactReadOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ArtifactReadOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('ArtifactReadOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
ArtifactReadOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ArtifactReadOutputVariant2Delivery = TypedDict('ArtifactReadOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[ArtifactReadOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[ArtifactReadOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[ArtifactReadOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
ArtifactReadOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ArtifactReadOutputVariant2RecoveryOperation = TypedDict('ArtifactReadOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
ArtifactReadOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ArtifactReadOutputVariant2Recovery = TypedDict('ArtifactReadOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[ArtifactReadOutputVariant2RecoveryOperation],
})
ArtifactReadOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ArtifactReadOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: ArtifactReadOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: ArtifactReadOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(ArtifactReadOutput).
ArtifactReadOutput = Union[ArtifactReadOutputVariant1, ArtifactReadOutputVariant2]

_ArtifactReadInputAdapter = TypeAdapter(ArtifactReadInput)
_ArtifactReadOutputAdapter = TypeAdapter(ArtifactReadOutput)