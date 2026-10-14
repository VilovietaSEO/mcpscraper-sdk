from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


ResolveLocalSourcebookTagsInputCandidatesItem = TypedDict('ResolveLocalSourcebookTagsInputCandidatesItem', {
    'tag': Required[Annotated[str, Field(min_length=1, max_length=60)]],
    'central': NotRequired[bool],
    'reusable': NotRequired[bool],
    'description': NotRequired[Annotated[str, Field(min_length=8, max_length=240)]],
})
ResolveLocalSourcebookTagsInputCandidatesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class ResolveLocalSourcebookTagsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    candidates: Annotated[list[ResolveLocalSourcebookTagsInputCandidatesItem], Field(min_length=1, max_length=20)] = Field(..., alias='candidates', description='Proposed reusable directory concepts to resolve against the live vocabulary.')


class ResolveLocalSourcebookTagsOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)



ResolveLocalSourcebookTagsOutputVariant2DeliveryArtifactsItem = TypedDict('ResolveLocalSourcebookTagsOutputVariant2DeliveryArtifactsItem', {
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
ResolveLocalSourcebookTagsOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ResolveLocalSourcebookTagsOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('ResolveLocalSourcebookTagsOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
ResolveLocalSourcebookTagsOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ResolveLocalSourcebookTagsOutputVariant2Delivery = TypedDict('ResolveLocalSourcebookTagsOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[ResolveLocalSourcebookTagsOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[ResolveLocalSourcebookTagsOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
ResolveLocalSourcebookTagsOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ResolveLocalSourcebookTagsOutputVariant2RecoveryOperation = TypedDict('ResolveLocalSourcebookTagsOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
ResolveLocalSourcebookTagsOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ResolveLocalSourcebookTagsOutputVariant2Recovery = TypedDict('ResolveLocalSourcebookTagsOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[ResolveLocalSourcebookTagsOutputVariant2RecoveryOperation],
})
ResolveLocalSourcebookTagsOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ResolveLocalSourcebookTagsOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: ResolveLocalSourcebookTagsOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: ResolveLocalSourcebookTagsOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(ResolveLocalSourcebookTagsOutput).
ResolveLocalSourcebookTagsOutput = Union[ResolveLocalSourcebookTagsOutputVariant2, ResolveLocalSourcebookTagsOutputVariant1]

_ResolveLocalSourcebookTagsInputAdapter = TypeAdapter(ResolveLocalSourcebookTagsInput)
_ResolveLocalSourcebookTagsOutputAdapter = TypeAdapter(ResolveLocalSourcebookTagsOutput)