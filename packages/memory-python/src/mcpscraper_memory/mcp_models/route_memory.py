from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class RouteMemoryInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    title: Annotated[str, Field(min_length=1)] = Field(..., alias='title', description='Human-readable title for the proposed record or authored content.')
    content: Annotated[str, Field(min_length=1)] = Field(..., alias='content', description='Complete content to route, validate, or store; do not substitute a partial excerpt when full content is required.')
    type: Union[str, None] = Field(None, alias='type', description='Governed content or record type used for routing and validation.')
    source: Union[str, None] = Field(None, alias='source', description='Optional source or provenance constraint appropriate to this tool; omit when no source restriction is intended.')


class RouteMemoryOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    vault: Union[str, None] = Field(None, alias='vault', description='')
    folder: Union[str, None] = Field(None, alias='folder', description='')
    reason: Union[str, None] = Field(None, alias='reason', description='')
    contract: Union[dict[str, Any], None] = Field(None, alias='contract', description='')
    error: Union[str, None] = Field(None, alias='error', description='')


RouteMemoryOutputVariant2DeliveryArtifactsItem = TypedDict('RouteMemoryOutputVariant2DeliveryArtifactsItem', {
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
RouteMemoryOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


RouteMemoryOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('RouteMemoryOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
RouteMemoryOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


RouteMemoryOutputVariant2Delivery = TypedDict('RouteMemoryOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[RouteMemoryOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[RouteMemoryOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
RouteMemoryOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


RouteMemoryOutputVariant2RecoveryOperation = TypedDict('RouteMemoryOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
RouteMemoryOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


RouteMemoryOutputVariant2Recovery = TypedDict('RouteMemoryOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[RouteMemoryOutputVariant2RecoveryOperation],
})
RouteMemoryOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class RouteMemoryOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: RouteMemoryOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: RouteMemoryOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(RouteMemoryOutput).
RouteMemoryOutput = Union[RouteMemoryOutputVariant2, RouteMemoryOutputVariant1]

_RouteMemoryInputAdapter = TypeAdapter(RouteMemoryInput)
_RouteMemoryOutputAdapter = TypeAdapter(RouteMemoryOutput)