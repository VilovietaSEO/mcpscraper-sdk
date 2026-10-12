from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class MemoryBacklinksInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    note: Annotated[str, Field(min_length=1)] = Field(..., alias='note', description='Exact memory note path or resolvable note reference used as the graph target.')
    vault: Union[str, None] = Field(None, alias='vault', description='Exact accessible Memory vault name; omit only when this tool documents a safe active-vault default.')


MemoryBacklinksOutputVariant1NodesItem = TypedDict('MemoryBacklinksOutputVariant1NodesItem', {
    'id': Required[str],
    'vault': Required[str],
    'path': Required[str],
    'title': Required[str],
    'resolved': Required[bool],
})
MemoryBacklinksOutputVariant1NodesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemoryBacklinksOutputVariant1EdgesItem = TypedDict('MemoryBacklinksOutputVariant1EdgesItem', {
    'source': Required[str],
    'target': Required[str],
    'type': Required[str],
    'evidence': Required[str],
    'sourceField': Required[str],
    'resolved': Required[bool],
})
MemoryBacklinksOutputVariant1EdgesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class MemoryBacklinksOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    nodes: Union[list[MemoryBacklinksOutputVariant1NodesItem], None] = Field(None, alias='nodes', description='')
    edges: Union[list[MemoryBacklinksOutputVariant1EdgesItem], None] = Field(None, alias='edges', description='')
    error: Union[str, None] = Field(None, alias='error', description='')


MemoryBacklinksOutputVariant2DeliveryArtifactsItem = TypedDict('MemoryBacklinksOutputVariant2DeliveryArtifactsItem', {
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
MemoryBacklinksOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemoryBacklinksOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('MemoryBacklinksOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
MemoryBacklinksOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemoryBacklinksOutputVariant2Delivery = TypedDict('MemoryBacklinksOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[MemoryBacklinksOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[MemoryBacklinksOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
MemoryBacklinksOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemoryBacklinksOutputVariant2RecoveryOperation = TypedDict('MemoryBacklinksOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
MemoryBacklinksOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemoryBacklinksOutputVariant2Recovery = TypedDict('MemoryBacklinksOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[MemoryBacklinksOutputVariant2RecoveryOperation],
})
MemoryBacklinksOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class MemoryBacklinksOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: MemoryBacklinksOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: MemoryBacklinksOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(MemoryBacklinksOutput).
MemoryBacklinksOutput = Union[MemoryBacklinksOutputVariant2, MemoryBacklinksOutputVariant1]

_MemoryBacklinksInputAdapter = TypeAdapter(MemoryBacklinksInput)
_MemoryBacklinksOutputAdapter = TypeAdapter(MemoryBacklinksOutput)