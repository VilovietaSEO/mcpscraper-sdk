from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class GetLocalSourcebookContractInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    category: Union[Literal['home', 'professional', 'restaurants', 'financial', 'realestate', 'auto', 'wellness'], None] = Field(None, alias='category', description='Optional category whose required canonical tag and contract details should be selected.')


class GetLocalSourcebookContractOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)



GetLocalSourcebookContractOutputVariant2DeliveryArtifactsItem = TypedDict('GetLocalSourcebookContractOutputVariant2DeliveryArtifactsItem', {
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
GetLocalSourcebookContractOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetLocalSourcebookContractOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('GetLocalSourcebookContractOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
GetLocalSourcebookContractOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetLocalSourcebookContractOutputVariant2Delivery = TypedDict('GetLocalSourcebookContractOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[GetLocalSourcebookContractOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[GetLocalSourcebookContractOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
GetLocalSourcebookContractOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetLocalSourcebookContractOutputVariant2RecoveryOperation = TypedDict('GetLocalSourcebookContractOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
GetLocalSourcebookContractOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetLocalSourcebookContractOutputVariant2Recovery = TypedDict('GetLocalSourcebookContractOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[GetLocalSourcebookContractOutputVariant2RecoveryOperation],
})
GetLocalSourcebookContractOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class GetLocalSourcebookContractOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: GetLocalSourcebookContractOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: GetLocalSourcebookContractOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(GetLocalSourcebookContractOutput).
GetLocalSourcebookContractOutput = Union[GetLocalSourcebookContractOutputVariant2, GetLocalSourcebookContractOutputVariant1]

_GetLocalSourcebookContractInputAdapter = TypeAdapter(GetLocalSourcebookContractInput)
_GetLocalSourcebookContractOutputAdapter = TypeAdapter(GetLocalSourcebookContractOutput)