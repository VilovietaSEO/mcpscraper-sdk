from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class RemoveChannelMemberInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    vault: Annotated[str, Field(min_length=1)] = Field(..., alias='vault', description='The vault (channel) to remove the member from. You must own it.')
    identity: Annotated[str, Field(min_length=1)] = Field(..., alias='identity', description='The member to remove.')


class RemoveChannelMemberOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='True on success; false on auth/scope/ownership error.')
    removed: Union[bool, None] = Field(None, alias='removed', description='True if a membership was found and removed; false if they were not a member.')
    error: Union[str, None] = Field(None, alias='error', description='Human-readable failure reason when ok is false.')


RemoveChannelMemberOutputVariant2DeliveryArtifactsItem = TypedDict('RemoveChannelMemberOutputVariant2DeliveryArtifactsItem', {
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
RemoveChannelMemberOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


RemoveChannelMemberOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('RemoveChannelMemberOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
RemoveChannelMemberOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


RemoveChannelMemberOutputVariant2Delivery = TypedDict('RemoveChannelMemberOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[RemoveChannelMemberOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[RemoveChannelMemberOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
RemoveChannelMemberOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


RemoveChannelMemberOutputVariant2RecoveryOperation = TypedDict('RemoveChannelMemberOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
RemoveChannelMemberOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


RemoveChannelMemberOutputVariant2Recovery = TypedDict('RemoveChannelMemberOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[RemoveChannelMemberOutputVariant2RecoveryOperation],
})
RemoveChannelMemberOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class RemoveChannelMemberOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: RemoveChannelMemberOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: RemoveChannelMemberOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(RemoveChannelMemberOutput).
RemoveChannelMemberOutput = Union[RemoveChannelMemberOutputVariant2, RemoveChannelMemberOutputVariant1]

_RemoveChannelMemberInputAdapter = TypeAdapter(RemoveChannelMemberInput)
_RemoveChannelMemberOutputAdapter = TypeAdapter(RemoveChannelMemberOutput)