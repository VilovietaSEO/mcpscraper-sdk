from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class CostUsageInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    period: Union[str, None] = Field(None, alias='period', description='Billing month as YYYY-MM. Optional; defaults to the current month.')


CostUsageOutputVariant1ByTierItem = TypedDict('CostUsageOutputVariant1ByTierItem', {
    'plan': Required[str],
    'users': Required[Union[float, int]],
    'totalUsd': Required[Union[float, int]],
    'avgUsdPerUser': Required[Union[float, int]],
})
CostUsageOutputVariant1ByTierItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CostUsageOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='True when usage was computed; false on auth/scope error.')
    identity: Union[str, None] = Field(None, alias='identity', description='The caller identity the costs are scoped to.')
    period: Union[str, None] = Field(None, alias='period', description='Billing month the figures cover (YYYY-MM).')
    plan: Union[str, None] = Field(None, alias='plan', description='Caller plan.')
    cost_usd: Union[Union[float, int], None] = Field(None, alias='costUsd', description='Total metered cost this period in USD.')
    by_source: Union[dict[str, Union[float, int]], None] = Field(None, alias='bySource', description='Cost breakdown by source (llm/embed/storage/compute).')
    free_cap_usd: Union[Union[float, int], None] = Field(None, alias='freeCapUsd', description='The free-tier monthly processing cap in USD.')
    free_cap_reached: Union[bool, None] = Field(None, alias='freeCapReached', description='True when a free caller is at/over the cap (embeds/optimization paused).')
    pro_budget_usd: Union[Union[float, int], None] = Field(None, alias='proBudgetUsd', description='The Pro soft fair-use budget (price / 3) in USD.')
    total_bytes: Union[Union[float, int], None] = Field(None, alias='totalBytes', description='Total stored bytes for the caller.')
    total_gb: Union[Union[float, int], None] = Field(None, alias='totalGb', description='Total stored GB for the caller.')
    quota_gb: Union[Union[Union[float, int], None], None] = Field(None, alias='quotaGb', description='Storage quota in GB for the caller plan. Null when the plan is unlimited.')
    unlimited: Union[bool, None] = Field(None, alias='unlimited', description='True when the caller is on the unlimited plan (no storage ceiling, exempt from the free cost cap).')
    by_tier: Union[list[CostUsageOutputVariant1ByTierItem], None] = Field(None, alias='byTier', description='Operator-only: blended cost-per-user per plan for the current period.')
    error: Union[str, None] = Field(None, alias='error', description='Human-readable failure reason when ok is false.')


CostUsageOutputVariant2DeliveryArtifactsItem = TypedDict('CostUsageOutputVariant2DeliveryArtifactsItem', {
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
CostUsageOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CostUsageOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('CostUsageOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
CostUsageOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CostUsageOutputVariant2Delivery = TypedDict('CostUsageOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[CostUsageOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[CostUsageOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
CostUsageOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CostUsageOutputVariant2RecoveryOperation = TypedDict('CostUsageOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CostUsageOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CostUsageOutputVariant2Recovery = TypedDict('CostUsageOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[CostUsageOutputVariant2RecoveryOperation],
})
CostUsageOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CostUsageOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: CostUsageOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: CostUsageOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(CostUsageOutput).
CostUsageOutput = Union[CostUsageOutputVariant2, CostUsageOutputVariant1]

_CostUsageInputAdapter = TypeAdapter(CostUsageInput)
_CostUsageOutputAdapter = TypeAdapter(CostUsageOutput)