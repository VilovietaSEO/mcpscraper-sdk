from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class MergeMemoryTagsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    from_: Annotated[str, Field(min_length=1)] = Field(..., alias='from', description='The duplicate tag to retire.')
    into: Annotated[str, Field(min_length=1)] = Field(..., alias='into', description='The canonical tag to keep. Every note using "from" is retagged to this.')


class MergeMemoryTagsOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    from_: Union[str, None] = Field(None, alias='from', description='')
    into: Union[str, None] = Field(None, alias='into', description='')
    notes_retagged: Union[Union[float, int], None] = Field(None, alias='notesRetagged', description='')
    aliases: Union[list[str], None] = Field(None, alias='aliases', description='')
    description_copied: Union[bool, None] = Field(None, alias='descriptionCopied', description='')
    error: Union[str, None] = Field(None, alias='error', description='')


MergeMemoryTagsOutputVariant2DeliveryArtifactsItem = TypedDict('MergeMemoryTagsOutputVariant2DeliveryArtifactsItem', {
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
MergeMemoryTagsOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MergeMemoryTagsOutputVariant2DeliveryAvailableExportsItem = TypedDict('MergeMemoryTagsOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
MergeMemoryTagsOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MergeMemoryTagsOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('MergeMemoryTagsOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
MergeMemoryTagsOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MergeMemoryTagsOutputVariant2Delivery = TypedDict('MergeMemoryTagsOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[MergeMemoryTagsOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[MergeMemoryTagsOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[MergeMemoryTagsOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
MergeMemoryTagsOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MergeMemoryTagsOutputVariant2RecoveryOperation = TypedDict('MergeMemoryTagsOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
MergeMemoryTagsOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MergeMemoryTagsOutputVariant2Recovery = TypedDict('MergeMemoryTagsOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[MergeMemoryTagsOutputVariant2RecoveryOperation],
})
MergeMemoryTagsOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class MergeMemoryTagsOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: MergeMemoryTagsOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: MergeMemoryTagsOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(MergeMemoryTagsOutput).
MergeMemoryTagsOutput = Union[MergeMemoryTagsOutputVariant2, MergeMemoryTagsOutputVariant1]

_MergeMemoryTagsInputAdapter = TypeAdapter(MergeMemoryTagsInput)
_MergeMemoryTagsOutputAdapter = TypeAdapter(MergeMemoryTagsOutput)