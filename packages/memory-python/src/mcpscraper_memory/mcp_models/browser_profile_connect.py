from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class BrowserProfileConnectInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    email: Union[str, None] = Field(None, alias='email', description='Account email for the login. Derives a stable profile name and is recorded as a note. Does NOT import existing cookies — the user signs in fresh.')
    profile: Union[str, None] = Field(None, alias='profile', description='Profile to add this login to. Omit to derive from email. A single profile holds MANY logins — pass the same name with a different domain to stack accounts.')
    domain: Union[str, None] = Field(None, alias='domain', description='Site to log into, e.g. chatgpt.com, claude.ai, reddit.com. Defaults to chatgpt.com.')
    login_url: Union[str, None] = Field(None, alias='login_url', description='Login page for the domain. Defaults to https://<domain>/.')
    url: Union[str, None] = Field(None, alias='url', description='Deprecated alias for login_url.')
    note: Union[str, None] = Field(None, alias='note', description='Free-text note describing this login. Surfaced by browser_profile_list.')
    label: Union[str, None] = Field(None, alias='label', description='Optional human label for this sign-in setup session.')
    timeout_seconds: Union[Annotated[int, Field(ge=60, le=600)], None] = Field(None, alias='timeout_seconds', description='Sign-in session lifetime before auto-termination. Defaults to 600 and cannot exceed 600.')


BrowserProfileConnectOutputVariant1ConnectedLoginsItem = TypedDict('BrowserProfileConnectOutputVariant1ConnectedLoginsItem', {
    'connection_id': Required[Union[str, None]],
    'domain': Required[str],
    'status': Required[str],
    'account_email': Required[Union[str, None]],
    'note': Required[Union[str, None]],
    'watch_url': Required[Union[str, None]],
    'last_connected_at': Required[Union[str, None]],
})
BrowserProfileConnectOutputVariant1ConnectedLoginsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class BrowserProfileConnectOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    tool: Literal['browser_profile_connect'] = Field(..., alias='tool', description='')
    session_id: Union[str, None] = Field(..., alias='session_id', description='The underlying live browser session id backing this sign-in.')
    auth_connection_id: str = Field(..., alias='auth_connection_id', description='')
    watch_url: str = Field(..., alias='watch_url', description='mcpscraper.dev sign-in link to give the user so they can complete this login.')
    live_view_url: Union[str, None] = Field(..., alias='live_view_url', description='Deprecated; always null. Open watch_url to view the sign-in.')
    profile: str = Field(..., alias='profile', description='Profile this login was added to. Reuse it to stack more logins or to open a session.')
    domain: str = Field(..., alias='domain', description='')
    setup_url: str = Field(..., alias='setup_url', description='')
    account_email: Union[str, None] = Field(..., alias='account_email', description='')
    note: Union[str, None] = Field(..., alias='note', description='')
    status: str = Field(..., alias='status', description='')
    flow_status: Union[str, None] = Field(..., alias='flow_status', description='Deprecated; always null.')
    flow_step: Union[str, None] = Field(..., alias='flow_step', description='Deprecated; always null.')
    flow_expires_at: Union[str, None] = Field(..., alias='flow_expires_at', description='Deprecated; always null.')
    post_login_url: Union[str, None] = Field(..., alias='post_login_url', description='Deprecated; always null.')
    connected_logins: list[BrowserProfileConnectOutputVariant1ConnectedLoginsItem] = Field(..., alias='connected_logins', description='Every login currently saved in this profile, so you can see what else is connected.')
    next_steps: list[str] = Field(..., alias='next_steps', description='')
    raw: Union[dict[str, Any], None] = Field(None, alias='raw', description='')


BrowserProfileConnectOutputVariant2DeliveryArtifactsItem = TypedDict('BrowserProfileConnectOutputVariant2DeliveryArtifactsItem', {
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
BrowserProfileConnectOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserProfileConnectOutputVariant2DeliveryAvailableExportsItem = TypedDict('BrowserProfileConnectOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
BrowserProfileConnectOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserProfileConnectOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('BrowserProfileConnectOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
BrowserProfileConnectOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserProfileConnectOutputVariant2Delivery = TypedDict('BrowserProfileConnectOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[BrowserProfileConnectOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[BrowserProfileConnectOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[BrowserProfileConnectOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
BrowserProfileConnectOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserProfileConnectOutputVariant2RecoveryOperation = TypedDict('BrowserProfileConnectOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
BrowserProfileConnectOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserProfileConnectOutputVariant2Recovery = TypedDict('BrowserProfileConnectOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[BrowserProfileConnectOutputVariant2RecoveryOperation],
})
BrowserProfileConnectOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class BrowserProfileConnectOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: BrowserProfileConnectOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: BrowserProfileConnectOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(BrowserProfileConnectOutput).
BrowserProfileConnectOutput = Union[BrowserProfileConnectOutputVariant1, BrowserProfileConnectOutputVariant2]

_BrowserProfileConnectInputAdapter = TypeAdapter(BrowserProfileConnectInput)
_BrowserProfileConnectOutputAdapter = TypeAdapter(BrowserProfileConnectOutput)