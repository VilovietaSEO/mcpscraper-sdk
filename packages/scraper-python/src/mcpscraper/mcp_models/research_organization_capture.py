from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


ResearchOrganizationCaptureInputSourceEvidenceItem = TypedDict('ResearchOrganizationCaptureInputSourceEvidenceItem', {
    'sourceRef': Required[Annotated[str, Field(min_length=1, max_length=2000)]],
    'claim': NotRequired[Annotated[str, Field(max_length=4000)]],
})
ResearchOrganizationCaptureInputSourceEvidenceItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


ResearchOrganizationCaptureInputLineage = TypedDict('ResearchOrganizationCaptureInputLineage', {
    'authority': NotRequired[Literal['memory_manual', 'memory_agent', 'connected_source', 'crm_import', 'xray_derived']],
    'sensitivity': Required[Literal['public', 'internal', 'personal', 'restricted']],
    'sourceRef': NotRequired[Union[Annotated[str, Field(max_length=2000)], None]],
    'observedAt': Required[str],
    'confidence': NotRequired[Union[Annotated[Union[float, int], Field(ge=0, le=1)], None]],
})
ResearchOrganizationCaptureInputLineage.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class ResearchOrganizationCaptureInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    entity_id: Union[str, None] = Field(None, alias='entityId', description='Existing governed entity identifier for this relation or edit.')
    base_revision: Annotated[int, Field(ge=0)] = Field(..., alias='baseRevision', description='Use 0 to create a Research Organization; for an edit, supply the current positive revision read from research-organization-get.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=200)] = Field(..., alias='idempotencyKey', description='Caller-owned opaque key for this intended operation; reuse only when retrying the same operation.')
    display_name: Annotated[str, Field(min_length=1, max_length=300)] = Field(..., alias='displayName', description='Human-readable person or organization name; paths, filenames, Vault references, and email-only labels are rejected.')
    content: Union[Annotated[str, Field(max_length=200000)], None] = Field(None, alias='content', description='Complete content to route, validate, or store; do not substitute a partial excerpt when full content is required.')
    source_evidence: Annotated[list[ResearchOrganizationCaptureInputSourceEvidenceItem], Field(min_length=1, max_length=100)] = Field(..., alias='sourceEvidence', description='One or more cited source references supporting this Research capture.')
    topics: Union[Annotated[list[Annotated[str, Field(min_length=1, max_length=200)]], Field(max_length=100)], None] = Field(None, alias='topics', description='Research topics supported by the captured source evidence.')
    research_roles: Union[Annotated[list[Annotated[str, Field(min_length=1, max_length=200)]], Field(max_length=100)], None] = Field(None, alias='researchRoles', description='Sourced roles associated with this Research subject.')
    props: Union[dict[str, Any], None] = Field(None, alias='props', description='Complete governed note properties required by the target vault contract.')
    lineage: ResearchOrganizationCaptureInputLineage = Field(..., alias='lineage', description='Field authority, sensitivity, source, observation time, and confidence recorded with this governed write.')


ResearchOrganizationCaptureOutputVariant1Record = TypedDict('ResearchOrganizationCaptureOutputVariant1Record', {
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
ResearchOrganizationCaptureOutputVariant1Record.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ResearchOrganizationCaptureOutputVariant1Receipt = TypedDict('ResearchOrganizationCaptureOutputVariant1Receipt', {
    'receiptId': Required[str],
    'replayed': NotRequired[bool],
})
ResearchOrganizationCaptureOutputVariant1Receipt.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ResearchOrganizationCaptureOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    message: str = Field(..., alias='message', description='')
    record: Union[ResearchOrganizationCaptureOutputVariant1Record, None] = Field(None, alias='record', description='')
    receipt: Union[ResearchOrganizationCaptureOutputVariant1Receipt, None] = Field(None, alias='receipt', description='')
    code: Union[str, None] = Field(None, alias='code', description='')
    error: Union[str, None] = Field(None, alias='error', description='')


ResearchOrganizationCaptureOutputVariant2DeliveryArtifactsItem = TypedDict('ResearchOrganizationCaptureOutputVariant2DeliveryArtifactsItem', {
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
ResearchOrganizationCaptureOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ResearchOrganizationCaptureOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('ResearchOrganizationCaptureOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
ResearchOrganizationCaptureOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ResearchOrganizationCaptureOutputVariant2Delivery = TypedDict('ResearchOrganizationCaptureOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[ResearchOrganizationCaptureOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[ResearchOrganizationCaptureOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
ResearchOrganizationCaptureOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ResearchOrganizationCaptureOutputVariant2RecoveryOperation = TypedDict('ResearchOrganizationCaptureOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
ResearchOrganizationCaptureOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ResearchOrganizationCaptureOutputVariant2Recovery = TypedDict('ResearchOrganizationCaptureOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[ResearchOrganizationCaptureOutputVariant2RecoveryOperation],
})
ResearchOrganizationCaptureOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ResearchOrganizationCaptureOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: ResearchOrganizationCaptureOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: ResearchOrganizationCaptureOutputVariant2Recovery = Field(..., alias='recovery', description='')


ResearchOrganizationCaptureOutputVariant3Operation = TypedDict('ResearchOrganizationCaptureOutputVariant3Operation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
ResearchOrganizationCaptureOutputVariant3Operation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ResearchOrganizationCaptureOutputVariant3(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    idempotency_key: Union[Annotated[str, Field(max_length=512)], None] = Field(None, alias='idempotencyKey', description='')
    operation: Union[ResearchOrganizationCaptureOutputVariant3Operation, None] = Field(None, alias='operation', description='')
    error_code: str = Field(..., alias='error_code', description='')
    error_type: str = Field(..., alias='error_type', description='')
    message: str = Field(..., alias='message', description='')
    retryable: bool = Field(..., alias='retryable', description='')
    retry_after_seconds: Union[Union[float, int], None] = Field(None, alias='retry_after_seconds', description='')
    charge_status: Union[str, None] = Field(None, alias='charge_status', description='')
    details: Union[dict[str, Any], None] = Field(None, alias='details', description='')


# Union schema: validate external payloads with TypeAdapter(ResearchOrganizationCaptureOutput).
ResearchOrganizationCaptureOutput = Union[ResearchOrganizationCaptureOutputVariant2, ResearchOrganizationCaptureOutputVariant3, ResearchOrganizationCaptureOutputVariant1]

_ResearchOrganizationCaptureInputAdapter = TypeAdapter(ResearchOrganizationCaptureInput)
_ResearchOrganizationCaptureOutputAdapter = TypeAdapter(ResearchOrganizationCaptureOutput)