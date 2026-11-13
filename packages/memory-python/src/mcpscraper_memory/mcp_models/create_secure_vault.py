from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class CreateSecureVaultInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    name: Annotated[str, Field(min_length=1)] = Field(..., alias='name', description='Vault name. Must match ^[A-Za-z0-9 _-]{1,48}$. Defaults to a name like "Passwords" if the caller has no preference.')


class CreateSecureVaultOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='True when the vault was created; false on auth/scope/validation error.')
    vault: Union[str, None] = Field(None, alias='vault', description='The vault name. Present when ok is true.')
    created: Union[bool, None] = Field(None, alias='created', description='True if newly created; false if a vault with this name already existed for you (idempotent) — note this does NOT confirm the existing vault is secure-kind; check list-vaults if unsure.')
    error: Union[str, None] = Field(None, alias='error', description='Human-readable failure reason when ok is false.')


CreateSecureVaultOutputVariant2DeliveryArtifactsItem = TypedDict('CreateSecureVaultOutputVariant2DeliveryArtifactsItem', {
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
CreateSecureVaultOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateSecureVaultOutputVariant2DeliveryAvailableExportsItem = TypedDict('CreateSecureVaultOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
CreateSecureVaultOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateSecureVaultOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('CreateSecureVaultOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
CreateSecureVaultOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateSecureVaultOutputVariant2Delivery = TypedDict('CreateSecureVaultOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[CreateSecureVaultOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[CreateSecureVaultOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[CreateSecureVaultOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
CreateSecureVaultOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateSecureVaultOutputVariant2RecoveryOperation = TypedDict('CreateSecureVaultOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CreateSecureVaultOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateSecureVaultOutputVariant2Recovery = TypedDict('CreateSecureVaultOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[CreateSecureVaultOutputVariant2RecoveryOperation],
})
CreateSecureVaultOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CreateSecureVaultOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: CreateSecureVaultOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: CreateSecureVaultOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(CreateSecureVaultOutput).
CreateSecureVaultOutput = Union[CreateSecureVaultOutputVariant2, CreateSecureVaultOutputVariant1]

_CreateSecureVaultInputAdapter = TypeAdapter(CreateSecureVaultInput)
_CreateSecureVaultOutputAdapter = TypeAdapter(CreateSecureVaultOutput)