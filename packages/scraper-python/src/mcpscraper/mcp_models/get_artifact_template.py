from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class GetArtifactTemplateInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    template_id: str = Field(..., alias='templateId', description='Opaque saved-template identifier returned by an artifact-template tool.')


GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant1Config = TypedDict('GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant1Config', {
    'theme': Required[Literal['paper', 'ink', 'warm']],
    'density': Required[Literal['comfortable', 'compact']],
    'showSourceRail': Required[bool],
    'showGeneratedAt': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
})
GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant1Config.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant1 = TypedDict('GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant1', {
    'templateVersionId': Required[str],
    'templateId': Required[str],
    'version': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'rendererVersion': Required[Literal[1]],
    'inputContractVersion': Required[Literal[1]],
    'authoringInstructions': Required[Annotated[str, Field(max_length=4000)]],
    'createdAt': Required[str],
    'rendererKey': Required[Literal['editorial_reading_room_v1']],
    'config': Required[GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant1Config],
})
GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant2ConfigFeatureFlags = TypedDict('GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant2ConfigFeatureFlags', {
    'navigation': Required[bool],
    'socialLinks': Required[bool],
    'authority': Required[bool],
    'consultation': Required[bool],
    'learning': Required[bool],
    'services': Required[bool],
    'proof': Required[bool],
    'finalCta': Required[bool],
})
GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant2ConfigFeatureFlags.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant2Config = TypedDict('GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant2Config', {
    'theme': Required[Literal['blue', 'slate', 'monochrome']],
    'showGeneratedAt': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'featureFlags': Required[GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant2ConfigFeatureFlags],
})
GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant2Config.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant2 = TypedDict('GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant2', {
    'templateVersionId': Required[str],
    'templateId': Required[str],
    'version': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'rendererVersion': Required[Literal[1]],
    'inputContractVersion': Required[Literal[1]],
    'authoringInstructions': Required[Annotated[str, Field(max_length=4000)]],
    'createdAt': Required[str],
    'rendererKey': Required[Literal['personal_authority_v1']],
    'config': Required[GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant2Config],
})
GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant2.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3ConfigColors = TypedDict('GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3ConfigColors', {
    'accent': NotRequired[str],
    'background': NotRequired[str],
    'surface': NotRequired[str],
    'text': NotRequired[str],
})
GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3ConfigColors.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3ConfigTypography = TypedDict('GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3ConfigTypography', {
    'display': Required[Literal['editorial-serif', 'modern-sans', 'humanist-sans']],
    'body': Required[Literal['editorial-serif', 'modern-sans', 'humanist-sans']],
})
GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3ConfigTypography.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3ConfigFeatureFlags = TypedDict('GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3ConfigFeatureFlags', {
    'navigation': Required[bool],
    'socialLinks': Required[bool],
    'authority': Required[bool],
    'consultation': Required[bool],
    'learning': Required[bool],
    'services': Required[bool],
    'proof': Required[bool],
    'finalCta': Required[bool],
})
GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3ConfigFeatureFlags.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3Config = TypedDict('GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3Config', {
    'theme': Required[Literal['blue', 'terracotta', 'slate', 'monochrome']],
    'showGeneratedAt': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'colors': NotRequired[GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3ConfigColors],
    'typography': NotRequired[GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3ConfigTypography],
    'featureFlags': Required[GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3ConfigFeatureFlags],
})
GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3Config.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3 = TypedDict('GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3', {
    'templateVersionId': Required[str],
    'templateId': Required[str],
    'version': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'rendererVersion': Required[Literal[1]],
    'inputContractVersion': Required[Literal[1]],
    'authoringInstructions': Required[Annotated[str, Field(max_length=4000)]],
    'createdAt': Required[str],
    'rendererKey': Required[Literal['personal_authority_v2']],
    'config': Required[GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3Config],
})
GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant4ConfigFeatureFlags = TypedDict('GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant4ConfigFeatureFlags', {
    'breakingTicker': Required[bool],
    'navigation': Required[bool],
    'leadGrid': Required[bool],
    'latestNews': Required[bool],
    'categorySections': Required[bool],
    'newsletter': Required[bool],
    'pressRoom': Required[bool],
    'trustFooter': Required[bool],
})
GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant4ConfigFeatureFlags.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant4Config = TypedDict('GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant4Config', {
    'theme': Required[Literal['daily', 'journal', 'midnight']],
    'showGeneratedAt': Required[bool],
    'showBylines': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'featureFlags': Required[GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant4ConfigFeatureFlags],
})
GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant4Config.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant4 = TypedDict('GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant4', {
    'templateVersionId': Required[str],
    'templateId': Required[str],
    'version': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'rendererVersion': Required[Literal[1]],
    'inputContractVersion': Required[Literal[1]],
    'authoringInstructions': Required[Annotated[str, Field(max_length=4000)]],
    'createdAt': Required[str],
    'rendererKey': Required[Literal['newsroom_publisher_v1']],
    'config': Required[GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant4Config],
})
GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant4.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant5ConfigFeatureFlags = TypedDict('GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant5ConfigFeatureFlags', {
    'sidebarMedia': Required[bool],
    'disclosure': Required[bool],
    'stickyToc': Required[bool],
    'faq': Required[bool],
    'citation': Required[bool],
    'share': Required[bool],
    'authorCard': Required[bool],
})
GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant5ConfigFeatureFlags.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant5Config = TypedDict('GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant5Config', {
    'theme': Required[Literal['navy', 'slate', 'forest']],
    'showGeneratedAt': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'featureFlags': Required[GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant5ConfigFeatureFlags],
})
GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant5Config.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant5 = TypedDict('GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant5', {
    'templateVersionId': Required[str],
    'templateId': Required[str],
    'version': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'rendererVersion': Required[Literal[1]],
    'inputContractVersion': Required[Literal[1]],
    'authoringInstructions': Required[Annotated[str, Field(max_length=4000)]],
    'createdAt': Required[str],
    'rendererKey': Required[Literal['blog_article_v1']],
    'config': Required[GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant5Config],
})
GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant5.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant1Config = TypedDict('GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant1Config', {
    'theme': Required[Literal['paper', 'ink', 'warm']],
    'density': Required[Literal['comfortable', 'compact']],
    'showSourceRail': Required[bool],
    'showGeneratedAt': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
})
GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant1Config.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant1 = TypedDict('GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant1', {
    'templateVersionId': Required[str],
    'templateId': Required[str],
    'version': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'rendererVersion': Required[Literal[1]],
    'inputContractVersion': Required[Literal[1]],
    'authoringInstructions': Required[Annotated[str, Field(max_length=4000)]],
    'createdAt': Required[str],
    'rendererKey': Required[Literal['editorial_reading_room_v1']],
    'config': Required[GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant1Config],
})
GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant2ConfigFeatureFlags = TypedDict('GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant2ConfigFeatureFlags', {
    'navigation': Required[bool],
    'socialLinks': Required[bool],
    'authority': Required[bool],
    'consultation': Required[bool],
    'learning': Required[bool],
    'services': Required[bool],
    'proof': Required[bool],
    'finalCta': Required[bool],
})
GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant2ConfigFeatureFlags.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant2Config = TypedDict('GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant2Config', {
    'theme': Required[Literal['blue', 'slate', 'monochrome']],
    'showGeneratedAt': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'featureFlags': Required[GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant2ConfigFeatureFlags],
})
GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant2Config.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant2 = TypedDict('GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant2', {
    'templateVersionId': Required[str],
    'templateId': Required[str],
    'version': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'rendererVersion': Required[Literal[1]],
    'inputContractVersion': Required[Literal[1]],
    'authoringInstructions': Required[Annotated[str, Field(max_length=4000)]],
    'createdAt': Required[str],
    'rendererKey': Required[Literal['personal_authority_v1']],
    'config': Required[GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant2Config],
})
GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant2.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant3ConfigColors = TypedDict('GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant3ConfigColors', {
    'accent': NotRequired[str],
    'background': NotRequired[str],
    'surface': NotRequired[str],
    'text': NotRequired[str],
})
GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant3ConfigColors.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant3ConfigTypography = TypedDict('GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant3ConfigTypography', {
    'display': Required[Literal['editorial-serif', 'modern-sans', 'humanist-sans']],
    'body': Required[Literal['editorial-serif', 'modern-sans', 'humanist-sans']],
})
GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant3ConfigTypography.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant3ConfigFeatureFlags = TypedDict('GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant3ConfigFeatureFlags', {
    'navigation': Required[bool],
    'socialLinks': Required[bool],
    'authority': Required[bool],
    'consultation': Required[bool],
    'learning': Required[bool],
    'services': Required[bool],
    'proof': Required[bool],
    'finalCta': Required[bool],
})
GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant3ConfigFeatureFlags.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant3Config = TypedDict('GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant3Config', {
    'theme': Required[Literal['blue', 'terracotta', 'slate', 'monochrome']],
    'showGeneratedAt': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'colors': NotRequired[GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant3ConfigColors],
    'typography': NotRequired[GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant3ConfigTypography],
    'featureFlags': Required[GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant3ConfigFeatureFlags],
})
GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant3Config.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant3 = TypedDict('GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant3', {
    'templateVersionId': Required[str],
    'templateId': Required[str],
    'version': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'rendererVersion': Required[Literal[1]],
    'inputContractVersion': Required[Literal[1]],
    'authoringInstructions': Required[Annotated[str, Field(max_length=4000)]],
    'createdAt': Required[str],
    'rendererKey': Required[Literal['personal_authority_v2']],
    'config': Required[GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant3Config],
})
GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant3.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant4ConfigFeatureFlags = TypedDict('GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant4ConfigFeatureFlags', {
    'breakingTicker': Required[bool],
    'navigation': Required[bool],
    'leadGrid': Required[bool],
    'latestNews': Required[bool],
    'categorySections': Required[bool],
    'newsletter': Required[bool],
    'pressRoom': Required[bool],
    'trustFooter': Required[bool],
})
GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant4ConfigFeatureFlags.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant4Config = TypedDict('GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant4Config', {
    'theme': Required[Literal['daily', 'journal', 'midnight']],
    'showGeneratedAt': Required[bool],
    'showBylines': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'featureFlags': Required[GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant4ConfigFeatureFlags],
})
GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant4Config.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant4 = TypedDict('GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant4', {
    'templateVersionId': Required[str],
    'templateId': Required[str],
    'version': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'rendererVersion': Required[Literal[1]],
    'inputContractVersion': Required[Literal[1]],
    'authoringInstructions': Required[Annotated[str, Field(max_length=4000)]],
    'createdAt': Required[str],
    'rendererKey': Required[Literal['newsroom_publisher_v1']],
    'config': Required[GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant4Config],
})
GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant4.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant5ConfigFeatureFlags = TypedDict('GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant5ConfigFeatureFlags', {
    'sidebarMedia': Required[bool],
    'disclosure': Required[bool],
    'stickyToc': Required[bool],
    'faq': Required[bool],
    'citation': Required[bool],
    'share': Required[bool],
    'authorCard': Required[bool],
})
GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant5ConfigFeatureFlags.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant5Config = TypedDict('GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant5Config', {
    'theme': Required[Literal['navy', 'slate', 'forest']],
    'showGeneratedAt': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'featureFlags': Required[GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant5ConfigFeatureFlags],
})
GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant5Config.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant5 = TypedDict('GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant5', {
    'templateVersionId': Required[str],
    'templateId': Required[str],
    'version': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'rendererVersion': Required[Literal[1]],
    'inputContractVersion': Required[Literal[1]],
    'authoringInstructions': Required[Annotated[str, Field(max_length=4000)]],
    'createdAt': Required[str],
    'rendererKey': Required[Literal['blog_article_v1']],
    'config': Required[GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant5Config],
})
GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant5.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetArtifactTemplateOutputVariant1Template = TypedDict('GetArtifactTemplateOutputVariant1Template', {
    'templateId': Required[str],
    'name': Required[Annotated[str, Field(min_length=1, max_length=120)]],
    'description': Required[Annotated[str, Field(max_length=500)]],
    'currentVersionId': Required[str],
    'status': Required[Literal['active', 'archived']],
    'currentVersion': NotRequired[Union[GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant1, GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant2, GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3, GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant4, GetArtifactTemplateOutputVariant1TemplateCurrentVersionVariant5]],
    'versions': NotRequired[list[Union[GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant1, GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant2, GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant3, GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant4, GetArtifactTemplateOutputVariant1TemplateVersionsItemVariant5]]],
    'createdAt': Required[str],
    'updatedAt': Required[str],
})
GetArtifactTemplateOutputVariant1Template.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class GetArtifactTemplateOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    template: Union[GetArtifactTemplateOutputVariant1Template, None] = Field(None, alias='template', description='')
    error: Union[Annotated[str, Field(min_length=1, max_length=500)], None] = Field(None, alias='error', description='')
    error_code: Union[Literal['invalid_request', 'not_found', 'conflict', 'template_archived', 'renderer_unavailable', 'artifact_unavailable', 'internal_error'], None] = Field(None, alias='errorCode', description='')
    request_id: Union[Annotated[str, Field(max_length=200)], None] = Field(None, alias='requestId', description='')


GetArtifactTemplateOutputVariant2DeliveryArtifactsItem = TypedDict('GetArtifactTemplateOutputVariant2DeliveryArtifactsItem', {
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
GetArtifactTemplateOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetArtifactTemplateOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('GetArtifactTemplateOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
GetArtifactTemplateOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetArtifactTemplateOutputVariant2Delivery = TypedDict('GetArtifactTemplateOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[GetArtifactTemplateOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[GetArtifactTemplateOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
GetArtifactTemplateOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetArtifactTemplateOutputVariant2RecoveryOperation = TypedDict('GetArtifactTemplateOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
GetArtifactTemplateOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetArtifactTemplateOutputVariant2Recovery = TypedDict('GetArtifactTemplateOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[GetArtifactTemplateOutputVariant2RecoveryOperation],
})
GetArtifactTemplateOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class GetArtifactTemplateOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: GetArtifactTemplateOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: GetArtifactTemplateOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(GetArtifactTemplateOutput).
GetArtifactTemplateOutput = Union[GetArtifactTemplateOutputVariant2, GetArtifactTemplateOutputVariant1]

_GetArtifactTemplateInputAdapter = TypeAdapter(GetArtifactTemplateInput)
_GetArtifactTemplateOutputAdapter = TypeAdapter(GetArtifactTemplateOutput)