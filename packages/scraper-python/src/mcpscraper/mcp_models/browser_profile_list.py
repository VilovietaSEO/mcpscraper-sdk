from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class BrowserProfileListInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    profile: Union[str, None] = Field(None, alias='profile', description='Profile whose saved logins to list. Omit to derive from email.')
    email: Union[str, None] = Field(None, alias='email', description='Account email used to derive the profile name when profile is not given.')
    domain: Union[str, None] = Field(None, alias='domain', description='Restrict to one site login, e.g. chatgpt.com. Use this to poll a single login until its status reads AUTHENTICATED.')
    connection_id: Union[str, None] = Field(None, alias='connection_id', description='A specific login connection id returned by browser_profile_connect, to poll just that one.')


BrowserProfileListOutputVariant1ConnectionsItem = TypedDict('BrowserProfileListOutputVariant1ConnectionsItem', {
    'connection_id': Required[Union[str, None]],
    'domain': Required[str],
    'status': Required[str],
    'account_email': Required[Union[str, None]],
    'note': Required[Union[str, None]],
    'watch_url': Required[Union[str, None]],
    'last_connected_at': Required[Union[str, None]],
})
BrowserProfileListOutputVariant1ConnectionsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class BrowserProfileListOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    tool: Literal['browser_profile_list'] = Field(..., alias='tool', description='')
    session_id: None = Field(..., alias='session_id', description='')
    profile: str = Field(..., alias='profile', description='Profile these logins belong to.')
    connections: list[BrowserProfileListOutputVariant1ConnectionsItem] = Field(..., alias='connections', description='All site logins saved in this profile, each with its current auth status and note.')
    count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='count', description='')


BrowserProfileListOutputVariant2DeliveryArtifactsItem = TypedDict('BrowserProfileListOutputVariant2DeliveryArtifactsItem', {
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
BrowserProfileListOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserProfileListOutputVariant2DeliveryAvailableExportsItem = TypedDict('BrowserProfileListOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
BrowserProfileListOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserProfileListOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('BrowserProfileListOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
BrowserProfileListOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserProfileListOutputVariant2Delivery = TypedDict('BrowserProfileListOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[BrowserProfileListOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[BrowserProfileListOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[BrowserProfileListOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
BrowserProfileListOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserProfileListOutputVariant2RecoveryOperation = TypedDict('BrowserProfileListOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
BrowserProfileListOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserProfileListOutputVariant2Recovery = TypedDict('BrowserProfileListOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[BrowserProfileListOutputVariant2RecoveryOperation],
})
BrowserProfileListOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class BrowserProfileListOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: BrowserProfileListOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: BrowserProfileListOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(BrowserProfileListOutput).
BrowserProfileListOutput = Union[BrowserProfileListOutputVariant1, BrowserProfileListOutputVariant2]

_BrowserProfileListInputAdapter = TypeAdapter(BrowserProfileListInput)
_BrowserProfileListOutputAdapter = TypeAdapter(BrowserProfileListOutput)