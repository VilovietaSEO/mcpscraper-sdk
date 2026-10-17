from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class DeleteVaultInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    vault: Annotated[str, Field(min_length=1)] = Field(..., alias='vault', description='Exact name of the vault to delete. The caller must own this vault and hold admin scope on it.')


class DeleteVaultOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='True when the vault was deleted; false on auth/scope/ownership error.')
    vault: Union[str, None] = Field(None, alias='vault', description='The deleted vault name. Present when ok is true.')
    deleted_notes: Union[Union[float, int], None] = Field(None, alias='deletedNotes', description='Number of notes removed from the vault. Present when ok is true.')
    deleted_facts: Union[Union[float, int], None] = Field(None, alias='deletedFacts', description='Number of facts (active + superseded) removed from the vault. Present when ok is true.')
    error: Union[str, None] = Field(None, alias='error', description='Human-readable failure reason when ok is false.')


DeleteVaultOutputVariant2DeliveryArtifactsItem = TypedDict('DeleteVaultOutputVariant2DeliveryArtifactsItem', {
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
DeleteVaultOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


DeleteVaultOutputVariant2DeliveryAvailableExportsItem = TypedDict('DeleteVaultOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
DeleteVaultOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


DeleteVaultOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('DeleteVaultOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
DeleteVaultOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


DeleteVaultOutputVariant2Delivery = TypedDict('DeleteVaultOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[DeleteVaultOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[DeleteVaultOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[DeleteVaultOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
DeleteVaultOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


DeleteVaultOutputVariant2RecoveryOperation = TypedDict('DeleteVaultOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
DeleteVaultOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


DeleteVaultOutputVariant2Recovery = TypedDict('DeleteVaultOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[DeleteVaultOutputVariant2RecoveryOperation],
})
DeleteVaultOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class DeleteVaultOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: DeleteVaultOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: DeleteVaultOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(DeleteVaultOutput).
DeleteVaultOutput = Union[DeleteVaultOutputVariant2, DeleteVaultOutputVariant1]

_DeleteVaultInputAdapter = TypeAdapter(DeleteVaultInput)
_DeleteVaultOutputAdapter = TypeAdapter(DeleteVaultOutput)