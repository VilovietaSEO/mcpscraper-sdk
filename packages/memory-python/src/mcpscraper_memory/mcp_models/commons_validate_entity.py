from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


CommonsValidateEntityInputFeaturedImage = TypedDict('CommonsValidateEntityInputFeaturedImage', {
    'url': Required[str],
    'alt': NotRequired[Annotated[str, Field(max_length=500)]],
    'caption': NotRequired[Annotated[str, Field(max_length=1000)]],
    'sourceUrl': NotRequired[str],
    'license': NotRequired[Annotated[str, Field(max_length=240)]],
    'width': NotRequired[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'height': NotRequired[Annotated[int, Field(le=9007199254740991, gt=0)]],
})
CommonsValidateEntityInputFeaturedImage.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CommonsValidateEntityInputSource = TypedDict('CommonsValidateEntityInputSource', {
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
CommonsValidateEntityInputSource.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CommonsValidateEntityInputRelatedEntitiesItem = TypedDict('CommonsValidateEntityInputRelatedEntitiesItem', {
    'entityId': NotRequired[Annotated[str, Field(max_length=80)]],
    'title': Required[Annotated[str, Field(min_length=1, max_length=180)]],
    'relationship': NotRequired[Annotated[str, Field(max_length=120)]],
    'slug': NotRequired[Annotated[str, Field(max_length=180)]],
    'url': NotRequired[str],
    'description': NotRequired[Annotated[str, Field(max_length=300)]],
})
CommonsValidateEntityInputRelatedEntitiesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CommonsValidateEntityInputClaimsItemReferencesItem = TypedDict('CommonsValidateEntityInputClaimsItemReferencesItem', {
    'title': Required[Annotated[str, Field(min_length=1, max_length=240)]],
    'url': NotRequired[str],
    'source': NotRequired[Annotated[str, Field(max_length=240)]],
    'note': NotRequired[Annotated[str, Field(max_length=1000)]],
    'accessedAt': NotRequired[Annotated[str, Field(max_length=80)]],
})
CommonsValidateEntityInputClaimsItemReferencesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CommonsValidateEntityInputClaimsItem = TypedDict('CommonsValidateEntityInputClaimsItem', {
    'predicate': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'predicateLabel': NotRequired[Annotated[str, Field(max_length=160)]],
    'objectEntityId': NotRequired[Annotated[str, Field(max_length=80)]],
    'objectUrl': NotRequired[str],
    'title': NotRequired[Annotated[str, Field(max_length=500)]],
    'mediaType': NotRequired[Annotated[str, Field(max_length=160)]],
    'hreflang': NotRequired[Annotated[list[Annotated[str, Field(min_length=1, max_length=80)]], Field(max_length=20)]],
    'qualifiers': NotRequired[dict[str, Union[str, Union[float, int], bool, None]]],
    'references': NotRequired[Annotated[list[CommonsValidateEntityInputClaimsItemReferencesItem], Field(max_length=50)]],
    'rank': NotRequired[Literal['preferred', 'normal', 'deprecated']],
    'confidence': NotRequired[Annotated[Union[float, int], Field(ge=0, le=1)]],
    'confidenceReason': NotRequired[Annotated[str, Field(max_length=1000)]],
    'disputeState': NotRequired[Literal['undisputed', 'attributed', 'disputed', 'contested', 'needs_review', 'deprecated']],
    'validFrom': NotRequired[Annotated[str, Field(max_length=80)]],
    'validTo': NotRequired[Annotated[str, Field(max_length=80)]],
    'asOf': NotRequired[Annotated[str, Field(max_length=80)]],
    'sourceFamily': NotRequired[Literal['first_party', 'partner', 'independent', 'community', 'unknown']],
})
CommonsValidateEntityInputClaimsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CommonsValidateEntityInputContentSectionsItemCitationsItem = TypedDict('CommonsValidateEntityInputContentSectionsItemCitationsItem', {
    'title': Required[Annotated[str, Field(min_length=1, max_length=240)]],
    'url': NotRequired[str],
    'source': NotRequired[Annotated[str, Field(max_length=240)]],
    'note': NotRequired[Annotated[str, Field(max_length=1000)]],
    'accessedAt': NotRequired[Annotated[str, Field(max_length=80)]],
})
CommonsValidateEntityInputContentSectionsItemCitationsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CommonsValidateEntityInputContentSectionsItem = TypedDict('CommonsValidateEntityInputContentSectionsItem', {
    'id': NotRequired[Annotated[str, Field(max_length=180)]],
    'heading': Required[Annotated[str, Field(min_length=1, max_length=180)]],
    'body': Required[Annotated[str, Field(min_length=1, max_length=100000)]],
    'position': NotRequired[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'citations': NotRequired[Annotated[list[CommonsValidateEntityInputContentSectionsItemCitationsItem], Field(max_length=300)]],
})
CommonsValidateEntityInputContentSectionsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CommonsValidateEntityInputArticleSectionsRelatedLinksItem = TypedDict('CommonsValidateEntityInputArticleSectionsRelatedLinksItem', {
    'title': Required[Annotated[str, Field(min_length=1, max_length=180)]],
    'url': NotRequired[Annotated[str, Field(max_length=2000)]],
    'slug': NotRequired[Annotated[str, Field(max_length=180)]],
    'entityId': NotRequired[Annotated[str, Field(max_length=80)]],
    'relationship': NotRequired[Annotated[str, Field(max_length=120)]],
    'summary': NotRequired[Annotated[str, Field(max_length=300)]],
    'imageUrl': NotRequired[Annotated[str, Field(max_length=2000)]],
    'needsLink': NotRequired[bool],
})
CommonsValidateEntityInputArticleSectionsRelatedLinksItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CommonsValidateEntityInputArticleSectionsNotesItem = TypedDict('CommonsValidateEntityInputArticleSectionsNotesItem', {
    'marker': NotRequired[Annotated[str, Field(max_length=20)]],
    'body': Required[Annotated[str, Field(min_length=1, max_length=2000)]],
})
CommonsValidateEntityInputArticleSectionsNotesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CommonsValidateEntityInputArticleSectionsCitationsItem = TypedDict('CommonsValidateEntityInputArticleSectionsCitationsItem', {
    'title': Required[Annotated[str, Field(min_length=1, max_length=240)]],
    'url': NotRequired[str],
    'source': NotRequired[Annotated[str, Field(max_length=240)]],
    'note': NotRequired[Annotated[str, Field(max_length=1000)]],
    'accessedAt': NotRequired[Annotated[str, Field(max_length=80)]],
})
CommonsValidateEntityInputArticleSectionsCitationsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CommonsValidateEntityInputArticleSectionsExternalLinksItem = TypedDict('CommonsValidateEntityInputArticleSectionsExternalLinksItem', {
    'title': Required[Annotated[str, Field(min_length=1, max_length=180)]],
    'url': Required[str],
    'summary': NotRequired[Annotated[str, Field(max_length=300)]],
})
CommonsValidateEntityInputArticleSectionsExternalLinksItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CommonsValidateEntityInputArticleSections = TypedDict('CommonsValidateEntityInputArticleSections', {
    'relatedLinks': NotRequired[Annotated[list[CommonsValidateEntityInputArticleSectionsRelatedLinksItem], Field(max_length=100)]],
    'notes': NotRequired[Annotated[list[CommonsValidateEntityInputArticleSectionsNotesItem], Field(max_length=100)]],
    'citations': NotRequired[Annotated[list[CommonsValidateEntityInputArticleSectionsCitationsItem], Field(max_length=300)]],
    'externalLinks': NotRequired[Annotated[list[CommonsValidateEntityInputArticleSectionsExternalLinksItem], Field(max_length=100)]],
    'categories': NotRequired[Annotated[list[Annotated[str, Field(min_length=1, max_length=120)]], Field(max_length=50)]],
})
CommonsValidateEntityInputArticleSections.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CommonsValidateEntityInputMediaItem = TypedDict('CommonsValidateEntityInputMediaItem', {
    'type': Required[Literal['image', 'video', 'audio']],
    'url': Required[str],
    'alt': NotRequired[Annotated[str, Field(max_length=500)]],
    'caption': NotRequired[Annotated[str, Field(max_length=1000)]],
    'posterUrl': NotRequired[str],
    'sourceUrl': NotRequired[str],
    'license': NotRequired[Annotated[str, Field(max_length=240)]],
    'width': NotRequired[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'height': NotRequired[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'durationSeconds': NotRequired[Annotated[int, Field(le=9007199254740991, gt=0)]],
})
CommonsValidateEntityInputMediaItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CommonsValidateEntityInputSeo = TypedDict('CommonsValidateEntityInputSeo', {
    'canonicalUrl': NotRequired[str],
    'relCanonical': NotRequired[str],
    'metaTitle': NotRequired[Annotated[str, Field(max_length=240)]],
    'metaDescription': NotRequired[Annotated[str, Field(max_length=500)]],
    'ogImage': NotRequired[str],
    'schemaOrgType': NotRequired[Annotated[str, Field(max_length=80)]],
    'noIndex': NotRequired[bool],
})
CommonsValidateEntityInputSeo.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class CommonsValidateEntityInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    idempotency_key: Union[Annotated[str, Field(min_length=8, max_length=200)], None] = Field(None, alias='idempotencyKey', description='Optional write idempotency key. Validation does not write, so this is checked only when supplied.')
    title: Union[Annotated[str, Field(max_length=180)], None] = Field(None, alias='title', description='Candidate public page title. Validation reports an error when it is absent or shorter than the publishable minimum.')
    description: Union[Annotated[str, Field(max_length=600)], None] = Field(None, alias='description', description='Candidate schema.org description. Validation reports an error when it is absent or shorter than the publishable minimum.')
    slug: Union[Annotated[str, Field(max_length=180)], None] = Field(None, alias='slug', description='Optional URL slug. Omit to derive one from title.')
    entity_id: Union[Annotated[str, Field(max_length=80)], None] = Field(None, alias='entityId', description='Existing Transparent Public Wiki entity id when proposing an edit. New entities normally omit this and receive a TPW-Q id.')
    entity_type: Union[Annotated[str, Field(max_length=120)], None] = Field(None, alias='entityType', description='Backend Wikidata-style type. Prefer precise entity classes such as SoftwareApplication, Organization, Person, Event, Place, Taxon, ScienceConcept, MathConcept, TechArticle, or PublicArticle; the public article structure should match the selected type.')
    disambiguation_name: Union[Annotated[str, Field(max_length=240)], None] = Field(None, alias='disambiguationName', description='Clarifying name used when the concept could be confused with another entity.')
    featured_image: Union[CommonsValidateEntityInputFeaturedImage, None] = Field(None, alias='featuredImage', description='Required for auto-published public entities. First call commons_host_image with attachment bytes, an image artifact, a direct image URL, or a webpage URL, then place its returned permanent URL here. Validation does not fetch external images and reports unregistered URLs as not publishable. Submit retains a compatibility fallback for public URLs. The image is also added to the media manifest if absent.')
    source: Union[CommonsValidateEntityInputSource, None] = Field(None, alias='source', description='Source provenance. Store original URL, source byline, and origin canonical here; canonical does not replace rights review.')
    tags: Union[Annotated[list[Annotated[str, Field(min_length=1, max_length=80)]], Field(max_length=24)], None] = Field(None, alias='tags', description='Standardized topic tags. Use existing/searchable concepts when possible.')
    keywords: Union[Annotated[list[Annotated[str, Field(min_length=1, max_length=120)]], Field(max_length=50)], None] = Field(None, alias='keywords', description='SEO and retrieval keywords.')
    related_entities: Union[Annotated[list[CommonsValidateEntityInputRelatedEntitiesItem], Field(max_length=200)], None] = Field(None, alias='relatedEntities', description='Related concepts, including trails. Existing entities should use entityId.')
    claims: Union[Annotated[list[CommonsValidateEntityInputClaimsItem], Field(max_length=300)], None] = Field(None, alias='claims', description='Governed relationship assertions. Supplying claims replaces the accepted claim set for this entity; omitting claims preserves it. Only approved, active, non-disputed claims project into the RFC 9264 linkset.')
    body_markdown: Union[Annotated[str, Field(max_length=500000)], None] = Field(None, alias='bodyMarkdown', description='Structured encyclopedia body in neutral Markdown, not a raw scrape dump or blog essay. Use H2 for entity-profile sections and H3/H4/H5 for subtopics; every heading appears in the public page menu. Call commons_prepare_entity first for the live entity profile and commons_validate_entity before submit. Profile sections are adaptive: include History, Pricing, Reception, Timeline, Classification, or similar sections only when source evidence supports them; omit unsupported sections instead of adding empty/filler headings. Apply NPOV, verifiability, and no-original-research rules; self-published sources can support only uncontroversial source-owned facts.')
    content_sections: Union[Annotated[list[CommonsValidateEntityInputContentSectionsItem], Field(max_length=80)], None] = Field(None, alias='contentSections', description='Structured article sections. If bodyMarkdown is omitted, these are rendered into the article body. Headings should follow the selected entity profile, and body text may include H3/H4/H5 subheadings for every visible page-menu subitem.')
    article_sections: Union[CommonsValidateEntityInputArticleSections, None] = Field(None, alias='articleSections', description='Wikipedia-style bottom article sections: See also, Notes, Citations, External links, Categories.')
    media: Union[Annotated[list[CommonsValidateEntityInputMediaItem], Field(max_length=300)], None] = Field(None, alias='media', description='Image, video, and audio assets for the public entity. Videos are kept in the media manifest but are not vectorized as comments/community content.')
    json_ld: Union[dict[str, Any], None] = Field(None, alias='jsonLd', description='Optional caller-supplied JSON-LD. Omit to let the server generate schema.org Article JSON-LD from the entity fields.')
    seo: Union[CommonsValidateEntityInputSeo, None] = Field(None, alias='seo', description='schema.org/SEO controls. Use relCanonical for substantial source republishing.')
    actor_channel: Union[Literal['mcp', 'frontend', 'api'], None] = Field(None, alias='actorChannel', description='How this contribution was made.')
    actor_label: Union[Annotated[str, Field(max_length=120)], None] = Field(None, alias='actorLabel', description='Human, agent, team, or organization label recorded in the public contribution ledger.')
    change_summary: Union[Annotated[str, Field(max_length=500)], None] = Field(None, alias='changeSummary', description='Short contribution note recorded in the ledger.')
    base_revision: Union[Annotated[int, Field(le=9007199254740991, gt=0)], None] = Field(None, alias='baseRevision', description='Required when editing an existing entity if you want auto-publish. Without a matching revision, the proposal is held for review.')
    review_policy: Union[Literal['auto_publish_if_safe', 'always_review'], None] = Field(None, alias='reviewPolicy', description='Default auto-publishes only safe non-conflicting writes. Use always_review when the contributor wants human review.')


CommonsValidateEntityOutputVariant1DataImageDiagnosticsFeaturedImage = TypedDict('CommonsValidateEntityOutputVariant1DataImageDiagnosticsFeaturedImage', {
    'state': Required[Literal['missing', 'external_unhosted', 'commons_hosted']],
    'url': Required[Union[str, None]],
    'commonsImageId': Required[Union[str, None]],
    'readyForPublish': Required[bool],
    'submitWillAttemptAutoHost': Required[bool],
    'requiredAction': Required[Union[str, None]],
})
CommonsValidateEntityOutputVariant1DataImageDiagnosticsFeaturedImage.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsValidateEntityOutputVariant1DataImageDiagnostics = TypedDict('CommonsValidateEntityOutputVariant1DataImageDiagnostics', {
    'featuredImage': Required[CommonsValidateEntityOutputVariant1DataImageDiagnosticsFeaturedImage],
})
CommonsValidateEntityOutputVariant1DataImageDiagnostics.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsValidateEntityOutputVariant1Data = TypedDict('CommonsValidateEntityOutputVariant1Data', {
    'ok': Required[Literal[True]],
    'valid': Required[bool],
    'publishable': Required[bool],
    'autoPublishEligible': Required[bool],
    'errors': Required[list[str]],
    'warnings': Required[list[str]],
    'imageDiagnostics': Required[CommonsValidateEntityOutputVariant1DataImageDiagnostics],
})
CommonsValidateEntityOutputVariant1Data.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CommonsValidateEntityOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    data: Union[CommonsValidateEntityOutputVariant1Data, None] = Field(None, alias='data', description='')
    error: Union[str, None] = Field(None, alias='error', description='')
    message: Union[str, None] = Field(None, alias='message', description='')


CommonsValidateEntityOutputVariant2DeliveryArtifactsItem = TypedDict('CommonsValidateEntityOutputVariant2DeliveryArtifactsItem', {
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
CommonsValidateEntityOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsValidateEntityOutputVariant2DeliveryAvailableExportsItem = TypedDict('CommonsValidateEntityOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
CommonsValidateEntityOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsValidateEntityOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('CommonsValidateEntityOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
CommonsValidateEntityOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsValidateEntityOutputVariant2Delivery = TypedDict('CommonsValidateEntityOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[CommonsValidateEntityOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[CommonsValidateEntityOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[CommonsValidateEntityOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
CommonsValidateEntityOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsValidateEntityOutputVariant2RecoveryOperation = TypedDict('CommonsValidateEntityOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CommonsValidateEntityOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsValidateEntityOutputVariant2Recovery = TypedDict('CommonsValidateEntityOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[CommonsValidateEntityOutputVariant2RecoveryOperation],
})
CommonsValidateEntityOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CommonsValidateEntityOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: CommonsValidateEntityOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: CommonsValidateEntityOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(CommonsValidateEntityOutput).
CommonsValidateEntityOutput = Union[CommonsValidateEntityOutputVariant2, CommonsValidateEntityOutputVariant1]

_CommonsValidateEntityInputAdapter = TypeAdapter(CommonsValidateEntityInput)
_CommonsValidateEntityOutputAdapter = TypeAdapter(CommonsValidateEntityOutput)