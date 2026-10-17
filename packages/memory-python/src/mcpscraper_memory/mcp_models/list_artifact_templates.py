from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class ListArtifactTemplatesInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    status: Union[Literal['active', 'archived', 'all'], None] = Field(None, alias='status', description='Lifecycle status used to filter or update the selected records.')
    query: Union[Annotated[str, Field(min_length=1, max_length=120)], None] = Field(None, alias='query', description='Optional case-insensitive search text for preset and saved-template names, descriptions, renderer keys, and authoring guidance.')
    preset_key: Union[Literal['editorial_reading_room_v1', 'personal_authority_v1', 'personal_authority_v2', 'newsroom_publisher_v1', 'blog_article_v1'], None] = Field(None, alias='presetKey', description='Optional renderer-family filter. Saved templates are matched through their current immutable version.')


ListArtifactTemplatesOutputVariant1PresetsItemFeatureFlagsItem = TypedDict('ListArtifactTemplatesOutputVariant1PresetsItemFeatureFlagsItem', {
    'key': Required[Annotated[str, Field(min_length=1)]],
    'label': Required[Annotated[str, Field(min_length=1)]],
    'description': Required[Annotated[str, Field(min_length=1)]],
})
ListArtifactTemplatesOutputVariant1PresetsItemFeatureFlagsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListArtifactTemplatesOutputVariant1PresetsItemDefaultConfigVariant1 = TypedDict('ListArtifactTemplatesOutputVariant1PresetsItemDefaultConfigVariant1', {
    'theme': Required[Literal['paper', 'ink', 'warm']],
    'density': Required[Literal['comfortable', 'compact']],
    'showSourceRail': Required[bool],
    'showGeneratedAt': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
})
ListArtifactTemplatesOutputVariant1PresetsItemDefaultConfigVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListArtifactTemplatesOutputVariant1PresetsItemDefaultConfigVariant2FeatureFlags = TypedDict('ListArtifactTemplatesOutputVariant1PresetsItemDefaultConfigVariant2FeatureFlags', {
    'navigation': Required[bool],
    'socialLinks': Required[bool],
    'authority': Required[bool],
    'consultation': Required[bool],
    'learning': Required[bool],
    'services': Required[bool],
    'proof': Required[bool],
    'finalCta': Required[bool],
})
ListArtifactTemplatesOutputVariant1PresetsItemDefaultConfigVariant2FeatureFlags.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListArtifactTemplatesOutputVariant1PresetsItemDefaultConfigVariant2 = TypedDict('ListArtifactTemplatesOutputVariant1PresetsItemDefaultConfigVariant2', {
    'theme': Required[Literal['blue', 'slate', 'monochrome']],
    'showGeneratedAt': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'featureFlags': Required[ListArtifactTemplatesOutputVariant1PresetsItemDefaultConfigVariant2FeatureFlags],
})
ListArtifactTemplatesOutputVariant1PresetsItemDefaultConfigVariant2.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListArtifactTemplatesOutputVariant1PresetsItemDefaultConfigVariant3Colors = TypedDict('ListArtifactTemplatesOutputVariant1PresetsItemDefaultConfigVariant3Colors', {
    'accent': NotRequired[str],
    'background': NotRequired[str],
    'surface': NotRequired[str],
    'text': NotRequired[str],
})
ListArtifactTemplatesOutputVariant1PresetsItemDefaultConfigVariant3Colors.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListArtifactTemplatesOutputVariant1PresetsItemDefaultConfigVariant3Typography = TypedDict('ListArtifactTemplatesOutputVariant1PresetsItemDefaultConfigVariant3Typography', {
    'display': Required[Literal['editorial-serif', 'modern-sans', 'humanist-sans']],
    'body': Required[Literal['editorial-serif', 'modern-sans', 'humanist-sans']],
})
ListArtifactTemplatesOutputVariant1PresetsItemDefaultConfigVariant3Typography.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListArtifactTemplatesOutputVariant1PresetsItemDefaultConfigVariant3FeatureFlags = TypedDict('ListArtifactTemplatesOutputVariant1PresetsItemDefaultConfigVariant3FeatureFlags', {
    'navigation': Required[bool],
    'socialLinks': Required[bool],
    'authority': Required[bool],
    'consultation': Required[bool],
    'learning': Required[bool],
    'services': Required[bool],
    'proof': Required[bool],
    'finalCta': Required[bool],
})
ListArtifactTemplatesOutputVariant1PresetsItemDefaultConfigVariant3FeatureFlags.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListArtifactTemplatesOutputVariant1PresetsItemDefaultConfigVariant3 = TypedDict('ListArtifactTemplatesOutputVariant1PresetsItemDefaultConfigVariant3', {
    'theme': Required[Literal['blue', 'terracotta', 'slate', 'monochrome']],
    'showGeneratedAt': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'colors': NotRequired[ListArtifactTemplatesOutputVariant1PresetsItemDefaultConfigVariant3Colors],
    'typography': NotRequired[ListArtifactTemplatesOutputVariant1PresetsItemDefaultConfigVariant3Typography],
    'featureFlags': Required[ListArtifactTemplatesOutputVariant1PresetsItemDefaultConfigVariant3FeatureFlags],
})
ListArtifactTemplatesOutputVariant1PresetsItemDefaultConfigVariant3.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListArtifactTemplatesOutputVariant1PresetsItemDefaultConfigVariant4FeatureFlags = TypedDict('ListArtifactTemplatesOutputVariant1PresetsItemDefaultConfigVariant4FeatureFlags', {
    'breakingTicker': Required[bool],
    'navigation': Required[bool],
    'leadGrid': Required[bool],
    'latestNews': Required[bool],
    'categorySections': Required[bool],
    'newsletter': Required[bool],
    'pressRoom': Required[bool],
    'trustFooter': Required[bool],
})
ListArtifactTemplatesOutputVariant1PresetsItemDefaultConfigVariant4FeatureFlags.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListArtifactTemplatesOutputVariant1PresetsItemDefaultConfigVariant4 = TypedDict('ListArtifactTemplatesOutputVariant1PresetsItemDefaultConfigVariant4', {
    'theme': Required[Literal['daily', 'journal', 'midnight']],
    'showGeneratedAt': Required[bool],
    'showBylines': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'featureFlags': Required[ListArtifactTemplatesOutputVariant1PresetsItemDefaultConfigVariant4FeatureFlags],
})
ListArtifactTemplatesOutputVariant1PresetsItemDefaultConfigVariant4.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListArtifactTemplatesOutputVariant1PresetsItemDefaultConfigVariant5FeatureFlags = TypedDict('ListArtifactTemplatesOutputVariant1PresetsItemDefaultConfigVariant5FeatureFlags', {
    'sidebarMedia': Required[bool],
    'disclosure': Required[bool],
    'stickyToc': Required[bool],
    'faq': Required[bool],
    'citation': Required[bool],
    'share': Required[bool],
    'authorCard': Required[bool],
})
ListArtifactTemplatesOutputVariant1PresetsItemDefaultConfigVariant5FeatureFlags.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListArtifactTemplatesOutputVariant1PresetsItemDefaultConfigVariant5 = TypedDict('ListArtifactTemplatesOutputVariant1PresetsItemDefaultConfigVariant5', {
    'theme': Required[Literal['navy', 'slate', 'forest']],
    'showGeneratedAt': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'featureFlags': Required[ListArtifactTemplatesOutputVariant1PresetsItemDefaultConfigVariant5FeatureFlags],
})
ListArtifactTemplatesOutputVariant1PresetsItemDefaultConfigVariant5.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListArtifactTemplatesOutputVariant1PresetsItem = TypedDict('ListArtifactTemplatesOutputVariant1PresetsItem', {
    'presetKey': Required[Literal['editorial_reading_room_v1', 'personal_authority_v1', 'personal_authority_v2', 'newsroom_publisher_v1', 'blog_article_v1']],
    'name': Required[str],
    'description': Required[str],
    'mark': Required[Annotated[str, Field(min_length=1, max_length=4)]],
    'featureFlags': Required[list[ListArtifactTemplatesOutputVariant1PresetsItemFeatureFlagsItem]],
    'defaultConfig': Required[Union[ListArtifactTemplatesOutputVariant1PresetsItemDefaultConfigVariant1, ListArtifactTemplatesOutputVariant1PresetsItemDefaultConfigVariant2, ListArtifactTemplatesOutputVariant1PresetsItemDefaultConfigVariant3, ListArtifactTemplatesOutputVariant1PresetsItemDefaultConfigVariant4, ListArtifactTemplatesOutputVariant1PresetsItemDefaultConfigVariant5]],
})
ListArtifactTemplatesOutputVariant1PresetsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant1Config = TypedDict('ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant1Config', {
    'theme': Required[Literal['paper', 'ink', 'warm']],
    'density': Required[Literal['comfortable', 'compact']],
    'showSourceRail': Required[bool],
    'showGeneratedAt': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
})
ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant1Config.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant1 = TypedDict('ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant1', {
    'templateVersionId': Required[str],
    'templateId': Required[str],
    'version': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'rendererVersion': Required[Literal[1]],
    'inputContractVersion': Required[Literal[1]],
    'authoringInstructions': Required[Annotated[str, Field(max_length=4000)]],
    'createdAt': Required[str],
    'rendererKey': Required[Literal['editorial_reading_room_v1']],
    'config': Required[ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant1Config],
})
ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant2ConfigFeatureFlags = TypedDict('ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant2ConfigFeatureFlags', {
    'navigation': Required[bool],
    'socialLinks': Required[bool],
    'authority': Required[bool],
    'consultation': Required[bool],
    'learning': Required[bool],
    'services': Required[bool],
    'proof': Required[bool],
    'finalCta': Required[bool],
})
ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant2ConfigFeatureFlags.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant2Config = TypedDict('ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant2Config', {
    'theme': Required[Literal['blue', 'slate', 'monochrome']],
    'showGeneratedAt': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'featureFlags': Required[ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant2ConfigFeatureFlags],
})
ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant2Config.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant2 = TypedDict('ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant2', {
    'templateVersionId': Required[str],
    'templateId': Required[str],
    'version': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'rendererVersion': Required[Literal[1]],
    'inputContractVersion': Required[Literal[1]],
    'authoringInstructions': Required[Annotated[str, Field(max_length=4000)]],
    'createdAt': Required[str],
    'rendererKey': Required[Literal['personal_authority_v1']],
    'config': Required[ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant2Config],
})
ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant2.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant3ConfigColors = TypedDict('ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant3ConfigColors', {
    'accent': NotRequired[str],
    'background': NotRequired[str],
    'surface': NotRequired[str],
    'text': NotRequired[str],
})
ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant3ConfigColors.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant3ConfigTypography = TypedDict('ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant3ConfigTypography', {
    'display': Required[Literal['editorial-serif', 'modern-sans', 'humanist-sans']],
    'body': Required[Literal['editorial-serif', 'modern-sans', 'humanist-sans']],
})
ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant3ConfigTypography.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant3ConfigFeatureFlags = TypedDict('ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant3ConfigFeatureFlags', {
    'navigation': Required[bool],
    'socialLinks': Required[bool],
    'authority': Required[bool],
    'consultation': Required[bool],
    'learning': Required[bool],
    'services': Required[bool],
    'proof': Required[bool],
    'finalCta': Required[bool],
})
ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant3ConfigFeatureFlags.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant3Config = TypedDict('ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant3Config', {
    'theme': Required[Literal['blue', 'terracotta', 'slate', 'monochrome']],
    'showGeneratedAt': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'colors': NotRequired[ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant3ConfigColors],
    'typography': NotRequired[ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant3ConfigTypography],
    'featureFlags': Required[ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant3ConfigFeatureFlags],
})
ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant3Config.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant3 = TypedDict('ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant3', {
    'templateVersionId': Required[str],
    'templateId': Required[str],
    'version': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'rendererVersion': Required[Literal[1]],
    'inputContractVersion': Required[Literal[1]],
    'authoringInstructions': Required[Annotated[str, Field(max_length=4000)]],
    'createdAt': Required[str],
    'rendererKey': Required[Literal['personal_authority_v2']],
    'config': Required[ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant3Config],
})
ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant3.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant4ConfigFeatureFlags = TypedDict('ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant4ConfigFeatureFlags', {
    'breakingTicker': Required[bool],
    'navigation': Required[bool],
    'leadGrid': Required[bool],
    'latestNews': Required[bool],
    'categorySections': Required[bool],
    'newsletter': Required[bool],
    'pressRoom': Required[bool],
    'trustFooter': Required[bool],
})
ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant4ConfigFeatureFlags.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant4Config = TypedDict('ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant4Config', {
    'theme': Required[Literal['daily', 'journal', 'midnight']],
    'showGeneratedAt': Required[bool],
    'showBylines': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'featureFlags': Required[ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant4ConfigFeatureFlags],
})
ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant4Config.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant4 = TypedDict('ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant4', {
    'templateVersionId': Required[str],
    'templateId': Required[str],
    'version': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'rendererVersion': Required[Literal[1]],
    'inputContractVersion': Required[Literal[1]],
    'authoringInstructions': Required[Annotated[str, Field(max_length=4000)]],
    'createdAt': Required[str],
    'rendererKey': Required[Literal['newsroom_publisher_v1']],
    'config': Required[ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant4Config],
})
ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant4.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant5ConfigFeatureFlags = TypedDict('ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant5ConfigFeatureFlags', {
    'sidebarMedia': Required[bool],
    'disclosure': Required[bool],
    'stickyToc': Required[bool],
    'faq': Required[bool],
    'citation': Required[bool],
    'share': Required[bool],
    'authorCard': Required[bool],
})
ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant5ConfigFeatureFlags.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant5Config = TypedDict('ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant5Config', {
    'theme': Required[Literal['navy', 'slate', 'forest']],
    'showGeneratedAt': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'featureFlags': Required[ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant5ConfigFeatureFlags],
})
ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant5Config.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant5 = TypedDict('ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant5', {
    'templateVersionId': Required[str],
    'templateId': Required[str],
    'version': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'rendererVersion': Required[Literal[1]],
    'inputContractVersion': Required[Literal[1]],
    'authoringInstructions': Required[Annotated[str, Field(max_length=4000)]],
    'createdAt': Required[str],
    'rendererKey': Required[Literal['blog_article_v1']],
    'config': Required[ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant5Config],
})
ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant5.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant1Config = TypedDict('ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant1Config', {
    'theme': Required[Literal['paper', 'ink', 'warm']],
    'density': Required[Literal['comfortable', 'compact']],
    'showSourceRail': Required[bool],
    'showGeneratedAt': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
})
ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant1Config.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant1 = TypedDict('ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant1', {
    'templateVersionId': Required[str],
    'templateId': Required[str],
    'version': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'rendererVersion': Required[Literal[1]],
    'inputContractVersion': Required[Literal[1]],
    'authoringInstructions': Required[Annotated[str, Field(max_length=4000)]],
    'createdAt': Required[str],
    'rendererKey': Required[Literal['editorial_reading_room_v1']],
    'config': Required[ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant1Config],
})
ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant2ConfigFeatureFlags = TypedDict('ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant2ConfigFeatureFlags', {
    'navigation': Required[bool],
    'socialLinks': Required[bool],
    'authority': Required[bool],
    'consultation': Required[bool],
    'learning': Required[bool],
    'services': Required[bool],
    'proof': Required[bool],
    'finalCta': Required[bool],
})
ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant2ConfigFeatureFlags.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant2Config = TypedDict('ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant2Config', {
    'theme': Required[Literal['blue', 'slate', 'monochrome']],
    'showGeneratedAt': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'featureFlags': Required[ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant2ConfigFeatureFlags],
})
ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant2Config.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant2 = TypedDict('ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant2', {
    'templateVersionId': Required[str],
    'templateId': Required[str],
    'version': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'rendererVersion': Required[Literal[1]],
    'inputContractVersion': Required[Literal[1]],
    'authoringInstructions': Required[Annotated[str, Field(max_length=4000)]],
    'createdAt': Required[str],
    'rendererKey': Required[Literal['personal_authority_v1']],
    'config': Required[ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant2Config],
})
ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant2.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant3ConfigColors = TypedDict('ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant3ConfigColors', {
    'accent': NotRequired[str],
    'background': NotRequired[str],
    'surface': NotRequired[str],
    'text': NotRequired[str],
})
ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant3ConfigColors.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant3ConfigTypography = TypedDict('ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant3ConfigTypography', {
    'display': Required[Literal['editorial-serif', 'modern-sans', 'humanist-sans']],
    'body': Required[Literal['editorial-serif', 'modern-sans', 'humanist-sans']],
})
ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant3ConfigTypography.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant3ConfigFeatureFlags = TypedDict('ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant3ConfigFeatureFlags', {
    'navigation': Required[bool],
    'socialLinks': Required[bool],
    'authority': Required[bool],
    'consultation': Required[bool],
    'learning': Required[bool],
    'services': Required[bool],
    'proof': Required[bool],
    'finalCta': Required[bool],
})
ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant3ConfigFeatureFlags.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant3Config = TypedDict('ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant3Config', {
    'theme': Required[Literal['blue', 'terracotta', 'slate', 'monochrome']],
    'showGeneratedAt': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'colors': NotRequired[ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant3ConfigColors],
    'typography': NotRequired[ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant3ConfigTypography],
    'featureFlags': Required[ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant3ConfigFeatureFlags],
})
ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant3Config.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant3 = TypedDict('ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant3', {
    'templateVersionId': Required[str],
    'templateId': Required[str],
    'version': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'rendererVersion': Required[Literal[1]],
    'inputContractVersion': Required[Literal[1]],
    'authoringInstructions': Required[Annotated[str, Field(max_length=4000)]],
    'createdAt': Required[str],
    'rendererKey': Required[Literal['personal_authority_v2']],
    'config': Required[ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant3Config],
})
ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant3.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant4ConfigFeatureFlags = TypedDict('ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant4ConfigFeatureFlags', {
    'breakingTicker': Required[bool],
    'navigation': Required[bool],
    'leadGrid': Required[bool],
    'latestNews': Required[bool],
    'categorySections': Required[bool],
    'newsletter': Required[bool],
    'pressRoom': Required[bool],
    'trustFooter': Required[bool],
})
ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant4ConfigFeatureFlags.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant4Config = TypedDict('ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant4Config', {
    'theme': Required[Literal['daily', 'journal', 'midnight']],
    'showGeneratedAt': Required[bool],
    'showBylines': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'featureFlags': Required[ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant4ConfigFeatureFlags],
})
ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant4Config.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant4 = TypedDict('ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant4', {
    'templateVersionId': Required[str],
    'templateId': Required[str],
    'version': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'rendererVersion': Required[Literal[1]],
    'inputContractVersion': Required[Literal[1]],
    'authoringInstructions': Required[Annotated[str, Field(max_length=4000)]],
    'createdAt': Required[str],
    'rendererKey': Required[Literal['newsroom_publisher_v1']],
    'config': Required[ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant4Config],
})
ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant4.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant5ConfigFeatureFlags = TypedDict('ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant5ConfigFeatureFlags', {
    'sidebarMedia': Required[bool],
    'disclosure': Required[bool],
    'stickyToc': Required[bool],
    'faq': Required[bool],
    'citation': Required[bool],
    'share': Required[bool],
    'authorCard': Required[bool],
})
ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant5ConfigFeatureFlags.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant5Config = TypedDict('ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant5Config', {
    'theme': Required[Literal['navy', 'slate', 'forest']],
    'showGeneratedAt': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'featureFlags': Required[ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant5ConfigFeatureFlags],
})
ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant5Config.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant5 = TypedDict('ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant5', {
    'templateVersionId': Required[str],
    'templateId': Required[str],
    'version': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'rendererVersion': Required[Literal[1]],
    'inputContractVersion': Required[Literal[1]],
    'authoringInstructions': Required[Annotated[str, Field(max_length=4000)]],
    'createdAt': Required[str],
    'rendererKey': Required[Literal['blog_article_v1']],
    'config': Required[ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant5Config],
})
ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant5.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListArtifactTemplatesOutputVariant1TemplatesItem = TypedDict('ListArtifactTemplatesOutputVariant1TemplatesItem', {
    'templateId': Required[str],
    'name': Required[Annotated[str, Field(min_length=1, max_length=120)]],
    'description': Required[Annotated[str, Field(max_length=500)]],
    'currentVersionId': Required[str],
    'status': Required[Literal['active', 'archived']],
    'currentVersion': NotRequired[Union[ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant1, ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant2, ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant3, ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant4, ListArtifactTemplatesOutputVariant1TemplatesItemCurrentVersionVariant5]],
    'versions': NotRequired[list[Union[ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant1, ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant2, ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant3, ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant4, ListArtifactTemplatesOutputVariant1TemplatesItemVersionsItemVariant5]]],
    'createdAt': Required[str],
    'updatedAt': Required[str],
})
ListArtifactTemplatesOutputVariant1TemplatesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ListArtifactTemplatesOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    presets: Union[list[ListArtifactTemplatesOutputVariant1PresetsItem], None] = Field(None, alias='presets', description='')
    templates: Union[list[ListArtifactTemplatesOutputVariant1TemplatesItem], None] = Field(None, alias='templates', description='')
    error: Union[Annotated[str, Field(min_length=1, max_length=500)], None] = Field(None, alias='error', description='')
    error_code: Union[Literal['invalid_request', 'not_found', 'conflict', 'template_archived', 'renderer_unavailable', 'artifact_unavailable', 'internal_error'], None] = Field(None, alias='errorCode', description='')
    request_id: Union[Annotated[str, Field(max_length=200)], None] = Field(None, alias='requestId', description='')


ListArtifactTemplatesOutputVariant2DeliveryArtifactsItem = TypedDict('ListArtifactTemplatesOutputVariant2DeliveryArtifactsItem', {
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
ListArtifactTemplatesOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListArtifactTemplatesOutputVariant2DeliveryAvailableExportsItem = TypedDict('ListArtifactTemplatesOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
ListArtifactTemplatesOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListArtifactTemplatesOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('ListArtifactTemplatesOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
ListArtifactTemplatesOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListArtifactTemplatesOutputVariant2Delivery = TypedDict('ListArtifactTemplatesOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[ListArtifactTemplatesOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[ListArtifactTemplatesOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[ListArtifactTemplatesOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
ListArtifactTemplatesOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListArtifactTemplatesOutputVariant2RecoveryOperation = TypedDict('ListArtifactTemplatesOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
ListArtifactTemplatesOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListArtifactTemplatesOutputVariant2Recovery = TypedDict('ListArtifactTemplatesOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[ListArtifactTemplatesOutputVariant2RecoveryOperation],
})
ListArtifactTemplatesOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ListArtifactTemplatesOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: ListArtifactTemplatesOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: ListArtifactTemplatesOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(ListArtifactTemplatesOutput).
ListArtifactTemplatesOutput = Union[ListArtifactTemplatesOutputVariant2, ListArtifactTemplatesOutputVariant1]

_ListArtifactTemplatesInputAdapter = TypeAdapter(ListArtifactTemplatesInput)
_ListArtifactTemplatesOutputAdapter = TypeAdapter(ListArtifactTemplatesOutput)