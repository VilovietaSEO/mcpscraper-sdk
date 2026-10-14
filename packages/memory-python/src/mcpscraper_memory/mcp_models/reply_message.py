from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


ReplyMessageInputAttachNote = TypedDict('ReplyMessageInputAttachNote', {
    'vault': Required[Annotated[str, Field(min_length=1)]],
    'path': Required[Annotated[str, Field(min_length=1)]],
})
ReplyMessageInputAttachNote.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class ReplyMessageInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    vault: Annotated[str, Field(min_length=1)] = Field(..., alias='vault', description='The channel (vault) the parent message is in.')
    parent_message_id: Annotated[str, Field(min_length=1)] = Field(..., alias='parentMessageId', description='The top-level message to reply under (messageId from post-message or list-channel-messages).')
    content: Annotated[str, Field(min_length=1)] = Field(..., alias='content', description='The reply text.')
    attach_note: Union[ReplyMessageInputAttachNote, None] = Field(None, alias='attachNote', description='Attach one of your own notes to this reply, auto-shared with every current channel member. Optional.')


ReplyMessageOutputVariant1AttachedNote = TypedDict('ReplyMessageOutputVariant1AttachedNote', {
    'title': Required[str],
    'path': Required[str],
})
ReplyMessageOutputVariant1AttachedNote.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ReplyMessageOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='True when the reply was posted; false on auth/scope/lookup error.')
    message_id: Union[str, None] = Field(None, alias='messageId', description='Path-style identifier for this reply (e.g. for react-message).')
    posted_at: Union[str, None] = Field(None, alias='postedAt', description='ISO-8601 timestamp the reply was posted.')
    attached_note: Union[ReplyMessageOutputVariant1AttachedNote, None] = Field(None, alias='attachedNote', description='Present when attachNote was given and the share succeeded.')
    error: Union[str, None] = Field(None, alias='error', description='Human-readable failure reason when ok is false.')


ReplyMessageOutputVariant2DeliveryArtifactsItem = TypedDict('ReplyMessageOutputVariant2DeliveryArtifactsItem', {
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
ReplyMessageOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ReplyMessageOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('ReplyMessageOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
ReplyMessageOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ReplyMessageOutputVariant2Delivery = TypedDict('ReplyMessageOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[ReplyMessageOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[ReplyMessageOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
ReplyMessageOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ReplyMessageOutputVariant2RecoveryOperation = TypedDict('ReplyMessageOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
ReplyMessageOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ReplyMessageOutputVariant2Recovery = TypedDict('ReplyMessageOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[ReplyMessageOutputVariant2RecoveryOperation],
})
ReplyMessageOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ReplyMessageOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: ReplyMessageOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: ReplyMessageOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(ReplyMessageOutput).
ReplyMessageOutput = Union[ReplyMessageOutputVariant2, ReplyMessageOutputVariant1]

_ReplyMessageInputAdapter = TypeAdapter(ReplyMessageInput)
_ReplyMessageOutputAdapter = TypeAdapter(ReplyMessageOutput)