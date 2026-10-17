from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class QueryFanoutWorkflowInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    session_id: str = Field(..., alias='session_id', description='Session id from browser_open. Must be on chatgpt.com or claude.ai, logged in via a saved hosted profile.')
    prompt: Union[str, None] = Field(None, alias='prompt', description='Optional prompt to type and submit before capturing. Omit to passively capture a prompt the user just ran. Must trigger web search to produce a fan-out.')
    wait_ms: Union[Annotated[int, Field(ge=0, le=180000)], None] = Field(None, alias='wait_ms', description='How long to wait for the answer stream to finish. Defaults to 90000 when a prompt is sent, 8000 for passive capture.')
    first_party_domain: Union[str, None] = Field(None, alias='first_party_domain', description='The brand/site being researched, e.g. example.com — sources on this domain are tagged First-party/vendor.')
    reset: Union[bool, None] = Field(None, alias='reset', description='Clear any previously buffered stream for this page before capturing.')
    export: Union[bool, None] = Field(None, alias='export', description='When using the installed local MCP server, write JSON/CSV/TSV/HTML exports to MCP_SCRAPER_OUTPUT_DIR/fanout. Hosted clients such as ChatGPT always receive the complete structured result inline and leave exports null.')


QueryFanoutWorkflowOutputVariant1Meta = TypedDict('QueryFanoutWorkflowOutputVariant1Meta', {
    'model': Required[str],
    'finishType': Required[str],
    'title': Required[str],
    'rounds': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
QueryFanoutWorkflowOutputVariant1Meta.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


QueryFanoutWorkflowOutputVariant1BrowsedUrlsItem = TypedDict('QueryFanoutWorkflowOutputVariant1BrowsedUrlsItem', {
    'url': Required[str],
    'domain': Required[str],
    'title': Required[str],
    'cited': Required[bool],
    'timesCited': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'snippet': Required[str],
    'round': Required[Union[Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)], None]],
    'siteType': Required[str],
})
QueryFanoutWorkflowOutputVariant1BrowsedUrlsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


QueryFanoutWorkflowOutputVariant1CitedUrlsItem = TypedDict('QueryFanoutWorkflowOutputVariant1CitedUrlsItem', {
    'url': Required[str],
    'domain': Required[str],
    'title': Required[str],
    'cited': Required[bool],
    'timesCited': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'snippet': Required[str],
    'round': Required[Union[Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)], None]],
    'siteType': Required[str],
})
QueryFanoutWorkflowOutputVariant1CitedUrlsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


QueryFanoutWorkflowOutputVariant1BrowsedOnlyItem = TypedDict('QueryFanoutWorkflowOutputVariant1BrowsedOnlyItem', {
    'url': Required[str],
    'domain': Required[str],
    'title': Required[str],
    'cited': Required[bool],
    'timesCited': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'snippet': Required[str],
    'round': Required[Union[Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)], None]],
    'siteType': Required[str],
})
QueryFanoutWorkflowOutputVariant1BrowsedOnlyItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


QueryFanoutWorkflowOutputVariant1SnippetsItem = TypedDict('QueryFanoutWorkflowOutputVariant1SnippetsItem', {
    'url': Required[str],
    'domain': Required[str],
    'title': Required[str],
    'text': Required[str],
})
QueryFanoutWorkflowOutputVariant1SnippetsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


QueryFanoutWorkflowOutputVariant1Counts = TypedDict('QueryFanoutWorkflowOutputVariant1Counts', {
    'subQueries': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'browsed': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'cited': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'browsedOnly': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
QueryFanoutWorkflowOutputVariant1Counts.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


QueryFanoutWorkflowOutputVariant1AggregatesTopSitesItem = TypedDict('QueryFanoutWorkflowOutputVariant1AggregatesTopSitesItem', {
    'domain': Required[str],
    'count': Required[Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)]],
    'cited': Required[bool],
    'timesCited': Required[Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)]],
    'siteType': Required[str],
})
QueryFanoutWorkflowOutputVariant1AggregatesTopSitesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


QueryFanoutWorkflowOutputVariant1AggregatesCitationOrderItem = TypedDict('QueryFanoutWorkflowOutputVariant1AggregatesCitationOrderItem', {
    'rank': Required[Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)]],
    'domain': Required[str],
    'url': Required[str],
    'timesCited': Required[Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)]],
})
QueryFanoutWorkflowOutputVariant1AggregatesCitationOrderItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


QueryFanoutWorkflowOutputVariant1Aggregates = TypedDict('QueryFanoutWorkflowOutputVariant1Aggregates', {
    'topSites': Required[list[QueryFanoutWorkflowOutputVariant1AggregatesTopSitesItem]],
    'citationOrder': Required[list[QueryFanoutWorkflowOutputVariant1AggregatesCitationOrderItem]],
    'byCategory': Required[dict[str, Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)]]],
})
QueryFanoutWorkflowOutputVariant1Aggregates.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


QueryFanoutWorkflowOutputVariant1ExportsVariant1 = TypedDict('QueryFanoutWorkflowOutputVariant1ExportsVariant1', {
    'relativeTo': Required[str],
    'dir': Required[str],
    'json': Required[str],
    'queriesCsv': Required[str],
    'queriesTsv': Required[str],
    'citationsCsv': Required[str],
    'sourcesCsv': Required[str],
    'browsedOnlyCsv': Required[str],
    'snippetsCsv': Required[str],
    'domainsCsv': Required[str],
    'report': Required[str],
})
QueryFanoutWorkflowOutputVariant1ExportsVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


QueryFanoutWorkflowOutputVariant1Debug = TypedDict('QueryFanoutWorkflowOutputVariant1Debug', {
    'interceptorReady': Required[bool],
    'rawBytes': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'unmappedKeys': Required[list[str]],
    'note': Required[str],
})
QueryFanoutWorkflowOutputVariant1Debug.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class QueryFanoutWorkflowOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='Whether the browser-agent action succeeded.')
    tool: Literal['query_fanout_workflow'] = Field(..., alias='tool', description='')
    session_id: Union[str, None] = Field(..., alias='session_id', description='Browser session id when the response is scoped to a session.')
    platform: Literal['ChatGPT', 'Claude'] = Field(..., alias='platform', description='Which AI-search surface the fan-out was captured from.')
    captured_at: str = Field(..., alias='captured_at', description='')
    prompt: str = Field(..., alias='prompt', description='The user prompt that triggered the captured fan-out, when recoverable.')
    meta: QueryFanoutWorkflowOutputVariant1Meta = Field(..., alias='meta', description='')
    queries: list[str] = Field(..., alias='queries', description='Every web-search sub-query issued, in capture order.')
    browsed_urls: list[QueryFanoutWorkflowOutputVariant1BrowsedUrlsItem] = Field(..., alias='browsed_urls', description='Every researched URL, cited first.')
    cited_urls: list[QueryFanoutWorkflowOutputVariant1CitedUrlsItem] = Field(..., alias='cited_urls', description='Researched URLs cited in the final answer.')
    browsed_only: list[QueryFanoutWorkflowOutputVariant1BrowsedOnlyItem] = Field(..., alias='browsed_only', description='Researched URLs pulled but not cited.')
    snippets: list[QueryFanoutWorkflowOutputVariant1SnippetsItem] = Field(..., alias='snippets', description='')
    counts: QueryFanoutWorkflowOutputVariant1Counts = Field(..., alias='counts', description='')
    aggregates: QueryFanoutWorkflowOutputVariant1Aggregates = Field(..., alias='aggregates', description='Objective aggregates: top sourced sites by frequency, citation order, and URL-category counts.')
    first_party_domain: Union[str, None] = Field(..., alias='first_party_domain', description='')
    export_error: Union[Union[str, None], None] = Field(None, alias='export_error', description='Non-fatal local export failure. The inline capture remains complete when this is present.')
    exports: Union[QueryFanoutWorkflowOutputVariant1ExportsVariant1, None] = Field(..., alias='exports', description='Local-only export paths when export=true, otherwise null. Hosted clients receive the complete structured result inline instead of inaccessible server paths.')
    debug: Union[QueryFanoutWorkflowOutputVariant1Debug, None] = Field(None, alias='debug', description='')


QueryFanoutWorkflowOutputVariant2DeliveryArtifactsItem = TypedDict('QueryFanoutWorkflowOutputVariant2DeliveryArtifactsItem', {
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
QueryFanoutWorkflowOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


QueryFanoutWorkflowOutputVariant2DeliveryAvailableExportsItem = TypedDict('QueryFanoutWorkflowOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
QueryFanoutWorkflowOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


QueryFanoutWorkflowOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('QueryFanoutWorkflowOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
QueryFanoutWorkflowOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


QueryFanoutWorkflowOutputVariant2Delivery = TypedDict('QueryFanoutWorkflowOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[QueryFanoutWorkflowOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[QueryFanoutWorkflowOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[QueryFanoutWorkflowOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
QueryFanoutWorkflowOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


QueryFanoutWorkflowOutputVariant2RecoveryOperation = TypedDict('QueryFanoutWorkflowOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
QueryFanoutWorkflowOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


QueryFanoutWorkflowOutputVariant2Recovery = TypedDict('QueryFanoutWorkflowOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[QueryFanoutWorkflowOutputVariant2RecoveryOperation],
})
QueryFanoutWorkflowOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class QueryFanoutWorkflowOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: QueryFanoutWorkflowOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: QueryFanoutWorkflowOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(QueryFanoutWorkflowOutput).
QueryFanoutWorkflowOutput = Union[QueryFanoutWorkflowOutputVariant1, QueryFanoutWorkflowOutputVariant2]

_QueryFanoutWorkflowInputAdapter = TypeAdapter(QueryFanoutWorkflowInput)
_QueryFanoutWorkflowOutputAdapter = TypeAdapter(QueryFanoutWorkflowOutput)