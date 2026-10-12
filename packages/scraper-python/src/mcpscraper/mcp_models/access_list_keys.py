from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class AccessListKeysInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    vault: Union[str, None] = Field(None, alias='vault', description='Filter to keys entitled to this vault. Optional; omit to list across all vaults.')
    plan: Union[str, None] = Field(None, alias='plan', description='Filter to keys on this plan (free/pro/team/enterprise). Optional; omit to list all plans.')


AccessListKeysOutputVariant1KeysItem = TypedDict('AccessListKeysOutputVariant1KeysItem', {
    'keyId': Required[str],
    'identity': Required[str],
    'vaults': Required[list[str]],
    'plan': Required[str],
    'revoked': Required[bool],
    'usageCount': Required[Union[float, int]],
    'expiresAt': Required[Union[str, None]],
    'lastUsedAt': Required[Union[str, None]],
})
AccessListKeysOutputVariant1KeysItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AccessListKeysOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='True when the listing succeeded; false on auth/scope error.')
    keys: Union[list[AccessListKeysOutputVariant1KeysItem], None] = Field(None, alias='keys', description='Key metadata for the caller identity. NEVER includes secrets. Present when ok is true.')
    error: Union[str, None] = Field(None, alias='error', description='Human-readable failure reason when ok is false.')


AccessListKeysOutputVariant2DeliveryArtifactsItem = TypedDict('AccessListKeysOutputVariant2DeliveryArtifactsItem', {
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
AccessListKeysOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessListKeysOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AccessListKeysOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AccessListKeysOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessListKeysOutputVariant2Delivery = TypedDict('AccessListKeysOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AccessListKeysOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AccessListKeysOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AccessListKeysOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessListKeysOutputVariant2RecoveryOperation = TypedDict('AccessListKeysOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AccessListKeysOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessListKeysOutputVariant2Recovery = TypedDict('AccessListKeysOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AccessListKeysOutputVariant2RecoveryOperation],
})
AccessListKeysOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AccessListKeysOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AccessListKeysOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AccessListKeysOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AccessListKeysOutput).
AccessListKeysOutput = Union[AccessListKeysOutputVariant2, AccessListKeysOutputVariant1]

_AccessListKeysInputAdapter = TypeAdapter(AccessListKeysInput)
_AccessListKeysOutputAdapter = TypeAdapter(AccessListKeysOutput)