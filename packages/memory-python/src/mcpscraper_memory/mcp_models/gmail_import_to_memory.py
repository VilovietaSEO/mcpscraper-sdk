from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class GmailImportToMemoryInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    idempotency_key: Annotated[str, Field(min_length=8, max_length=200)] = Field(..., alias='idempotencyKey', description='Stable retry key bound to the immutable import plan; reuse resumes and conflicting input fails before a write.')
    import_plan_id: Annotated[str, Field(min_length=1, max_length=500)] = Field(..., alias='importPlanId', description='Reviewed, unexpired importPlanId returned by gmail_prepare_memory_import.')


GmailImportToMemoryOutputVariant1IngestMessages = TypedDict('GmailImportToMemoryOutputVariant1IngestMessages', {
    'planned': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'stored': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'indexed': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'failed': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
GmailImportToMemoryOutputVariant1IngestMessages.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailImportToMemoryOutputVariant1IngestAttachments = TypedDict('GmailImportToMemoryOutputVariant1IngestAttachments', {
    'planned': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'stored': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'indexed': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storedUnindexed': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'failed': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
GmailImportToMemoryOutputVariant1IngestAttachments.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailImportToMemoryOutputVariant1IngestSamplesItem = TypedDict('GmailImportToMemoryOutputVariant1IngestSamplesItem', {
    'sourceKey': Required[str],
    'state': Required[Literal['pending', 'stored_unindexed', 'indexed', 'failed']],
    'path': NotRequired[str],
    'error': NotRequired[str],
})
GmailImportToMemoryOutputVariant1IngestSamplesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailImportToMemoryOutputVariant1Ingest = TypedDict('GmailImportToMemoryOutputVariant1Ingest', {
    'ingestId': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'importPlanId': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'status': Required[Literal['pending', 'running', 'complete', 'partial', 'failed']],
    'messages': Required[GmailImportToMemoryOutputVariant1IngestMessages],
    'attachments': Required[GmailImportToMemoryOutputVariant1IngestAttachments],
    'manifestStored': Required[bool],
    'complete': Required[bool],
    'samples': Required[Annotated[list[GmailImportToMemoryOutputVariant1IngestSamplesItem], Field(max_length=25)]],
    'nextAction': Required[Literal['call_gmail_import_to_memory', 'call_gmail_import_status', 'complete', 'inspect_failures']],
})
GmailImportToMemoryOutputVariant1Ingest.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class GmailImportToMemoryOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    ingest: Union[GmailImportToMemoryOutputVariant1Ingest, None] = Field(None, alias='ingest', description='')
    error: Union[str, None] = Field(..., alias='error', description='')


GmailImportToMemoryOutputVariant2DeliveryArtifactsItem = TypedDict('GmailImportToMemoryOutputVariant2DeliveryArtifactsItem', {
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
GmailImportToMemoryOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailImportToMemoryOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('GmailImportToMemoryOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
GmailImportToMemoryOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailImportToMemoryOutputVariant2Delivery = TypedDict('GmailImportToMemoryOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[GmailImportToMemoryOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[GmailImportToMemoryOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
GmailImportToMemoryOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailImportToMemoryOutputVariant2RecoveryOperation = TypedDict('GmailImportToMemoryOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
GmailImportToMemoryOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailImportToMemoryOutputVariant2Recovery = TypedDict('GmailImportToMemoryOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[GmailImportToMemoryOutputVariant2RecoveryOperation],
})
GmailImportToMemoryOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class GmailImportToMemoryOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: GmailImportToMemoryOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: GmailImportToMemoryOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(GmailImportToMemoryOutput).
GmailImportToMemoryOutput = Union[GmailImportToMemoryOutputVariant2, GmailImportToMemoryOutputVariant1]

_GmailImportToMemoryInputAdapter = TypeAdapter(GmailImportToMemoryInput)
_GmailImportToMemoryOutputAdapter = TypeAdapter(GmailImportToMemoryOutput)