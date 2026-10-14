from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class CrmActivityAppendInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    idempotency_key: Annotated[str, Field(min_length=8, max_length=200)] = Field(..., alias='idempotencyKey', description='Caller-owned opaque key for this intended operation; reuse only when retrying the same operation.')
    entity_id: Union[str, None] = Field(None, alias='entityId', description='Optional stable ID for this new activity work record, not a CRM person or organization ID.')
    person_entity_id: Union[str, None] = Field(None, alias='personEntityId', description='CRM Person entity ID to associate with this activity.')
    entity_ids: Union[Annotated[list[str], Field(max_length=100)], None] = Field(None, alias='entityIds', description='CRM person or organization entity IDs associated with this activity; at least one association is required.')
    activity_type: Union[Literal['call', 'meeting', 'email', 'message', 'form', 'form_submission', 'conversion', 'note', 'calendar_event'], None] = Field(None, alias='activityType', description='Canonical CRM activity family recorded on the associated CRM relationship.')
    kind: Union[Literal['form_submission'], None] = Field(None, alias='kind', description='Governed type discriminator for this rule, score, event, or record.')
    occurred_at: str = Field(..., alias='occurredAt', description='ISO 8601 timestamp when the source event actually occurred.')
    title: Union[Annotated[str, Field(min_length=1, max_length=300)], None] = Field(None, alias='title', description='Human-readable title for the proposed record or authored content.')
    content: Union[Annotated[str, Field(max_length=200000)], None] = Field(None, alias='content', description='Complete content to route, validate, or store; do not substitute a partial excerpt when full content is required.')
    submitted_fields: Union[dict[str, Any], None] = Field(None, alias='submittedFields', description='Bounded submitted form fields retained only on the canonical CRM Communication.')
    source: Union[dict[str, Any], None] = Field(None, alias='source', description='Optional source provenance stored with the CRM activity; this is not a record filter.')
    props: Union[dict[str, Any], None] = Field(None, alias='props', description='Complete governed note properties required by the target vault contract.')


CrmActivityAppendOutputVariant1Record = TypedDict('CrmActivityAppendOutputVariant1Record', {
    'entityId': Required[str],
    'revision': Required[int],
    'noteId': NotRequired[str],
    'vault': NotRequired[str],
    'path': NotRequired[str],
    'associationIds': NotRequired[list[str]],
})
CrmActivityAppendOutputVariant1Record.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmActivityAppendOutputVariant1Receipt = TypedDict('CrmActivityAppendOutputVariant1Receipt', {
    'receiptId': Required[str],
    'replayed': NotRequired[bool],
})
CrmActivityAppendOutputVariant1Receipt.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmActivityAppendOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    message: str = Field(..., alias='message', description='')
    record: Union[CrmActivityAppendOutputVariant1Record, None] = Field(None, alias='record', description='')
    receipt: Union[CrmActivityAppendOutputVariant1Receipt, None] = Field(None, alias='receipt', description='')
    code: Union[str, None] = Field(None, alias='code', description='')
    error: Union[str, None] = Field(None, alias='error', description='')


CrmActivityAppendOutputVariant2DeliveryArtifactsItem = TypedDict('CrmActivityAppendOutputVariant2DeliveryArtifactsItem', {
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
CrmActivityAppendOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmActivityAppendOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('CrmActivityAppendOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
CrmActivityAppendOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmActivityAppendOutputVariant2Delivery = TypedDict('CrmActivityAppendOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[CrmActivityAppendOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[CrmActivityAppendOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
CrmActivityAppendOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmActivityAppendOutputVariant2RecoveryOperation = TypedDict('CrmActivityAppendOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CrmActivityAppendOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmActivityAppendOutputVariant2Recovery = TypedDict('CrmActivityAppendOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[CrmActivityAppendOutputVariant2RecoveryOperation],
})
CrmActivityAppendOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmActivityAppendOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: CrmActivityAppendOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: CrmActivityAppendOutputVariant2Recovery = Field(..., alias='recovery', description='')


CrmActivityAppendOutputVariant3Operation = TypedDict('CrmActivityAppendOutputVariant3Operation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CrmActivityAppendOutputVariant3Operation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmActivityAppendOutputVariant3(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    idempotency_key: Union[Annotated[str, Field(max_length=512)], None] = Field(None, alias='idempotencyKey', description='')
    operation: Union[CrmActivityAppendOutputVariant3Operation, None] = Field(None, alias='operation', description='')
    error_code: str = Field(..., alias='error_code', description='')
    error_type: str = Field(..., alias='error_type', description='')
    message: str = Field(..., alias='message', description='')
    retryable: bool = Field(..., alias='retryable', description='')
    retry_after_seconds: Union[Union[float, int], None] = Field(None, alias='retry_after_seconds', description='')
    charge_status: Union[str, None] = Field(None, alias='charge_status', description='')
    details: Union[dict[str, Any], None] = Field(None, alias='details', description='')


# Union schema: validate external payloads with TypeAdapter(CrmActivityAppendOutput).
CrmActivityAppendOutput = Union[CrmActivityAppendOutputVariant2, CrmActivityAppendOutputVariant3, CrmActivityAppendOutputVariant1]

_CrmActivityAppendInputAdapter = TypeAdapter(CrmActivityAppendInput)
_CrmActivityAppendOutputAdapter = TypeAdapter(CrmActivityAppendOutput)