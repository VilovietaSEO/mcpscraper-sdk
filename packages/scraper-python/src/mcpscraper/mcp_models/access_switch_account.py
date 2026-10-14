from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class AccessSwitchAccountInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    owner: Union[str, None] = Field(None, alias='owner', description='Identity whose account to make active. Must be your own identity (switch back) or one that has invited you. Omit to just list available accounts.')


class AccessSwitchAccountOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='True on success; false on auth/scope error.')
    active_owner: Union[str, None] = Field(None, alias='activeOwner', description='The account now active for your identity (your own identity means your own account).')
    is_own_account: Union[bool, None] = Field(None, alias='isOwnAccount', description='True when the active account is your own.')
    available: Union[list[str], None] = Field(None, alias='available', description='Identities whose accounts you can switch into (you have been invited).')
    error: Union[str, None] = Field(None, alias='error', description='Human-readable failure reason when ok is false.')


AccessSwitchAccountOutputVariant2DeliveryArtifactsItem = TypedDict('AccessSwitchAccountOutputVariant2DeliveryArtifactsItem', {
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
AccessSwitchAccountOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessSwitchAccountOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AccessSwitchAccountOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AccessSwitchAccountOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessSwitchAccountOutputVariant2Delivery = TypedDict('AccessSwitchAccountOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AccessSwitchAccountOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AccessSwitchAccountOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AccessSwitchAccountOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessSwitchAccountOutputVariant2RecoveryOperation = TypedDict('AccessSwitchAccountOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AccessSwitchAccountOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessSwitchAccountOutputVariant2Recovery = TypedDict('AccessSwitchAccountOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AccessSwitchAccountOutputVariant2RecoveryOperation],
})
AccessSwitchAccountOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AccessSwitchAccountOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AccessSwitchAccountOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AccessSwitchAccountOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AccessSwitchAccountOutput).
AccessSwitchAccountOutput = Union[AccessSwitchAccountOutputVariant2, AccessSwitchAccountOutputVariant1]

_AccessSwitchAccountInputAdapter = TypeAdapter(AccessSwitchAccountInput)
_AccessSwitchAccountOutputAdapter = TypeAdapter(AccessSwitchAccountOutput)