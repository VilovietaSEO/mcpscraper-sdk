from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class AccessRevokeKeyInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    key_id: Annotated[str, Field(min_length=1)] = Field(..., alias='keyId', description='Identifier of the key to revoke (from access-list-keys). Must be a key the caller owns or fully covers.')


class AccessRevokeKeyOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='True when the revoke operation completed; false on auth/scope error or not-found.')
    key_id: Union[str, None] = Field(None, alias='keyId', description='The key that was targeted for revocation.')
    revoked: Union[bool, None] = Field(None, alias='revoked', description='True if the key is now revoked.')
    error: Union[str, None] = Field(None, alias='error', description='Human-readable failure reason when ok is false (e.g. "key not found").')


AccessRevokeKeyOutputVariant2DeliveryArtifactsItem = TypedDict('AccessRevokeKeyOutputVariant2DeliveryArtifactsItem', {
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
AccessRevokeKeyOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessRevokeKeyOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AccessRevokeKeyOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AccessRevokeKeyOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessRevokeKeyOutputVariant2Delivery = TypedDict('AccessRevokeKeyOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AccessRevokeKeyOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AccessRevokeKeyOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AccessRevokeKeyOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessRevokeKeyOutputVariant2RecoveryOperation = TypedDict('AccessRevokeKeyOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AccessRevokeKeyOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessRevokeKeyOutputVariant2Recovery = TypedDict('AccessRevokeKeyOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AccessRevokeKeyOutputVariant2RecoveryOperation],
})
AccessRevokeKeyOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AccessRevokeKeyOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AccessRevokeKeyOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AccessRevokeKeyOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AccessRevokeKeyOutput).
AccessRevokeKeyOutput = Union[AccessRevokeKeyOutputVariant2, AccessRevokeKeyOutputVariant1]

_AccessRevokeKeyInputAdapter = TypeAdapter(AccessRevokeKeyInput)
_AccessRevokeKeyOutputAdapter = TypeAdapter(AccessRevokeKeyOutput)