from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class PollChannelInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    vault: Annotated[str, Field(min_length=1)] = Field(..., alias='vault', description='The channel (vault) to poll.')
    since: Union[str, None] = Field(None, alias='since', description='ISO-8601 timestamp to override the server-remembered cursor. Optional; omit to use (and then advance) your own last-poll cursor for this channel.')


PollChannelOutputVariant1NewMessagesItem = TypedDict('PollChannelOutputVariant1NewMessagesItem', {
    'messageId': Required[str],
    'authorIdentity': Required[Union[str, None]],
    'authorIsAgent': Required[bool],
    'content': Required[str],
    'postedAt': Required[str],
})
PollChannelOutputVariant1NewMessagesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


PollChannelOutputVariant1NewRepliesItem = TypedDict('PollChannelOutputVariant1NewRepliesItem', {
    'messageId': Required[str],
    'parentMessageId': Required[str],
    'authorIdentity': Required[Union[str, None]],
    'authorIsAgent': Required[bool],
    'content': Required[str],
    'postedAt': Required[str],
})
PollChannelOutputVariant1NewRepliesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


PollChannelOutputVariant1NewReactionsItem = TypedDict('PollChannelOutputVariant1NewReactionsItem', {
    'messageId': Required[str],
    'identity': Required[str],
    'emoji': Required[str],
    'createdAt': Required[str],
})
PollChannelOutputVariant1NewReactionsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class PollChannelOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='True on success; false on auth/scope error.')
    since: Union[str, None] = Field(None, alias='since', description='The cursor this poll was measured from (your previous last_polled_at, or the override you passed).')
    polled_at: Union[str, None] = Field(None, alias='polledAt', description='The new cursor value, now stored — your next no-argument poll starts from here.')
    new_messages: Union[list[PollChannelOutputVariant1NewMessagesItem], None] = Field(None, alias='newMessages', description='New top-level messages since the cursor.')
    new_replies: Union[list[PollChannelOutputVariant1NewRepliesItem], None] = Field(None, alias='newReplies', description='New thread replies since the cursor, across all threads in the channel.')
    new_reactions: Union[list[PollChannelOutputVariant1NewReactionsItem], None] = Field(None, alias='newReactions', description='New reactions since the cursor.')
    error: Union[str, None] = Field(None, alias='error', description='Human-readable failure reason when ok is false.')


PollChannelOutputVariant2DeliveryArtifactsItem = TypedDict('PollChannelOutputVariant2DeliveryArtifactsItem', {
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
PollChannelOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


PollChannelOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('PollChannelOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
PollChannelOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


PollChannelOutputVariant2Delivery = TypedDict('PollChannelOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[PollChannelOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[PollChannelOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
PollChannelOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


PollChannelOutputVariant2RecoveryOperation = TypedDict('PollChannelOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
PollChannelOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


PollChannelOutputVariant2Recovery = TypedDict('PollChannelOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[PollChannelOutputVariant2RecoveryOperation],
})
PollChannelOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class PollChannelOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: PollChannelOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: PollChannelOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(PollChannelOutput).
PollChannelOutput = Union[PollChannelOutputVariant2, PollChannelOutputVariant1]

_PollChannelInputAdapter = TypeAdapter(PollChannelInput)
_PollChannelOutputAdapter = TypeAdapter(PollChannelOutput)