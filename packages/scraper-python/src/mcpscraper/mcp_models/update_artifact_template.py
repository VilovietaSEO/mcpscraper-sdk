from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


UpdateArtifactTemplateInputConfigVariant1 = TypedDict('UpdateArtifactTemplateInputConfigVariant1', {
    'theme': Required[Literal['paper', 'ink', 'warm']],
    'density': Required[Literal['comfortable', 'compact']],
    'showSourceRail': Required[bool],
    'showGeneratedAt': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
})
UpdateArtifactTemplateInputConfigVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


UpdateArtifactTemplateInputConfigVariant2FeatureFlags = TypedDict('UpdateArtifactTemplateInputConfigVariant2FeatureFlags', {
    'navigation': Required[bool],
    'socialLinks': Required[bool],
    'authority': Required[bool],
    'consultation': Required[bool],
    'learning': Required[bool],
    'services': Required[bool],
    'proof': Required[bool],
    'finalCta': Required[bool],
})
UpdateArtifactTemplateInputConfigVariant2FeatureFlags.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


UpdateArtifactTemplateInputConfigVariant2 = TypedDict('UpdateArtifactTemplateInputConfigVariant2', {
    'theme': Required[Literal['blue', 'slate', 'monochrome']],
    'showGeneratedAt': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'featureFlags': Required[UpdateArtifactTemplateInputConfigVariant2FeatureFlags],
})
UpdateArtifactTemplateInputConfigVariant2.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


UpdateArtifactTemplateInputConfigVariant3Colors = TypedDict('UpdateArtifactTemplateInputConfigVariant3Colors', {
    'accent': NotRequired[str],
    'background': NotRequired[str],
    'surface': NotRequired[str],
    'text': NotRequired[str],
})
UpdateArtifactTemplateInputConfigVariant3Colors.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


UpdateArtifactTemplateInputConfigVariant3Typography = TypedDict('UpdateArtifactTemplateInputConfigVariant3Typography', {
    'display': Required[Literal['editorial-serif', 'modern-sans', 'humanist-sans']],
    'body': Required[Literal['editorial-serif', 'modern-sans', 'humanist-sans']],
})
UpdateArtifactTemplateInputConfigVariant3Typography.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


UpdateArtifactTemplateInputConfigVariant3FeatureFlags = TypedDict('UpdateArtifactTemplateInputConfigVariant3FeatureFlags', {
    'navigation': Required[bool],
    'socialLinks': Required[bool],
    'authority': Required[bool],
    'consultation': Required[bool],
    'learning': Required[bool],
    'services': Required[bool],
    'proof': Required[bool],
    'finalCta': Required[bool],
})
UpdateArtifactTemplateInputConfigVariant3FeatureFlags.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


UpdateArtifactTemplateInputConfigVariant3 = TypedDict('UpdateArtifactTemplateInputConfigVariant3', {
    'theme': Required[Literal['blue', 'terracotta', 'slate', 'monochrome']],
    'showGeneratedAt': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'colors': NotRequired[UpdateArtifactTemplateInputConfigVariant3Colors],
    'typography': NotRequired[UpdateArtifactTemplateInputConfigVariant3Typography],
    'featureFlags': Required[UpdateArtifactTemplateInputConfigVariant3FeatureFlags],
})
UpdateArtifactTemplateInputConfigVariant3.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


UpdateArtifactTemplateInputConfigVariant4FeatureFlags = TypedDict('UpdateArtifactTemplateInputConfigVariant4FeatureFlags', {
    'breakingTicker': Required[bool],
    'navigation': Required[bool],
    'leadGrid': Required[bool],
    'latestNews': Required[bool],
    'categorySections': Required[bool],
    'newsletter': Required[bool],
    'pressRoom': Required[bool],
    'trustFooter': Required[bool],
})
UpdateArtifactTemplateInputConfigVariant4FeatureFlags.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


UpdateArtifactTemplateInputConfigVariant4 = TypedDict('UpdateArtifactTemplateInputConfigVariant4', {
    'theme': Required[Literal['daily', 'journal', 'midnight']],
    'showGeneratedAt': Required[bool],
    'showBylines': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'featureFlags': Required[UpdateArtifactTemplateInputConfigVariant4FeatureFlags],
})
UpdateArtifactTemplateInputConfigVariant4.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


UpdateArtifactTemplateInputConfigVariant5FeatureFlags = TypedDict('UpdateArtifactTemplateInputConfigVariant5FeatureFlags', {
    'sidebarMedia': Required[bool],
    'disclosure': Required[bool],
    'stickyToc': Required[bool],
    'faq': Required[bool],
    'citation': Required[bool],
    'share': Required[bool],
    'authorCard': Required[bool],
})
UpdateArtifactTemplateInputConfigVariant5FeatureFlags.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


UpdateArtifactTemplateInputConfigVariant5 = TypedDict('UpdateArtifactTemplateInputConfigVariant5', {
    'theme': Required[Literal['navy', 'slate', 'forest']],
    'showGeneratedAt': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'featureFlags': Required[UpdateArtifactTemplateInputConfigVariant5FeatureFlags],
})
UpdateArtifactTemplateInputConfigVariant5.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class UpdateArtifactTemplateInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    template_id: str = Field(..., alias='templateId', description='Opaque saved-template identifier returned by an artifact-template tool.')
    name: Union[Annotated[str, Field(min_length=1, max_length=120)], None] = Field(None, alias='name', description='Human-readable name for the record being created or updated.')
    description: Union[Annotated[str, Field(max_length=500)], None] = Field(None, alias='description', description='Human-readable summary that distinguishes this record from similarly named records.')
    config: Union[Union[UpdateArtifactTemplateInputConfigVariant1, UpdateArtifactTemplateInputConfigVariant2, UpdateArtifactTemplateInputConfigVariant3, UpdateArtifactTemplateInputConfigVariant4, UpdateArtifactTemplateInputConfigVariant5], None] = Field(None, alias='config', description='Validated renderer configuration for the new immutable template version; arbitrary code is rejected.')
    authoring_instructions: Union[Annotated[str, Field(max_length=4000)], None] = Field(None, alias='authoringInstructions', description='Presentation guidance for authors using this saved template; executable prompts or code are rejected.')


UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant1Config = TypedDict('UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant1Config', {
    'theme': Required[Literal['paper', 'ink', 'warm']],
    'density': Required[Literal['comfortable', 'compact']],
    'showSourceRail': Required[bool],
    'showGeneratedAt': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
})
UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant1Config.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant1 = TypedDict('UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant1', {
    'templateVersionId': Required[str],
    'templateId': Required[str],
    'version': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'rendererVersion': Required[Literal[1]],
    'inputContractVersion': Required[Literal[1]],
    'authoringInstructions': Required[Annotated[str, Field(max_length=4000)]],
    'createdAt': Required[str],
    'rendererKey': Required[Literal['editorial_reading_room_v1']],
    'config': Required[UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant1Config],
})
UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant2ConfigFeatureFlags = TypedDict('UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant2ConfigFeatureFlags', {
    'navigation': Required[bool],
    'socialLinks': Required[bool],
    'authority': Required[bool],
    'consultation': Required[bool],
    'learning': Required[bool],
    'services': Required[bool],
    'proof': Required[bool],
    'finalCta': Required[bool],
})
UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant2ConfigFeatureFlags.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant2Config = TypedDict('UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant2Config', {
    'theme': Required[Literal['blue', 'slate', 'monochrome']],
    'showGeneratedAt': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'featureFlags': Required[UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant2ConfigFeatureFlags],
})
UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant2Config.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant2 = TypedDict('UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant2', {
    'templateVersionId': Required[str],
    'templateId': Required[str],
    'version': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'rendererVersion': Required[Literal[1]],
    'inputContractVersion': Required[Literal[1]],
    'authoringInstructions': Required[Annotated[str, Field(max_length=4000)]],
    'createdAt': Required[str],
    'rendererKey': Required[Literal['personal_authority_v1']],
    'config': Required[UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant2Config],
})
UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant2.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3ConfigColors = TypedDict('UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3ConfigColors', {
    'accent': NotRequired[str],
    'background': NotRequired[str],
    'surface': NotRequired[str],
    'text': NotRequired[str],
})
UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3ConfigColors.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3ConfigTypography = TypedDict('UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3ConfigTypography', {
    'display': Required[Literal['editorial-serif', 'modern-sans', 'humanist-sans']],
    'body': Required[Literal['editorial-serif', 'modern-sans', 'humanist-sans']],
})
UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3ConfigTypography.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3ConfigFeatureFlags = TypedDict('UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3ConfigFeatureFlags', {
    'navigation': Required[bool],
    'socialLinks': Required[bool],
    'authority': Required[bool],
    'consultation': Required[bool],
    'learning': Required[bool],
    'services': Required[bool],
    'proof': Required[bool],
    'finalCta': Required[bool],
})
UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3ConfigFeatureFlags.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3Config = TypedDict('UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3Config', {
    'theme': Required[Literal['blue', 'terracotta', 'slate', 'monochrome']],
    'showGeneratedAt': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'colors': NotRequired[UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3ConfigColors],
    'typography': NotRequired[UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3ConfigTypography],
    'featureFlags': Required[UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3ConfigFeatureFlags],
})
UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3Config.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3 = TypedDict('UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3', {
    'templateVersionId': Required[str],
    'templateId': Required[str],
    'version': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'rendererVersion': Required[Literal[1]],
    'inputContractVersion': Required[Literal[1]],
    'authoringInstructions': Required[Annotated[str, Field(max_length=4000)]],
    'createdAt': Required[str],
    'rendererKey': Required[Literal['personal_authority_v2']],
    'config': Required[UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3Config],
})
UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant4ConfigFeatureFlags = TypedDict('UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant4ConfigFeatureFlags', {
    'breakingTicker': Required[bool],
    'navigation': Required[bool],
    'leadGrid': Required[bool],
    'latestNews': Required[bool],
    'categorySections': Required[bool],
    'newsletter': Required[bool],
    'pressRoom': Required[bool],
    'trustFooter': Required[bool],
})
UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant4ConfigFeatureFlags.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant4Config = TypedDict('UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant4Config', {
    'theme': Required[Literal['daily', 'journal', 'midnight']],
    'showGeneratedAt': Required[bool],
    'showBylines': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'featureFlags': Required[UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant4ConfigFeatureFlags],
})
UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant4Config.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant4 = TypedDict('UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant4', {
    'templateVersionId': Required[str],
    'templateId': Required[str],
    'version': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'rendererVersion': Required[Literal[1]],
    'inputContractVersion': Required[Literal[1]],
    'authoringInstructions': Required[Annotated[str, Field(max_length=4000)]],
    'createdAt': Required[str],
    'rendererKey': Required[Literal['newsroom_publisher_v1']],
    'config': Required[UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant4Config],
})
UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant4.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant5ConfigFeatureFlags = TypedDict('UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant5ConfigFeatureFlags', {
    'sidebarMedia': Required[bool],
    'disclosure': Required[bool],
    'stickyToc': Required[bool],
    'faq': Required[bool],
    'citation': Required[bool],
    'share': Required[bool],
    'authorCard': Required[bool],
})
UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant5ConfigFeatureFlags.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant5Config = TypedDict('UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant5Config', {
    'theme': Required[Literal['navy', 'slate', 'forest']],
    'showGeneratedAt': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'featureFlags': Required[UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant5ConfigFeatureFlags],
})
UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant5Config.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant5 = TypedDict('UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant5', {
    'templateVersionId': Required[str],
    'templateId': Required[str],
    'version': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'rendererVersion': Required[Literal[1]],
    'inputContractVersion': Required[Literal[1]],
    'authoringInstructions': Required[Annotated[str, Field(max_length=4000)]],
    'createdAt': Required[str],
    'rendererKey': Required[Literal['blog_article_v1']],
    'config': Required[UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant5Config],
})
UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant5.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant1Config = TypedDict('UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant1Config', {
    'theme': Required[Literal['paper', 'ink', 'warm']],
    'density': Required[Literal['comfortable', 'compact']],
    'showSourceRail': Required[bool],
    'showGeneratedAt': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
})
UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant1Config.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant1 = TypedDict('UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant1', {
    'templateVersionId': Required[str],
    'templateId': Required[str],
    'version': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'rendererVersion': Required[Literal[1]],
    'inputContractVersion': Required[Literal[1]],
    'authoringInstructions': Required[Annotated[str, Field(max_length=4000)]],
    'createdAt': Required[str],
    'rendererKey': Required[Literal['editorial_reading_room_v1']],
    'config': Required[UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant1Config],
})
UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant2ConfigFeatureFlags = TypedDict('UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant2ConfigFeatureFlags', {
    'navigation': Required[bool],
    'socialLinks': Required[bool],
    'authority': Required[bool],
    'consultation': Required[bool],
    'learning': Required[bool],
    'services': Required[bool],
    'proof': Required[bool],
    'finalCta': Required[bool],
})
UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant2ConfigFeatureFlags.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant2Config = TypedDict('UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant2Config', {
    'theme': Required[Literal['blue', 'slate', 'monochrome']],
    'showGeneratedAt': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'featureFlags': Required[UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant2ConfigFeatureFlags],
})
UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant2Config.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant2 = TypedDict('UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant2', {
    'templateVersionId': Required[str],
    'templateId': Required[str],
    'version': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'rendererVersion': Required[Literal[1]],
    'inputContractVersion': Required[Literal[1]],
    'authoringInstructions': Required[Annotated[str, Field(max_length=4000)]],
    'createdAt': Required[str],
    'rendererKey': Required[Literal['personal_authority_v1']],
    'config': Required[UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant2Config],
})
UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant2.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant3ConfigColors = TypedDict('UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant3ConfigColors', {
    'accent': NotRequired[str],
    'background': NotRequired[str],
    'surface': NotRequired[str],
    'text': NotRequired[str],
})
UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant3ConfigColors.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant3ConfigTypography = TypedDict('UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant3ConfigTypography', {
    'display': Required[Literal['editorial-serif', 'modern-sans', 'humanist-sans']],
    'body': Required[Literal['editorial-serif', 'modern-sans', 'humanist-sans']],
})
UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant3ConfigTypography.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant3ConfigFeatureFlags = TypedDict('UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant3ConfigFeatureFlags', {
    'navigation': Required[bool],
    'socialLinks': Required[bool],
    'authority': Required[bool],
    'consultation': Required[bool],
    'learning': Required[bool],
    'services': Required[bool],
    'proof': Required[bool],
    'finalCta': Required[bool],
})
UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant3ConfigFeatureFlags.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant3Config = TypedDict('UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant3Config', {
    'theme': Required[Literal['blue', 'terracotta', 'slate', 'monochrome']],
    'showGeneratedAt': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'colors': NotRequired[UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant3ConfigColors],
    'typography': NotRequired[UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant3ConfigTypography],
    'featureFlags': Required[UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant3ConfigFeatureFlags],
})
UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant3Config.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant3 = TypedDict('UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant3', {
    'templateVersionId': Required[str],
    'templateId': Required[str],
    'version': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'rendererVersion': Required[Literal[1]],
    'inputContractVersion': Required[Literal[1]],
    'authoringInstructions': Required[Annotated[str, Field(max_length=4000)]],
    'createdAt': Required[str],
    'rendererKey': Required[Literal['personal_authority_v2']],
    'config': Required[UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant3Config],
})
UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant3.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant4ConfigFeatureFlags = TypedDict('UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant4ConfigFeatureFlags', {
    'breakingTicker': Required[bool],
    'navigation': Required[bool],
    'leadGrid': Required[bool],
    'latestNews': Required[bool],
    'categorySections': Required[bool],
    'newsletter': Required[bool],
    'pressRoom': Required[bool],
    'trustFooter': Required[bool],
})
UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant4ConfigFeatureFlags.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant4Config = TypedDict('UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant4Config', {
    'theme': Required[Literal['daily', 'journal', 'midnight']],
    'showGeneratedAt': Required[bool],
    'showBylines': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'featureFlags': Required[UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant4ConfigFeatureFlags],
})
UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant4Config.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant4 = TypedDict('UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant4', {
    'templateVersionId': Required[str],
    'templateId': Required[str],
    'version': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'rendererVersion': Required[Literal[1]],
    'inputContractVersion': Required[Literal[1]],
    'authoringInstructions': Required[Annotated[str, Field(max_length=4000)]],
    'createdAt': Required[str],
    'rendererKey': Required[Literal['newsroom_publisher_v1']],
    'config': Required[UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant4Config],
})
UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant4.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant5ConfigFeatureFlags = TypedDict('UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant5ConfigFeatureFlags', {
    'sidebarMedia': Required[bool],
    'disclosure': Required[bool],
    'stickyToc': Required[bool],
    'faq': Required[bool],
    'citation': Required[bool],
    'share': Required[bool],
    'authorCard': Required[bool],
})
UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant5ConfigFeatureFlags.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant5Config = TypedDict('UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant5Config', {
    'theme': Required[Literal['navy', 'slate', 'forest']],
    'showGeneratedAt': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'featureFlags': Required[UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant5ConfigFeatureFlags],
})
UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant5Config.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant5 = TypedDict('UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant5', {
    'templateVersionId': Required[str],
    'templateId': Required[str],
    'version': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'rendererVersion': Required[Literal[1]],
    'inputContractVersion': Required[Literal[1]],
    'authoringInstructions': Required[Annotated[str, Field(max_length=4000)]],
    'createdAt': Required[str],
    'rendererKey': Required[Literal['blog_article_v1']],
    'config': Required[UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant5Config],
})
UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant5.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


UpdateArtifactTemplateOutputVariant1Template = TypedDict('UpdateArtifactTemplateOutputVariant1Template', {
    'templateId': Required[str],
    'name': Required[Annotated[str, Field(min_length=1, max_length=120)]],
    'description': Required[Annotated[str, Field(max_length=500)]],
    'currentVersionId': Required[str],
    'status': Required[Literal['active', 'archived']],
    'currentVersion': NotRequired[Union[UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant1, UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant2, UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3, UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant4, UpdateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant5]],
    'versions': NotRequired[list[Union[UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant1, UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant2, UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant3, UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant4, UpdateArtifactTemplateOutputVariant1TemplateVersionsItemVariant5]]],
    'createdAt': Required[str],
    'updatedAt': Required[str],
})
UpdateArtifactTemplateOutputVariant1Template.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class UpdateArtifactTemplateOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    template: Union[UpdateArtifactTemplateOutputVariant1Template, None] = Field(None, alias='template', description='')
    error: Union[Annotated[str, Field(min_length=1, max_length=500)], None] = Field(None, alias='error', description='')
    error_code: Union[Literal['invalid_request', 'not_found', 'conflict', 'template_archived', 'renderer_unavailable', 'artifact_unavailable', 'internal_error'], None] = Field(None, alias='errorCode', description='')
    request_id: Union[Annotated[str, Field(max_length=200)], None] = Field(None, alias='requestId', description='')


UpdateArtifactTemplateOutputVariant2DeliveryArtifactsItem = TypedDict('UpdateArtifactTemplateOutputVariant2DeliveryArtifactsItem', {
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
UpdateArtifactTemplateOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


UpdateArtifactTemplateOutputVariant2DeliveryAvailableExportsItem = TypedDict('UpdateArtifactTemplateOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
UpdateArtifactTemplateOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


UpdateArtifactTemplateOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('UpdateArtifactTemplateOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
UpdateArtifactTemplateOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


UpdateArtifactTemplateOutputVariant2Delivery = TypedDict('UpdateArtifactTemplateOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[UpdateArtifactTemplateOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[UpdateArtifactTemplateOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[UpdateArtifactTemplateOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
UpdateArtifactTemplateOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


UpdateArtifactTemplateOutputVariant2RecoveryOperation = TypedDict('UpdateArtifactTemplateOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
UpdateArtifactTemplateOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


UpdateArtifactTemplateOutputVariant2Recovery = TypedDict('UpdateArtifactTemplateOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[UpdateArtifactTemplateOutputVariant2RecoveryOperation],
})
UpdateArtifactTemplateOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class UpdateArtifactTemplateOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: UpdateArtifactTemplateOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: UpdateArtifactTemplateOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(UpdateArtifactTemplateOutput).
UpdateArtifactTemplateOutput = Union[UpdateArtifactTemplateOutputVariant2, UpdateArtifactTemplateOutputVariant1]

_UpdateArtifactTemplateInputAdapter = TypeAdapter(UpdateArtifactTemplateInput)
_UpdateArtifactTemplateOutputAdapter = TypeAdapter(UpdateArtifactTemplateOutput)