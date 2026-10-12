from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


CrmPersonUpsertInputContact = TypedDict('CrmPersonUpsertInputContact', {
    'email': NotRequired[str],
    'phone': NotRequired[Annotated[str, Field(max_length=100)]],
    'address': NotRequired[Annotated[str, Field(max_length=2000)]],
})
CrmPersonUpsertInputContact.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CrmPersonUpsertInputSource = TypedDict('CrmPersonUpsertInputSource', {
    'kind': Required[str],
    'siteId': NotRequired[str],
    'formId': NotRequired[str],
    'submissionId': NotRequired[str],
    'observedAt': Required[str],
})
CrmPersonUpsertInputSource.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CrmPersonUpsertInputLineage = TypedDict('CrmPersonUpsertInputLineage', {
    'authority': NotRequired[Literal['memory_manual', 'memory_agent', 'connected_source', 'crm_import', 'xray_derived']],
    'sensitivity': NotRequired[Literal['public', 'internal', 'personal', 'restricted']],
    'sourceRef': NotRequired[Union[Annotated[str, Field(max_length=2000)], None]],
    'observedAt': Required[str],
    'confidence': NotRequired[Union[Annotated[Union[float, int], Field(ge=0, le=1)], None]],
})
CrmPersonUpsertInputLineage.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class CrmPersonUpsertInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    entity_id: Union[str, None] = Field(None, alias='entityId', description='Existing governed entity identifier for this relation or edit.')
    base_revision: Union[Annotated[int, Field(ge=0)], None] = Field(None, alias='baseRevision', description='Last revision read by the caller; supply it to reject an update if the record changed meanwhile.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=200)] = Field(..., alias='idempotencyKey', description='Caller-owned opaque key for this intended operation; reuse only when retrying the same operation.')
    display_name: Annotated[str, Field(min_length=1, max_length=300)] = Field(..., alias='displayName', description='Human-readable person or organization name; paths, filenames, Vault references, and email-only labels are rejected.')
    content: Union[Annotated[str, Field(max_length=200000)], None] = Field(None, alias='content', description='Complete content to route, validate, or store; do not substitute a partial excerpt when full content is required.')
    relationship_types: Annotated[list[Literal['prospect', 'customer', 'former_customer', 'friend', 'coworker', 'collaborator', 'vendor', 'partner', 'advisor', 'media', 'community', 'other']], Field(min_length=1, max_length=12)] = Field(..., alias='relationshipTypes', description='One or more owner-declared relationship types; at least one is required for CRM creation.')
    relationship_status: Union[Literal['active', 'inactive', 'archived', 'merged'], None] = Field(None, alias='relationshipStatus', description='Operational relationship status independent of optional commercial lifecycle.')
    commercial_lifecycle: Union[Union[Literal['lead', 'qualified', 'opportunity', 'customer', 'retained', 'churned', 'disqualified'], None], None] = Field(None, alias='commercialLifecycle', description='Optional commercial lifecycle; friends, coworkers, and other non-commercial relationships may leave it null.')
    relationship_owner_id: Union[Union[Annotated[str, Field(max_length=300)], None], None] = Field(None, alias='relationshipOwnerId', description='Optional owner identifier responsible for the CRM relationship.')
    contact: Union[CrmPersonUpsertInputContact, None] = Field(None, alias='contact', description='Purpose-authorized confirmed contact projection; candidate evidence is forbidden.')
    email: Union[str, None] = Field(None, alias='email', description='Bridge-compatible top-level email; normalized into contact provenance.')
    phone: Union[Annotated[str, Field(max_length=100)], None] = Field(None, alias='phone', description='Bridge-compatible top-level phone; normalized into contact provenance.')
    organization_name: Union[Annotated[str, Field(max_length=300)], None] = Field(None, alias='organizationName', description='Bridge-compatible organization label; it never creates or resolves an organization by inference.')
    source: Union[CrmPersonUpsertInputSource, None] = Field(None, alias='source', description='Optional source or provenance constraint appropriate to this tool; omit when no source restriction is intended.')
    props: Union[dict[str, Any], None] = Field(None, alias='props', description='Complete governed note properties required by the target vault contract.')
    lineage: Union[CrmPersonUpsertInputLineage, None] = Field(None, alias='lineage', description='Field authority, sensitivity, source, observation time, and confidence recorded with this governed write.')


CrmPersonUpsertOutputVariant1Record = TypedDict('CrmPersonUpsertOutputVariant1Record', {
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
CrmPersonUpsertOutputVariant1Record.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmPersonUpsertOutputVariant1Receipt = TypedDict('CrmPersonUpsertOutputVariant1Receipt', {
    'receiptId': Required[str],
    'replayed': NotRequired[bool],
})
CrmPersonUpsertOutputVariant1Receipt.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmPersonUpsertOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    message: str = Field(..., alias='message', description='')
    record: Union[CrmPersonUpsertOutputVariant1Record, None] = Field(None, alias='record', description='')
    receipt: Union[CrmPersonUpsertOutputVariant1Receipt, None] = Field(None, alias='receipt', description='')
    code: Union[str, None] = Field(None, alias='code', description='')
    error: Union[str, None] = Field(None, alias='error', description='')


CrmPersonUpsertOutputVariant2DeliveryArtifactsItem = TypedDict('CrmPersonUpsertOutputVariant2DeliveryArtifactsItem', {
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
CrmPersonUpsertOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmPersonUpsertOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('CrmPersonUpsertOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
CrmPersonUpsertOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmPersonUpsertOutputVariant2Delivery = TypedDict('CrmPersonUpsertOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[CrmPersonUpsertOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[CrmPersonUpsertOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
CrmPersonUpsertOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmPersonUpsertOutputVariant2RecoveryOperation = TypedDict('CrmPersonUpsertOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CrmPersonUpsertOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmPersonUpsertOutputVariant2Recovery = TypedDict('CrmPersonUpsertOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[CrmPersonUpsertOutputVariant2RecoveryOperation],
})
CrmPersonUpsertOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmPersonUpsertOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: CrmPersonUpsertOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: CrmPersonUpsertOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(CrmPersonUpsertOutput).
CrmPersonUpsertOutput = Union[CrmPersonUpsertOutputVariant2, CrmPersonUpsertOutputVariant1]

_CrmPersonUpsertInputAdapter = TypeAdapter(CrmPersonUpsertInput)
_CrmPersonUpsertOutputAdapter = TypeAdapter(CrmPersonUpsertOutput)