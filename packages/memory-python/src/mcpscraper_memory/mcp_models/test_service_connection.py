from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class TestServiceConnectionInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    connection_id: Annotated[str, Field(min_length=1)] = Field(..., alias='connectionId', description='A tenant-owned connectionId from list_service_connections.')
    provider_config_key: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='providerConfigKey', description='Optional provider hint from list_service_connections.')


class TestServiceConnectionOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    operational_status: Union[Literal['available', 'unavailable'], None] = Field(None, alias='operationalStatus', description='')
    checked_at: Union[str, None] = Field(None, alias='checkedAt', description='')
    tool_count: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(None, alias='toolCount', description='')
    code: Union[str, None] = Field(None, alias='code', description='')
    error: Union[str, None] = Field(..., alias='error', description='')


TestServiceConnectionOutputVariant2DeliveryArtifactsItem = TypedDict('TestServiceConnectionOutputVariant2DeliveryArtifactsItem', {
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
TestServiceConnectionOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TestServiceConnectionOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('TestServiceConnectionOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
TestServiceConnectionOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TestServiceConnectionOutputVariant2Delivery = TypedDict('TestServiceConnectionOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[TestServiceConnectionOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[TestServiceConnectionOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
TestServiceConnectionOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TestServiceConnectionOutputVariant2RecoveryOperation = TypedDict('TestServiceConnectionOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
TestServiceConnectionOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TestServiceConnectionOutputVariant2Recovery = TypedDict('TestServiceConnectionOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[TestServiceConnectionOutputVariant2RecoveryOperation],
})
TestServiceConnectionOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class TestServiceConnectionOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: TestServiceConnectionOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: TestServiceConnectionOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(TestServiceConnectionOutput).
TestServiceConnectionOutput = Union[TestServiceConnectionOutputVariant2, TestServiceConnectionOutputVariant1]

_TestServiceConnectionInputAdapter = TypeAdapter(TestServiceConnectionInput)
_TestServiceConnectionOutputAdapter = TypeAdapter(TestServiceConnectionOutput)