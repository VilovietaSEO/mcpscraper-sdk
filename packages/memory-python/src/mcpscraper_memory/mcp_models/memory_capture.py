from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


MemoryCaptureInputProps = TypedDict('MemoryCaptureInputProps', {
    'status': NotRequired[str],
    'summary': NotRequired[str],
    'tags': NotRequired[list[str]],
    'pinned': NotRequired[bool],
    'source_type': NotRequired[str],
    'source_ref': NotRequired[str],
    'related': NotRequired[list[str]],
    'related_vault_notes': NotRequired[list[str]],
    'embed': NotRequired[bool],
    'embed_priority': NotRequired[Literal['low', 'normal', 'high']],
    'embedding_summary': NotRequired[str],
    'type': NotRequired[str],
    'domain': NotRequired[str],
    'folder': NotRequired[str],
    'script_links': NotRequired[list[str]],
    'reference_links': NotRequired[list[str]],
    'template_links': NotRequired[list[str]],
    'parentMessageId': NotRequired[str],
})
MemoryCaptureInputProps.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


MemoryCaptureInputTagDecisionsItem = TypedDict('MemoryCaptureInputTagDecisionsItem', {
    'tag': Required[Annotated[str, Field(min_length=1)]],
    'central': Required[bool],
    'reusable': Required[bool],
    'description': NotRequired[str],
    'acceptCanonical': NotRequired[str],
})
MemoryCaptureInputTagDecisionsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class MemoryCaptureInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    vault: str = Field(..., alias='vault', description='Exact accessible Memory vault name; omit only when this tool documents a safe active-vault default.')
    folder: Union[str, None] = Field(None, alias='folder', description='Optional governed folder override inside the selected vault.')
    path: Annotated[str, Field(min_length=1)] = Field(..., alias='path', description='Exact path value used by this tool; preserve its leading slash or vault-relative form as required.')
    title: Annotated[str, Field(min_length=1)] = Field(..., alias='title', description='Human-readable title for the proposed record or authored content.')
    content: Annotated[str, Field(min_length=1)] = Field(..., alias='content', description='Complete content to route, validate, or store; do not substitute a partial excerpt when full content is required.')
    props: MemoryCaptureInputProps = Field(..., alias='props', description='Complete governed note properties required by the target vault contract.')
    base_revision: Union[Union[float, int], None] = Field(None, alias='baseRevision', description='Last revision read by the caller; supply it to reject an update if the record changed meanwhile.')
    tag_decisions: Union[Annotated[list[MemoryCaptureInputTagDecisionsItem], Field(max_length=8)], None] = Field(None, alias='tagDecisions', description="Required justification for any tag that does not already exist. Tags resolve against the account's existing vocabulary; new tags require a one-line description.")


MemoryCaptureOutputVariant1TagResolutionsItemCandidatesItem = TypedDict('MemoryCaptureOutputVariant1TagResolutionsItemCandidatesItem', {
    'tag': Required[str],
    'matchedVia': Required[str],
    'score': Required[Union[float, int]],
    'description': Required[Union[str, None]],
})
MemoryCaptureOutputVariant1TagResolutionsItemCandidatesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemoryCaptureOutputVariant1TagResolutionsItem = TypedDict('MemoryCaptureOutputVariant1TagResolutionsItem', {
    'candidate': Required[str],
    'action': Required[Literal['reuse', 'review', 'create', 'omit']],
    'tag': NotRequired[str],
    'candidates': NotRequired[list[MemoryCaptureOutputVariant1TagResolutionsItemCandidatesItem]],
    'reason': Required[str],
})
MemoryCaptureOutputVariant1TagResolutionsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemoryCaptureOutputVariant1Note = TypedDict('MemoryCaptureOutputVariant1Note', {
    'path': Required[str],
    'title': Required[str],
    'updatedAt': Required[str],
    'revision': Required[Union[float, int]],
})
MemoryCaptureOutputVariant1Note.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemoryCaptureOutputVariant1Verified = TypedDict('MemoryCaptureOutputVariant1Verified', {
    'contentBytes': Required[Union[float, int]],
    'propsPersisted': Required[bool],
    'revision': Required[Union[float, int]],
})
MemoryCaptureOutputVariant1Verified.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class MemoryCaptureOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    valid: Union[bool, None] = Field(None, alias='valid', description='')
    errors: Union[list[str], None] = Field(None, alias='errors', description='')
    warnings: Union[list[str], None] = Field(None, alias='warnings', description='')
    tag_resolutions: Union[list[MemoryCaptureOutputVariant1TagResolutionsItem], None] = Field(None, alias='tagResolutions', description='')
    note: Union[MemoryCaptureOutputVariant1Note, None] = Field(None, alias='note', description='')
    indexed: Union[Union[float, int], None] = Field(None, alias='indexed', description='')
    verified: Union[MemoryCaptureOutputVariant1Verified, None] = Field(None, alias='verified', description='')
    conflict: Union[bool, None] = Field(None, alias='conflict', description='')
    code: Union[str, None] = Field(None, alias='code', description='')
    error: Union[str, None] = Field(None, alias='error', description='')


MemoryCaptureOutputVariant2DeliveryArtifactsItem = TypedDict('MemoryCaptureOutputVariant2DeliveryArtifactsItem', {
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
MemoryCaptureOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemoryCaptureOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('MemoryCaptureOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
MemoryCaptureOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemoryCaptureOutputVariant2Delivery = TypedDict('MemoryCaptureOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[MemoryCaptureOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[MemoryCaptureOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
MemoryCaptureOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemoryCaptureOutputVariant2RecoveryOperation = TypedDict('MemoryCaptureOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
MemoryCaptureOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemoryCaptureOutputVariant2Recovery = TypedDict('MemoryCaptureOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[MemoryCaptureOutputVariant2RecoveryOperation],
})
MemoryCaptureOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class MemoryCaptureOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: MemoryCaptureOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: MemoryCaptureOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(MemoryCaptureOutput).
MemoryCaptureOutput = Union[MemoryCaptureOutputVariant2, MemoryCaptureOutputVariant1]

_MemoryCaptureInputAdapter = TypeAdapter(MemoryCaptureInput)
_MemoryCaptureOutputAdapter = TypeAdapter(MemoryCaptureOutput)