from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class ListServiceConnectionsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    connection_id: Union[Annotated[str, Field(min_length=1, max_length=200)], None] = Field(None, alias='connectionId', description='Select one previously discovered tenant-owned connection instead of listing every service.')
    projection: Union[Literal['full', 'identity'], None] = Field(None, alias='projection', description='Use identity with connectionId for compact account, availability and read-capability evidence; omitted preserves the full inventory.')
    required_read_tools: Union[Annotated[list[Annotated[str, Field(min_length=1, max_length=200)]], Field(max_length=20)], None] = Field(None, alias='requiredReadTools', description='Exact provider read-tool names to verify in the identity projection, such as list-messages and get-message.')


ListServiceConnectionsOutputVariant1ConnectionsItemVariant1ReadCapabilitiesItem = TypedDict('ListServiceConnectionsOutputVariant1ConnectionsItemVariant1ReadCapabilitiesItem', {
    'name': Required[str],
    'available': Required[bool],
    'blockedReason': Required[Union[str, None]],
})
ListServiceConnectionsOutputVariant1ConnectionsItemVariant1ReadCapabilitiesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListServiceConnectionsOutputVariant1ConnectionsItemVariant1 = TypedDict('ListServiceConnectionsOutputVariant1ConnectionsItemVariant1', {
    'projection': Required[Literal['identity']],
    'connectionId': Required[str],
    'providerAccountId': Required[Union[str, None]],
    'providerAccountEmail': Required[Union[str, None]],
    'providerIdentityStatus': Required[str],
    'status': Required[str],
    'lifecycleStatus': Required[Union[str, None]],
    'operationalStatus': Required[Union[str, None]],
    'reconnectRequired': Required[bool],
    'transport': Required[Literal['managed_oauth', 'remote_mcp']],
    'toolRevision': Required[Union[str, None]],
    'lastCheckedAt': Required[Union[str, None]],
    'readTools': Required[list[str]],
    'readToolsComplete': Required[bool],
    'readCapabilities': Required[list[ListServiceConnectionsOutputVariant1ConnectionsItemVariant1ReadCapabilitiesItem]],
})
ListServiceConnectionsOutputVariant1ConnectionsItemVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListServiceConnectionsOutputVariant1ConnectionsItemVariant2ToolCapabilitiesItem = TypedDict('ListServiceConnectionsOutputVariant1ConnectionsItemVariant2ToolCapabilitiesItem', {
    'name': Required[str],
    'classification': Required[Literal['read', 'action']],
    'requiredPermissions': Required[list[str]],
    'requiredFeatures': Required[list[str]],
    'available': Required[bool],
    'blockedReason': Required[Union[Literal['missing_permission', 'missing_app_feature', 'permission_policy_missing', 'permission_verification_unavailable'], None]],
    'missingPermissions': Required[list[str]],
    'missingFeatures': Required[list[str]],
})
ListServiceConnectionsOutputVariant1ConnectionsItemVariant2ToolCapabilitiesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListServiceConnectionsOutputVariant1ConnectionsItemVariant2 = TypedDict('ListServiceConnectionsOutputVariant1ConnectionsItemVariant2', {
    'connectionId': Required[str],
    'providerConfigKey': Required[str],
    'label': Required[str],
    'userLabel': NotRequired[Union[str, None]],
    'providerAccountId': NotRequired[Union[str, None]],
    'providerAccountEmail': NotRequired[Union[str, None]],
    'providerAccountName': NotRequired[Union[str, None]],
    'providerIdentityStatus': NotRequired[Literal['pending', 'verified', 'unavailable']],
    'status': Required[str],
    'lifecycleStatus': NotRequired[Literal['pending', 'connected', 'needs_reauth', 'disconnecting', 'disconnected']],
    'operationalStatus': NotRequired[Literal['unknown', 'available', 'degraded', 'unavailable']],
    'reconnectRequired': NotRequired[bool],
    'transport': Required[Literal['managed_oauth', 'remote_mcp']],
    'actionsEnabled': Required[bool],
    'readTools': Required[list[str]],
    'actionTools': Required[list[str]],
    'toolCapabilities': Required[list[ListServiceConnectionsOutputVariant1ConnectionsItemVariant2ToolCapabilitiesItem]],
    'grantedPermissions': Required[list[str]],
    'enabledFeatures': Required[list[str]],
    'permissionVerification': Required[Union[Literal['verified', 'unavailable'], None]],
    'adminBlockedTools': Required[list[str]],
    'mcpEndpoint': Required[Union[str, None]],
    'schemaDiscovery': Required[Literal['connection_tools_list', 'compatibility_describe']],
    'toolRevision': Required[Union[str, None]],
    'lastCheckedAt': NotRequired[Union[str, None]],
    'lastSuccessfulCallAt': NotRequired[Union[str, None]],
    'lastFailureAt': NotRequired[Union[str, None]],
    'lastFailureCode': NotRequired[Union[str, None]],
    'lastFailureRetryable': NotRequired[Union[bool, None]],
    'vaultName': Required[Union[str, None]],
    'tableName': Required[Union[str, None]],
})
ListServiceConnectionsOutputVariant1ConnectionsItemVariant2.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ListServiceConnectionsOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    connections: list[Union[ListServiceConnectionsOutputVariant1ConnectionsItemVariant1, ListServiceConnectionsOutputVariant1ConnectionsItemVariant2]] = Field(..., alias='connections', description='')


ListServiceConnectionsOutputVariant2DeliveryArtifactsItem = TypedDict('ListServiceConnectionsOutputVariant2DeliveryArtifactsItem', {
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
ListServiceConnectionsOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListServiceConnectionsOutputVariant2DeliveryAvailableExportsItem = TypedDict('ListServiceConnectionsOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
ListServiceConnectionsOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListServiceConnectionsOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('ListServiceConnectionsOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
ListServiceConnectionsOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListServiceConnectionsOutputVariant2Delivery = TypedDict('ListServiceConnectionsOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[ListServiceConnectionsOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[ListServiceConnectionsOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[ListServiceConnectionsOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
ListServiceConnectionsOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListServiceConnectionsOutputVariant2RecoveryOperation = TypedDict('ListServiceConnectionsOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
ListServiceConnectionsOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListServiceConnectionsOutputVariant2Recovery = TypedDict('ListServiceConnectionsOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[ListServiceConnectionsOutputVariant2RecoveryOperation],
})
ListServiceConnectionsOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ListServiceConnectionsOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: ListServiceConnectionsOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: ListServiceConnectionsOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(ListServiceConnectionsOutput).
ListServiceConnectionsOutput = Union[ListServiceConnectionsOutputVariant2, ListServiceConnectionsOutputVariant1]

_ListServiceConnectionsInputAdapter = TypeAdapter(ListServiceConnectionsInput)
_ListServiceConnectionsOutputAdapter = TypeAdapter(ListServiceConnectionsOutput)