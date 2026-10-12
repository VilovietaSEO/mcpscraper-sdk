from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


ResearchPersonCaptureInputSourceEvidenceItem = TypedDict('ResearchPersonCaptureInputSourceEvidenceItem', {
    'sourceRef': Required[Annotated[str, Field(min_length=1, max_length=2000)]],
    'claim': NotRequired[Annotated[str, Field(max_length=4000)]],
})
ResearchPersonCaptureInputSourceEvidenceItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


ResearchPersonCaptureInputLineage = TypedDict('ResearchPersonCaptureInputLineage', {
    'authority': NotRequired[Literal['memory_manual', 'memory_agent', 'connected_source', 'crm_import', 'xray_derived']],
    'sensitivity': Required[Literal['public', 'internal', 'personal', 'restricted']],
    'sourceRef': NotRequired[Union[Annotated[str, Field(max_length=2000)], None]],
    'observedAt': Required[str],
    'confidence': NotRequired[Union[Annotated[Union[float, int], Field(ge=0, le=1)], None]],
})
ResearchPersonCaptureInputLineage.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class ResearchPersonCaptureInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    entity_id: Union[str, None] = Field(None, alias='entityId', description='Existing governed entity identifier for this relation or edit.')
    base_revision: Annotated[int, Field(ge=0)] = Field(..., alias='baseRevision', description='Use 0 to create a Research Person; for an edit, supply the current positive revision read from research-person-get.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=200)] = Field(..., alias='idempotencyKey', description='Caller-owned opaque key for this intended operation; reuse only when retrying the same operation.')
    display_name: Annotated[str, Field(min_length=1, max_length=300)] = Field(..., alias='displayName', description='Human-readable person or organization name; paths, filenames, Vault references, and email-only labels are rejected.')
    content: Union[Annotated[str, Field(max_length=200000)], None] = Field(None, alias='content', description='Complete content to route, validate, or store; do not substitute a partial excerpt when full content is required.')
    source_evidence: Annotated[list[ResearchPersonCaptureInputSourceEvidenceItem], Field(min_length=1, max_length=100)] = Field(..., alias='sourceEvidence', description='One or more cited source references supporting this Research capture.')
    topics: Union[Annotated[list[Annotated[str, Field(min_length=1, max_length=200)]], Field(max_length=100)], None] = Field(None, alias='topics', description='Research topics supported by the captured source evidence.')
    research_roles: Union[Annotated[list[Annotated[str, Field(min_length=1, max_length=200)]], Field(max_length=100)], None] = Field(None, alias='researchRoles', description='Sourced roles associated with this Research subject.')
    props: Union[dict[str, Any], None] = Field(None, alias='props', description='Complete governed note properties required by the target vault contract.')
    lineage: ResearchPersonCaptureInputLineage = Field(..., alias='lineage', description='Field authority, sensitivity, source, observation time, and confidence recorded with this governed write.')


ResearchPersonCaptureOutputVariant1Record = TypedDict('ResearchPersonCaptureOutputVariant1Record', {
    'entityId': Required[str],
    'domain': Required[Literal['research_person', 'research_organization', 'crm_person', 'crm_organization']],
    'entityKind': Required[Literal['person', 'organization']],
    'displayName': Required[str],
    'content': Required[str],
    'props': Required[dict[str, Any]],
    'relationshipStatus': Required[Union[Literal['active', 'inactive', 'archived', 'merged'], None]],
    'relationshipTypes': Required[list[Literal['prospect', 'customer', 'former_customer', 'friend', 'coworker', 'collaborator', 'vendor', 'partner', 'advisor', 'media', 'community', 'other']]],
    'commercialLifecycle': Required[Union[Literal['lead', 'qualified', 'opportunity', 'customer', 'retained', 'churned', 'disqualified'], None]],
    'relationshipOwnerId': Required[Union[str, None]],
    'topics': Required[list[str]],
    'researchRoles': Required[list[str]],
    'revision': Required[int],
    'createdAt': Required[str],
    'updatedAt': Required[str],
})
ResearchPersonCaptureOutputVariant1Record.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ResearchPersonCaptureOutputVariant1Receipt = TypedDict('ResearchPersonCaptureOutputVariant1Receipt', {
    'receiptId': Required[str],
    'replayed': NotRequired[bool],
})
ResearchPersonCaptureOutputVariant1Receipt.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ResearchPersonCaptureOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    message: str = Field(..., alias='message', description='')
    record: Union[ResearchPersonCaptureOutputVariant1Record, None] = Field(None, alias='record', description='')
    receipt: Union[ResearchPersonCaptureOutputVariant1Receipt, None] = Field(None, alias='receipt', description='')
    code: Union[str, None] = Field(None, alias='code', description='')
    error: Union[str, None] = Field(None, alias='error', description='')


ResearchPersonCaptureOutputVariant2DeliveryArtifactsItem = TypedDict('ResearchPersonCaptureOutputVariant2DeliveryArtifactsItem', {
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
ResearchPersonCaptureOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ResearchPersonCaptureOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('ResearchPersonCaptureOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
ResearchPersonCaptureOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ResearchPersonCaptureOutputVariant2Delivery = TypedDict('ResearchPersonCaptureOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[ResearchPersonCaptureOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[ResearchPersonCaptureOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
ResearchPersonCaptureOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ResearchPersonCaptureOutputVariant2RecoveryOperation = TypedDict('ResearchPersonCaptureOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
ResearchPersonCaptureOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ResearchPersonCaptureOutputVariant2Recovery = TypedDict('ResearchPersonCaptureOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[ResearchPersonCaptureOutputVariant2RecoveryOperation],
})
ResearchPersonCaptureOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ResearchPersonCaptureOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: ResearchPersonCaptureOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: ResearchPersonCaptureOutputVariant2Recovery = Field(..., alias='recovery', description='')


ResearchPersonCaptureOutputVariant3Operation = TypedDict('ResearchPersonCaptureOutputVariant3Operation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
ResearchPersonCaptureOutputVariant3Operation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ResearchPersonCaptureOutputVariant3(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    idempotency_key: Union[Annotated[str, Field(max_length=512)], None] = Field(None, alias='idempotencyKey', description='')
    operation: Union[ResearchPersonCaptureOutputVariant3Operation, None] = Field(None, alias='operation', description='')
    error_code: str = Field(..., alias='error_code', description='')
    error_type: str = Field(..., alias='error_type', description='')
    message: str = Field(..., alias='message', description='')
    retryable: bool = Field(..., alias='retryable', description='')
    retry_after_seconds: Union[Union[float, int], None] = Field(None, alias='retry_after_seconds', description='')
    charge_status: Union[str, None] = Field(None, alias='charge_status', description='')
    details: Union[dict[str, Any], None] = Field(None, alias='details', description='')


# Union schema: validate external payloads with TypeAdapter(ResearchPersonCaptureOutput).
ResearchPersonCaptureOutput = Union[ResearchPersonCaptureOutputVariant2, ResearchPersonCaptureOutputVariant3, ResearchPersonCaptureOutputVariant1]

_ResearchPersonCaptureInputAdapter = TypeAdapter(ResearchPersonCaptureInput)
_ResearchPersonCaptureOutputAdapter = TypeAdapter(ResearchPersonCaptureOutput)