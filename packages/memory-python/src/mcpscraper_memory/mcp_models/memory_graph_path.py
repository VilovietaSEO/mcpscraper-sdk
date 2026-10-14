from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class MemoryGraphPathInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    from_: Annotated[str, Field(min_length=1)] = Field(..., alias='from', description='Exact starting memory note path or resolvable note reference.')
    to: Annotated[str, Field(min_length=1)] = Field(..., alias='to', description='Exact destination memory note path or resolvable note reference.')
    from_vault: Union[str, None] = Field(None, alias='fromVault', description='Vault containing the starting memory note; omit only when the note reference already resolves unambiguously.')
    to_vault: Union[str, None] = Field(None, alias='toVault', description='Vault containing the destination memory note; omit only when the note reference already resolves unambiguously.')
    max_depth: Union[Annotated[int, Field(ge=1, le=12)], None] = Field(None, alias='maxDepth', description='Maximum number of graph edges to traverse before reporting no path.')


MemoryGraphPathOutputVariant1NodesItem = TypedDict('MemoryGraphPathOutputVariant1NodesItem', {
    'id': Required[str],
    'vault': Required[str],
    'path': Required[str],
    'title': Required[str],
    'resolved': Required[bool],
})
MemoryGraphPathOutputVariant1NodesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemoryGraphPathOutputVariant1EdgesItem = TypedDict('MemoryGraphPathOutputVariant1EdgesItem', {
    'source': Required[str],
    'target': Required[str],
    'type': Required[str],
    'evidence': Required[str],
    'sourceField': Required[str],
    'resolved': Required[bool],
})
MemoryGraphPathOutputVariant1EdgesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class MemoryGraphPathOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    nodes: Union[list[MemoryGraphPathOutputVariant1NodesItem], None] = Field(None, alias='nodes', description='')
    edges: Union[list[MemoryGraphPathOutputVariant1EdgesItem], None] = Field(None, alias='edges', description='')
    error: Union[str, None] = Field(None, alias='error', description='')


MemoryGraphPathOutputVariant2DeliveryArtifactsItem = TypedDict('MemoryGraphPathOutputVariant2DeliveryArtifactsItem', {
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
MemoryGraphPathOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemoryGraphPathOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('MemoryGraphPathOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
MemoryGraphPathOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemoryGraphPathOutputVariant2Delivery = TypedDict('MemoryGraphPathOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[MemoryGraphPathOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[MemoryGraphPathOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
MemoryGraphPathOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemoryGraphPathOutputVariant2RecoveryOperation = TypedDict('MemoryGraphPathOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
MemoryGraphPathOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemoryGraphPathOutputVariant2Recovery = TypedDict('MemoryGraphPathOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[MemoryGraphPathOutputVariant2RecoveryOperation],
})
MemoryGraphPathOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class MemoryGraphPathOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: MemoryGraphPathOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: MemoryGraphPathOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(MemoryGraphPathOutput).
MemoryGraphPathOutput = Union[MemoryGraphPathOutputVariant2, MemoryGraphPathOutputVariant1]

_MemoryGraphPathInputAdapter = TypeAdapter(MemoryGraphPathInput)
_MemoryGraphPathOutputAdapter = TypeAdapter(MemoryGraphPathOutput)