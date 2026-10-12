from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class GetScheduleStatusInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)



class GetScheduleStatusOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    enabled: Union[bool, None] = Field(None, alias='enabled', description='')
    billing_mode: Union[Literal['credits'], None] = Field(None, alias='billingMode', description='')
    run_base_credits: Union[Union[float, int], None] = Field(None, alias='runBaseCredits', description='')
    llm_cost_multiplier: Union[Union[float, int], None] = Field(None, alias='llmCostMultiplier', description='')
    quota_per_period: Union[Union[float, int], None] = Field(None, alias='quotaPerPeriod', description='')
    used_this_period: Union[Union[float, int], None] = Field(None, alias='usedThisPeriod', description='')
    period_start: Union[str, None] = Field(None, alias='periodStart', description='')
    default_timezone: Union[Union[str, None], None] = Field(None, alias='defaultTimezone', description='IANA timezone applied to new schedules that name a time without a zone; null means UTC.')
    code: Union[str, None] = Field(None, alias='code', description='Machine-readable reason scheduling is unavailable.')
    error: Union[str, None] = Field(None, alias='error', description='')


GetScheduleStatusOutputVariant2DeliveryArtifactsItem = TypedDict('GetScheduleStatusOutputVariant2DeliveryArtifactsItem', {
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
GetScheduleStatusOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetScheduleStatusOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('GetScheduleStatusOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
GetScheduleStatusOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetScheduleStatusOutputVariant2Delivery = TypedDict('GetScheduleStatusOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[GetScheduleStatusOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[GetScheduleStatusOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
GetScheduleStatusOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetScheduleStatusOutputVariant2RecoveryOperation = TypedDict('GetScheduleStatusOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
GetScheduleStatusOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetScheduleStatusOutputVariant2Recovery = TypedDict('GetScheduleStatusOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[GetScheduleStatusOutputVariant2RecoveryOperation],
})
GetScheduleStatusOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class GetScheduleStatusOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: GetScheduleStatusOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: GetScheduleStatusOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(GetScheduleStatusOutput).
GetScheduleStatusOutput = Union[GetScheduleStatusOutputVariant2, GetScheduleStatusOutputVariant1]

_GetScheduleStatusInputAdapter = TypeAdapter(GetScheduleStatusInput)
_GetScheduleStatusOutputAdapter = TypeAdapter(GetScheduleStatusOutput)