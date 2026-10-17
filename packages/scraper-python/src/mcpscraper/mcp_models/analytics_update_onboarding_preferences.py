from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


AnalyticsUpdateOnboardingPreferencesInputPreferences = TypedDict('AnalyticsUpdateOnboardingPreferencesInputPreferences', {
    'compact': NotRequired[bool],
    'showCompleted': NotRequired[bool],
    'emailAlerts': NotRequired[bool],
})
AnalyticsUpdateOnboardingPreferencesInputPreferences.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class AnalyticsUpdateOnboardingPreferencesInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    site_id: str = Field(..., alias='siteId', description='Analytics Site id returned by analytics_list_sites.')
    preferences: Union[AnalyticsUpdateOnboardingPreferencesInputPreferences, None] = Field(None, alias='preferences', description='Presentation-only account preferences.')
    last_presented_step: Union[Union[Annotated[str, Field(min_length=1, max_length=80)], None], None] = Field(None, alias='lastPresentedStep', description='Setup step most recently presented to the account operator.')
    dismissed_help: Union[Annotated[list[Annotated[str, Field(min_length=1, max_length=80)]], Field(max_length=40)], None] = Field(None, alias='dismissedHelp', description='Help-card keys the account operator dismissed. This cannot complete evidence milestones.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=160)] = Field(..., alias='idempotencyKey', description='Caller-owned idempotency key. Reuse it only when retrying the same logical mutation.')


class AnalyticsUpdateOnboardingPreferencesOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    presentation: dict[str, Any] = Field(..., alias='presentation', description='')


AnalyticsUpdateOnboardingPreferencesOutputVariant2DeliveryArtifactsItem = TypedDict('AnalyticsUpdateOnboardingPreferencesOutputVariant2DeliveryArtifactsItem', {
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
AnalyticsUpdateOnboardingPreferencesOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsUpdateOnboardingPreferencesOutputVariant2DeliveryAvailableExportsItem = TypedDict('AnalyticsUpdateOnboardingPreferencesOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
AnalyticsUpdateOnboardingPreferencesOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsUpdateOnboardingPreferencesOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AnalyticsUpdateOnboardingPreferencesOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AnalyticsUpdateOnboardingPreferencesOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsUpdateOnboardingPreferencesOutputVariant2Delivery = TypedDict('AnalyticsUpdateOnboardingPreferencesOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AnalyticsUpdateOnboardingPreferencesOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[AnalyticsUpdateOnboardingPreferencesOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AnalyticsUpdateOnboardingPreferencesOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AnalyticsUpdateOnboardingPreferencesOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsUpdateOnboardingPreferencesOutputVariant2RecoveryOperation = TypedDict('AnalyticsUpdateOnboardingPreferencesOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AnalyticsUpdateOnboardingPreferencesOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsUpdateOnboardingPreferencesOutputVariant2Recovery = TypedDict('AnalyticsUpdateOnboardingPreferencesOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AnalyticsUpdateOnboardingPreferencesOutputVariant2RecoveryOperation],
})
AnalyticsUpdateOnboardingPreferencesOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsUpdateOnboardingPreferencesOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AnalyticsUpdateOnboardingPreferencesOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AnalyticsUpdateOnboardingPreferencesOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AnalyticsUpdateOnboardingPreferencesOutput).
AnalyticsUpdateOnboardingPreferencesOutput = Union[AnalyticsUpdateOnboardingPreferencesOutputVariant2, AnalyticsUpdateOnboardingPreferencesOutputVariant1]

_AnalyticsUpdateOnboardingPreferencesInputAdapter = TypeAdapter(AnalyticsUpdateOnboardingPreferencesInput)
_AnalyticsUpdateOnboardingPreferencesOutputAdapter = TypeAdapter(AnalyticsUpdateOnboardingPreferencesOutput)