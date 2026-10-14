from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class AddVaultInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    vault: Annotated[str, Field(min_length=1)] = Field(..., alias='vault', description='Name of the vault to create. Must match ^[A-Za-z0-9 _-]{1,48}$ (letters, digits, space, _ or -, 1-48 chars).')
    owner: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='owner', description='Identity that should OWN the new vault (becomes the owner entitlement, so list-vaults reports role "owner" for them). Optional; defaults to the caller. Used when an admin bootstraps a personal vault on a user\'s behalf so the user owns it rather than receiving it as a share.')


class AddVaultOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='True when the request succeeded (whether or not a new vault was created); false on auth/scope/validation error.')
    vault: Union[str, None] = Field(None, alias='vault', description='The vault name. Present when ok is true.')
    created: Union[bool, None] = Field(None, alias='created', description='True if a new vault was created; false if it already existed (idempotent no-op). Present when ok is true.')
    error: Union[str, None] = Field(None, alias='error', description='Human-readable failure reason when ok is false.')


AddVaultOutputVariant2DeliveryArtifactsItem = TypedDict('AddVaultOutputVariant2DeliveryArtifactsItem', {
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
AddVaultOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AddVaultOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AddVaultOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AddVaultOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AddVaultOutputVariant2Delivery = TypedDict('AddVaultOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AddVaultOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AddVaultOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AddVaultOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AddVaultOutputVariant2RecoveryOperation = TypedDict('AddVaultOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AddVaultOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AddVaultOutputVariant2Recovery = TypedDict('AddVaultOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AddVaultOutputVariant2RecoveryOperation],
})
AddVaultOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AddVaultOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AddVaultOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AddVaultOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AddVaultOutput).
AddVaultOutput = Union[AddVaultOutputVariant2, AddVaultOutputVariant1]

_AddVaultInputAdapter = TypeAdapter(AddVaultInput)
_AddVaultOutputAdapter = TypeAdapter(AddVaultOutput)