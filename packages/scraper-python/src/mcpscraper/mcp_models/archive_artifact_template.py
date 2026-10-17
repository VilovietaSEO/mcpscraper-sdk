from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class ArchiveArtifactTemplateInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    template_id: str = Field(..., alias='templateId', description='Opaque saved-template identifier returned by an artifact-template tool.')
    archived: bool = Field(..., alias='archived', description='Set true to archive the record or false to restore it.')


ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant1Config = TypedDict('ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant1Config', {
    'theme': Required[Literal['paper', 'ink', 'warm']],
    'density': Required[Literal['comfortable', 'compact']],
    'showSourceRail': Required[bool],
    'showGeneratedAt': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
})
ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant1Config.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant1 = TypedDict('ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant1', {
    'templateVersionId': Required[str],
    'templateId': Required[str],
    'version': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'rendererVersion': Required[Literal[1]],
    'inputContractVersion': Required[Literal[1]],
    'authoringInstructions': Required[Annotated[str, Field(max_length=4000)]],
    'createdAt': Required[str],
    'rendererKey': Required[Literal['editorial_reading_room_v1']],
    'config': Required[ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant1Config],
})
ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant2ConfigFeatureFlags = TypedDict('ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant2ConfigFeatureFlags', {
    'navigation': Required[bool],
    'socialLinks': Required[bool],
    'authority': Required[bool],
    'consultation': Required[bool],
    'learning': Required[bool],
    'services': Required[bool],
    'proof': Required[bool],
    'finalCta': Required[bool],
})
ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant2ConfigFeatureFlags.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant2Config = TypedDict('ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant2Config', {
    'theme': Required[Literal['blue', 'slate', 'monochrome']],
    'showGeneratedAt': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'featureFlags': Required[ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant2ConfigFeatureFlags],
})
ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant2Config.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant2 = TypedDict('ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant2', {
    'templateVersionId': Required[str],
    'templateId': Required[str],
    'version': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'rendererVersion': Required[Literal[1]],
    'inputContractVersion': Required[Literal[1]],
    'authoringInstructions': Required[Annotated[str, Field(max_length=4000)]],
    'createdAt': Required[str],
    'rendererKey': Required[Literal['personal_authority_v1']],
    'config': Required[ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant2Config],
})
ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant2.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3ConfigColors = TypedDict('ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3ConfigColors', {
    'accent': NotRequired[str],
    'background': NotRequired[str],
    'surface': NotRequired[str],
    'text': NotRequired[str],
})
ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3ConfigColors.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3ConfigTypography = TypedDict('ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3ConfigTypography', {
    'display': Required[Literal['editorial-serif', 'modern-sans', 'humanist-sans']],
    'body': Required[Literal['editorial-serif', 'modern-sans', 'humanist-sans']],
})
ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3ConfigTypography.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3ConfigFeatureFlags = TypedDict('ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3ConfigFeatureFlags', {
    'navigation': Required[bool],
    'socialLinks': Required[bool],
    'authority': Required[bool],
    'consultation': Required[bool],
    'learning': Required[bool],
    'services': Required[bool],
    'proof': Required[bool],
    'finalCta': Required[bool],
})
ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3ConfigFeatureFlags.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3Config = TypedDict('ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3Config', {
    'theme': Required[Literal['blue', 'terracotta', 'slate', 'monochrome']],
    'showGeneratedAt': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'colors': NotRequired[ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3ConfigColors],
    'typography': NotRequired[ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3ConfigTypography],
    'featureFlags': Required[ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3ConfigFeatureFlags],
})
ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3Config.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3 = TypedDict('ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3', {
    'templateVersionId': Required[str],
    'templateId': Required[str],
    'version': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'rendererVersion': Required[Literal[1]],
    'inputContractVersion': Required[Literal[1]],
    'authoringInstructions': Required[Annotated[str, Field(max_length=4000)]],
    'createdAt': Required[str],
    'rendererKey': Required[Literal['personal_authority_v2']],
    'config': Required[ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3Config],
})
ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant4ConfigFeatureFlags = TypedDict('ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant4ConfigFeatureFlags', {
    'breakingTicker': Required[bool],
    'navigation': Required[bool],
    'leadGrid': Required[bool],
    'latestNews': Required[bool],
    'categorySections': Required[bool],
    'newsletter': Required[bool],
    'pressRoom': Required[bool],
    'trustFooter': Required[bool],
})
ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant4ConfigFeatureFlags.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant4Config = TypedDict('ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant4Config', {
    'theme': Required[Literal['daily', 'journal', 'midnight']],
    'showGeneratedAt': Required[bool],
    'showBylines': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'featureFlags': Required[ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant4ConfigFeatureFlags],
})
ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant4Config.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant4 = TypedDict('ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant4', {
    'templateVersionId': Required[str],
    'templateId': Required[str],
    'version': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'rendererVersion': Required[Literal[1]],
    'inputContractVersion': Required[Literal[1]],
    'authoringInstructions': Required[Annotated[str, Field(max_length=4000)]],
    'createdAt': Required[str],
    'rendererKey': Required[Literal['newsroom_publisher_v1']],
    'config': Required[ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant4Config],
})
ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant4.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant5ConfigFeatureFlags = TypedDict('ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant5ConfigFeatureFlags', {
    'sidebarMedia': Required[bool],
    'disclosure': Required[bool],
    'stickyToc': Required[bool],
    'faq': Required[bool],
    'citation': Required[bool],
    'share': Required[bool],
    'authorCard': Required[bool],
})
ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant5ConfigFeatureFlags.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant5Config = TypedDict('ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant5Config', {
    'theme': Required[Literal['navy', 'slate', 'forest']],
    'showGeneratedAt': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'featureFlags': Required[ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant5ConfigFeatureFlags],
})
ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant5Config.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant5 = TypedDict('ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant5', {
    'templateVersionId': Required[str],
    'templateId': Required[str],
    'version': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'rendererVersion': Required[Literal[1]],
    'inputContractVersion': Required[Literal[1]],
    'authoringInstructions': Required[Annotated[str, Field(max_length=4000)]],
    'createdAt': Required[str],
    'rendererKey': Required[Literal['blog_article_v1']],
    'config': Required[ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant5Config],
})
ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant5.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant1Config = TypedDict('ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant1Config', {
    'theme': Required[Literal['paper', 'ink', 'warm']],
    'density': Required[Literal['comfortable', 'compact']],
    'showSourceRail': Required[bool],
    'showGeneratedAt': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
})
ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant1Config.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant1 = TypedDict('ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant1', {
    'templateVersionId': Required[str],
    'templateId': Required[str],
    'version': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'rendererVersion': Required[Literal[1]],
    'inputContractVersion': Required[Literal[1]],
    'authoringInstructions': Required[Annotated[str, Field(max_length=4000)]],
    'createdAt': Required[str],
    'rendererKey': Required[Literal['editorial_reading_room_v1']],
    'config': Required[ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant1Config],
})
ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant2ConfigFeatureFlags = TypedDict('ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant2ConfigFeatureFlags', {
    'navigation': Required[bool],
    'socialLinks': Required[bool],
    'authority': Required[bool],
    'consultation': Required[bool],
    'learning': Required[bool],
    'services': Required[bool],
    'proof': Required[bool],
    'finalCta': Required[bool],
})
ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant2ConfigFeatureFlags.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant2Config = TypedDict('ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant2Config', {
    'theme': Required[Literal['blue', 'slate', 'monochrome']],
    'showGeneratedAt': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'featureFlags': Required[ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant2ConfigFeatureFlags],
})
ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant2Config.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant2 = TypedDict('ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant2', {
    'templateVersionId': Required[str],
    'templateId': Required[str],
    'version': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'rendererVersion': Required[Literal[1]],
    'inputContractVersion': Required[Literal[1]],
    'authoringInstructions': Required[Annotated[str, Field(max_length=4000)]],
    'createdAt': Required[str],
    'rendererKey': Required[Literal['personal_authority_v1']],
    'config': Required[ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant2Config],
})
ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant2.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant3ConfigColors = TypedDict('ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant3ConfigColors', {
    'accent': NotRequired[str],
    'background': NotRequired[str],
    'surface': NotRequired[str],
    'text': NotRequired[str],
})
ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant3ConfigColors.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant3ConfigTypography = TypedDict('ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant3ConfigTypography', {
    'display': Required[Literal['editorial-serif', 'modern-sans', 'humanist-sans']],
    'body': Required[Literal['editorial-serif', 'modern-sans', 'humanist-sans']],
})
ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant3ConfigTypography.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant3ConfigFeatureFlags = TypedDict('ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant3ConfigFeatureFlags', {
    'navigation': Required[bool],
    'socialLinks': Required[bool],
    'authority': Required[bool],
    'consultation': Required[bool],
    'learning': Required[bool],
    'services': Required[bool],
    'proof': Required[bool],
    'finalCta': Required[bool],
})
ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant3ConfigFeatureFlags.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant3Config = TypedDict('ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant3Config', {
    'theme': Required[Literal['blue', 'terracotta', 'slate', 'monochrome']],
    'showGeneratedAt': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'colors': NotRequired[ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant3ConfigColors],
    'typography': NotRequired[ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant3ConfigTypography],
    'featureFlags': Required[ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant3ConfigFeatureFlags],
})
ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant3Config.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant3 = TypedDict('ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant3', {
    'templateVersionId': Required[str],
    'templateId': Required[str],
    'version': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'rendererVersion': Required[Literal[1]],
    'inputContractVersion': Required[Literal[1]],
    'authoringInstructions': Required[Annotated[str, Field(max_length=4000)]],
    'createdAt': Required[str],
    'rendererKey': Required[Literal['personal_authority_v2']],
    'config': Required[ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant3Config],
})
ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant3.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant4ConfigFeatureFlags = TypedDict('ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant4ConfigFeatureFlags', {
    'breakingTicker': Required[bool],
    'navigation': Required[bool],
    'leadGrid': Required[bool],
    'latestNews': Required[bool],
    'categorySections': Required[bool],
    'newsletter': Required[bool],
    'pressRoom': Required[bool],
    'trustFooter': Required[bool],
})
ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant4ConfigFeatureFlags.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant4Config = TypedDict('ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant4Config', {
    'theme': Required[Literal['daily', 'journal', 'midnight']],
    'showGeneratedAt': Required[bool],
    'showBylines': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'featureFlags': Required[ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant4ConfigFeatureFlags],
})
ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant4Config.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant4 = TypedDict('ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant4', {
    'templateVersionId': Required[str],
    'templateId': Required[str],
    'version': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'rendererVersion': Required[Literal[1]],
    'inputContractVersion': Required[Literal[1]],
    'authoringInstructions': Required[Annotated[str, Field(max_length=4000)]],
    'createdAt': Required[str],
    'rendererKey': Required[Literal['newsroom_publisher_v1']],
    'config': Required[ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant4Config],
})
ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant4.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant5ConfigFeatureFlags = TypedDict('ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant5ConfigFeatureFlags', {
    'sidebarMedia': Required[bool],
    'disclosure': Required[bool],
    'stickyToc': Required[bool],
    'faq': Required[bool],
    'citation': Required[bool],
    'share': Required[bool],
    'authorCard': Required[bool],
})
ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant5ConfigFeatureFlags.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant5Config = TypedDict('ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant5Config', {
    'theme': Required[Literal['navy', 'slate', 'forest']],
    'showGeneratedAt': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'featureFlags': Required[ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant5ConfigFeatureFlags],
})
ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant5Config.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant5 = TypedDict('ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant5', {
    'templateVersionId': Required[str],
    'templateId': Required[str],
    'version': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'rendererVersion': Required[Literal[1]],
    'inputContractVersion': Required[Literal[1]],
    'authoringInstructions': Required[Annotated[str, Field(max_length=4000)]],
    'createdAt': Required[str],
    'rendererKey': Required[Literal['blog_article_v1']],
    'config': Required[ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant5Config],
})
ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant5.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ArchiveArtifactTemplateOutputVariant1Template = TypedDict('ArchiveArtifactTemplateOutputVariant1Template', {
    'templateId': Required[str],
    'name': Required[Annotated[str, Field(min_length=1, max_length=120)]],
    'description': Required[Annotated[str, Field(max_length=500)]],
    'currentVersionId': Required[str],
    'status': Required[Literal['active', 'archived']],
    'currentVersion': NotRequired[Union[ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant1, ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant2, ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3, ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant4, ArchiveArtifactTemplateOutputVariant1TemplateCurrentVersionVariant5]],
    'versions': NotRequired[list[Union[ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant1, ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant2, ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant3, ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant4, ArchiveArtifactTemplateOutputVariant1TemplateVersionsItemVariant5]]],
    'createdAt': Required[str],
    'updatedAt': Required[str],
})
ArchiveArtifactTemplateOutputVariant1Template.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ArchiveArtifactTemplateOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    template: Union[ArchiveArtifactTemplateOutputVariant1Template, None] = Field(None, alias='template', description='')
    error: Union[Annotated[str, Field(min_length=1, max_length=500)], None] = Field(None, alias='error', description='')
    error_code: Union[Literal['invalid_request', 'not_found', 'conflict', 'template_archived', 'renderer_unavailable', 'artifact_unavailable', 'internal_error'], None] = Field(None, alias='errorCode', description='')
    request_id: Union[Annotated[str, Field(max_length=200)], None] = Field(None, alias='requestId', description='')


ArchiveArtifactTemplateOutputVariant2DeliveryArtifactsItem = TypedDict('ArchiveArtifactTemplateOutputVariant2DeliveryArtifactsItem', {
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
ArchiveArtifactTemplateOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ArchiveArtifactTemplateOutputVariant2DeliveryAvailableExportsItem = TypedDict('ArchiveArtifactTemplateOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
ArchiveArtifactTemplateOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ArchiveArtifactTemplateOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('ArchiveArtifactTemplateOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
ArchiveArtifactTemplateOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ArchiveArtifactTemplateOutputVariant2Delivery = TypedDict('ArchiveArtifactTemplateOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[ArchiveArtifactTemplateOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[ArchiveArtifactTemplateOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[ArchiveArtifactTemplateOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
ArchiveArtifactTemplateOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ArchiveArtifactTemplateOutputVariant2RecoveryOperation = TypedDict('ArchiveArtifactTemplateOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
ArchiveArtifactTemplateOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ArchiveArtifactTemplateOutputVariant2Recovery = TypedDict('ArchiveArtifactTemplateOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[ArchiveArtifactTemplateOutputVariant2RecoveryOperation],
})
ArchiveArtifactTemplateOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ArchiveArtifactTemplateOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: ArchiveArtifactTemplateOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: ArchiveArtifactTemplateOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(ArchiveArtifactTemplateOutput).
ArchiveArtifactTemplateOutput = Union[ArchiveArtifactTemplateOutputVariant2, ArchiveArtifactTemplateOutputVariant1]

_ArchiveArtifactTemplateInputAdapter = TypeAdapter(ArchiveArtifactTemplateInput)
_ArchiveArtifactTemplateOutputAdapter = TypeAdapter(ArchiveArtifactTemplateOutput)