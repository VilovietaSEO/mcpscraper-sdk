from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class GmailGetMessageInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    connection_id: Annotated[str, Field(min_length=1, max_length=500)] = Field(..., alias='connectionId', description='The same tenant-owned Gmail connectionId used to discover this message.')
    message_id: Annotated[str, Field(min_length=1, max_length=500)] = Field(..., alias='messageId', description='One Gmail messageId returned by gmail_search_messages or a frozen selection preview.')
    include_raw_artifact: Union[bool, None] = Field(None, alias='includeRawArtifact', description='Keep true when complete RFC 822 fidelity or later export is required; large content is returned through an owned artifact, never silently truncated.')


GmailGetMessageOutputVariant1MessageHeadersItem = TypedDict('GmailGetMessageOutputVariant1MessageHeadersItem', {
    'name': Required[str],
    'value': Required[str],
})
GmailGetMessageOutputVariant1MessageHeadersItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailGetMessageOutputVariant1MessageAttachmentsItem = TypedDict('GmailGetMessageOutputVariant1MessageAttachmentsItem', {
    'attachmentRef': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'filename': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'mimeType': Required[Annotated[str, Field(min_length=1, max_length=255)]],
    'bytes': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'contentId': NotRequired[Union[Annotated[str, Field(max_length=500)], None]],
    'disposition': NotRequired[Literal['attachment', 'inline']],
})
GmailGetMessageOutputVariant1MessageAttachmentsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailGetMessageOutputVariant1MessageProvenance = TypedDict('GmailGetMessageOutputVariant1MessageProvenance', {
    'connectionId': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'fetchedAt': Required[str],
    'format': Required[Literal['full']],
})
GmailGetMessageOutputVariant1MessageProvenance.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailGetMessageOutputVariant1MessageRawArtifact = TypedDict('GmailGetMessageOutputVariant1MessageRawArtifact', {
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
GmailGetMessageOutputVariant1MessageRawArtifact.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailGetMessageOutputVariant1MessageBodyArtifact = TypedDict('GmailGetMessageOutputVariant1MessageBodyArtifact', {
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
GmailGetMessageOutputVariant1MessageBodyArtifact.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailGetMessageOutputVariant1Message = TypedDict('GmailGetMessageOutputVariant1Message', {
    'messageId': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'threadId': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'messageIdHeader': Required[Union[str, None]],
    'historyId': NotRequired[str],
    'internalDate': Required[Union[str, None]],
    'headers': Required[list[GmailGetMessageOutputVariant1MessageHeadersItem]],
    'from': Required[str],
    'to': Required[list[str]],
    'cc': Required[list[str]],
    'bcc': Required[list[str]],
    'replyTo': Required[list[str]],
    'subject': Required[str],
    'sentAt': Required[Union[str, None]],
    'textBody': Required[Union[str, None]],
    'htmlBody': Required[Union[str, None]],
    'bodyComplete': Required[bool],
    'labelIds': Required[list[str]],
    'attachments': Required[list[GmailGetMessageOutputVariant1MessageAttachmentsItem]],
    'providerSizeEstimate': Required[Union[Annotated[int, Field(ge=0, le=9007199254740991)], None]],
    'provenance': Required[GmailGetMessageOutputVariant1MessageProvenance],
    'mime': Required[Any],
    'rawArtifact': NotRequired[GmailGetMessageOutputVariant1MessageRawArtifact],
    'bodyArtifact': NotRequired[GmailGetMessageOutputVariant1MessageBodyArtifact],
    'untrustedContent': Required[Literal[True]],
})
GmailGetMessageOutputVariant1Message.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class GmailGetMessageOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    message: Union[GmailGetMessageOutputVariant1Message, None] = Field(None, alias='message', description='')
    error: Union[str, None] = Field(..., alias='error', description='')


GmailGetMessageOutputVariant2DeliveryArtifactsItem = TypedDict('GmailGetMessageOutputVariant2DeliveryArtifactsItem', {
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
GmailGetMessageOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailGetMessageOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('GmailGetMessageOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
GmailGetMessageOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailGetMessageOutputVariant2Delivery = TypedDict('GmailGetMessageOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[GmailGetMessageOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[GmailGetMessageOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
GmailGetMessageOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailGetMessageOutputVariant2RecoveryOperation = TypedDict('GmailGetMessageOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
GmailGetMessageOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailGetMessageOutputVariant2Recovery = TypedDict('GmailGetMessageOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[GmailGetMessageOutputVariant2RecoveryOperation],
})
GmailGetMessageOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class GmailGetMessageOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: GmailGetMessageOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: GmailGetMessageOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(GmailGetMessageOutput).
GmailGetMessageOutput = Union[GmailGetMessageOutputVariant2, GmailGetMessageOutputVariant1]

_GmailGetMessageInputAdapter = TypeAdapter(GmailGetMessageInput)
_GmailGetMessageOutputAdapter = TypeAdapter(GmailGetMessageOutput)