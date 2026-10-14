from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class MemoryGraphUniverseInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    note: Annotated[str, Field(min_length=1)] = Field(..., alias='note', description='Exact memory note path or resolvable note reference used as the graph target.')
    vault: Union[str, None] = Field(None, alias='vault', description='Exact accessible Memory vault name; omit only when this tool documents a safe active-vault default.')
    depth: Union[Annotated[int, Field(ge=0, le=6)], None] = Field(None, alias='depth', description='Maximum graph traversal depth from the root note.')
    max_nodes: Union[Annotated[int, Field(ge=1, le=500)], None] = Field(None, alias='maxNodes', description='Maximum graph nodes to return before marking the result truncated.')


MemoryGraphUniverseOutputVariant1NodesItem = TypedDict('MemoryGraphUniverseOutputVariant1NodesItem', {
    'id': Required[str],
    'vault': Required[str],
    'path': Required[str],
    'title': Required[str],
    'resolved': Required[bool],
})
MemoryGraphUniverseOutputVariant1NodesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemoryGraphUniverseOutputVariant1EdgesItem = TypedDict('MemoryGraphUniverseOutputVariant1EdgesItem', {
    'source': Required[str],
    'target': Required[str],
    'type': Required[str],
    'evidence': Required[str],
    'sourceField': Required[str],
    'resolved': Required[bool],
})
MemoryGraphUniverseOutputVariant1EdgesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class MemoryGraphUniverseOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    root: Union[str, None] = Field(None, alias='root', description='')
    depth: Union[Union[float, int], None] = Field(None, alias='depth', description='')
    truncated: Union[bool, None] = Field(None, alias='truncated', description='')
    nodes: Union[list[MemoryGraphUniverseOutputVariant1NodesItem], None] = Field(None, alias='nodes', description='')
    edges: Union[list[MemoryGraphUniverseOutputVariant1EdgesItem], None] = Field(None, alias='edges', description='')
    error: Union[str, None] = Field(None, alias='error', description='')


MemoryGraphUniverseOutputVariant2DeliveryArtifactsItem = TypedDict('MemoryGraphUniverseOutputVariant2DeliveryArtifactsItem', {
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
MemoryGraphUniverseOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemoryGraphUniverseOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('MemoryGraphUniverseOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
MemoryGraphUniverseOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemoryGraphUniverseOutputVariant2Delivery = TypedDict('MemoryGraphUniverseOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[MemoryGraphUniverseOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[MemoryGraphUniverseOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
MemoryGraphUniverseOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemoryGraphUniverseOutputVariant2RecoveryOperation = TypedDict('MemoryGraphUniverseOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
MemoryGraphUniverseOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemoryGraphUniverseOutputVariant2Recovery = TypedDict('MemoryGraphUniverseOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[MemoryGraphUniverseOutputVariant2RecoveryOperation],
})
MemoryGraphUniverseOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class MemoryGraphUniverseOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: MemoryGraphUniverseOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: MemoryGraphUniverseOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(MemoryGraphUniverseOutput).
MemoryGraphUniverseOutput = Union[MemoryGraphUniverseOutputVariant2, MemoryGraphUniverseOutputVariant1]

_MemoryGraphUniverseInputAdapter = TypeAdapter(MemoryGraphUniverseInput)
_MemoryGraphUniverseOutputAdapter = TypeAdapter(MemoryGraphUniverseOutput)