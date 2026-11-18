from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class AiVisibilityReportGuideInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    focus: Union[Literal['workflow', 'data_contract', 'example'], None] = Field(None, alias='focus', description='Which part of the AI visibility report guide to return. Start with workflow; fetch data_contract for how each measure is computed, or example for a complete input.')


class AiVisibilityReportGuideOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    focus: Literal['workflow', 'data_contract', 'example'] = Field(..., alias='focus', description='')
    guide: str = Field(..., alias='guide', description='')


AiVisibilityReportGuideOutputVariant2DeliveryArtifactsItem = TypedDict('AiVisibilityReportGuideOutputVariant2DeliveryArtifactsItem', {
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
AiVisibilityReportGuideOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AiVisibilityReportGuideOutputVariant2DeliveryAvailableExportsItem = TypedDict('AiVisibilityReportGuideOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
AiVisibilityReportGuideOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AiVisibilityReportGuideOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AiVisibilityReportGuideOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AiVisibilityReportGuideOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AiVisibilityReportGuideOutputVariant2Delivery = TypedDict('AiVisibilityReportGuideOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AiVisibilityReportGuideOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[AiVisibilityReportGuideOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AiVisibilityReportGuideOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AiVisibilityReportGuideOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AiVisibilityReportGuideOutputVariant2RecoveryOperation = TypedDict('AiVisibilityReportGuideOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AiVisibilityReportGuideOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AiVisibilityReportGuideOutputVariant2Recovery = TypedDict('AiVisibilityReportGuideOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AiVisibilityReportGuideOutputVariant2RecoveryOperation],
})
AiVisibilityReportGuideOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AiVisibilityReportGuideOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AiVisibilityReportGuideOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AiVisibilityReportGuideOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AiVisibilityReportGuideOutput).
AiVisibilityReportGuideOutput = Union[AiVisibilityReportGuideOutputVariant2, AiVisibilityReportGuideOutputVariant1]

_AiVisibilityReportGuideInputAdapter = TypeAdapter(AiVisibilityReportGuideInput)
_AiVisibilityReportGuideOutputAdapter = TypeAdapter(AiVisibilityReportGuideOutput)