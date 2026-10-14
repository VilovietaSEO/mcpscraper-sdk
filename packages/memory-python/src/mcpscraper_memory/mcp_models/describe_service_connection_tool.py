from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class DescribeServiceConnectionToolInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    connection_id: Annotated[str, Field(min_length=1)] = Field(..., alias='connectionId', description='A tenant-owned connectionId from list_service_connections.')
    tool: Annotated[str, Field(min_length=1)] = Field(..., alias='tool', description="One exact name from that connection's readTools or actionTools. Admin-blocked and arbitrary names are rejected.")
    fresh: Union[bool, None] = Field(None, alias='fresh', description='Bypass the short-lived sanitized schema cache. Ownership, connection state, and tool policy are still rechecked; use only when a provider tool catalog just changed.')


DescribeServiceConnectionToolOutputVariant1ToolAnnotations = TypedDict('DescribeServiceConnectionToolOutputVariant1ToolAnnotations', {
    'title': NotRequired[str],
    'readOnlyHint': NotRequired[bool],
    'destructiveHint': NotRequired[bool],
    'idempotentHint': NotRequired[bool],
    'openWorldHint': NotRequired[bool],
})
DescribeServiceConnectionToolOutputVariant1ToolAnnotations.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


DescribeServiceConnectionToolOutputVariant1ToolIconsItem = TypedDict('DescribeServiceConnectionToolOutputVariant1ToolIconsItem', {
    'src': Required[str],
    'mimeType': NotRequired[str],
    'sizes': NotRequired[list[str]],
    'theme': NotRequired[Literal['light', 'dark']],
})
DescribeServiceConnectionToolOutputVariant1ToolIconsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


DescribeServiceConnectionToolOutputVariant1ToolExecution = TypedDict('DescribeServiceConnectionToolOutputVariant1ToolExecution', {
    'taskSupport': Required[Literal['forbidden', 'optional', 'required']],
})
DescribeServiceConnectionToolOutputVariant1ToolExecution.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


DescribeServiceConnectionToolOutputVariant1Tool = TypedDict('DescribeServiceConnectionToolOutputVariant1Tool', {
    'name': Required[str],
    'title': Required[Union[str, None]],
    'description': Required[Union[str, None]],
    'classification': Required[Literal['read', 'action']],
    'callable': NotRequired[bool],
    'blockedReason': NotRequired[Union[Literal['actions_disabled', 'inactive_connection', 'missing_permission', 'missing_app_feature', 'permission_policy_missing', 'permission_verification_unavailable'], None]],
    'requiredPermissions': NotRequired[list[str]],
    'missingPermissions': NotRequired[list[str]],
    'requiredFeatures': NotRequired[list[str]],
    'missingFeatures': NotRequired[list[str]],
    'transport': NotRequired[Literal['managed_oauth', 'remote_mcp']],
    'providerConfigKey': NotRequired[str],
    'protocolVersion': NotRequired[Union[str, None]],
    'schemaSource': NotRequired[Literal['live_tools_list']],
    'inputSchema': Required[dict[str, Any]],
    'outputSchema': NotRequired[dict[str, Any]],
    'annotations': NotRequired[DescribeServiceConnectionToolOutputVariant1ToolAnnotations],
    'icons': NotRequired[list[DescribeServiceConnectionToolOutputVariant1ToolIconsItem]],
    'execution': NotRequired[DescribeServiceConnectionToolOutputVariant1ToolExecution],
    'schemaHash': NotRequired[str],
    'fetchedAt': NotRequired[str],
})
DescribeServiceConnectionToolOutputVariant1Tool.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class DescribeServiceConnectionToolOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    tool: Union[DescribeServiceConnectionToolOutputVariant1Tool, None] = Field(None, alias='tool', description='')
    retryable: Union[bool, None] = Field(None, alias='retryable', description='')
    error_code: Union[str, None] = Field(None, alias='errorCode', description='')
    error: Union[str, None] = Field(..., alias='error', description='')


DescribeServiceConnectionToolOutputVariant2DeliveryArtifactsItem = TypedDict('DescribeServiceConnectionToolOutputVariant2DeliveryArtifactsItem', {
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
DescribeServiceConnectionToolOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


DescribeServiceConnectionToolOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('DescribeServiceConnectionToolOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
DescribeServiceConnectionToolOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


DescribeServiceConnectionToolOutputVariant2Delivery = TypedDict('DescribeServiceConnectionToolOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[DescribeServiceConnectionToolOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[DescribeServiceConnectionToolOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
DescribeServiceConnectionToolOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


DescribeServiceConnectionToolOutputVariant2RecoveryOperation = TypedDict('DescribeServiceConnectionToolOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
DescribeServiceConnectionToolOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


DescribeServiceConnectionToolOutputVariant2Recovery = TypedDict('DescribeServiceConnectionToolOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[DescribeServiceConnectionToolOutputVariant2RecoveryOperation],
})
DescribeServiceConnectionToolOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class DescribeServiceConnectionToolOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: DescribeServiceConnectionToolOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: DescribeServiceConnectionToolOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(DescribeServiceConnectionToolOutput).
DescribeServiceConnectionToolOutput = Union[DescribeServiceConnectionToolOutputVariant2, DescribeServiceConnectionToolOutputVariant1]

_DescribeServiceConnectionToolInputAdapter = TypeAdapter(DescribeServiceConnectionToolInput)
_DescribeServiceConnectionToolOutputAdapter = TypeAdapter(DescribeServiceConnectionToolOutput)