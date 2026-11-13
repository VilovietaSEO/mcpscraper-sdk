from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class ExtractUrlStatusInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    job_id: Annotated[str, Field(min_length=1, max_length=200)] = Field(..., alias='jobId', description='The jobId returned by extract_url. Polling never starts or bills another extraction.')


ExtractUrlStatusOutputVariant1ResultVariant1HeadingsItem = TypedDict('ExtractUrlStatusOutputVariant1ResultVariant1HeadingsItem', {
    'level': Required[Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)]],
    'text': Required[str],
})
ExtractUrlStatusOutputVariant1ResultVariant1HeadingsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExtractUrlStatusOutputVariant1ResultVariant1ContactEvidenceEmailsItem = TypedDict('ExtractUrlStatusOutputVariant1ResultVariant1ContactEvidenceEmailsItem', {
    'value': Required[str],
    'sourceUrl': Required[str],
    'context': Required[Annotated[str, Field(max_length=280)]],
    'sourceType': Required[Literal['first_party_page', 'structured_data', 'provided', 'serp_snippet']],
    'sourceTitle': NotRequired[str],
    'sourcePosition': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
ExtractUrlStatusOutputVariant1ResultVariant1ContactEvidenceEmailsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExtractUrlStatusOutputVariant1ResultVariant1ContactEvidenceSocialProfilesItem = TypedDict('ExtractUrlStatusOutputVariant1ResultVariant1ContactEvidenceSocialProfilesItem', {
    'url': Required[str],
    'network': Required[str],
    'sourceUrl': Required[str],
    'context': Required[Annotated[str, Field(max_length=280)]],
})
ExtractUrlStatusOutputVariant1ResultVariant1ContactEvidenceSocialProfilesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExtractUrlStatusOutputVariant1ResultVariant1ContactEvidenceContactFormsItem = TypedDict('ExtractUrlStatusOutputVariant1ResultVariant1ContactEvidenceContactFormsItem', {
    'url': Required[str],
    'sourceUrl': Required[str],
    'context': Required[Annotated[str, Field(max_length=280)]],
})
ExtractUrlStatusOutputVariant1ResultVariant1ContactEvidenceContactFormsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExtractUrlStatusOutputVariant1ResultVariant1ContactEvidenceCandidatePageUrlsItem = TypedDict('ExtractUrlStatusOutputVariant1ResultVariant1ContactEvidenceCandidatePageUrlsItem', {
    'url': Required[str],
    'sourceUrl': Required[str],
    'context': Required[Annotated[str, Field(max_length=280)]],
})
ExtractUrlStatusOutputVariant1ResultVariant1ContactEvidenceCandidatePageUrlsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExtractUrlStatusOutputVariant1ResultVariant1ContactEvidence = TypedDict('ExtractUrlStatusOutputVariant1ResultVariant1ContactEvidence', {
    'emails': Required[Annotated[list[ExtractUrlStatusOutputVariant1ResultVariant1ContactEvidenceEmailsItem], Field(max_length=20)]],
    'socialProfiles': Required[Annotated[list[ExtractUrlStatusOutputVariant1ResultVariant1ContactEvidenceSocialProfilesItem], Field(max_length=20)]],
    'contactForms': Required[Annotated[list[ExtractUrlStatusOutputVariant1ResultVariant1ContactEvidenceContactFormsItem], Field(max_length=10)]],
    'candidatePageUrls': Required[Annotated[list[ExtractUrlStatusOutputVariant1ResultVariant1ContactEvidenceCandidatePageUrlsItem], Field(max_length=20)]],
})
ExtractUrlStatusOutputVariant1ResultVariant1ContactEvidence.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExtractUrlStatusOutputVariant1ResultVariant1ScreenshotArtifact = TypedDict('ExtractUrlStatusOutputVariant1ResultVariant1ScreenshotArtifact', {
    'artifactId': Required[str],
    'filename': Required[str],
    'contentType': Required[str],
    'bytes': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'sha256': Required[str],
    'expiresAt': Required[str],
    'downloadUrl': Required[Union[str, None]],
    'downloadUrlExpiresAt': Required[Union[str, None]],
})
ExtractUrlStatusOutputVariant1ResultVariant1ScreenshotArtifact.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExtractUrlStatusOutputVariant1ResultVariant1ArchiveVariant1 = TypedDict('ExtractUrlStatusOutputVariant1ResultVariant1ArchiveVariant1', {
    'timestamp': Required[str],
    'originalUrl': Required[str],
    'replayUrl': Required[str],
    'rawReplayUrl': Required[str],
})
ExtractUrlStatusOutputVariant1ResultVariant1ArchiveVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExtractUrlStatusOutputVariant1ResultVariant1FeaturedImageVariant1 = TypedDict('ExtractUrlStatusOutputVariant1ResultVariant1FeaturedImageVariant1', {
    'url': Required[str],
    'archivedUrl': Required[Union[str, None]],
    'source': Required[Literal['og:image', 'twitter:image', 'json-ld', 'content-image']],
})
ExtractUrlStatusOutputVariant1ResultVariant1FeaturedImageVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExtractUrlStatusOutputVariant1ResultVariant1BrandingVariant1Colors = TypedDict('ExtractUrlStatusOutputVariant1ResultVariant1BrandingVariant1Colors', {
    'primary': Required[Union[str, None]],
    'accent': Required[Union[str, None]],
    'background': Required[Union[str, None]],
    'text': Required[Union[str, None]],
    'heading': Required[Union[str, None]],
})
ExtractUrlStatusOutputVariant1ResultVariant1BrandingVariant1Colors.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExtractUrlStatusOutputVariant1ResultVariant1BrandingVariant1ColorEvidencePrimaryVariant1 = TypedDict('ExtractUrlStatusOutputVariant1ResultVariant1BrandingVariant1ColorEvidencePrimaryVariant1', {
    'value': Required[str],
    'source': Required[Literal['css_variable', 'theme_color', 'visible_cta', 'navigation_background', 'header_svg', 'visible_background', 'body_background', 'body_text', 'heading_text']],
    'confidence': Required[Literal['high', 'medium', 'low']],
    'detail': Required[Union[str, None]],
})
ExtractUrlStatusOutputVariant1ResultVariant1BrandingVariant1ColorEvidencePrimaryVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExtractUrlStatusOutputVariant1ResultVariant1BrandingVariant1ColorEvidenceAccentVariant1 = TypedDict('ExtractUrlStatusOutputVariant1ResultVariant1BrandingVariant1ColorEvidenceAccentVariant1', {
    'value': Required[str],
    'source': Required[Literal['css_variable', 'theme_color', 'visible_cta', 'navigation_background', 'header_svg', 'visible_background', 'body_background', 'body_text', 'heading_text']],
    'confidence': Required[Literal['high', 'medium', 'low']],
    'detail': Required[Union[str, None]],
})
ExtractUrlStatusOutputVariant1ResultVariant1BrandingVariant1ColorEvidenceAccentVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExtractUrlStatusOutputVariant1ResultVariant1BrandingVariant1ColorEvidenceBackgroundVariant1 = TypedDict('ExtractUrlStatusOutputVariant1ResultVariant1BrandingVariant1ColorEvidenceBackgroundVariant1', {
    'value': Required[str],
    'source': Required[Literal['body_background']],
    'confidence': Required[Literal['high', 'medium', 'low']],
    'detail': Required[Union[str, None]],
})
ExtractUrlStatusOutputVariant1ResultVariant1BrandingVariant1ColorEvidenceBackgroundVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExtractUrlStatusOutputVariant1ResultVariant1BrandingVariant1ColorEvidenceTextVariant1 = TypedDict('ExtractUrlStatusOutputVariant1ResultVariant1BrandingVariant1ColorEvidenceTextVariant1', {
    'value': Required[str],
    'source': Required[Literal['body_text']],
    'confidence': Required[Literal['high', 'medium', 'low']],
    'detail': Required[Union[str, None]],
})
ExtractUrlStatusOutputVariant1ResultVariant1BrandingVariant1ColorEvidenceTextVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExtractUrlStatusOutputVariant1ResultVariant1BrandingVariant1ColorEvidenceHeadingVariant1 = TypedDict('ExtractUrlStatusOutputVariant1ResultVariant1BrandingVariant1ColorEvidenceHeadingVariant1', {
    'value': Required[str],
    'source': Required[Literal['heading_text']],
    'confidence': Required[Literal['high', 'medium', 'low']],
    'detail': Required[Union[str, None]],
})
ExtractUrlStatusOutputVariant1ResultVariant1BrandingVariant1ColorEvidenceHeadingVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExtractUrlStatusOutputVariant1ResultVariant1BrandingVariant1ColorEvidence = TypedDict('ExtractUrlStatusOutputVariant1ResultVariant1BrandingVariant1ColorEvidence', {
    'primary': Required[Union[ExtractUrlStatusOutputVariant1ResultVariant1BrandingVariant1ColorEvidencePrimaryVariant1, None]],
    'accent': Required[Union[ExtractUrlStatusOutputVariant1ResultVariant1BrandingVariant1ColorEvidenceAccentVariant1, None]],
    'background': Required[Union[ExtractUrlStatusOutputVariant1ResultVariant1BrandingVariant1ColorEvidenceBackgroundVariant1, None]],
    'text': Required[Union[ExtractUrlStatusOutputVariant1ResultVariant1BrandingVariant1ColorEvidenceTextVariant1, None]],
    'heading': Required[Union[ExtractUrlStatusOutputVariant1ResultVariant1BrandingVariant1ColorEvidenceHeadingVariant1, None]],
})
ExtractUrlStatusOutputVariant1ResultVariant1BrandingVariant1ColorEvidence.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExtractUrlStatusOutputVariant1ResultVariant1BrandingVariant1Fonts = TypedDict('ExtractUrlStatusOutputVariant1ResultVariant1BrandingVariant1Fonts', {
    'heading': Required[Union[str, None]],
    'body': Required[Union[str, None]],
})
ExtractUrlStatusOutputVariant1ResultVariant1BrandingVariant1Fonts.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExtractUrlStatusOutputVariant1ResultVariant1BrandingVariant1AssetsLogoCandidatesItem = TypedDict('ExtractUrlStatusOutputVariant1ResultVariant1BrandingVariant1AssetsLogoCandidatesItem', {
    'url': Required[str],
    'score': Required[Union[float, int]],
    'confidence': Required[Literal['high', 'medium', 'low']],
    'region': Required[Literal['json_ld', 'header', 'nav', 'footer', 'body', 'favicon']],
    'evidence': Required[list[str]],
    'alt': Required[Union[str, None]],
    'width': Required[Union[Union[float, int], None]],
    'height': Required[Union[Union[float, int], None]],
})
ExtractUrlStatusOutputVariant1ResultVariant1BrandingVariant1AssetsLogoCandidatesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExtractUrlStatusOutputVariant1ResultVariant1BrandingVariant1AssetsProofImagesItem = TypedDict('ExtractUrlStatusOutputVariant1ResultVariant1BrandingVariant1AssetsProofImagesItem', {
    'url': Required[str],
    'proofType': Required[Literal['certification', 'accreditation', 'award', 'membership', 'partner_or_customer', 'press_mention', 'trust_mark']],
    'score': Required[Union[float, int]],
    'confidence': Required[Literal['high', 'medium', 'low']],
    'evidence': Required[list[str]],
    'alt': Required[Union[str, None]],
    'context': Required[Union[str, None]],
    'width': Required[Union[Union[float, int], None]],
    'height': Required[Union[Union[float, int], None]],
})
ExtractUrlStatusOutputVariant1ResultVariant1BrandingVariant1AssetsProofImagesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExtractUrlStatusOutputVariant1ResultVariant1BrandingVariant1Assets = TypedDict('ExtractUrlStatusOutputVariant1ResultVariant1BrandingVariant1Assets', {
    'logo': Required[Union[str, None]],
    'favicon': Required[Union[str, None]],
    'logoConfidence': Required[Union[Literal['high', 'medium', 'low'], None]],
    'logoSelectionReason': Required[Union[str, None]],
    'logoVariants': Required[list[str]],
    'logoCandidates': Required[list[ExtractUrlStatusOutputVariant1ResultVariant1BrandingVariant1AssetsLogoCandidatesItem]],
    'proofImages': Required[list[ExtractUrlStatusOutputVariant1ResultVariant1BrandingVariant1AssetsProofImagesItem]],
})
ExtractUrlStatusOutputVariant1ResultVariant1BrandingVariant1Assets.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExtractUrlStatusOutputVariant1ResultVariant1BrandingVariant1 = TypedDict('ExtractUrlStatusOutputVariant1ResultVariant1BrandingVariant1', {
    'colorScheme': Required[Union[Literal['light', 'dark'], None]],
    'colors': Required[ExtractUrlStatusOutputVariant1ResultVariant1BrandingVariant1Colors],
    'colorEvidence': Required[ExtractUrlStatusOutputVariant1ResultVariant1BrandingVariant1ColorEvidence],
    'fonts': Required[ExtractUrlStatusOutputVariant1ResultVariant1BrandingVariant1Fonts],
    'assets': Required[ExtractUrlStatusOutputVariant1ResultVariant1BrandingVariant1Assets],
})
ExtractUrlStatusOutputVariant1ResultVariant1BrandingVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExtractUrlStatusOutputVariant1ResultVariant1MediaAssetsVariant1Item = TypedDict('ExtractUrlStatusOutputVariant1ResultVariant1MediaAssetsVariant1Item', {
    'url': Required[str],
    'type': Required[Literal['image', 'video', 'audio']],
    'mimeType': Required[Union[str, None]],
    'filename': Required[str],
    'savedPath': Required[Union[str, None]],
    'sizeBytes': Required[Union[Annotated[int, Field(ge=0, le=9007199254740991)], None]],
    'discoveryMethods': Required[list[str]],
    'altTexts': Required[list[str]],
    'contexts': Required[list[str]],
    'width': Required[Union[Annotated[int, Field(ge=0, le=9007199254740991)], None]],
    'height': Required[Union[Annotated[int, Field(ge=0, le=9007199254740991)], None]],
    'variants': Required[list[str]],
    'finalUrl': NotRequired[Union[str, None]],
    'duplicateOf': NotRequired[Union[str, None]],
    'sha256': NotRequired[Union[str, None]],
    'downloadStatus': NotRequired[Literal['downloaded', 'failed', 'not_attempted']],
    'downloadError': NotRequired[Union[str, None]],
    'contentIndex': Required[Union[Annotated[int, Field(ge=0, le=9007199254740991)], None]],
})
ExtractUrlStatusOutputVariant1ResultVariant1MediaAssetsVariant1Item.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExtractUrlStatusOutputVariant1ResultVariant1MediaVariant1AssetsItem = TypedDict('ExtractUrlStatusOutputVariant1ResultVariant1MediaVariant1AssetsItem', {
    'url': Required[str],
    'type': Required[Literal['image', 'video', 'audio']],
    'mimeType': Required[Union[str, None]],
    'filename': Required[str],
    'savedPath': Required[Union[str, None]],
    'sizeBytes': Required[Union[Annotated[int, Field(ge=0, le=9007199254740991)], None]],
    'discoveryMethods': Required[list[str]],
    'altTexts': Required[list[str]],
    'contexts': Required[list[str]],
    'width': Required[Union[Annotated[int, Field(ge=0, le=9007199254740991)], None]],
    'height': Required[Union[Annotated[int, Field(ge=0, le=9007199254740991)], None]],
    'variants': Required[list[str]],
    'finalUrl': NotRequired[Union[str, None]],
    'duplicateOf': NotRequired[Union[str, None]],
    'sha256': NotRequired[Union[str, None]],
    'downloadStatus': NotRequired[Literal['downloaded', 'failed', 'not_attempted']],
    'downloadError': NotRequired[Union[str, None]],
    'contentIndex': Required[Union[Annotated[int, Field(ge=0, le=9007199254740991)], None]],
})
ExtractUrlStatusOutputVariant1ResultVariant1MediaVariant1AssetsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExtractUrlStatusOutputVariant1ResultVariant1MediaVariant1ArtifactVariant1 = TypedDict('ExtractUrlStatusOutputVariant1ResultVariant1MediaVariant1ArtifactVariant1', {
    'artifactId': Required[str],
    'filename': Required[str],
    'contentType': Required[str],
    'bytes': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'sha256': Required[str],
    'expiresAt': Required[str],
    'downloadUrl': Required[Union[str, None]],
    'downloadUrlExpiresAt': Required[Union[str, None]],
    'localPath': Required[Union[str, None]],
})
ExtractUrlStatusOutputVariant1ResultVariant1MediaVariant1ArtifactVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExtractUrlStatusOutputVariant1ResultVariant1MediaVariant1 = TypedDict('ExtractUrlStatusOutputVariant1ResultVariant1MediaVariant1', {
    'pageUrl': Required[str],
    'staticFound': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'renderedFound': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'totalFound': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'filteredCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'retainedCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'completeness': Required[Literal['complete', 'partial']],
    'exhausted': Required[bool],
    'stopReason': Required[Literal['page_exhausted', 'asset_limit', 'scroll_round_limit', 'render_unavailable']],
    'scrollRounds': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'warnings': Required[list[str]],
    'assets': Required[list[ExtractUrlStatusOutputVariant1ResultVariant1MediaVariant1AssetsItem]],
    'artifact': Required[Union[ExtractUrlStatusOutputVariant1ResultVariant1MediaVariant1ArtifactVariant1, None]],
})
ExtractUrlStatusOutputVariant1ResultVariant1MediaVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExtractUrlStatusOutputVariant1ResultVariant1Memory = TypedDict('ExtractUrlStatusOutputVariant1ResultVariant1Memory', {
    'deposited': Required[bool],
    'vault': NotRequired[str],
    'noteId': NotRequired[str],
    'path': NotRequired[str],
    'chunks': NotRequired[Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)]],
    'fileUrl': NotRequired[str],
    'fileExpiresAt': NotRequired[str],
    'error': NotRequired[str],
})
ExtractUrlStatusOutputVariant1ResultVariant1Memory.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExtractUrlStatusOutputVariant1ResultVariant1MemoryImagesAssetsItem = TypedDict('ExtractUrlStatusOutputVariant1ResultVariant1MemoryImagesAssetsItem', {
    'sourceUrl': Required[str],
    'sourceKind': Required[Literal['screenshot', 'page_image']],
    'saved': Required[bool],
    'assetId': NotRequired[str],
    'error': NotRequired[str],
})
ExtractUrlStatusOutputVariant1ResultVariant1MemoryImagesAssetsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExtractUrlStatusOutputVariant1ResultVariant1MemoryImages = TypedDict('ExtractUrlStatusOutputVariant1ResultVariant1MemoryImages', {
    'requested': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'saved': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'skipped': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'assets': Required[list[ExtractUrlStatusOutputVariant1ResultVariant1MemoryImagesAssetsItem]],
    'error': NotRequired[str],
})
ExtractUrlStatusOutputVariant1ResultVariant1MemoryImages.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExtractUrlStatusOutputVariant1ResultVariant1Delivery = TypedDict('ExtractUrlStatusOutputVariant1ResultVariant1Delivery', {
    'requested': Required[Literal['auto', 'inline', 'artifact', 'memory']],
    'effective': Required[Literal['inline', 'artifact', 'memory', 'local_file']],
    'retained': Required[bool],
    'nextAction': Required[Union[str, None]],
})
ExtractUrlStatusOutputVariant1ResultVariant1Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExtractUrlStatusOutputVariant1ResultVariant1Artifact = TypedDict('ExtractUrlStatusOutputVariant1ResultVariant1Artifact', {
    'artifactId': Required[str],
    'mimeType': Required[str],
    'sizeBytes': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'bytes': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'sha256': Required[str],
    'expiresAt': Required[str],
    'downloadUrl': Required[Union[str, None]],
    'downloadUrlExpiresAt': Required[Union[str, None]],
    'preview': Required[str],
})
ExtractUrlStatusOutputVariant1ResultVariant1Artifact.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExtractUrlStatusOutputVariant1ResultVariant1 = TypedDict('ExtractUrlStatusOutputVariant1ResultVariant1', {
    'url': Required[str],
    'title': Required[Union[str, None]],
    'headings': Required[list[ExtractUrlStatusOutputVariant1ResultVariant1HeadingsItem]],
    'schemaBlockCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'entityName': Required[Union[str, None]],
    'entityTypes': Required[list[str]],
    'structuredDataLogo': Required[Union[str, None]],
    'napScore': Required[Union[Union[float, int], None]],
    'missingSchemaFields': Required[list[str]],
    'contactEvidence': Required[ExtractUrlStatusOutputVariant1ResultVariant1ContactEvidence],
    'screenshotSaved': Required[Union[str, None]],
    'screenshotArtifact': NotRequired[ExtractUrlStatusOutputVariant1ResultVariant1ScreenshotArtifact],
    'archive': Required[Union[ExtractUrlStatusOutputVariant1ResultVariant1ArchiveVariant1, None]],
    'featuredImage': Required[Union[ExtractUrlStatusOutputVariant1ResultVariant1FeaturedImageVariant1, None]],
    'branding': Required[Union[ExtractUrlStatusOutputVariant1ResultVariant1BrandingVariant1, None]],
    'mediaAssets': Required[Union[list[ExtractUrlStatusOutputVariant1ResultVariant1MediaAssetsVariant1Item], None]],
    'media': Required[Union[ExtractUrlStatusOutputVariant1ResultVariant1MediaVariant1, None]],
    'memory': NotRequired[ExtractUrlStatusOutputVariant1ResultVariant1Memory],
    'memoryImages': NotRequired[ExtractUrlStatusOutputVariant1ResultVariant1MemoryImages],
    'delivery': NotRequired[ExtractUrlStatusOutputVariant1ResultVariant1Delivery],
    'localPath': NotRequired[str],
    'artifact': NotRequired[ExtractUrlStatusOutputVariant1ResultVariant1Artifact],
})
ExtractUrlStatusOutputVariant1ResultVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExtractUrlStatusOutputVariant1Billing = TypedDict('ExtractUrlStatusOutputVariant1Billing', {
    'chargeStatus': Required[str],
    'credits': Required[Annotated[Union[float, int], Field(ge=0)]],
})
ExtractUrlStatusOutputVariant1Billing.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ExtractUrlStatusOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    job_id: str = Field(..., alias='jobId', description='')
    status: Literal['pending', 'running', 'done', 'failed', 'cancelled'] = Field(..., alias='status', description='')
    status_tool: Literal['extract_url_status'] = Field(..., alias='statusTool', description='')
    replayed: bool = Field(..., alias='replayed', description='')
    result: Union[ExtractUrlStatusOutputVariant1ResultVariant1, None] = Field(..., alias='result', description='')
    error: Union[dict[str, Any], None] = Field(..., alias='error', description='')
    billing: ExtractUrlStatusOutputVariant1Billing = Field(..., alias='billing', description='')


ExtractUrlStatusOutputVariant2DeliveryArtifactsItem = TypedDict('ExtractUrlStatusOutputVariant2DeliveryArtifactsItem', {
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
ExtractUrlStatusOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExtractUrlStatusOutputVariant2DeliveryAvailableExportsItem = TypedDict('ExtractUrlStatusOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
ExtractUrlStatusOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExtractUrlStatusOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('ExtractUrlStatusOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
ExtractUrlStatusOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExtractUrlStatusOutputVariant2Delivery = TypedDict('ExtractUrlStatusOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[ExtractUrlStatusOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[ExtractUrlStatusOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[ExtractUrlStatusOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
ExtractUrlStatusOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExtractUrlStatusOutputVariant2RecoveryOperation = TypedDict('ExtractUrlStatusOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
ExtractUrlStatusOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExtractUrlStatusOutputVariant2Recovery = TypedDict('ExtractUrlStatusOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[ExtractUrlStatusOutputVariant2RecoveryOperation],
})
ExtractUrlStatusOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ExtractUrlStatusOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: ExtractUrlStatusOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: ExtractUrlStatusOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(ExtractUrlStatusOutput).
ExtractUrlStatusOutput = Union[ExtractUrlStatusOutputVariant1, ExtractUrlStatusOutputVariant2]

_ExtractUrlStatusInputAdapter = TypeAdapter(ExtractUrlStatusInput)
_ExtractUrlStatusOutputAdapter = TypeAdapter(ExtractUrlStatusOutput)