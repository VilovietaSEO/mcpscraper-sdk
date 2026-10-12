from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class GmailExportSelectionInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    connection_id: Annotated[str, Field(min_length=1, max_length=500)] = Field(..., alias='connectionId', description='The tenant-owned Gmail connectionId bound into this immutable selection.')
    selection_id: Annotated[str, Field(min_length=1, max_length=500)] = Field(..., alias='selectionId', description='Immutable owner-bound selectionId returned by gmail_prepare_selection with purpose export.')
    selection_sha256: str = Field(..., alias='selectionSha256', description='Unchanged selection digest returned by gmail_prepare_selection.')
    expected_count: Annotated[int, Field(ge=1, le=5000)] = Field(..., alias='expectedCount', description='Exact frozen message count; export fails if the receipt does not match.')


GmailExportSelectionOutputVariant1PreviewItem = TypedDict('GmailExportSelectionOutputVariant1PreviewItem', {
    'messageId': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'threadId': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'subject': Required[str],
    'from': Required[str],
    'to': Required[list[str]],
    'sentAt': Required[Union[str, None]],
    'snippet': Required[str],
    'labelIds': Required[list[str]],
    'hasAttachments': Required[bool],
})
GmailExportSelectionOutputVariant1PreviewItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailExportSelectionOutputVariant1Artifact = TypedDict('GmailExportSelectionOutputVariant1Artifact', {
    'artifactId': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'filename': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'mimeType': Required[Annotated[str, Field(min_length=1, max_length=255)]],
    'bytes': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'sha256': Required[str],
    'createdAt': Required[str],
    'expiresAt': Required[str],
    'downloadUrl': NotRequired[str],
    'downloadUrlExpiresAt': NotRequired[str],
    'textReadable': Required[bool],
    'archiveReadable': Required[bool],
    'persistable': Required[bool],
})
GmailExportSelectionOutputVariant1Artifact.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class GmailExportSelectionOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    selection_id: Union[Annotated[str, Field(min_length=1, max_length=500)], None] = Field(None, alias='selectionId', description='')
    count: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(None, alias='count', description='')
    complete: Union[bool, None] = Field(None, alias='complete', description='')
    preview: Union[Annotated[list[GmailExportSelectionOutputVariant1PreviewItem], Field(max_length=25)], None] = Field(None, alias='preview', description='')
    artifact: Union[GmailExportSelectionOutputVariant1Artifact, None] = Field(None, alias='artifact', description='')
    warnings: Union[list[str], None] = Field(None, alias='warnings', description='')
    untrusted_content: Literal[True] = Field(..., alias='untrustedContent', description='')
    error: Union[str, None] = Field(..., alias='error', description='')


GmailExportSelectionOutputVariant2DeliveryArtifactsItem = TypedDict('GmailExportSelectionOutputVariant2DeliveryArtifactsItem', {
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
GmailExportSelectionOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailExportSelectionOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('GmailExportSelectionOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
GmailExportSelectionOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailExportSelectionOutputVariant2Delivery = TypedDict('GmailExportSelectionOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[GmailExportSelectionOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[GmailExportSelectionOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
GmailExportSelectionOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailExportSelectionOutputVariant2RecoveryOperation = TypedDict('GmailExportSelectionOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
GmailExportSelectionOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailExportSelectionOutputVariant2Recovery = TypedDict('GmailExportSelectionOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[GmailExportSelectionOutputVariant2RecoveryOperation],
})
GmailExportSelectionOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class GmailExportSelectionOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: GmailExportSelectionOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: GmailExportSelectionOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(GmailExportSelectionOutput).
GmailExportSelectionOutput = Union[GmailExportSelectionOutputVariant2, GmailExportSelectionOutputVariant1]

_GmailExportSelectionInputAdapter = TypeAdapter(GmailExportSelectionInput)
_GmailExportSelectionOutputAdapter = TypeAdapter(GmailExportSelectionOutput)