from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class MemorySearchInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    vault: Union[str, None] = Field(None, alias='vault', description='Exact logical vault handle to search. Omit to search every entitled vault.')
    query: Annotated[str, Field(min_length=1)] = Field(..., alias='query', description='A focused semantic reformulation of the request.')
    user_message: Union[str, None] = Field(None, alias='userMessage', description='Original human wording. Used as a distinct query variant when useful and logged for quality review.')
    queries: Union[Annotated[list[Annotated[str, Field(min_length=1)]], Field(min_length=2, max_length=4)], None] = Field(None, alias='queries', description='Caller-provided focused query variants. The planner deduplicates these with query, original wording, and tag/entity terms.')
    entities: Union[Annotated[list[Annotated[str, Field(min_length=1)]], Field(max_length=20)], None] = Field(None, alias='entities', description='Named entities or exact terms used to form a focused query variant.')
    tags: Union[Annotated[list[Annotated[str, Field(min_length=1)]], Field(max_length=20)], None] = Field(None, alias='tags', description='Exact canonical tags used for tag-channel retrieval and filtering.')
    tag_mode: Union[Literal['any', 'all'], None] = Field(None, alias='tagMode', description='Whether a note must match any or all supplied tags. Default any.')
    kind: Union[Literal['note', 'library', 'capture', 'decision', 'message'], None] = Field(None, alias='kind', description='Exact persisted note-kind filter.')
    type: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='type', description='Exact props.type filter.')
    date_from: Union[str, None] = Field(None, alias='dateFrom', description='Inclusive lower bound for note updatedAt.')
    date_to: Union[str, None] = Field(None, alias='dateTo', description='Inclusive upper bound for note updatedAt.')
    metadata: Union[dict[str, Union[str, Union[float, int], bool]], None] = Field(None, alias='metadata', description='Exact equality filters for primitive note props.')
    query_variant_count: Union[Annotated[int, Field(ge=2, le=4)], None] = Field(None, alias='queryVariantCount', description='Number of variants. Default 3.')
    candidate_pool: Union[Annotated[int, Field(ge=10, le=100)], None] = Field(None, alias='candidatePool', description='Total fused candidates before final reranking. Default 50.')
    graph_seed_count: Union[Annotated[int, Field(ge=0, le=20)], None] = Field(None, alias='graphSeedCount', description='Strong preliminary notes whose graph neighborhoods are considered. Default 8.')
    graph_depth: Union[Literal[1], None] = Field(None, alias='graphDepth', description='Graph expansion depth. Bounded to exactly one hop.')
    graph_neighbors_per_seed: Union[Annotated[int, Field(ge=1, le=10)], None] = Field(None, alias='graphNeighborsPerSeed', description='Maximum outgoing-link plus backlink neighbors per seed. Default 5.')
    rerank_top_n: Union[Annotated[int, Field(ge=1, le=50)], None] = Field(None, alias='rerankTopN', description='Final results retained after reranking. Default 30.')
    top_k: Union[Annotated[int, Field(ge=1, le=50)], None] = Field(None, alias='topK', description='Deprecated compatibility alias for rerankTopN. Prefer rerankTopN; default remains 30.')
    include_shared: Union[bool, None] = Field(None, alias='includeShared', description='Also search individually accepted shares. Default true. Exact note metadata filters exclude shares without accessible metadata.')


MemorySearchOutputVariant1Planner = TypedDict('MemorySearchOutputVariant1Planner', {
    'queryVariants': Required[list[str]],
    'candidatePool': Required[Union[float, int]],
    'graphSeedCount': Required[Union[float, int]],
    'graphDepth': Required[Union[float, int]],
    'graphNeighborsPerSeed': Required[Union[float, int]],
    'rerankTopN': Required[Union[float, int]],
    'seeds': Required[list[str]],
    'graphCandidatesAdded': Required[Union[float, int]],
})
MemorySearchOutputVariant1Planner.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemorySearchOutputVariant1Rerank = TypedDict('MemorySearchOutputVariant1Rerank', {
    'applied': Required[bool],
    'provider': Required[str],
    'fallbackReason': NotRequired[str],
})
MemorySearchOutputVariant1Rerank.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemorySearchOutputVariant1ResultsItem = TypedDict('MemorySearchOutputVariant1ResultsItem', {
    'text': Required[str],
    'source': Required[str],
    'score': Required[Union[float, int]],
    'originalScore': Required[Union[float, int]],
    'rerankScore': NotRequired[Union[float, int]],
    'vault': NotRequired[str],
    'sharedBy': NotRequired[str],
    'shareId': NotRequired[str],
    'matchChannels': Required[list[Literal['semantic', 'tag', 'metadata', 'graph']]],
    'matchedQueries': Required[list[str]],
    'graphFrom': Required[list[str]],
})
MemorySearchOutputVariant1ResultsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class MemorySearchOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    vault: Union[str, None] = Field(None, alias='vault', description='')
    vaults_searched: Union[list[str], None] = Field(None, alias='vaultsSearched', description='')
    planner: Union[MemorySearchOutputVariant1Planner, None] = Field(None, alias='planner', description='')
    rerank: Union[MemorySearchOutputVariant1Rerank, None] = Field(None, alias='rerank', description='')
    results: Union[list[MemorySearchOutputVariant1ResultsItem], None] = Field(None, alias='results', description='')
    error: Union[str, None] = Field(None, alias='error', description='')


MemorySearchOutputVariant2DeliveryArtifactsItem = TypedDict('MemorySearchOutputVariant2DeliveryArtifactsItem', {
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
MemorySearchOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemorySearchOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('MemorySearchOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
MemorySearchOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemorySearchOutputVariant2Delivery = TypedDict('MemorySearchOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[MemorySearchOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[MemorySearchOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
MemorySearchOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemorySearchOutputVariant2RecoveryOperation = TypedDict('MemorySearchOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
MemorySearchOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemorySearchOutputVariant2Recovery = TypedDict('MemorySearchOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[MemorySearchOutputVariant2RecoveryOperation],
})
MemorySearchOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class MemorySearchOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: MemorySearchOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: MemorySearchOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(MemorySearchOutput).
MemorySearchOutput = Union[MemorySearchOutputVariant2, MemorySearchOutputVariant1]

_MemorySearchInputAdapter = TypeAdapter(MemorySearchInput)
_MemorySearchOutputAdapter = TypeAdapter(MemorySearchOutput)