from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class BrowserOpenInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    label: Union[str, None] = Field(None, alias='label', description='Optional human label for this session, shown in the watch console.')
    url: Union[str, None] = Field(None, alias='url', description='Optional URL to navigate to immediately after opening.')
    profile: Union[str, None] = Field(None, alias='profile', description='Optional saved hosted profile name to load a logged-in session for a site.')
    serp_identity: Union[str, None] = Field(None, alias='serp_identity', description='Optional persistent SERP identity. Loads its saved browser state and fixed network identity; do not combine with profile.')
    save_profile_changes: Union[bool, None] = Field(None, alias='save_profile_changes', description='Persist cookies/storage back to the named profile on close. Avoid parallel sessions writing to the same profile.')
    timeout_seconds: Union[Annotated[int, Field(ge=60, le=600)], None] = Field(None, alias='timeout_seconds', description='Session lifetime before auto-termination. Defaults to 600 and cannot exceed 600.')
    extension_names: Union[list[str], None] = Field(None, alias='extension_names', description="Names of extensions previously added with browser_extension_import (see browser_extension_list for what's available) to load into this session. Loading extensions restarts the browser, adding a few seconds to startup.")


class BrowserOpenOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    tool: Literal['browser_open'] = Field(..., alias='tool', description='')
    session_id: str = Field(..., alias='session_id', description='Session id returned by browser_open. Use only this exact value in later browser_* calls; do not construct one yourself.')
    watch_url: str = Field(..., alias='watch_url', description='Human watch/takeover URL for this browser session on mcpscraper.dev.')
    live_view_url: Union[str, None] = Field(..., alias='live_view_url', description='Deprecated; always null. Open watch_url to view the live session.')
    url: Union[str, None] = Field(..., alias='url', description='Initial URL requested by the caller, when provided.')
    hint: str = Field(..., alias='hint', description='')
    raw: Union[dict[str, Any], None] = Field(None, alias='raw', description='')


BrowserOpenOutputVariant2DeliveryArtifactsItem = TypedDict('BrowserOpenOutputVariant2DeliveryArtifactsItem', {
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
BrowserOpenOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserOpenOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('BrowserOpenOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
BrowserOpenOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserOpenOutputVariant2Delivery = TypedDict('BrowserOpenOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[BrowserOpenOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[BrowserOpenOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
BrowserOpenOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserOpenOutputVariant2RecoveryOperation = TypedDict('BrowserOpenOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
BrowserOpenOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserOpenOutputVariant2Recovery = TypedDict('BrowserOpenOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[BrowserOpenOutputVariant2RecoveryOperation],
})
BrowserOpenOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class BrowserOpenOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: BrowserOpenOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: BrowserOpenOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(BrowserOpenOutput).
BrowserOpenOutput = Union[BrowserOpenOutputVariant1, BrowserOpenOutputVariant2]

_BrowserOpenInputAdapter = TypeAdapter(BrowserOpenInput)
_BrowserOpenOutputAdapter = TypeAdapter(BrowserOpenOutput)