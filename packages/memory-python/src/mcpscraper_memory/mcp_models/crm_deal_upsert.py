from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class CrmDealUpsertInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    deal_id: Union[str, None] = Field(None, alias='dealId', description='Stable CRM deal or opportunity identifier.')
    base_revision: Annotated[int, Field(ge=0)] = Field(..., alias='baseRevision', description='Use 0 to create a deal; for an edit, supply dealId and the current positive revision read from crm-work-get.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=200)] = Field(..., alias='idempotencyKey', description='Caller-owned opaque key for this intended operation; reuse only when retrying the same operation.')
    entity_ids: Annotated[list[str], Field(min_length=1, max_length=100)] = Field(..., alias='entityIds', description='Stable CRM entity identifiers associated with this CRM activity, task, or deal.')
    title: Annotated[str, Field(min_length=1, max_length=300)] = Field(..., alias='title', description='Human-readable title for the proposed record or authored content.')
    content: Union[Annotated[str, Field(max_length=200000)], None] = Field(None, alias='content', description='Complete content to route, validate, or store; do not substitute a partial excerpt when full content is required.')
    pipeline_id: str = Field(..., alias='pipelineId', description='Exact CRM pipeline identifier selected from authorized tenant discovery.')
    stage_id: str = Field(..., alias='stageId', description='Exact CRM stage identifier required for the conversion rule to match.')
    probability: Annotated[Union[float, int], Field(ge=0, le=1)] = Field(..., alias='probability', description='Deal probability from 0 through 1; must equal the selected stage probability returned by crm-pipeline-list.')
    party: str = Field(..., alias='party', description='Stable CRM person or organization party for the deal; this identifier must also appear in entityIds.')
    entered_at: str = Field(..., alias='enteredAt', description='ISO 8601 time when the deal entered the selected pipeline stage.')
    value: Union[Union[Annotated[Union[float, int], Field(ge=0)], None], None] = Field(None, alias='value', description='Typed bounded comparison or field value for this declarative rule.')
    currency: Union[Union[str, None], None] = Field(None, alias='currency', description='Three-letter ISO currency code for the event value.')
    props: Union[dict[str, Any], None] = Field(None, alias='props', description='Complete governed note properties required by the target vault contract.')


CrmDealUpsertOutputVariant1Record = TypedDict('CrmDealUpsertOutputVariant1Record', {
    'entityId': Required[str],
    'revision': Required[int],
    'noteId': NotRequired[str],
    'vault': NotRequired[str],
    'path': NotRequired[str],
    'associationIds': NotRequired[list[str]],
})
CrmDealUpsertOutputVariant1Record.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmDealUpsertOutputVariant1Receipt = TypedDict('CrmDealUpsertOutputVariant1Receipt', {
    'receiptId': Required[str],
    'replayed': NotRequired[bool],
})
CrmDealUpsertOutputVariant1Receipt.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmDealUpsertOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    message: str = Field(..., alias='message', description='')
    record: Union[CrmDealUpsertOutputVariant1Record, None] = Field(None, alias='record', description='')
    receipt: Union[CrmDealUpsertOutputVariant1Receipt, None] = Field(None, alias='receipt', description='')
    code: Union[str, None] = Field(None, alias='code', description='')
    error: Union[str, None] = Field(None, alias='error', description='')


CrmDealUpsertOutputVariant2DeliveryArtifactsItem = TypedDict('CrmDealUpsertOutputVariant2DeliveryArtifactsItem', {
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
CrmDealUpsertOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmDealUpsertOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('CrmDealUpsertOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
CrmDealUpsertOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmDealUpsertOutputVariant2Delivery = TypedDict('CrmDealUpsertOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[CrmDealUpsertOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[CrmDealUpsertOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
CrmDealUpsertOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmDealUpsertOutputVariant2RecoveryOperation = TypedDict('CrmDealUpsertOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CrmDealUpsertOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmDealUpsertOutputVariant2Recovery = TypedDict('CrmDealUpsertOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[CrmDealUpsertOutputVariant2RecoveryOperation],
})
CrmDealUpsertOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmDealUpsertOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: CrmDealUpsertOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: CrmDealUpsertOutputVariant2Recovery = Field(..., alias='recovery', description='')


CrmDealUpsertOutputVariant3Operation = TypedDict('CrmDealUpsertOutputVariant3Operation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CrmDealUpsertOutputVariant3Operation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmDealUpsertOutputVariant3(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    idempotency_key: Union[Annotated[str, Field(max_length=512)], None] = Field(None, alias='idempotencyKey', description='')
    operation: Union[CrmDealUpsertOutputVariant3Operation, None] = Field(None, alias='operation', description='')
    error_code: str = Field(..., alias='error_code', description='')
    error_type: str = Field(..., alias='error_type', description='')
    message: str = Field(..., alias='message', description='')
    retryable: bool = Field(..., alias='retryable', description='')
    retry_after_seconds: Union[Union[float, int], None] = Field(None, alias='retry_after_seconds', description='')
    charge_status: Union[str, None] = Field(None, alias='charge_status', description='')
    details: Union[dict[str, Any], None] = Field(None, alias='details', description='')


# Union schema: validate external payloads with TypeAdapter(CrmDealUpsertOutput).
CrmDealUpsertOutput = Union[CrmDealUpsertOutputVariant2, CrmDealUpsertOutputVariant3, CrmDealUpsertOutputVariant1]

_CrmDealUpsertInputAdapter = TypeAdapter(CrmDealUpsertInput)
_CrmDealUpsertOutputAdapter = TypeAdapter(CrmDealUpsertOutput)