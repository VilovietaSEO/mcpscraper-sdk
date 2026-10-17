from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class StorageUsageInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)



StorageUsageOutputVariant1PerVaultItem = TypedDict('StorageUsageOutputVariant1PerVaultItem', {
    'vault': Required[str],
    'bytes': Required[Union[float, int]],
    'gb': Required[Union[float, int]],
    'notes': Required[Union[float, int]],
})
StorageUsageOutputVariant1PerVaultItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class StorageUsageOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='True when usage was computed; false on an auth/scope error.')
    total_bytes: Union[Union[float, int], None] = Field(None, alias='totalBytes', description='Total stored bytes across all the caller vaults. Present when ok is true.')
    total_gb: Union[Union[float, int], None] = Field(None, alias='totalGb', description='Total stored size in decimal GB (bytes / 1e9), rounded to 2 decimals. Present when ok is true.')
    quota_bytes: Union[Union[Union[float, int], None], None] = Field(None, alias='quotaBytes', description='Storage quota in bytes for the caller plan. Null when the plan is unlimited. Present when ok is true.')
    quota_gb: Union[Union[Union[float, int], None], None] = Field(None, alias='quotaGb', description='Storage quota in decimal GB, rounded to 2 decimals. Null when the plan is unlimited. Present when ok is true.')
    unlimited: Union[bool, None] = Field(None, alias='unlimited', description='True when the caller plan is unlimited (no storage ceiling). Render "Unlimited" instead of a quota figure.')
    per_vault: Union[list[StorageUsageOutputVariant1PerVaultItem], None] = Field(None, alias='perVault', description='Per-vault storage breakdown for the caller vaults. Present when ok is true.')
    error: Union[str, None] = Field(None, alias='error', description='Human-readable failure reason when ok is false.')


StorageUsageOutputVariant2DeliveryArtifactsItem = TypedDict('StorageUsageOutputVariant2DeliveryArtifactsItem', {
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
StorageUsageOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


StorageUsageOutputVariant2DeliveryAvailableExportsItem = TypedDict('StorageUsageOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
StorageUsageOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


StorageUsageOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('StorageUsageOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
StorageUsageOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


StorageUsageOutputVariant2Delivery = TypedDict('StorageUsageOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[StorageUsageOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[StorageUsageOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[StorageUsageOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
StorageUsageOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


StorageUsageOutputVariant2RecoveryOperation = TypedDict('StorageUsageOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
StorageUsageOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


StorageUsageOutputVariant2Recovery = TypedDict('StorageUsageOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[StorageUsageOutputVariant2RecoveryOperation],
})
StorageUsageOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class StorageUsageOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: StorageUsageOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: StorageUsageOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(StorageUsageOutput).
StorageUsageOutput = Union[StorageUsageOutputVariant2, StorageUsageOutputVariant1]

_StorageUsageInputAdapter = TypeAdapter(StorageUsageInput)
_StorageUsageOutputAdapter = TypeAdapter(StorageUsageOutput)