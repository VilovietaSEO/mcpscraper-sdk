from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


PostMessageInputAttachNote = TypedDict('PostMessageInputAttachNote', {
    'vault': Required[Annotated[str, Field(min_length=1)]],
    'path': Required[Annotated[str, Field(min_length=1)]],
})
PostMessageInputAttachNote.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class PostMessageInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    vault: Annotated[str, Field(min_length=1)] = Field(..., alias='vault', description='The channel (vault) to post to.')
    content: Annotated[str, Field(min_length=1)] = Field(..., alias='content', description='The message text.')
    attach_note: Union[PostMessageInputAttachNote, None] = Field(None, alias='attachNote', description='Attach one of your own notes to this message, auto-shared with every current channel member. Optional.')


PostMessageOutputVariant1AttachedNote = TypedDict('PostMessageOutputVariant1AttachedNote', {
    'title': Required[str],
    'path': Required[str],
})
PostMessageOutputVariant1AttachedNote.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class PostMessageOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='True when the message was posted; false on auth/scope error.')
    message_id: Union[str, None] = Field(None, alias='messageId', description='Path-style identifier for this message: use it as parentMessageId on reply-message, or messageId on react-message.')
    posted_at: Union[str, None] = Field(None, alias='postedAt', description='ISO-8601 timestamp the message was posted.')
    attached_note: Union[PostMessageOutputVariant1AttachedNote, None] = Field(None, alias='attachedNote', description='Present when attachNote was given and the share succeeded.')
    error: Union[str, None] = Field(None, alias='error', description='Human-readable failure reason when ok is false.')


PostMessageOutputVariant2DeliveryArtifactsItem = TypedDict('PostMessageOutputVariant2DeliveryArtifactsItem', {
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
PostMessageOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


PostMessageOutputVariant2DeliveryAvailableExportsItem = TypedDict('PostMessageOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
PostMessageOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


PostMessageOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('PostMessageOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
PostMessageOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


PostMessageOutputVariant2Delivery = TypedDict('PostMessageOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[PostMessageOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[PostMessageOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[PostMessageOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
PostMessageOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


PostMessageOutputVariant2RecoveryOperation = TypedDict('PostMessageOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
PostMessageOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


PostMessageOutputVariant2Recovery = TypedDict('PostMessageOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[PostMessageOutputVariant2RecoveryOperation],
})
PostMessageOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class PostMessageOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: PostMessageOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: PostMessageOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(PostMessageOutput).
PostMessageOutput = Union[PostMessageOutputVariant2, PostMessageOutputVariant1]

_PostMessageInputAdapter = TypeAdapter(PostMessageInput)
_PostMessageOutputAdapter = TypeAdapter(PostMessageOutput)