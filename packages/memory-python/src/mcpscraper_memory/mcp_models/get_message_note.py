from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class GetMessageNoteInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    vault: Annotated[str, Field(min_length=1)] = Field(..., alias='vault', description='The channel (vault) the message is in.')
    message_id: Annotated[str, Field(min_length=1)] = Field(..., alias='messageId', description='The message (from list-channel-messages / poll-channel) whose attached note to read.')


GetMessageNoteOutputVariant1Note = TypedDict('GetMessageNoteOutputVariant1Note', {
    'path': Required[str],
    'title': Required[str],
    'content': Required[str],
    'ownerIdentity': Required[str],
})
GetMessageNoteOutputVariant1Note.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class GetMessageNoteOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='True when the note was found and readable; false on auth/scope/not-found error.')
    note: Union[GetMessageNoteOutputVariant1Note, None] = Field(None, alias='note', description='Present when ok is true.')
    error: Union[str, None] = Field(None, alias='error', description='Human-readable failure reason when ok is false.')


GetMessageNoteOutputVariant2DeliveryArtifactsItem = TypedDict('GetMessageNoteOutputVariant2DeliveryArtifactsItem', {
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
GetMessageNoteOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetMessageNoteOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('GetMessageNoteOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
GetMessageNoteOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetMessageNoteOutputVariant2Delivery = TypedDict('GetMessageNoteOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[GetMessageNoteOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[GetMessageNoteOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
GetMessageNoteOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetMessageNoteOutputVariant2RecoveryOperation = TypedDict('GetMessageNoteOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
GetMessageNoteOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetMessageNoteOutputVariant2Recovery = TypedDict('GetMessageNoteOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[GetMessageNoteOutputVariant2RecoveryOperation],
})
GetMessageNoteOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class GetMessageNoteOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: GetMessageNoteOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: GetMessageNoteOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(GetMessageNoteOutput).
GetMessageNoteOutput = Union[GetMessageNoteOutputVariant2, GetMessageNoteOutputVariant1]

_GetMessageNoteInputAdapter = TypeAdapter(GetMessageNoteInput)
_GetMessageNoteOutputAdapter = TypeAdapter(GetMessageNoteOutput)