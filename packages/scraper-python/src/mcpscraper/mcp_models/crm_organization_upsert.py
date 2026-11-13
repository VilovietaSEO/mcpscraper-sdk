from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


CrmOrganizationUpsertInputContact = TypedDict('CrmOrganizationUpsertInputContact', {
    'primaryDomain': NotRequired[Annotated[str, Field(max_length=500)]],
    'website': NotRequired[str],
    'phone': NotRequired[Annotated[str, Field(max_length=100)]],
    'address': NotRequired[Annotated[str, Field(max_length=2000)]],
})
CrmOrganizationUpsertInputContact.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CrmOrganizationUpsertInputLineage = TypedDict('CrmOrganizationUpsertInputLineage', {
    'authority': NotRequired[Literal['memory_manual', 'memory_agent', 'connected_source', 'crm_import', 'xray_derived']],
    'sensitivity': NotRequired[Literal['public', 'internal', 'personal', 'restricted']],
    'sourceRef': NotRequired[Union[Annotated[str, Field(max_length=2000)], None]],
    'observedAt': Required[str],
    'confidence': NotRequired[Union[Annotated[Union[float, int], Field(ge=0, le=1)], None]],
})
CrmOrganizationUpsertInputLineage.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class CrmOrganizationUpsertInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    entity_id: Union[str, None] = Field(None, alias='entityId', description='Existing governed entity identifier for this relation or edit.')
    base_revision: Annotated[int, Field(ge=0)] = Field(..., alias='baseRevision', description='Use 0 to create a CRM Organization; for an edit, supply entityId and the current positive revision read from crm-organization-get.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=200)] = Field(..., alias='idempotencyKey', description='Caller-owned opaque key for this intended operation; reuse only when retrying the same operation.')
    display_name: Annotated[str, Field(min_length=1, max_length=300)] = Field(..., alias='displayName', description='Human-readable person or organization name; paths, filenames, Vault references, and email-only labels are rejected.')
    content: Union[Annotated[str, Field(max_length=200000)], None] = Field(None, alias='content', description='Complete content to route, validate, or store; do not substitute a partial excerpt when full content is required.')
    relationship_types: Annotated[list[Literal['prospect', 'customer', 'former_customer', 'friend', 'coworker', 'collaborator', 'vendor', 'partner', 'advisor', 'media', 'community', 'other']], Field(min_length=1, max_length=12)] = Field(..., alias='relationshipTypes', description='One or more owner-declared relationship types; at least one is required for CRM creation.')
    relationship_status: Union[Literal['active', 'inactive', 'archived', 'merged'], None] = Field(None, alias='relationshipStatus', description='Operational relationship status independent of optional commercial lifecycle.')
    commercial_lifecycle: Union[Union[Literal['lead', 'qualified', 'opportunity', 'customer', 'retained', 'churned', 'disqualified'], None], None] = Field(None, alias='commercialLifecycle', description='Optional commercial lifecycle; friends, coworkers, and other non-commercial relationships may leave it null.')
    relationship_owner_id: Union[Union[Annotated[str, Field(max_length=300)], None], None] = Field(None, alias='relationshipOwnerId', description='Optional owner identifier responsible for the CRM relationship.')
    contact: Union[CrmOrganizationUpsertInputContact, None] = Field(None, alias='contact', description='Purpose-authorized confirmed contact projection; candidate evidence is forbidden.')
    props: Union[dict[str, Any], None] = Field(None, alias='props', description='Complete governed note properties required by the target vault contract.')
    lineage: CrmOrganizationUpsertInputLineage = Field(..., alias='lineage', description='Field authority, sensitivity, source, observation time, and confidence recorded with this governed write.')


CrmOrganizationUpsertOutputVariant1Variant1Record = TypedDict('CrmOrganizationUpsertOutputVariant1Variant1Record', {
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
CrmOrganizationUpsertOutputVariant1Variant1Record.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmOrganizationUpsertOutputVariant1Variant1Receipt = TypedDict('CrmOrganizationUpsertOutputVariant1Variant1Receipt', {
    'receiptId': Required[str],
    'replayed': NotRequired[bool],
})
CrmOrganizationUpsertOutputVariant1Variant1Receipt.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmOrganizationUpsertOutputVariant1Variant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    message: str = Field(..., alias='message', description='')
    record: Union[CrmOrganizationUpsertOutputVariant1Variant1Record, None] = Field(None, alias='record', description='')
    receipt: Union[CrmOrganizationUpsertOutputVariant1Variant1Receipt, None] = Field(None, alias='receipt', description='')
    code: Union[str, None] = Field(None, alias='code', description='')
    error: Union[str, None] = Field(None, alias='error', description='')


CrmOrganizationUpsertOutputVariant1Variant2DeliveryArtifactsItem = TypedDict('CrmOrganizationUpsertOutputVariant1Variant2DeliveryArtifactsItem', {
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
CrmOrganizationUpsertOutputVariant1Variant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmOrganizationUpsertOutputVariant1Variant2DeliveryStorageFailureVariant1 = TypedDict('CrmOrganizationUpsertOutputVariant1Variant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
CrmOrganizationUpsertOutputVariant1Variant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmOrganizationUpsertOutputVariant1Variant2Delivery = TypedDict('CrmOrganizationUpsertOutputVariant1Variant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[CrmOrganizationUpsertOutputVariant1Variant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[CrmOrganizationUpsertOutputVariant1Variant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
CrmOrganizationUpsertOutputVariant1Variant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmOrganizationUpsertOutputVariant1Variant2RecoveryOperation = TypedDict('CrmOrganizationUpsertOutputVariant1Variant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CrmOrganizationUpsertOutputVariant1Variant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmOrganizationUpsertOutputVariant1Variant2Recovery = TypedDict('CrmOrganizationUpsertOutputVariant1Variant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[CrmOrganizationUpsertOutputVariant1Variant2RecoveryOperation],
})
CrmOrganizationUpsertOutputVariant1Variant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmOrganizationUpsertOutputVariant1Variant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: CrmOrganizationUpsertOutputVariant1Variant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: CrmOrganizationUpsertOutputVariant1Variant2Recovery = Field(..., alias='recovery', description='')


CrmOrganizationUpsertOutputVariant1Variant3Operation = TypedDict('CrmOrganizationUpsertOutputVariant1Variant3Operation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CrmOrganizationUpsertOutputVariant1Variant3Operation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmOrganizationUpsertOutputVariant1Variant3(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    idempotency_key: Union[Annotated[str, Field(max_length=512)], None] = Field(None, alias='idempotencyKey', description='')
    operation: Union[CrmOrganizationUpsertOutputVariant1Variant3Operation, None] = Field(None, alias='operation', description='')
    error_code: str = Field(..., alias='error_code', description='')
    error_type: str = Field(..., alias='error_type', description='')
    message: str = Field(..., alias='message', description='')
    retryable: bool = Field(..., alias='retryable', description='')
    retry_after_seconds: Union[Union[float, int], None] = Field(None, alias='retry_after_seconds', description='')
    charge_status: Union[str, None] = Field(None, alias='charge_status', description='')
    details: Union[dict[str, Any], None] = Field(None, alias='details', description='')


# Union schema: validate external payloads with TypeAdapter(CrmOrganizationUpsertOutputVariant1).
CrmOrganizationUpsertOutputVariant1 = Union[CrmOrganizationUpsertOutputVariant1Variant2, CrmOrganizationUpsertOutputVariant1Variant3, CrmOrganizationUpsertOutputVariant1Variant1]


CrmOrganizationUpsertOutputVariant2DeliveryArtifactsItem = TypedDict('CrmOrganizationUpsertOutputVariant2DeliveryArtifactsItem', {
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
CrmOrganizationUpsertOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmOrganizationUpsertOutputVariant2DeliveryAvailableExportsItem = TypedDict('CrmOrganizationUpsertOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
CrmOrganizationUpsertOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmOrganizationUpsertOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('CrmOrganizationUpsertOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
CrmOrganizationUpsertOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmOrganizationUpsertOutputVariant2Delivery = TypedDict('CrmOrganizationUpsertOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[CrmOrganizationUpsertOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[CrmOrganizationUpsertOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[CrmOrganizationUpsertOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
CrmOrganizationUpsertOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmOrganizationUpsertOutputVariant2RecoveryOperation = TypedDict('CrmOrganizationUpsertOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CrmOrganizationUpsertOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmOrganizationUpsertOutputVariant2Recovery = TypedDict('CrmOrganizationUpsertOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[CrmOrganizationUpsertOutputVariant2RecoveryOperation],
})
CrmOrganizationUpsertOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmOrganizationUpsertOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: CrmOrganizationUpsertOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: CrmOrganizationUpsertOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(CrmOrganizationUpsertOutput).
CrmOrganizationUpsertOutput = Union[CrmOrganizationUpsertOutputVariant2, CrmOrganizationUpsertOutputVariant1]

_CrmOrganizationUpsertInputAdapter = TypeAdapter(CrmOrganizationUpsertInput)
_CrmOrganizationUpsertOutputAdapter = TypeAdapter(CrmOrganizationUpsertOutput)