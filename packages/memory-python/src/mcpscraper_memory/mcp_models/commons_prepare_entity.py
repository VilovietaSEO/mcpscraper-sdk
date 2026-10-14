from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


CommonsPrepareEntityInputSource = TypedDict('CommonsPrepareEntityInputSource', {
    'originalUrl': NotRequired[str],
    'resolvedUrl': NotRequired[str],
    'sourceCanonicalUrl': NotRequired[str],
    'relCanonicalHref': NotRequired[str],
    'sourceByline': NotRequired[Annotated[str, Field(max_length=240)]],
    'publisher': NotRequired[Annotated[str, Field(max_length=240)]],
    'authors': NotRequired[Annotated[list[Annotated[str, Field(min_length=1, max_length=120)]], Field(max_length=20)]],
    'publishedAt': NotRequired[Annotated[str, Field(max_length=80)]],
    'capturedAt': NotRequired[Annotated[str, Field(max_length=80)]],
    'license': NotRequired[Annotated[str, Field(max_length=240)]],
    'rightsSummary': NotRequired[Annotated[str, Field(max_length=1000)]],
    'contentHash': NotRequired[Annotated[str, Field(max_length=200)]],
})
CommonsPrepareEntityInputSource.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CommonsPrepareEntityInputContentSectionsItemCitationsItem = TypedDict('CommonsPrepareEntityInputContentSectionsItemCitationsItem', {
    'title': Required[Annotated[str, Field(min_length=1, max_length=240)]],
    'url': NotRequired[str],
    'source': NotRequired[Annotated[str, Field(max_length=240)]],
    'note': NotRequired[Annotated[str, Field(max_length=1000)]],
    'accessedAt': NotRequired[Annotated[str, Field(max_length=80)]],
})
CommonsPrepareEntityInputContentSectionsItemCitationsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CommonsPrepareEntityInputContentSectionsItem = TypedDict('CommonsPrepareEntityInputContentSectionsItem', {
    'id': NotRequired[Annotated[str, Field(max_length=180)]],
    'heading': Required[Annotated[str, Field(min_length=1, max_length=180)]],
    'body': Required[Annotated[str, Field(min_length=1, max_length=100000)]],
    'position': NotRequired[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'citations': NotRequired[Annotated[list[CommonsPrepareEntityInputContentSectionsItemCitationsItem], Field(max_length=300)]],
})
CommonsPrepareEntityInputContentSectionsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class CommonsPrepareEntityInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    title: Annotated[str, Field(min_length=1, max_length=180)] = Field(..., alias='title', description='Candidate public page title. Used to derive slug, choose a profile, and search duplicate entities.')
    description: Union[Annotated[str, Field(max_length=600)], None] = Field(None, alias='description', description='Optional candidate summary. Include when known so the prepare pass can route and validate the article shape.')
    slug: Union[Annotated[str, Field(max_length=180)], None] = Field(None, alias='slug', description='Optional desired URL slug. Omit to derive one from title.')
    entity_type: Union[Annotated[str, Field(max_length=120)], None] = Field(None, alias='entityType', description='Candidate backend Wikidata-style type. Use precise classes when possible: SoftwareApplication, Organization, Person, Event, Place, Taxon, ScienceConcept, MathConcept, TechArticle, Trail, or PublicArticle.')
    schema_org_type: Union[Annotated[str, Field(max_length=80)], None] = Field(None, alias='schemaOrgType', description='Optional candidate schema.org @type. If omitted, the profile chooses one from entityType.')
    source: Union[CommonsPrepareEntityInputSource, None] = Field(None, alias='source', description='Candidate source provenance used for duplicate checks and rel=canonical guidance.')
    tags: Union[Annotated[list[Annotated[str, Field(min_length=1, max_length=80)]], Field(max_length=24)], None] = Field(None, alias='tags', description='Candidate topic tags to resolve against existing Commons tag vocabulary.')
    keywords: Union[Annotated[list[Annotated[str, Field(min_length=1, max_length=120)]], Field(max_length=50)], None] = Field(None, alias='keywords', description='Candidate SEO/retrieval keywords to resolve against existing Commons vocabulary.')
    body_markdown: Union[Annotated[str, Field(max_length=500000)], None] = Field(None, alias='bodyMarkdown', description='Optional draft article body. Prepare will inspect headings and return profile alignment guidance without writing anything.')
    content_sections: Union[Annotated[list[CommonsPrepareEntityInputContentSectionsItem], Field(max_length=80)], None] = Field(None, alias='contentSections', description='Optional structured draft sections. Use when composing a page from source evidence before submit.')
    max_candidates: Union[Annotated[int, Field(ge=1, le=20)], None] = Field(None, alias='maxCandidates', description='Maximum duplicate candidates to return.')


class CommonsPrepareEntityOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    data: Union[Any, None] = Field(None, alias='data', description='')
    error: Union[str, None] = Field(None, alias='error', description='')
    message: Union[str, None] = Field(None, alias='message', description='')


CommonsPrepareEntityOutputVariant2DeliveryArtifactsItem = TypedDict('CommonsPrepareEntityOutputVariant2DeliveryArtifactsItem', {
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
CommonsPrepareEntityOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsPrepareEntityOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('CommonsPrepareEntityOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
CommonsPrepareEntityOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsPrepareEntityOutputVariant2Delivery = TypedDict('CommonsPrepareEntityOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[CommonsPrepareEntityOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[CommonsPrepareEntityOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
CommonsPrepareEntityOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsPrepareEntityOutputVariant2RecoveryOperation = TypedDict('CommonsPrepareEntityOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CommonsPrepareEntityOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsPrepareEntityOutputVariant2Recovery = TypedDict('CommonsPrepareEntityOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[CommonsPrepareEntityOutputVariant2RecoveryOperation],
})
CommonsPrepareEntityOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CommonsPrepareEntityOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: CommonsPrepareEntityOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: CommonsPrepareEntityOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(CommonsPrepareEntityOutput).
CommonsPrepareEntityOutput = Union[CommonsPrepareEntityOutputVariant2, CommonsPrepareEntityOutputVariant1]

_CommonsPrepareEntityInputAdapter = TypeAdapter(CommonsPrepareEntityInput)
_CommonsPrepareEntityOutputAdapter = TypeAdapter(CommonsPrepareEntityOutput)