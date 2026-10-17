from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


AccessInviteAccountInputScope = TypedDict('AccessInviteAccountInputScope', {
    'read': NotRequired[bool],
    'write': NotRequired[bool],
    'export': NotRequired[bool],
    'index': NotRequired[bool],
    'admin': NotRequired[bool],
    'swap': NotRequired[bool],
})
AccessInviteAccountInputScope.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class AccessInviteAccountInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    grantee_identity: Annotated[str, Field(min_length=1)] = Field(..., alias='granteeIdentity', description='Identity (email or user id) to invite into your full account.')
    scope: Union[AccessInviteAccountInputScope, None] = Field(None, alias='scope', description='Permissions to grant across your account. Optional; defaults to read+write (read, write, export, index, swap).')
    revoke: Union[bool, None] = Field(None, alias='revoke', description='Set true to revoke an existing account invite for this grantee instead of granting one.')


AccessInviteAccountOutputVariant1Granted = TypedDict('AccessInviteAccountOutputVariant1Granted', {
    'read': Required[bool],
    'write': Required[bool],
    'export': Required[bool],
    'index': Required[bool],
    'admin': Required[bool],
    'swap': Required[bool],
})
AccessInviteAccountOutputVariant1Granted.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AccessInviteAccountOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='True on success; false on auth/scope error.')
    grantee: Union[str, None] = Field(None, alias='grantee', description='The identity that was invited or revoked.')
    granted: Union[AccessInviteAccountOutputVariant1Granted, None] = Field(None, alias='granted', description='The permissions now in effect for the grantee. Absent on revoke.')
    revoked: Union[bool, None] = Field(None, alias='revoked', description='True when an existing invite was removed.')
    note: Union[str, None] = Field(None, alias='note', description='Guidance on next steps for the grantee.')
    error: Union[str, None] = Field(None, alias='error', description='Human-readable failure reason when ok is false.')


AccessInviteAccountOutputVariant2DeliveryArtifactsItem = TypedDict('AccessInviteAccountOutputVariant2DeliveryArtifactsItem', {
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
AccessInviteAccountOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessInviteAccountOutputVariant2DeliveryAvailableExportsItem = TypedDict('AccessInviteAccountOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
AccessInviteAccountOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessInviteAccountOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AccessInviteAccountOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AccessInviteAccountOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessInviteAccountOutputVariant2Delivery = TypedDict('AccessInviteAccountOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AccessInviteAccountOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[AccessInviteAccountOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AccessInviteAccountOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AccessInviteAccountOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessInviteAccountOutputVariant2RecoveryOperation = TypedDict('AccessInviteAccountOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AccessInviteAccountOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessInviteAccountOutputVariant2Recovery = TypedDict('AccessInviteAccountOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AccessInviteAccountOutputVariant2RecoveryOperation],
})
AccessInviteAccountOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AccessInviteAccountOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AccessInviteAccountOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AccessInviteAccountOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AccessInviteAccountOutput).
AccessInviteAccountOutput = Union[AccessInviteAccountOutputVariant2, AccessInviteAccountOutputVariant1]

_AccessInviteAccountInputAdapter = TypeAdapter(AccessInviteAccountInput)
_AccessInviteAccountOutputAdapter = TypeAdapter(AccessInviteAccountOutput)