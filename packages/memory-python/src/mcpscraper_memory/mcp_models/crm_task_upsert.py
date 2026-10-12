from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class CrmTaskUpsertInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    task_id: Union[str, None] = Field(None, alias='taskId', description='Stable CRM Task entity identifier for create or revision-checked update.')
    entity_id: Union[str, None] = Field(None, alias='entityId', description='Existing governed entity identifier for this relation or edit.')
    base_revision: Union[Annotated[int, Field(ge=0)], None] = Field(None, alias='baseRevision', description='Last revision read by the caller; supply it to reject an update if the record changed meanwhile.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=200)] = Field(..., alias='idempotencyKey', description='Caller-owned opaque key for this intended operation; reuse only when retrying the same operation.')
    person_entity_id: Union[str, None] = Field(None, alias='personEntityId', description='Stable CRM Person entity identifier; Research identifiers are rejected.')
    communication_entity_id: Union[str, None] = Field(None, alias='communicationEntityId', description='Stable CRM Communication entity identifier returned by the activity append operation.')
    entity_ids: Union[Annotated[list[str], Field(max_length=100)], None] = Field(None, alias='entityIds', description='Stable CRM entity identifiers associated with this CRM activity, task, or deal.')
    title: Annotated[str, Field(min_length=1, max_length=300)] = Field(..., alias='title', description='Human-readable title for the proposed record or authored content.')
    content: Union[Annotated[str, Field(max_length=200000)], None] = Field(None, alias='content', description='Complete content to route, validate, or store; do not substitute a partial excerpt when full content is required.')
    status: Union[Literal['todo', 'in_progress', 'blocked', 'done', 'cancelled'], None] = Field(None, alias='status', description='Lifecycle status used to filter or update the selected records.')
    due_at: Union[Union[str, None], None] = Field(None, alias='dueAt', description='Optional ISO 8601 due time for the CRM Task.')
    source: Union[dict[str, Any], None] = Field(None, alias='source', description='Optional source or provenance constraint appropriate to this tool; omit when no source restriction is intended.')
    props: Union[dict[str, Any], None] = Field(None, alias='props', description='Complete governed note properties required by the target vault contract.')


CrmTaskUpsertOutputVariant1Record = TypedDict('CrmTaskUpsertOutputVariant1Record', {
    'entityId': Required[str],
    'revision': Required[int],
    'noteId': NotRequired[str],
    'vault': NotRequired[str],
    'path': NotRequired[str],
    'associationIds': NotRequired[list[str]],
})
CrmTaskUpsertOutputVariant1Record.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmTaskUpsertOutputVariant1Receipt = TypedDict('CrmTaskUpsertOutputVariant1Receipt', {
    'receiptId': Required[str],
    'replayed': NotRequired[bool],
})
CrmTaskUpsertOutputVariant1Receipt.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmTaskUpsertOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    message: str = Field(..., alias='message', description='')
    record: Union[CrmTaskUpsertOutputVariant1Record, None] = Field(None, alias='record', description='')
    receipt: Union[CrmTaskUpsertOutputVariant1Receipt, None] = Field(None, alias='receipt', description='')
    code: Union[str, None] = Field(None, alias='code', description='')
    error: Union[str, None] = Field(None, alias='error', description='')


CrmTaskUpsertOutputVariant2DeliveryArtifactsItem = TypedDict('CrmTaskUpsertOutputVariant2DeliveryArtifactsItem', {
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
CrmTaskUpsertOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmTaskUpsertOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('CrmTaskUpsertOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
CrmTaskUpsertOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmTaskUpsertOutputVariant2Delivery = TypedDict('CrmTaskUpsertOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[CrmTaskUpsertOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[CrmTaskUpsertOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
CrmTaskUpsertOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmTaskUpsertOutputVariant2RecoveryOperation = TypedDict('CrmTaskUpsertOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CrmTaskUpsertOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmTaskUpsertOutputVariant2Recovery = TypedDict('CrmTaskUpsertOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[CrmTaskUpsertOutputVariant2RecoveryOperation],
})
CrmTaskUpsertOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmTaskUpsertOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: CrmTaskUpsertOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: CrmTaskUpsertOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(CrmTaskUpsertOutput).
CrmTaskUpsertOutput = Union[CrmTaskUpsertOutputVariant2, CrmTaskUpsertOutputVariant1]

_CrmTaskUpsertInputAdapter = TypeAdapter(CrmTaskUpsertInput)
_CrmTaskUpsertOutputAdapter = TypeAdapter(CrmTaskUpsertOutput)