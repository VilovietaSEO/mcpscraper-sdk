from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class ReactMessageInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    vault: Annotated[str, Field(min_length=1)] = Field(..., alias='vault', description='The channel (vault) the message is in.')
    message_id: Annotated[str, Field(min_length=1)] = Field(..., alias='messageId', description='The message or reply to react to (from post-message, reply-message, or list-channel-messages).')
    emoji: Annotated[str, Field(min_length=1)] = Field(..., alias='emoji', description='The emoji to add or remove, e.g. "👍".')
    remove: Union[bool, None] = Field(None, alias='remove', description='Set true to remove a reaction you previously added. Default false (add).')


class ReactMessageOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='True on success; false on auth/scope error.')
    message_id: Union[str, None] = Field(None, alias='messageId', description='The message reacted to.')
    emoji: Union[str, None] = Field(None, alias='emoji', description='The emoji applied or removed.')
    removed: Union[bool, None] = Field(None, alias='removed', description='True if this call removed a reaction; false if it added one.')
    error: Union[str, None] = Field(None, alias='error', description='Human-readable failure reason when ok is false.')


ReactMessageOutputVariant2DeliveryArtifactsItem = TypedDict('ReactMessageOutputVariant2DeliveryArtifactsItem', {
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
ReactMessageOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ReactMessageOutputVariant2DeliveryAvailableExportsItem = TypedDict('ReactMessageOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
ReactMessageOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ReactMessageOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('ReactMessageOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
ReactMessageOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ReactMessageOutputVariant2Delivery = TypedDict('ReactMessageOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[ReactMessageOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[ReactMessageOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[ReactMessageOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
ReactMessageOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ReactMessageOutputVariant2RecoveryOperation = TypedDict('ReactMessageOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
ReactMessageOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ReactMessageOutputVariant2Recovery = TypedDict('ReactMessageOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[ReactMessageOutputVariant2RecoveryOperation],
})
ReactMessageOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ReactMessageOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: ReactMessageOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: ReactMessageOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(ReactMessageOutput).
ReactMessageOutput = Union[ReactMessageOutputVariant2, ReactMessageOutputVariant1]

_ReactMessageInputAdapter = TypeAdapter(ReactMessageInput)
_ReactMessageOutputAdapter = TypeAdapter(ReactMessageOutput)