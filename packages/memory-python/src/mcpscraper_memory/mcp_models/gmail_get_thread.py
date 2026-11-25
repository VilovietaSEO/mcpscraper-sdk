from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class GmailGetThreadInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    connection_id: Annotated[str, Field(min_length=1, max_length=500)] = Field(..., alias='connectionId', description='An activated direct Gmail connection ID.')
    thread_id: str = Field(..., alias='threadId', description='The threadId returned by Gmail message search.')
    cursor: Union[Annotated[str, Field(min_length=1, max_length=2048)], None] = Field(None, alias='cursor', description='The nextCursor from the previous page of this thread.')


GmailGetThreadOutputVariant1ThreadMessagesItem = TypedDict('GmailGetThreadOutputVariant1ThreadMessagesItem', {
    'messageId': Required[str],
    'threadId': Required[str],
    'from': Required[Union[str, None]],
    'to': Required[list[str]],
    'subject': Required[Union[str, None]],
    'sentAt': Required[Union[str, None]],
    'textBody': Required[Union[str, None]],
    'htmlBody': NotRequired[str],
    'bodyComplete': Required[bool],
})
GmailGetThreadOutputVariant1ThreadMessagesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailGetThreadOutputVariant1ThreadOmittedItem = TypedDict('GmailGetThreadOutputVariant1ThreadOmittedItem', {
    'reason': Required[str],
    'omittedCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
GmailGetThreadOutputVariant1ThreadOmittedItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailGetThreadOutputVariant1Thread = TypedDict('GmailGetThreadOutputVariant1Thread', {
    'threadId': Required[str],
    'viewUrl': Required[Union[str, None]],
    'messages': Required[list[GmailGetThreadOutputVariant1ThreadMessagesItem]],
    'messageCount': Required[Union[Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)], None]],
    'omitted': Required[list[GmailGetThreadOutputVariant1ThreadOmittedItem]],
    'draftsExcluded': Required[Literal[True]],
    'providerCoverageComplete': Required[bool],
    'complete': Required[bool],
    'nextCursor': Required[Union[str, None]],
    'untrustedContent': Required[Literal[True]],
})
GmailGetThreadOutputVariant1Thread.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class GmailGetThreadOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: Literal[True] = Field(..., alias='ok', description='')
    thread: GmailGetThreadOutputVariant1Thread = Field(..., alias='thread', description='')
    error: None = Field(..., alias='error', description='')


GmailGetThreadOutputVariant2DeliveryArtifactsItem = TypedDict('GmailGetThreadOutputVariant2DeliveryArtifactsItem', {
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
GmailGetThreadOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailGetThreadOutputVariant2DeliveryAvailableExportsItem = TypedDict('GmailGetThreadOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
GmailGetThreadOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailGetThreadOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('GmailGetThreadOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
GmailGetThreadOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailGetThreadOutputVariant2Delivery = TypedDict('GmailGetThreadOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[GmailGetThreadOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[GmailGetThreadOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[GmailGetThreadOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
GmailGetThreadOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailGetThreadOutputVariant2RecoveryOperation = TypedDict('GmailGetThreadOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
GmailGetThreadOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailGetThreadOutputVariant2Recovery = TypedDict('GmailGetThreadOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[GmailGetThreadOutputVariant2RecoveryOperation],
})
GmailGetThreadOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class GmailGetThreadOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: GmailGetThreadOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: GmailGetThreadOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(GmailGetThreadOutput).
GmailGetThreadOutput = Union[GmailGetThreadOutputVariant2, GmailGetThreadOutputVariant1]

_GmailGetThreadInputAdapter = TypeAdapter(GmailGetThreadInput)
_GmailGetThreadOutputAdapter = TypeAdapter(GmailGetThreadOutput)