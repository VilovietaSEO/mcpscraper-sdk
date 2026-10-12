from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


ResolveMemoryTagsInputCandidatesItem = TypedDict('ResolveMemoryTagsInputCandidatesItem', {
    'tag': Required[Annotated[str, Field(min_length=1)]],
    'central': NotRequired[bool],
    'reusable': NotRequired[bool],
    'description': NotRequired[str],
})
ResolveMemoryTagsInputCandidatesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class ResolveMemoryTagsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    candidates: Annotated[list[ResolveMemoryTagsInputCandidatesItem], Field(min_length=1, max_length=20)] = Field(..., alias='candidates', description='Proposed concepts to resolve against the canonical vocabulary.')
    accept: Union[dict[str, str], None] = Field(None, alias='accept', description='Confirm a candidate returned by an earlier review, as {proposedTag: canonicalTag}. The proposed spelling is recorded as an alias of the canonical tag so the same judgement is never re-litigated.')


ResolveMemoryTagsOutputVariant1ResolutionsItemCandidatesItem = TypedDict('ResolveMemoryTagsOutputVariant1ResolutionsItemCandidatesItem', {
    'tag': Required[str],
    'matchedVia': Required[Literal['key', 'alias', 'stem', 'trigram', 'embedding']],
    'score': Required[Union[float, int]],
    'description': Required[Union[str, None]],
})
ResolveMemoryTagsOutputVariant1ResolutionsItemCandidatesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ResolveMemoryTagsOutputVariant1ResolutionsItem = TypedDict('ResolveMemoryTagsOutputVariant1ResolutionsItem', {
    'candidate': Required[str],
    'normalized': Required[str],
    'action': Required[Literal['reuse', 'review', 'create', 'omit']],
    'tag': NotRequired[str],
    'matchedBy': NotRequired[Literal['exact', 'alias', 'near']],
    'matchedVia': NotRequired[Literal['key', 'alias', 'stem', 'trigram', 'embedding']],
    'score': NotRequired[Union[float, int]],
    'candidates': NotRequired[list[ResolveMemoryTagsOutputVariant1ResolutionsItemCandidatesItem]],
    'reason': Required[str],
})
ResolveMemoryTagsOutputVariant1ResolutionsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ResolveMemoryTagsOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    resolutions: Union[list[ResolveMemoryTagsOutputVariant1ResolutionsItem], None] = Field(None, alias='resolutions', description='')
    error: Union[str, None] = Field(None, alias='error', description='')


ResolveMemoryTagsOutputVariant2DeliveryArtifactsItem = TypedDict('ResolveMemoryTagsOutputVariant2DeliveryArtifactsItem', {
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
ResolveMemoryTagsOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ResolveMemoryTagsOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('ResolveMemoryTagsOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
ResolveMemoryTagsOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ResolveMemoryTagsOutputVariant2Delivery = TypedDict('ResolveMemoryTagsOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[ResolveMemoryTagsOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[ResolveMemoryTagsOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
ResolveMemoryTagsOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ResolveMemoryTagsOutputVariant2RecoveryOperation = TypedDict('ResolveMemoryTagsOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
ResolveMemoryTagsOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ResolveMemoryTagsOutputVariant2Recovery = TypedDict('ResolveMemoryTagsOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[ResolveMemoryTagsOutputVariant2RecoveryOperation],
})
ResolveMemoryTagsOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ResolveMemoryTagsOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: ResolveMemoryTagsOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: ResolveMemoryTagsOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(ResolveMemoryTagsOutput).
ResolveMemoryTagsOutput = Union[ResolveMemoryTagsOutputVariant2, ResolveMemoryTagsOutputVariant1]

_ResolveMemoryTagsInputAdapter = TypeAdapter(ResolveMemoryTagsInput)
_ResolveMemoryTagsOutputAdapter = TypeAdapter(ResolveMemoryTagsOutput)