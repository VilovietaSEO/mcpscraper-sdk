from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


AccessShareVaultInputScope = TypedDict('AccessShareVaultInputScope', {
    'read': NotRequired[bool],
    'write': NotRequired[bool],
    'export': NotRequired[bool],
    'index': NotRequired[bool],
    'admin': NotRequired[bool],
    'swap': NotRequired[bool],
})
AccessShareVaultInputScope.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class AccessShareVaultInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    vault: Annotated[str, Field(min_length=1)] = Field(..., alias='vault', description='Vault to share. The caller must control (be entitled to) this vault and hold write scope.')
    grantee_identity: Annotated[str, Field(min_length=1)] = Field(..., alias='granteeIdentity', description='Identity to grant access to (e.g. an email or user id).')
    scope: Union[AccessShareVaultInputScope, None] = Field(None, alias='scope', description='Entitlement scope to grant (read/write/export/index/admin/swap). Optional; omit for least-privilege read-only.')


class AccessShareVaultOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='True when the entitlement was written; false on auth/scope error.')
    vault: Union[str, None] = Field(None, alias='vault', description='The vault that was shared.')
    grantee: Union[str, None] = Field(None, alias='grantee', description='The identity that was granted access.')
    note: Union[str, None] = Field(None, alias='note', description='Guidance on next steps (e.g. the grantee still needs a key tied to this vault).')
    error: Union[str, None] = Field(None, alias='error', description='Human-readable failure reason when ok is false.')


AccessShareVaultOutputVariant2DeliveryArtifactsItem = TypedDict('AccessShareVaultOutputVariant2DeliveryArtifactsItem', {
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
AccessShareVaultOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessShareVaultOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AccessShareVaultOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AccessShareVaultOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessShareVaultOutputVariant2Delivery = TypedDict('AccessShareVaultOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AccessShareVaultOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AccessShareVaultOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AccessShareVaultOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessShareVaultOutputVariant2RecoveryOperation = TypedDict('AccessShareVaultOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AccessShareVaultOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessShareVaultOutputVariant2Recovery = TypedDict('AccessShareVaultOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AccessShareVaultOutputVariant2RecoveryOperation],
})
AccessShareVaultOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AccessShareVaultOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AccessShareVaultOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AccessShareVaultOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AccessShareVaultOutput).
AccessShareVaultOutput = Union[AccessShareVaultOutputVariant2, AccessShareVaultOutputVariant1]

_AccessShareVaultInputAdapter = TypeAdapter(AccessShareVaultInput)
_AccessShareVaultOutputAdapter = TypeAdapter(AccessShareVaultOutput)