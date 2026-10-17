from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class BrowserReadInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    session_id: str = Field(..., alias='session_id', description='The session id returned by browser_open or browser_list_sessions.')


class BrowserReadOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='Whether the browser-agent action succeeded.')
    tool: Literal['browser_read'] = Field(..., alias='tool', description='')
    session_id: Union[str, None] = Field(..., alias='session_id', description='Browser session id when the response is scoped to a session.')
    url: Union[str, None] = Field(..., alias='url', description='')
    title: Union[str, None] = Field(..., alias='title', description='')
    text: str = Field(..., alias='text', description='')
    elements: list[dict[str, Any]] = Field(..., alias='elements', description='')
    raw: Union[dict[str, Any], None] = Field(None, alias='raw', description='')


BrowserReadOutputVariant2DeliveryArtifactsItem = TypedDict('BrowserReadOutputVariant2DeliveryArtifactsItem', {
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
BrowserReadOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserReadOutputVariant2DeliveryAvailableExportsItem = TypedDict('BrowserReadOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
BrowserReadOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserReadOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('BrowserReadOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
BrowserReadOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserReadOutputVariant2Delivery = TypedDict('BrowserReadOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[BrowserReadOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[BrowserReadOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[BrowserReadOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
BrowserReadOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserReadOutputVariant2RecoveryOperation = TypedDict('BrowserReadOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
BrowserReadOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserReadOutputVariant2Recovery = TypedDict('BrowserReadOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[BrowserReadOutputVariant2RecoveryOperation],
})
BrowserReadOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class BrowserReadOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: BrowserReadOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: BrowserReadOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(BrowserReadOutput).
BrowserReadOutput = Union[BrowserReadOutputVariant1, BrowserReadOutputVariant2]

_BrowserReadInputAdapter = TypeAdapter(BrowserReadInput)
_BrowserReadOutputAdapter = TypeAdapter(BrowserReadOutput)