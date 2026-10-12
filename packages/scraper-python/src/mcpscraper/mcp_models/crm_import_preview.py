from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


CrmImportPreviewInputRowsItem = TypedDict('CrmImportPreviewInputRowsItem', {
    'rowNumber': Required[Annotated[int, Field(ge=1)]],
    'domain': Required[Literal['crm_person', 'crm_organization']],
    'values': Required[dict[str, Any]],
})
CrmImportPreviewInputRowsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class CrmImportPreviewInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    idempotency_key: Annotated[str, Field(min_length=8, max_length=200)] = Field(..., alias='idempotencyKey', description='Caller-owned opaque key for this intended operation; reuse only when retrying the same operation.')
    ttl_minutes: Union[Annotated[int, Field(ge=5, le=1440)], None] = Field(None, alias='ttlMinutes', description='Bounded preview lifetime in minutes before the plan expires.')
    mapping: dict[str, str] = Field(..., alias='mapping', description='CSV-column mapping used to identify and protect supported CRM fields.')
    rows: Annotated[list[CrmImportPreviewInputRowsItem], Field(min_length=1, max_length=50000)] = Field(..., alias='rows', description='Bounded normalized import rows; every row must target crm_person or crm_organization.')


CrmImportPreviewOutputVariant1Plan = TypedDict('CrmImportPreviewOutputVariant1Plan', {
    'importId': Required[str],
    'planHandle': Required[str],
    'digest': Required[str],
    'expiresAt': Required[str],
    'acceptedRows': Required[int],
    'rejectedRows': Required[int],
    'issues': Required[list[dict[str, Any]]],
    'duplicateCandidates': Required[list[dict[str, Any]]],
    'totalIssues': Required[int],
    'totalDuplicateCandidates': Required[int],
    'resultTruncated': Required[bool],
})
CrmImportPreviewOutputVariant1Plan.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmImportPreviewOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    message: str = Field(..., alias='message', description='')
    plan: Union[CrmImportPreviewOutputVariant1Plan, None] = Field(None, alias='plan', description='')
    code: Union[str, None] = Field(None, alias='code', description='')
    error: Union[str, None] = Field(None, alias='error', description='')


CrmImportPreviewOutputVariant2DeliveryArtifactsItem = TypedDict('CrmImportPreviewOutputVariant2DeliveryArtifactsItem', {
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
CrmImportPreviewOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmImportPreviewOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('CrmImportPreviewOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
CrmImportPreviewOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmImportPreviewOutputVariant2Delivery = TypedDict('CrmImportPreviewOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[CrmImportPreviewOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[CrmImportPreviewOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
CrmImportPreviewOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmImportPreviewOutputVariant2RecoveryOperation = TypedDict('CrmImportPreviewOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CrmImportPreviewOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmImportPreviewOutputVariant2Recovery = TypedDict('CrmImportPreviewOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[CrmImportPreviewOutputVariant2RecoveryOperation],
})
CrmImportPreviewOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmImportPreviewOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: CrmImportPreviewOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: CrmImportPreviewOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(CrmImportPreviewOutput).
CrmImportPreviewOutput = Union[CrmImportPreviewOutputVariant2, CrmImportPreviewOutputVariant1]

_CrmImportPreviewInputAdapter = TypeAdapter(CrmImportPreviewInput)
_CrmImportPreviewOutputAdapter = TypeAdapter(CrmImportPreviewOutput)