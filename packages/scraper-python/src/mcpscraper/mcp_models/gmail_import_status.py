from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class GmailImportStatusInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    ingest_id: Annotated[str, Field(min_length=1, max_length=500)] = Field(..., alias='ingestId', description='Owner-scoped ingestId returned by gmail_import_to_memory; this status call never continues work.')


GmailImportStatusOutputVariant1IngestMessages = TypedDict('GmailImportStatusOutputVariant1IngestMessages', {
    'planned': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'stored': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'indexed': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'failed': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
GmailImportStatusOutputVariant1IngestMessages.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailImportStatusOutputVariant1IngestAttachments = TypedDict('GmailImportStatusOutputVariant1IngestAttachments', {
    'planned': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'stored': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'indexed': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storedUnindexed': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'failed': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
GmailImportStatusOutputVariant1IngestAttachments.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailImportStatusOutputVariant1IngestSamplesItem = TypedDict('GmailImportStatusOutputVariant1IngestSamplesItem', {
    'sourceKey': Required[str],
    'state': Required[Literal['pending', 'stored_unindexed', 'indexed', 'failed']],
    'path': NotRequired[str],
    'error': NotRequired[str],
})
GmailImportStatusOutputVariant1IngestSamplesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailImportStatusOutputVariant1Ingest = TypedDict('GmailImportStatusOutputVariant1Ingest', {
    'ingestId': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'importPlanId': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'status': Required[Literal['pending', 'running', 'complete', 'partial', 'failed']],
    'messages': Required[GmailImportStatusOutputVariant1IngestMessages],
    'attachments': Required[GmailImportStatusOutputVariant1IngestAttachments],
    'manifestStored': Required[bool],
    'complete': Required[bool],
    'samples': Required[Annotated[list[GmailImportStatusOutputVariant1IngestSamplesItem], Field(max_length=25)]],
    'nextAction': Required[Literal['call_gmail_import_to_memory', 'call_gmail_import_status', 'complete', 'inspect_failures']],
})
GmailImportStatusOutputVariant1Ingest.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class GmailImportStatusOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    ingest: Union[GmailImportStatusOutputVariant1Ingest, None] = Field(None, alias='ingest', description='')
    error: Union[str, None] = Field(..., alias='error', description='')


GmailImportStatusOutputVariant2DeliveryArtifactsItem = TypedDict('GmailImportStatusOutputVariant2DeliveryArtifactsItem', {
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
GmailImportStatusOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailImportStatusOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('GmailImportStatusOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
GmailImportStatusOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailImportStatusOutputVariant2Delivery = TypedDict('GmailImportStatusOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[GmailImportStatusOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[GmailImportStatusOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
GmailImportStatusOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailImportStatusOutputVariant2RecoveryOperation = TypedDict('GmailImportStatusOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
GmailImportStatusOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailImportStatusOutputVariant2Recovery = TypedDict('GmailImportStatusOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[GmailImportStatusOutputVariant2RecoveryOperation],
})
GmailImportStatusOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class GmailImportStatusOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: GmailImportStatusOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: GmailImportStatusOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(GmailImportStatusOutput).
GmailImportStatusOutput = Union[GmailImportStatusOutputVariant2, GmailImportStatusOutputVariant1]

_GmailImportStatusInputAdapter = TypeAdapter(GmailImportStatusInput)
_GmailImportStatusOutputAdapter = TypeAdapter(GmailImportStatusOutput)