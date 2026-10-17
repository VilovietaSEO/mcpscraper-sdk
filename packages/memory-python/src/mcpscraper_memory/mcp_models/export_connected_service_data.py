from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


ExportConnectedServiceDataInputContinuationScopeSlack = TypedDict('ExportConnectedServiceDataInputContinuationScopeSlack', {
    'channelId': Required[str],
    'includeThreads': Required[bool],
})
ExportConnectedServiceDataInputContinuationScopeSlack.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


ExportConnectedServiceDataInputContinuationScope = TypedDict('ExportConnectedServiceDataInputContinuationScope', {
    'slack': NotRequired[ExportConnectedServiceDataInputContinuationScopeSlack],
})
ExportConnectedServiceDataInputContinuationScope.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


ExportConnectedServiceDataInputContinuation = TypedDict('ExportConnectedServiceDataInputContinuation', {
    'cursor': Required[str],
    'from': Required[str],
    'to': Required[str],
    'dataset': Required[Literal['emails', 'calendar_events', 'zoom_recordings', 'zoom_transcripts', 'slack_channel_messages', 'meta_ads_insights', 'search_console_performance', 'resend_data', 'resend_emails', 'resend_received_emails', 'resend_logs', 'resend_contacts', 'resend_broadcasts', 'resend_templates']],
    'scope': NotRequired[ExportConnectedServiceDataInputContinuationScope],
})
ExportConnectedServiceDataInputContinuation.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class ExportConnectedServiceDataInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    connection_id: Annotated[str, Field(min_length=1)] = Field(..., alias='connectionId', description='A tenant-owned connectionId from list_service_connections.')
    dataset: Union[Literal['auto', 'emails', 'calendar_events', 'zoom_recordings', 'zoom_transcripts', 'slack_channel_messages', 'meta_ads_insights', 'search_console_performance', 'resend_data', 'resend_emails', 'resend_received_emails', 'resend_logs', 'resend_contacts', 'resend_broadcasts', 'resend_templates'], None] = Field(None, alias='dataset', description='Dataset to export. auto maps Gmail to emails, Google Calendar to calendar_events, Zoom to zoom_transcripts, Meta Marketing to meta_ads_insights, Google Search Console to search_console_performance, Resend to resend_data, and Slack to slack_channel_messages when channelId is supplied. Slack walks top-level channel history plus threaded replies server-side. Search Console walks bounded Search Analytics rows across every accessible property. Meta walks daily account, campaign, ad-set, and ad insight levels across the connected ad accounts. The Resend aggregate walks 12 practical safe collections; six core collections are also individually selectable.')
    channel_id: Union[Annotated[str, Field(min_length=2, max_length=100)], None] = Field(None, alias='channelId', description='Slack conversation ID to export. Required for a new slack_channel_messages export; preserved inside continuation on resume. The export never joins a channel.')
    include_threads: Union[bool, None] = Field(None, alias='includeThreads', description='For Slack exports, automatically fetch every threaded reply. Defaults to true.')
    all_time: Union[bool, None] = Field(None, alias='allTime', description='For Slack exports only, read all accessible channel history instead of the default seven-day range. Do not combine with from, lastDays, or continuation.')
    last_days: Union[Annotated[int, Field(ge=1, le=90)], None] = Field(None, alias='lastDays', description='Relative range ending at to (or now). Defaults to 7 when from is omitted. Do not pass together with from. Slack all-time exports use allTime instead.')
    from_: Union[str, None] = Field(None, alias='from', description='Inclusive RFC3339 range start. Use instead of lastDays.')
    to: Union[str, None] = Field(None, alias='to', description='Exclusive RFC3339 range end. Defaults to now.')
    max_items: Union[Annotated[int, Field(ge=1, le=5000)], None] = Field(None, alias='maxItems', description='Maximum records to include in this export invocation. Pagination and detail retrieval happen server-side.')
    delivery: Union[Literal['auto', 'artifact'], None] = Field(None, alias='delivery', description='auto returns small results inline and stores larger results in private Blob. artifact always creates a private downloadable JSONL artifact.')
    continuation: Union[ExportConnectedServiceDataInputContinuation, None] = Field(None, alias='continuation', description='Preferred resume input. Pass the entire continuation object returned by a prior partial export unchanged; it preserves the exact original range and dataset.')
    cursor: Union[str, None] = Field(None, alias='cursor', description='Legacy resume input. When used, also pass the exact original from, to, and dataset. Prefer continuation.')


ExportConnectedServiceDataOutputVariant1Range = TypedDict('ExportConnectedServiceDataOutputVariant1Range', {
    'from': Required[str],
    'to': Required[str],
})
ExportConnectedServiceDataOutputVariant1Range.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExportConnectedServiceDataOutputVariant1ScopeSlack = TypedDict('ExportConnectedServiceDataOutputVariant1ScopeSlack', {
    'channelId': Required[str],
    'includeThreads': Required[bool],
})
ExportConnectedServiceDataOutputVariant1ScopeSlack.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExportConnectedServiceDataOutputVariant1Scope = TypedDict('ExportConnectedServiceDataOutputVariant1Scope', {
    'slack': NotRequired[ExportConnectedServiceDataOutputVariant1ScopeSlack],
})
ExportConnectedServiceDataOutputVariant1Scope.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExportConnectedServiceDataOutputVariant1Counts = TypedDict('ExportConnectedServiceDataOutputVariant1Counts', {
    'pages': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'listed': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'exported': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'failed': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'bytes': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
ExportConnectedServiceDataOutputVariant1Counts.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExportConnectedServiceDataOutputVariant1ArtifactReadbackArguments = TypedDict('ExportConnectedServiceDataOutputVariant1ArtifactReadbackArguments', {
    'artifactId': Required[str],
    'offset': Required[Literal[0]],
    'maxBytes': Required[Literal[20000]],
})
ExportConnectedServiceDataOutputVariant1ArtifactReadbackArguments.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExportConnectedServiceDataOutputVariant1ArtifactReadback = TypedDict('ExportConnectedServiceDataOutputVariant1ArtifactReadback', {
    'tool': Required[Literal['report_artifact_read']],
    'arguments': Required[ExportConnectedServiceDataOutputVariant1ArtifactReadbackArguments],
    'continuation': Required[str],
})
ExportConnectedServiceDataOutputVariant1ArtifactReadback.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExportConnectedServiceDataOutputVariant1Artifact = TypedDict('ExportConnectedServiceDataOutputVariant1Artifact', {
    'artifactId': Required[str],
    'filename': Required[str],
    'contentType': Required[Literal['application/x-ndjson']],
    'bytes': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'sha256': Required[str],
    'expiresAt': Required[str],
    'downloadUrl': Required[Union[str, None]],
    'downloadUrlExpiresAt': Required[Union[str, None]],
    'readback': Required[ExportConnectedServiceDataOutputVariant1ArtifactReadback],
})
ExportConnectedServiceDataOutputVariant1Artifact.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExportConnectedServiceDataOutputVariant1ContinuationVariant1ScopeSlack = TypedDict('ExportConnectedServiceDataOutputVariant1ContinuationVariant1ScopeSlack', {
    'channelId': Required[str],
    'includeThreads': Required[bool],
})
ExportConnectedServiceDataOutputVariant1ContinuationVariant1ScopeSlack.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExportConnectedServiceDataOutputVariant1ContinuationVariant1Scope = TypedDict('ExportConnectedServiceDataOutputVariant1ContinuationVariant1Scope', {
    'slack': NotRequired[ExportConnectedServiceDataOutputVariant1ContinuationVariant1ScopeSlack],
})
ExportConnectedServiceDataOutputVariant1ContinuationVariant1Scope.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExportConnectedServiceDataOutputVariant1ContinuationVariant1 = TypedDict('ExportConnectedServiceDataOutputVariant1ContinuationVariant1', {
    'cursor': Required[str],
    'from': Required[str],
    'to': Required[str],
    'dataset': Required[Literal['emails', 'calendar_events', 'zoom_recordings', 'zoom_transcripts', 'slack_channel_messages', 'meta_ads_insights', 'search_console_performance', 'resend_data', 'resend_emails', 'resend_received_emails', 'resend_logs', 'resend_contacts', 'resend_broadcasts', 'resend_templates']],
    'scope': NotRequired[ExportConnectedServiceDataOutputVariant1ContinuationVariant1Scope],
})
ExportConnectedServiceDataOutputVariant1ContinuationVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ExportConnectedServiceDataOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    export_id: Union[str, None] = Field(None, alias='exportId', description='')
    status: Union[Literal['complete', 'partial'], None] = Field(None, alias='status', description='')
    provider_config_key: Union[str, None] = Field(None, alias='providerConfigKey', description='')
    dataset: Union[Literal['emails', 'calendar_events', 'zoom_recordings', 'zoom_transcripts', 'slack_channel_messages', 'meta_ads_insights', 'search_console_performance', 'resend_data', 'resend_emails', 'resend_received_emails', 'resend_logs', 'resend_contacts', 'resend_broadcasts', 'resend_templates'], None] = Field(None, alias='dataset', description='')
    range: Union[ExportConnectedServiceDataOutputVariant1Range, None] = Field(None, alias='range', description='')
    scope: Union[ExportConnectedServiceDataOutputVariant1Scope, None] = Field(None, alias='scope', description='')
    counts: Union[ExportConnectedServiceDataOutputVariant1Counts, None] = Field(None, alias='counts', description='')
    complete: Union[bool, None] = Field(None, alias='complete', description='')
    records: Union[list[Any], None] = Field(None, alias='records', description='')
    preview: Union[list[Any], None] = Field(None, alias='preview', description='')
    artifact: Union[ExportConnectedServiceDataOutputVariant1Artifact, None] = Field(None, alias='artifact', description='')
    continuation: Union[Union[ExportConnectedServiceDataOutputVariant1ContinuationVariant1, None], None] = Field(None, alias='continuation', description='')
    warnings: Union[list[str], None] = Field(None, alias='warnings', description='')
    untrusted_content: Union[bool, None] = Field(None, alias='untrustedContent', description='')
    error: Union[str, None] = Field(..., alias='error', description='')


ExportConnectedServiceDataOutputVariant2DeliveryArtifactsItem = TypedDict('ExportConnectedServiceDataOutputVariant2DeliveryArtifactsItem', {
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
ExportConnectedServiceDataOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExportConnectedServiceDataOutputVariant2DeliveryAvailableExportsItem = TypedDict('ExportConnectedServiceDataOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
ExportConnectedServiceDataOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExportConnectedServiceDataOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('ExportConnectedServiceDataOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
ExportConnectedServiceDataOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExportConnectedServiceDataOutputVariant2Delivery = TypedDict('ExportConnectedServiceDataOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[ExportConnectedServiceDataOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[ExportConnectedServiceDataOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[ExportConnectedServiceDataOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
ExportConnectedServiceDataOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExportConnectedServiceDataOutputVariant2RecoveryOperation = TypedDict('ExportConnectedServiceDataOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
ExportConnectedServiceDataOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExportConnectedServiceDataOutputVariant2Recovery = TypedDict('ExportConnectedServiceDataOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[ExportConnectedServiceDataOutputVariant2RecoveryOperation],
})
ExportConnectedServiceDataOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ExportConnectedServiceDataOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: ExportConnectedServiceDataOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: ExportConnectedServiceDataOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(ExportConnectedServiceDataOutput).
ExportConnectedServiceDataOutput = Union[ExportConnectedServiceDataOutputVariant2, ExportConnectedServiceDataOutputVariant1]

_ExportConnectedServiceDataInputAdapter = TypeAdapter(ExportConnectedServiceDataInput)
_ExportConnectedServiceDataOutputAdapter = TypeAdapter(ExportConnectedServiceDataOutput)