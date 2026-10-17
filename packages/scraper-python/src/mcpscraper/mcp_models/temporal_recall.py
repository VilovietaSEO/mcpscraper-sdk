from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class TemporalRecallInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    vault: Union[str, None] = Field(None, alias='vault', description='Vault to recall from. Optional; defaults to the session active vault, then the first vault the caller is entitled to.')
    query: Union[str, None] = Field(None, alias='query', description='Optional natural-language query; when present, a semantic search is blended into the results.')
    days_ago: Union[Annotated[int, Field(ge=0, le=3650)], None] = Field(None, alias='daysAgo', description='Recall a single calendar day this many days ago (0 = today). Optional; ignored when from/to are given.')
    from_: Union[str, None] = Field(None, alias='from', description='Start of an explicit window (ISO-8601 / parseable date). Use together with "to". Overrides daysAgo.')
    to: Union[str, None] = Field(None, alias='to', description='End of an explicit window (ISO-8601 / parseable date). Use together with "from".')


TemporalRecallOutputVariant1Range = TypedDict('TemporalRecallOutputVariant1Range', {
    'from': Required[str],
    'to': Required[str],
})
TemporalRecallOutputVariant1Range.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TemporalRecallOutputVariant1ItemsItem = TypedDict('TemporalRecallOutputVariant1ItemsItem', {
    'text': Required[str],
    'source': Required[str],
    'capturedAt': Required[str],
})
TemporalRecallOutputVariant1ItemsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TemporalRecallOutputVariant1SearchResultsItem = TypedDict('TemporalRecallOutputVariant1SearchResultsItem', {
    'text': Required[str],
    'source': Required[str],
    'score': Required[Union[float, int]],
})
TemporalRecallOutputVariant1SearchResultsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class TemporalRecallOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='True when recall succeeded; false on auth/scope error.')
    range: Union[TemporalRecallOutputVariant1Range, None] = Field(None, alias='range', description='The actual time window used after resolving daysAgo/from/to (default: last 7 days).')
    items: Union[list[TemporalRecallOutputVariant1ItemsItem], None] = Field(None, alias='items', description='Captures within the window, newest-first. Present when ok is true.')
    search_results: Union[list[TemporalRecallOutputVariant1SearchResultsItem], None] = Field(None, alias='searchResults', description='Blended semantic-search hits for the query. Present only when a query was supplied.')
    error: Union[str, None] = Field(None, alias='error', description='Human-readable failure reason when ok is false.')


TemporalRecallOutputVariant2DeliveryArtifactsItem = TypedDict('TemporalRecallOutputVariant2DeliveryArtifactsItem', {
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
TemporalRecallOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TemporalRecallOutputVariant2DeliveryAvailableExportsItem = TypedDict('TemporalRecallOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
TemporalRecallOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TemporalRecallOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('TemporalRecallOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
TemporalRecallOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TemporalRecallOutputVariant2Delivery = TypedDict('TemporalRecallOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[TemporalRecallOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[TemporalRecallOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[TemporalRecallOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
TemporalRecallOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TemporalRecallOutputVariant2RecoveryOperation = TypedDict('TemporalRecallOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
TemporalRecallOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TemporalRecallOutputVariant2Recovery = TypedDict('TemporalRecallOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[TemporalRecallOutputVariant2RecoveryOperation],
})
TemporalRecallOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class TemporalRecallOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: TemporalRecallOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: TemporalRecallOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(TemporalRecallOutput).
TemporalRecallOutput = Union[TemporalRecallOutputVariant2, TemporalRecallOutputVariant1]

_TemporalRecallInputAdapter = TypeAdapter(TemporalRecallInput)
_TemporalRecallOutputAdapter = TypeAdapter(TemporalRecallOutput)