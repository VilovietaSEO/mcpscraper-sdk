from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


GmailPrepareSelectionInputSourceVariant1 = TypedDict('GmailPrepareSelectionInputSourceVariant1', {
    'kind': Required[Literal['query']],
    'query': Required[Annotated[str, Field(min_length=1, max_length=1000)]],
})
GmailPrepareSelectionInputSourceVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


GmailPrepareSelectionInputSourceVariant2 = TypedDict('GmailPrepareSelectionInputSourceVariant2', {
    'kind': Required[Literal['message_ids']],
    'messageIds': Required[Annotated[list[Annotated[str, Field(min_length=1, max_length=500)]], Field(min_length=1, max_length=5000)]],
})
GmailPrepareSelectionInputSourceVariant2.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class GmailPrepareSelectionInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    connection_id: Annotated[str, Field(min_length=1, max_length=500)] = Field(..., alias='connectionId', description='A tenant-owned Gmail connectionId returned by list_service_connections.')
    purpose: Literal['export', 'mailbox_action', 'memory_import'] = Field(..., alias='purpose', description='The one downstream workflow this immutable selection authorizes. Choose export to download the frozen messages, mailbox_action to change them, or memory_import to preserve them in Memory. Native worker exports use the same export purpose through signed internal requests.')
    source: Union[GmailPrepareSelectionInputSourceVariant1, GmailPrepareSelectionInputSourceVariant2] = Field(..., alias='source', description='Choose exactly one query or explicit-message-ID source; invalid mixed modes are rejected.')


GmailPrepareSelectionOutputVariant1SelectionPreviewItem = TypedDict('GmailPrepareSelectionOutputVariant1SelectionPreviewItem', {
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
GmailPrepareSelectionOutputVariant1SelectionPreviewItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailPrepareSelectionOutputVariant1Selection = TypedDict('GmailPrepareSelectionOutputVariant1Selection', {
    'selectionId': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'purpose': Required[Literal['export', 'mailbox_action', 'memory_import']],
    'count': Required[Annotated[int, Field(ge=1, le=5000)]],
    'selectionSha256': Required[str],
    'preview': Required[Annotated[list[GmailPrepareSelectionOutputVariant1SelectionPreviewItem], Field(max_length=25)]],
    'createdAt': Required[str],
    'expiresAt': Required[str],
    'untrustedContent': Required[Literal[True]],
})
GmailPrepareSelectionOutputVariant1Selection.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class GmailPrepareSelectionOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    selection: Union[GmailPrepareSelectionOutputVariant1Selection, None] = Field(None, alias='selection', description='')
    error: Union[str, None] = Field(..., alias='error', description='')


GmailPrepareSelectionOutputVariant2DeliveryArtifactsItem = TypedDict('GmailPrepareSelectionOutputVariant2DeliveryArtifactsItem', {
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
GmailPrepareSelectionOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailPrepareSelectionOutputVariant2DeliveryAvailableExportsItem = TypedDict('GmailPrepareSelectionOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
GmailPrepareSelectionOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailPrepareSelectionOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('GmailPrepareSelectionOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
GmailPrepareSelectionOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailPrepareSelectionOutputVariant2Delivery = TypedDict('GmailPrepareSelectionOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[GmailPrepareSelectionOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[GmailPrepareSelectionOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[GmailPrepareSelectionOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
GmailPrepareSelectionOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailPrepareSelectionOutputVariant2RecoveryOperation = TypedDict('GmailPrepareSelectionOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
GmailPrepareSelectionOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailPrepareSelectionOutputVariant2Recovery = TypedDict('GmailPrepareSelectionOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[GmailPrepareSelectionOutputVariant2RecoveryOperation],
})
GmailPrepareSelectionOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class GmailPrepareSelectionOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: GmailPrepareSelectionOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: GmailPrepareSelectionOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(GmailPrepareSelectionOutput).
GmailPrepareSelectionOutput = Union[GmailPrepareSelectionOutputVariant2, GmailPrepareSelectionOutputVariant1]

_GmailPrepareSelectionInputAdapter = TypeAdapter(GmailPrepareSelectionInput)
_GmailPrepareSelectionOutputAdapter = TypeAdapter(GmailPrepareSelectionOutput)