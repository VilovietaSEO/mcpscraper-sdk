from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


PrepareMemoryWriteInputTagCandidatesItem = TypedDict('PrepareMemoryWriteInputTagCandidatesItem', {
    'tag': Required[Annotated[str, Field(min_length=1)]],
    'central': NotRequired[bool],
    'reusable': NotRequired[bool],
    'description': NotRequired[str],
})
PrepareMemoryWriteInputTagCandidatesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class PrepareMemoryWriteInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    title: Annotated[str, Field(min_length=1)] = Field(..., alias='title', description='Human-readable title for the proposed record or authored content.')
    content: Annotated[str, Field(min_length=1)] = Field(..., alias='content', description='Complete content to route, validate, or store; do not substitute a partial excerpt when full content is required.')
    source: Union[str, None] = Field(None, alias='source', description='Optional source or provenance constraint appropriate to this tool; omit when no source restriction is intended.')
    type: Union[str, None] = Field(None, alias='type', description='Governed content or record type used for routing and validation.')
    vault: Union[str, None] = Field(None, alias='vault', description='Exact accessible Memory vault name; omit only when this tool documents a safe active-vault default.')
    tag_candidates: Union[Annotated[list[PrepareMemoryWriteInputTagCandidatesItem], Field(max_length=20)], None] = Field(None, alias='tagCandidates', description='Proposed listing or memory tags to resolve against the live canonical vocabulary.')
    max_links: Union[Annotated[int, Field(ge=1, le=20)], None] = Field(None, alias='maxLinks', description='Maximum related-note candidates to return from the planning pass.')


class PrepareMemoryWriteOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    route: Union[dict[str, Any], None] = Field(None, alias='route', description='')
    contract: Union[dict[str, Any], None] = Field(None, alias='contract', description='')
    tag_resolutions: Union[list[dict[str, Any]], None] = Field(None, alias='tagResolutions', description='')
    link_opportunities: Union[list[dict[str, Any]], None] = Field(None, alias='linkOpportunities', description='')
    instructions: Union[list[str], None] = Field(None, alias='instructions', description='')
    error: Union[str, None] = Field(None, alias='error', description='')


PrepareMemoryWriteOutputVariant2DeliveryArtifactsItem = TypedDict('PrepareMemoryWriteOutputVariant2DeliveryArtifactsItem', {
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
PrepareMemoryWriteOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


PrepareMemoryWriteOutputVariant2DeliveryAvailableExportsItem = TypedDict('PrepareMemoryWriteOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
PrepareMemoryWriteOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


PrepareMemoryWriteOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('PrepareMemoryWriteOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
PrepareMemoryWriteOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


PrepareMemoryWriteOutputVariant2Delivery = TypedDict('PrepareMemoryWriteOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[PrepareMemoryWriteOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[PrepareMemoryWriteOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[PrepareMemoryWriteOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
PrepareMemoryWriteOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


PrepareMemoryWriteOutputVariant2RecoveryOperation = TypedDict('PrepareMemoryWriteOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
PrepareMemoryWriteOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


PrepareMemoryWriteOutputVariant2Recovery = TypedDict('PrepareMemoryWriteOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[PrepareMemoryWriteOutputVariant2RecoveryOperation],
})
PrepareMemoryWriteOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class PrepareMemoryWriteOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: PrepareMemoryWriteOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: PrepareMemoryWriteOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(PrepareMemoryWriteOutput).
PrepareMemoryWriteOutput = Union[PrepareMemoryWriteOutputVariant2, PrepareMemoryWriteOutputVariant1]

_PrepareMemoryWriteInputAdapter = TypeAdapter(PrepareMemoryWriteInput)
_PrepareMemoryWriteOutputAdapter = TypeAdapter(PrepareMemoryWriteOutput)