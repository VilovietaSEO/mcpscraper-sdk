from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class ListVaultsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)



ListVaultsOutputVariant1VaultsItem = TypedDict('ListVaultsOutputVariant1VaultsItem', {
    'vault': Required[str],
    'handle': Required[str],
    'role': Required[Literal['owner', 'shared']],
    'sharedBy': NotRequired[str],
    'notes': Required[Union[float, int]],
    'bytes': Required[Union[float, int]],
    'kind': Required[Literal['notes', 'channel', 'secure']],
})
ListVaultsOutputVariant1VaultsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ListVaultsOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='True when the listing succeeded; false on an auth/scope error.')
    active_account: Union[str, None] = Field(None, alias='activeAccount', description='The account these vaults belong to (your own identity unless you have switched into another account).')
    is_own_account: Union[bool, None] = Field(None, alias='isOwnAccount', description='True when the active account is your own; false when you have switched into an account someone invited you to.')
    vaults: Union[list[ListVaultsOutputVariant1VaultsItem], None] = Field(None, alias='vaults', description='Every vault visible in the active account, with role, addressable handle, and live storage usage. Present when ok is true.')
    error: Union[str, None] = Field(None, alias='error', description='Human-readable failure reason when ok is false.')


ListVaultsOutputVariant2DeliveryArtifactsItem = TypedDict('ListVaultsOutputVariant2DeliveryArtifactsItem', {
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
ListVaultsOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListVaultsOutputVariant2DeliveryAvailableExportsItem = TypedDict('ListVaultsOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
ListVaultsOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListVaultsOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('ListVaultsOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
ListVaultsOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListVaultsOutputVariant2Delivery = TypedDict('ListVaultsOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[ListVaultsOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[ListVaultsOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[ListVaultsOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
ListVaultsOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListVaultsOutputVariant2RecoveryOperation = TypedDict('ListVaultsOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
ListVaultsOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListVaultsOutputVariant2Recovery = TypedDict('ListVaultsOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[ListVaultsOutputVariant2RecoveryOperation],
})
ListVaultsOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ListVaultsOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: ListVaultsOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: ListVaultsOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(ListVaultsOutput).
ListVaultsOutput = Union[ListVaultsOutputVariant2, ListVaultsOutputVariant1]

_ListVaultsInputAdapter = TypeAdapter(ListVaultsInput)
_ListVaultsOutputAdapter = TypeAdapter(ListVaultsOutput)