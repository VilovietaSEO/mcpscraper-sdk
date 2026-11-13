from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class AccessInboxSettingsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    allow_unapproved_senders: bool = Field(..., alias='allowUnapprovedSenders', description='Set true to accept invites/shares from anyone; false to require approval.')


class AccessInboxSettingsOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='True on success; false on auth error.')
    allow_unapproved_senders: Union[bool, None] = Field(None, alias='allowUnapprovedSenders', description='The setting now in effect.')
    error: Union[str, None] = Field(None, alias='error', description='Human-readable failure reason when ok is false.')


AccessInboxSettingsOutputVariant2DeliveryArtifactsItem = TypedDict('AccessInboxSettingsOutputVariant2DeliveryArtifactsItem', {
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
AccessInboxSettingsOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessInboxSettingsOutputVariant2DeliveryAvailableExportsItem = TypedDict('AccessInboxSettingsOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
AccessInboxSettingsOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessInboxSettingsOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AccessInboxSettingsOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AccessInboxSettingsOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessInboxSettingsOutputVariant2Delivery = TypedDict('AccessInboxSettingsOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AccessInboxSettingsOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[AccessInboxSettingsOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AccessInboxSettingsOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AccessInboxSettingsOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessInboxSettingsOutputVariant2RecoveryOperation = TypedDict('AccessInboxSettingsOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AccessInboxSettingsOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessInboxSettingsOutputVariant2Recovery = TypedDict('AccessInboxSettingsOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AccessInboxSettingsOutputVariant2RecoveryOperation],
})
AccessInboxSettingsOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AccessInboxSettingsOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AccessInboxSettingsOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AccessInboxSettingsOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AccessInboxSettingsOutput).
AccessInboxSettingsOutput = Union[AccessInboxSettingsOutputVariant2, AccessInboxSettingsOutputVariant1]

_AccessInboxSettingsInputAdapter = TypeAdapter(AccessInboxSettingsInput)
_AccessInboxSettingsOutputAdapter = TypeAdapter(AccessInboxSettingsOutput)