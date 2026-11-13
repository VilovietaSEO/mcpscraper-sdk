from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class ListChannelMembersInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    vault: Annotated[str, Field(min_length=1)] = Field(..., alias='vault', description='The vault (channel) to list members of. You must own it.')


ListChannelMembersOutputVariant1MembersItemScope = TypedDict('ListChannelMembersOutputVariant1MembersItemScope', {
    'read': Required[bool],
    'write': Required[bool],
    'export': Required[bool],
    'index': Required[bool],
    'admin': Required[bool],
    'swap': Required[bool],
})
ListChannelMembersOutputVariant1MembersItemScope.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListChannelMembersOutputVariant1MembersItem = TypedDict('ListChannelMembersOutputVariant1MembersItem', {
    'identity': Required[str],
    'scope': Required[ListChannelMembersOutputVariant1MembersItemScope],
    'since': Required[str],
    'isAgent': Required[bool],
})
ListChannelMembersOutputVariant1MembersItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ListChannelMembersOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='True on success; false on auth/scope/ownership error.')
    owner: Union[str, None] = Field(None, alias='owner', description='The channel owner.')
    can_manage: Union[bool, None] = Field(None, alias='canManage', description='True if the caller is the owner (and so can call remove-channel-member).')
    members: Union[list[ListChannelMembersOutputVariant1MembersItem], None] = Field(None, alias='members', description='Present when ok is true. Always includes at least the owner.')
    error: Union[str, None] = Field(None, alias='error', description='Human-readable failure reason when ok is false.')


ListChannelMembersOutputVariant2DeliveryArtifactsItem = TypedDict('ListChannelMembersOutputVariant2DeliveryArtifactsItem', {
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
ListChannelMembersOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListChannelMembersOutputVariant2DeliveryAvailableExportsItem = TypedDict('ListChannelMembersOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
ListChannelMembersOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListChannelMembersOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('ListChannelMembersOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
ListChannelMembersOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListChannelMembersOutputVariant2Delivery = TypedDict('ListChannelMembersOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[ListChannelMembersOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[ListChannelMembersOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[ListChannelMembersOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
ListChannelMembersOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListChannelMembersOutputVariant2RecoveryOperation = TypedDict('ListChannelMembersOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
ListChannelMembersOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListChannelMembersOutputVariant2Recovery = TypedDict('ListChannelMembersOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[ListChannelMembersOutputVariant2RecoveryOperation],
})
ListChannelMembersOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ListChannelMembersOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: ListChannelMembersOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: ListChannelMembersOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(ListChannelMembersOutput).
ListChannelMembersOutput = Union[ListChannelMembersOutputVariant2, ListChannelMembersOutputVariant1]

_ListChannelMembersInputAdapter = TypeAdapter(ListChannelMembersInput)
_ListChannelMembersOutputAdapter = TypeAdapter(ListChannelMembersOutput)