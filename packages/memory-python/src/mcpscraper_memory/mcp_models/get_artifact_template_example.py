from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class GetArtifactTemplateExampleInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    preset_key: Literal['editorial_reading_room_v1', 'personal_authority_v1', 'personal_authority_v2', 'newsroom_publisher_v1', 'blog_article_v1'] = Field(..., alias='presetKey', description='Registered preset key returned by list_artifact_templates.')


GetArtifactTemplateExampleOutputVariant1ExampleDefaultConfigVariant1 = TypedDict('GetArtifactTemplateExampleOutputVariant1ExampleDefaultConfigVariant1', {
    'theme': Required[Literal['paper', 'ink', 'warm']],
    'density': Required[Literal['comfortable', 'compact']],
    'showSourceRail': Required[bool],
    'showGeneratedAt': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
})
GetArtifactTemplateExampleOutputVariant1ExampleDefaultConfigVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetArtifactTemplateExampleOutputVariant1ExampleDefaultConfigVariant2FeatureFlags = TypedDict('GetArtifactTemplateExampleOutputVariant1ExampleDefaultConfigVariant2FeatureFlags', {
    'navigation': Required[bool],
    'socialLinks': Required[bool],
    'authority': Required[bool],
    'consultation': Required[bool],
    'learning': Required[bool],
    'services': Required[bool],
    'proof': Required[bool],
    'finalCta': Required[bool],
})
GetArtifactTemplateExampleOutputVariant1ExampleDefaultConfigVariant2FeatureFlags.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetArtifactTemplateExampleOutputVariant1ExampleDefaultConfigVariant2 = TypedDict('GetArtifactTemplateExampleOutputVariant1ExampleDefaultConfigVariant2', {
    'theme': Required[Literal['blue', 'slate', 'monochrome']],
    'showGeneratedAt': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'featureFlags': Required[GetArtifactTemplateExampleOutputVariant1ExampleDefaultConfigVariant2FeatureFlags],
})
GetArtifactTemplateExampleOutputVariant1ExampleDefaultConfigVariant2.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetArtifactTemplateExampleOutputVariant1ExampleDefaultConfigVariant3Colors = TypedDict('GetArtifactTemplateExampleOutputVariant1ExampleDefaultConfigVariant3Colors', {
    'accent': NotRequired[str],
    'background': NotRequired[str],
    'surface': NotRequired[str],
    'text': NotRequired[str],
})
GetArtifactTemplateExampleOutputVariant1ExampleDefaultConfigVariant3Colors.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetArtifactTemplateExampleOutputVariant1ExampleDefaultConfigVariant3Typography = TypedDict('GetArtifactTemplateExampleOutputVariant1ExampleDefaultConfigVariant3Typography', {
    'display': Required[Literal['editorial-serif', 'modern-sans', 'humanist-sans']],
    'body': Required[Literal['editorial-serif', 'modern-sans', 'humanist-sans']],
})
GetArtifactTemplateExampleOutputVariant1ExampleDefaultConfigVariant3Typography.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetArtifactTemplateExampleOutputVariant1ExampleDefaultConfigVariant3FeatureFlags = TypedDict('GetArtifactTemplateExampleOutputVariant1ExampleDefaultConfigVariant3FeatureFlags', {
    'navigation': Required[bool],
    'socialLinks': Required[bool],
    'authority': Required[bool],
    'consultation': Required[bool],
    'learning': Required[bool],
    'services': Required[bool],
    'proof': Required[bool],
    'finalCta': Required[bool],
})
GetArtifactTemplateExampleOutputVariant1ExampleDefaultConfigVariant3FeatureFlags.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetArtifactTemplateExampleOutputVariant1ExampleDefaultConfigVariant3 = TypedDict('GetArtifactTemplateExampleOutputVariant1ExampleDefaultConfigVariant3', {
    'theme': Required[Literal['blue', 'terracotta', 'slate', 'monochrome']],
    'showGeneratedAt': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'colors': NotRequired[GetArtifactTemplateExampleOutputVariant1ExampleDefaultConfigVariant3Colors],
    'typography': NotRequired[GetArtifactTemplateExampleOutputVariant1ExampleDefaultConfigVariant3Typography],
    'featureFlags': Required[GetArtifactTemplateExampleOutputVariant1ExampleDefaultConfigVariant3FeatureFlags],
})
GetArtifactTemplateExampleOutputVariant1ExampleDefaultConfigVariant3.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetArtifactTemplateExampleOutputVariant1ExampleDefaultConfigVariant4FeatureFlags = TypedDict('GetArtifactTemplateExampleOutputVariant1ExampleDefaultConfigVariant4FeatureFlags', {
    'breakingTicker': Required[bool],
    'navigation': Required[bool],
    'leadGrid': Required[bool],
    'latestNews': Required[bool],
    'categorySections': Required[bool],
    'newsletter': Required[bool],
    'pressRoom': Required[bool],
    'trustFooter': Required[bool],
})
GetArtifactTemplateExampleOutputVariant1ExampleDefaultConfigVariant4FeatureFlags.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetArtifactTemplateExampleOutputVariant1ExampleDefaultConfigVariant4 = TypedDict('GetArtifactTemplateExampleOutputVariant1ExampleDefaultConfigVariant4', {
    'theme': Required[Literal['daily', 'journal', 'midnight']],
    'showGeneratedAt': Required[bool],
    'showBylines': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'featureFlags': Required[GetArtifactTemplateExampleOutputVariant1ExampleDefaultConfigVariant4FeatureFlags],
})
GetArtifactTemplateExampleOutputVariant1ExampleDefaultConfigVariant4.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetArtifactTemplateExampleOutputVariant1ExampleDefaultConfigVariant5FeatureFlags = TypedDict('GetArtifactTemplateExampleOutputVariant1ExampleDefaultConfigVariant5FeatureFlags', {
    'sidebarMedia': Required[bool],
    'disclosure': Required[bool],
    'stickyToc': Required[bool],
    'faq': Required[bool],
    'citation': Required[bool],
    'share': Required[bool],
    'authorCard': Required[bool],
})
GetArtifactTemplateExampleOutputVariant1ExampleDefaultConfigVariant5FeatureFlags.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetArtifactTemplateExampleOutputVariant1ExampleDefaultConfigVariant5 = TypedDict('GetArtifactTemplateExampleOutputVariant1ExampleDefaultConfigVariant5', {
    'theme': Required[Literal['navy', 'slate', 'forest']],
    'showGeneratedAt': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'featureFlags': Required[GetArtifactTemplateExampleOutputVariant1ExampleDefaultConfigVariant5FeatureFlags],
})
GetArtifactTemplateExampleOutputVariant1ExampleDefaultConfigVariant5.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetArtifactTemplateExampleOutputVariant1ExamplePreviewPagesItem = TypedDict('GetArtifactTemplateExampleOutputVariant1ExamplePreviewPagesItem', {
    'label': Required[Annotated[str, Field(min_length=1, max_length=120)]],
    'url': Required[str],
    'description': Required[Annotated[str, Field(min_length=1, max_length=500)]],
})
GetArtifactTemplateExampleOutputVariant1ExamplePreviewPagesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetArtifactTemplateExampleOutputVariant1Example = TypedDict('GetArtifactTemplateExampleOutputVariant1Example', {
    'presetKey': Required[Literal['editorial_reading_room_v1', 'personal_authority_v1', 'personal_authority_v2', 'newsroom_publisher_v1', 'blog_article_v1']],
    'name': Required[Annotated[str, Field(min_length=1, max_length=120)]],
    'description': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'rendererKey': Required[Literal['editorial_reading_room_v1', 'personal_authority_v1', 'personal_authority_v2', 'newsroom_publisher_v1', 'blog_article_v1']],
    'rendererVersion': Required[Literal[1]],
    'inputContractVersion': Required[Literal[1]],
    'defaultConfig': Required[Union[GetArtifactTemplateExampleOutputVariant1ExampleDefaultConfigVariant1, GetArtifactTemplateExampleOutputVariant1ExampleDefaultConfigVariant2, GetArtifactTemplateExampleOutputVariant1ExampleDefaultConfigVariant3, GetArtifactTemplateExampleOutputVariant1ExampleDefaultConfigVariant4, GetArtifactTemplateExampleOutputVariant1ExampleDefaultConfigVariant5]],
    'recommendedAuthoringInstructions': Required[Annotated[str, Field(min_length=1, max_length=4000)]],
    'previewPages': Required[Annotated[list[GetArtifactTemplateExampleOutputVariant1ExamplePreviewPagesItem], Field(min_length=1, max_length=8)]],
    'machineReadableExampleUrl': Required[str],
    'exampleInput': Required[dict[str, Any]],
})
GetArtifactTemplateExampleOutputVariant1Example.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class GetArtifactTemplateExampleOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    example: Union[GetArtifactTemplateExampleOutputVariant1Example, None] = Field(None, alias='example', description='')
    error: Union[Annotated[str, Field(min_length=1, max_length=500)], None] = Field(None, alias='error', description='')
    error_code: Union[Literal['invalid_request', 'not_found', 'conflict', 'template_archived', 'renderer_unavailable', 'artifact_unavailable', 'internal_error'], None] = Field(None, alias='errorCode', description='')
    request_id: Union[Annotated[str, Field(max_length=200)], None] = Field(None, alias='requestId', description='')


GetArtifactTemplateExampleOutputVariant2DeliveryArtifactsItem = TypedDict('GetArtifactTemplateExampleOutputVariant2DeliveryArtifactsItem', {
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
GetArtifactTemplateExampleOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetArtifactTemplateExampleOutputVariant2DeliveryAvailableExportsItem = TypedDict('GetArtifactTemplateExampleOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
GetArtifactTemplateExampleOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetArtifactTemplateExampleOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('GetArtifactTemplateExampleOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
GetArtifactTemplateExampleOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetArtifactTemplateExampleOutputVariant2Delivery = TypedDict('GetArtifactTemplateExampleOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[GetArtifactTemplateExampleOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[GetArtifactTemplateExampleOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[GetArtifactTemplateExampleOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
GetArtifactTemplateExampleOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetArtifactTemplateExampleOutputVariant2RecoveryOperation = TypedDict('GetArtifactTemplateExampleOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
GetArtifactTemplateExampleOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetArtifactTemplateExampleOutputVariant2Recovery = TypedDict('GetArtifactTemplateExampleOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[GetArtifactTemplateExampleOutputVariant2RecoveryOperation],
})
GetArtifactTemplateExampleOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class GetArtifactTemplateExampleOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: GetArtifactTemplateExampleOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: GetArtifactTemplateExampleOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(GetArtifactTemplateExampleOutput).
GetArtifactTemplateExampleOutput = Union[GetArtifactTemplateExampleOutputVariant2, GetArtifactTemplateExampleOutputVariant1]

_GetArtifactTemplateExampleInputAdapter = TypeAdapter(GetArtifactTemplateExampleInput)
_GetArtifactTemplateExampleOutputAdapter = TypeAdapter(GetArtifactTemplateExampleOutput)