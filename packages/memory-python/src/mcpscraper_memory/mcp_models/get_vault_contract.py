from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class GetVaultContractInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    vault: str = Field(..., alias='vault', description='One governed vault: Ideas, Examples and Inspirations, Knowledge, Library, People, Organizations, Deals, Communication, Calendar, Tasks, Projects, Issues, Improvement Log, Experiments, Sprint, or Skills. Former names Inspiration and Communications still resolve.')


class GetVaultContractOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    vault: Union[str, None] = Field(None, alias='vault', description='')
    contract: Union[dict[str, Any], None] = Field(None, alias='contract', description='')
    error: Union[str, None] = Field(None, alias='error', description='')


GetVaultContractOutputVariant2DeliveryArtifactsItem = TypedDict('GetVaultContractOutputVariant2DeliveryArtifactsItem', {
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
GetVaultContractOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetVaultContractOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('GetVaultContractOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
GetVaultContractOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetVaultContractOutputVariant2Delivery = TypedDict('GetVaultContractOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[GetVaultContractOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[GetVaultContractOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
GetVaultContractOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetVaultContractOutputVariant2RecoveryOperation = TypedDict('GetVaultContractOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
GetVaultContractOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetVaultContractOutputVariant2Recovery = TypedDict('GetVaultContractOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[GetVaultContractOutputVariant2RecoveryOperation],
})
GetVaultContractOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class GetVaultContractOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: GetVaultContractOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: GetVaultContractOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(GetVaultContractOutput).
GetVaultContractOutput = Union[GetVaultContractOutputVariant2, GetVaultContractOutputVariant1]

_GetVaultContractInputAdapter = TypeAdapter(GetVaultContractInput)
_GetVaultContractOutputAdapter = TypeAdapter(GetVaultContractOutput)