from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class GmailCreateReplyDraftInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    connection_id: Annotated[str, Field(min_length=1, max_length=500)] = Field(..., alias='connectionId', description='The same activated, action-enabled Gmail connection.')
    thread_id: str = Field(..., alias='threadId', description='The thread ID returned by Gmail thread read.')
    parent_message_id: str = Field(..., alias='parentMessageId', description='Exact message ID of the parent in that thread.')
    body: Annotated[str, Field(min_length=1, max_length=20000)] = Field(..., alias='body', description='The reply as plain text.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=200)] = Field(..., alias='idempotencyKey', description='Reuse this key for a retry of the identical draft request.')
    confirmed: Union[bool, None] = Field(None, alias='confirmed', description='Set true when the person authorized saving this exact draft.')


GmailCreateReplyDraftOutputVariant1DraftVariant1 = TypedDict('GmailCreateReplyDraftOutputVariant1DraftVariant1', {
    'status': Required[Literal['draft_created']],
    'actionId': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'draftId': Required[str],
    'threadId': Required[str],
    'parentMessageId': Required[str],
    'viewUrl': Required[Union[str, None]],
    'sent': Required[Literal[False]],
    'replay': Required[bool],
})
GmailCreateReplyDraftOutputVariant1DraftVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailCreateReplyDraftOutputVariant1DraftVariant2 = TypedDict('GmailCreateReplyDraftOutputVariant1DraftVariant2', {
    'status': Required[Literal['draft_not_created']],
    'actionId': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'code': Required[str],
    'sent': Required[Literal[False]],
    'replay': Required[Literal[True]],
})
GmailCreateReplyDraftOutputVariant1DraftVariant2.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailCreateReplyDraftOutputVariant1DraftVariant3 = TypedDict('GmailCreateReplyDraftOutputVariant1DraftVariant3', {
    'status': Required[Literal['outcome_unknown']],
    'actionId': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'retryable': Required[Literal[False]],
    'replay': Required[Literal[True]],
})
GmailCreateReplyDraftOutputVariant1DraftVariant3.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class GmailCreateReplyDraftOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: Literal[True] = Field(..., alias='ok', description='')
    draft: Union[GmailCreateReplyDraftOutputVariant1DraftVariant1, GmailCreateReplyDraftOutputVariant1DraftVariant2, GmailCreateReplyDraftOutputVariant1DraftVariant3] = Field(..., alias='draft', description='')
    error: None = Field(..., alias='error', description='')


GmailCreateReplyDraftOutputVariant2DeliveryArtifactsItem = TypedDict('GmailCreateReplyDraftOutputVariant2DeliveryArtifactsItem', {
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
GmailCreateReplyDraftOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailCreateReplyDraftOutputVariant2DeliveryAvailableExportsItem = TypedDict('GmailCreateReplyDraftOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
GmailCreateReplyDraftOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailCreateReplyDraftOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('GmailCreateReplyDraftOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
GmailCreateReplyDraftOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailCreateReplyDraftOutputVariant2Delivery = TypedDict('GmailCreateReplyDraftOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[GmailCreateReplyDraftOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[GmailCreateReplyDraftOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[GmailCreateReplyDraftOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
GmailCreateReplyDraftOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailCreateReplyDraftOutputVariant2RecoveryOperation = TypedDict('GmailCreateReplyDraftOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
GmailCreateReplyDraftOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailCreateReplyDraftOutputVariant2Recovery = TypedDict('GmailCreateReplyDraftOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[GmailCreateReplyDraftOutputVariant2RecoveryOperation],
})
GmailCreateReplyDraftOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class GmailCreateReplyDraftOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: GmailCreateReplyDraftOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: GmailCreateReplyDraftOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(GmailCreateReplyDraftOutput).
GmailCreateReplyDraftOutput = Union[GmailCreateReplyDraftOutputVariant2, GmailCreateReplyDraftOutputVariant1]

_GmailCreateReplyDraftInputAdapter = TypeAdapter(GmailCreateReplyDraftInput)
_GmailCreateReplyDraftOutputAdapter = TypeAdapter(GmailCreateReplyDraftOutput)