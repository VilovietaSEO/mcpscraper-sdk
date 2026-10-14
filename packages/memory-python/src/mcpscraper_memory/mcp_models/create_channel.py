from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


CreateChannelInputInviteMembersItemScope = TypedDict('CreateChannelInputInviteMembersItemScope', {
    'read': NotRequired[bool],
    'write': NotRequired[bool],
    'admin': NotRequired[bool],
})
CreateChannelInputInviteMembersItemScope.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CreateChannelInputInviteMembersItem = TypedDict('CreateChannelInputInviteMembersItem', {
    'identity': Required[Annotated[str, Field(min_length=1)]],
    'scope': NotRequired[CreateChannelInputInviteMembersItemScope],
})
CreateChannelInputInviteMembersItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class CreateChannelInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    name: Annotated[str, Field(min_length=1)] = Field(..., alias='name', description='Channel name. Must match ^[A-Za-z0-9 _-]{1,48}$.')
    invite_members: Union[list[CreateChannelInputInviteMembersItem], None] = Field(None, alias='inviteMembers', description='Members to invite at creation. Optional; you can also invite later with share-vault.')


CreateChannelOutputVariant1MembersItem = TypedDict('CreateChannelOutputVariant1MembersItem', {
    'identity': Required[str],
    'ok': Required[bool],
    'error': NotRequired[str],
})
CreateChannelOutputVariant1MembersItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CreateChannelOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='True when the channel was created; false on auth/scope/validation error.')
    channel: Union[str, None] = Field(None, alias='channel', description='The channel (vault) name. Present when ok is true.')
    created: Union[bool, None] = Field(None, alias='created', description='True if newly created; false if a vault with this name already existed for you (idempotent).')
    members: Union[list[CreateChannelOutputVariant1MembersItem], None] = Field(None, alias='members', description='Per-member invite result. A member entry with ok:false did NOT block channel creation; invite them again later once approved.')
    error: Union[str, None] = Field(None, alias='error', description='Human-readable failure reason when ok is false.')


CreateChannelOutputVariant2DeliveryArtifactsItem = TypedDict('CreateChannelOutputVariant2DeliveryArtifactsItem', {
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
CreateChannelOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateChannelOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('CreateChannelOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
CreateChannelOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateChannelOutputVariant2Delivery = TypedDict('CreateChannelOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[CreateChannelOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[CreateChannelOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
CreateChannelOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateChannelOutputVariant2RecoveryOperation = TypedDict('CreateChannelOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CreateChannelOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateChannelOutputVariant2Recovery = TypedDict('CreateChannelOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[CreateChannelOutputVariant2RecoveryOperation],
})
CreateChannelOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CreateChannelOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: CreateChannelOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: CreateChannelOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(CreateChannelOutput).
CreateChannelOutput = Union[CreateChannelOutputVariant2, CreateChannelOutputVariant1]

_CreateChannelInputAdapter = TypeAdapter(CreateChannelInput)
_CreateChannelOutputAdapter = TypeAdapter(CreateChannelOutput)