from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class AccessSwapVaultInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    vault: Annotated[str, Field(min_length=1)] = Field(..., alias='vault', description='Vault to make active for the session. Must be an entitled vault and the key must hold "swap" scope.')


class AccessSwapVaultOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='True when the active vault was set; false on auth/scope error.')
    active_vault: Union[str, None] = Field(None, alias='activeVault', description='The vault now active for the session.')
    session: Union[str, None] = Field(None, alias='session', description='The session the active vault was set for.')
    error: Union[str, None] = Field(None, alias='error', description='Human-readable failure reason when ok is false.')


AccessSwapVaultOutputVariant2DeliveryArtifactsItem = TypedDict('AccessSwapVaultOutputVariant2DeliveryArtifactsItem', {
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
AccessSwapVaultOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessSwapVaultOutputVariant2DeliveryAvailableExportsItem = TypedDict('AccessSwapVaultOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
AccessSwapVaultOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessSwapVaultOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AccessSwapVaultOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AccessSwapVaultOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessSwapVaultOutputVariant2Delivery = TypedDict('AccessSwapVaultOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AccessSwapVaultOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[AccessSwapVaultOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AccessSwapVaultOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AccessSwapVaultOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessSwapVaultOutputVariant2RecoveryOperation = TypedDict('AccessSwapVaultOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AccessSwapVaultOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessSwapVaultOutputVariant2Recovery = TypedDict('AccessSwapVaultOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AccessSwapVaultOutputVariant2RecoveryOperation],
})
AccessSwapVaultOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AccessSwapVaultOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AccessSwapVaultOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AccessSwapVaultOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AccessSwapVaultOutput).
AccessSwapVaultOutput = Union[AccessSwapVaultOutputVariant2, AccessSwapVaultOutputVariant1]

_AccessSwapVaultInputAdapter = TypeAdapter(AccessSwapVaultInput)
_AccessSwapVaultOutputAdapter = TypeAdapter(AccessSwapVaultOutput)