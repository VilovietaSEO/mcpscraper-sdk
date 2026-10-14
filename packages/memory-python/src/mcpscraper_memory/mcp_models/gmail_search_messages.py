from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class GmailSearchMessagesInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    connection_id: Annotated[str, Field(min_length=1, max_length=500)] = Field(..., alias='connectionId', description='A tenant-owned Gmail connectionId returned by list_service_connections.')
    query: Annotated[str, Field(min_length=1, max_length=1000)] = Field(..., alias='query', description='Standard Gmail search query for messages; use gmail_search_contacts when the desired result is a deduplicated sender list.')
    limit: Union[Annotated[int, Field(ge=1, le=500)], None] = Field(None, alias='limit', description='Maximum message previews in this page; use the returned opaque cursor for another bounded page.')
    cursor: Union[Annotated[str, Field(min_length=1, max_length=500)], None] = Field(None, alias='cursor', description='Opaque owner-bound cursor returned by a prior identical gmail_search_messages query; never pass a provider page token.')


GmailSearchMessagesOutputVariant1MessagesItem = TypedDict('GmailSearchMessagesOutputVariant1MessagesItem', {
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
GmailSearchMessagesOutputVariant1MessagesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class GmailSearchMessagesOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    messages: list[GmailSearchMessagesOutputVariant1MessagesItem] = Field(..., alias='messages', description='')
    estimated_matches: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(..., alias='estimatedMatches', description='')
    complete: bool = Field(..., alias='complete', description='')
    truncated: bool = Field(..., alias='truncated', description='')
    next_cursor: Union[Annotated[str, Field(min_length=1, max_length=500)], None] = Field(..., alias='nextCursor', description='')
    untrusted_content: Literal[True] = Field(..., alias='untrustedContent', description='')
    error: Union[str, None] = Field(..., alias='error', description='')


GmailSearchMessagesOutputVariant2DeliveryArtifactsItem = TypedDict('GmailSearchMessagesOutputVariant2DeliveryArtifactsItem', {
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
GmailSearchMessagesOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailSearchMessagesOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('GmailSearchMessagesOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
GmailSearchMessagesOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailSearchMessagesOutputVariant2Delivery = TypedDict('GmailSearchMessagesOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[GmailSearchMessagesOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[GmailSearchMessagesOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
GmailSearchMessagesOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailSearchMessagesOutputVariant2RecoveryOperation = TypedDict('GmailSearchMessagesOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
GmailSearchMessagesOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailSearchMessagesOutputVariant2Recovery = TypedDict('GmailSearchMessagesOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[GmailSearchMessagesOutputVariant2RecoveryOperation],
})
GmailSearchMessagesOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class GmailSearchMessagesOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: GmailSearchMessagesOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: GmailSearchMessagesOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(GmailSearchMessagesOutput).
GmailSearchMessagesOutput = Union[GmailSearchMessagesOutputVariant1, GmailSearchMessagesOutputVariant2]

_GmailSearchMessagesInputAdapter = TypeAdapter(GmailSearchMessagesInput)
_GmailSearchMessagesOutputAdapter = TypeAdapter(GmailSearchMessagesOutput)