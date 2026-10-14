from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class ListChannelMessagesInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    vault: Annotated[str, Field(min_length=1)] = Field(..., alias='vault', description='The channel (vault) to read.')
    parent_message_id: Union[str, None] = Field(None, alias='parentMessageId', description="If given, list this thread's replies instead of top-level channel messages.")


ListChannelMessagesOutputVariant1MessagesItemReadByItem = TypedDict('ListChannelMessagesOutputVariant1MessagesItemReadByItem', {
    'identity': Required[str],
    'readAt': Required[str],
})
ListChannelMessagesOutputVariant1MessagesItemReadByItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListChannelMessagesOutputVariant1MessagesItemReactionsItem = TypedDict('ListChannelMessagesOutputVariant1MessagesItemReactionsItem', {
    'identity': Required[str],
    'emoji': Required[str],
})
ListChannelMessagesOutputVariant1MessagesItemReactionsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListChannelMessagesOutputVariant1MessagesItemAttachedNote = TypedDict('ListChannelMessagesOutputVariant1MessagesItemAttachedNote', {
    'title': Required[str],
    'path': Required[str],
})
ListChannelMessagesOutputVariant1MessagesItemAttachedNote.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListChannelMessagesOutputVariant1MessagesItem = TypedDict('ListChannelMessagesOutputVariant1MessagesItem', {
    'messageId': Required[str],
    'authorIdentity': Required[Union[str, None]],
    'authorIsAgent': Required[bool],
    'content': Required[str],
    'postedAt': Required[str],
    'revision': Required[Union[float, int]],
    'replyCount': NotRequired[Union[float, int]],
    'lastReplyAt': NotRequired[Union[str, None]],
    'readBy': Required[list[ListChannelMessagesOutputVariant1MessagesItemReadByItem]],
    'reactions': Required[list[ListChannelMessagesOutputVariant1MessagesItemReactionsItem]],
    'attachedNote': NotRequired[ListChannelMessagesOutputVariant1MessagesItemAttachedNote],
})
ListChannelMessagesOutputVariant1MessagesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ListChannelMessagesOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='True on success; false on auth/scope error.')
    messages: Union[list[ListChannelMessagesOutputVariant1MessagesItem], None] = Field(None, alias='messages', description='Messages oldest-first. Present when ok is true.')
    error: Union[str, None] = Field(None, alias='error', description='Human-readable failure reason when ok is false.')


ListChannelMessagesOutputVariant2DeliveryArtifactsItem = TypedDict('ListChannelMessagesOutputVariant2DeliveryArtifactsItem', {
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
ListChannelMessagesOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListChannelMessagesOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('ListChannelMessagesOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
ListChannelMessagesOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListChannelMessagesOutputVariant2Delivery = TypedDict('ListChannelMessagesOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[ListChannelMessagesOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[ListChannelMessagesOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
ListChannelMessagesOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListChannelMessagesOutputVariant2RecoveryOperation = TypedDict('ListChannelMessagesOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
ListChannelMessagesOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListChannelMessagesOutputVariant2Recovery = TypedDict('ListChannelMessagesOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[ListChannelMessagesOutputVariant2RecoveryOperation],
})
ListChannelMessagesOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ListChannelMessagesOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: ListChannelMessagesOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: ListChannelMessagesOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(ListChannelMessagesOutput).
ListChannelMessagesOutput = Union[ListChannelMessagesOutputVariant2, ListChannelMessagesOutputVariant1]

_ListChannelMessagesInputAdapter = TypeAdapter(ListChannelMessagesInput)
_ListChannelMessagesOutputAdapter = TypeAdapter(ListChannelMessagesOutput)