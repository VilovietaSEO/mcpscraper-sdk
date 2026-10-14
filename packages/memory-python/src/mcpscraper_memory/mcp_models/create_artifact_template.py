from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


CreateArtifactTemplateInputVariant1Config = TypedDict('CreateArtifactTemplateInputVariant1Config', {
    'theme': Required[Literal['paper', 'ink', 'warm']],
    'density': Required[Literal['comfortable', 'compact']],
    'showSourceRail': Required[bool],
    'showGeneratedAt': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
})
CreateArtifactTemplateInputVariant1Config.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class CreateArtifactTemplateInputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    preset_key: Literal['editorial_reading_room_v1'] = Field(..., alias='presetKey', description='Registered preset key returned by list_artifact_templates.')
    name: Annotated[str, Field(min_length=1, max_length=120)] = Field(..., alias='name', description='Human-readable name for the record being created or updated.')
    description: Union[Annotated[str, Field(max_length=500)], None] = Field(None, alias='description', description='Human-readable summary that distinguishes this record from similarly named records.')
    authoring_instructions: Annotated[str, Field(max_length=4000)] = Field(..., alias='authoringInstructions', description='Presentation guidance for authors using this saved template; executable prompts or code are rejected.')
    config: CreateArtifactTemplateInputVariant1Config = Field(..., alias='config', description='Validated renderer configuration for the new immutable template version; arbitrary code is rejected.')


CreateArtifactTemplateInputVariant2ConfigFeatureFlags = TypedDict('CreateArtifactTemplateInputVariant2ConfigFeatureFlags', {
    'navigation': Required[bool],
    'socialLinks': Required[bool],
    'authority': Required[bool],
    'consultation': Required[bool],
    'learning': Required[bool],
    'services': Required[bool],
    'proof': Required[bool],
    'finalCta': Required[bool],
})
CreateArtifactTemplateInputVariant2ConfigFeatureFlags.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CreateArtifactTemplateInputVariant2Config = TypedDict('CreateArtifactTemplateInputVariant2Config', {
    'theme': Required[Literal['blue', 'slate', 'monochrome']],
    'showGeneratedAt': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'featureFlags': Required[CreateArtifactTemplateInputVariant2ConfigFeatureFlags],
})
CreateArtifactTemplateInputVariant2Config.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class CreateArtifactTemplateInputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    preset_key: Literal['personal_authority_v1'] = Field(..., alias='presetKey', description='Registered preset key returned by list_artifact_templates.')
    name: Annotated[str, Field(min_length=1, max_length=120)] = Field(..., alias='name', description='Human-readable name for the record being created or updated.')
    description: Union[Annotated[str, Field(max_length=500)], None] = Field(None, alias='description', description='Human-readable summary that distinguishes this record from similarly named records.')
    authoring_instructions: Annotated[str, Field(max_length=4000)] = Field(..., alias='authoringInstructions', description='Presentation guidance for authors using this saved template; executable prompts or code are rejected.')
    config: CreateArtifactTemplateInputVariant2Config = Field(..., alias='config', description='Validated renderer configuration for the new immutable template version; arbitrary code is rejected.')


CreateArtifactTemplateInputVariant3ConfigColors = TypedDict('CreateArtifactTemplateInputVariant3ConfigColors', {
    'accent': NotRequired[str],
    'background': NotRequired[str],
    'surface': NotRequired[str],
    'text': NotRequired[str],
})
CreateArtifactTemplateInputVariant3ConfigColors.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CreateArtifactTemplateInputVariant3ConfigTypography = TypedDict('CreateArtifactTemplateInputVariant3ConfigTypography', {
    'display': Required[Literal['editorial-serif', 'modern-sans', 'humanist-sans']],
    'body': Required[Literal['editorial-serif', 'modern-sans', 'humanist-sans']],
})
CreateArtifactTemplateInputVariant3ConfigTypography.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CreateArtifactTemplateInputVariant3ConfigFeatureFlags = TypedDict('CreateArtifactTemplateInputVariant3ConfigFeatureFlags', {
    'navigation': Required[bool],
    'socialLinks': Required[bool],
    'authority': Required[bool],
    'consultation': Required[bool],
    'learning': Required[bool],
    'services': Required[bool],
    'proof': Required[bool],
    'finalCta': Required[bool],
})
CreateArtifactTemplateInputVariant3ConfigFeatureFlags.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CreateArtifactTemplateInputVariant3Config = TypedDict('CreateArtifactTemplateInputVariant3Config', {
    'theme': Required[Literal['blue', 'terracotta', 'slate', 'monochrome']],
    'showGeneratedAt': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'colors': NotRequired[CreateArtifactTemplateInputVariant3ConfigColors],
    'typography': NotRequired[CreateArtifactTemplateInputVariant3ConfigTypography],
    'featureFlags': Required[CreateArtifactTemplateInputVariant3ConfigFeatureFlags],
})
CreateArtifactTemplateInputVariant3Config.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class CreateArtifactTemplateInputVariant3(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    preset_key: Literal['personal_authority_v2'] = Field(..., alias='presetKey', description='Registered preset key returned by list_artifact_templates.')
    name: Annotated[str, Field(min_length=1, max_length=120)] = Field(..., alias='name', description='Human-readable name for the record being created or updated.')
    description: Union[Annotated[str, Field(max_length=500)], None] = Field(None, alias='description', description='Human-readable summary that distinguishes this record from similarly named records.')
    authoring_instructions: Annotated[str, Field(max_length=4000)] = Field(..., alias='authoringInstructions', description='Presentation guidance for authors using this saved template; executable prompts or code are rejected.')
    config: CreateArtifactTemplateInputVariant3Config = Field(..., alias='config', description='Validated renderer configuration for the new immutable template version; arbitrary code is rejected.')


CreateArtifactTemplateInputVariant4ConfigFeatureFlags = TypedDict('CreateArtifactTemplateInputVariant4ConfigFeatureFlags', {
    'breakingTicker': Required[bool],
    'navigation': Required[bool],
    'leadGrid': Required[bool],
    'latestNews': Required[bool],
    'categorySections': Required[bool],
    'newsletter': Required[bool],
    'pressRoom': Required[bool],
    'trustFooter': Required[bool],
})
CreateArtifactTemplateInputVariant4ConfigFeatureFlags.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CreateArtifactTemplateInputVariant4Config = TypedDict('CreateArtifactTemplateInputVariant4Config', {
    'theme': Required[Literal['daily', 'journal', 'midnight']],
    'showGeneratedAt': Required[bool],
    'showBylines': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'featureFlags': Required[CreateArtifactTemplateInputVariant4ConfigFeatureFlags],
})
CreateArtifactTemplateInputVariant4Config.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class CreateArtifactTemplateInputVariant4(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    preset_key: Literal['newsroom_publisher_v1'] = Field(..., alias='presetKey', description='Registered preset key returned by list_artifact_templates.')
    name: Annotated[str, Field(min_length=1, max_length=120)] = Field(..., alias='name', description='Human-readable name for the record being created or updated.')
    description: Union[Annotated[str, Field(max_length=500)], None] = Field(None, alias='description', description='Human-readable summary that distinguishes this record from similarly named records.')
    authoring_instructions: Annotated[str, Field(max_length=4000)] = Field(..., alias='authoringInstructions', description='Presentation guidance for authors using this saved template; executable prompts or code are rejected.')
    config: CreateArtifactTemplateInputVariant4Config = Field(..., alias='config', description='Validated renderer configuration for the new immutable template version; arbitrary code is rejected.')


CreateArtifactTemplateInputVariant5ConfigFeatureFlags = TypedDict('CreateArtifactTemplateInputVariant5ConfigFeatureFlags', {
    'sidebarMedia': Required[bool],
    'disclosure': Required[bool],
    'stickyToc': Required[bool],
    'faq': Required[bool],
    'citation': Required[bool],
    'share': Required[bool],
    'authorCard': Required[bool],
})
CreateArtifactTemplateInputVariant5ConfigFeatureFlags.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CreateArtifactTemplateInputVariant5Config = TypedDict('CreateArtifactTemplateInputVariant5Config', {
    'theme': Required[Literal['navy', 'slate', 'forest']],
    'showGeneratedAt': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'featureFlags': Required[CreateArtifactTemplateInputVariant5ConfigFeatureFlags],
})
CreateArtifactTemplateInputVariant5Config.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class CreateArtifactTemplateInputVariant5(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    preset_key: Literal['blog_article_v1'] = Field(..., alias='presetKey', description='Registered preset key returned by list_artifact_templates.')
    name: Annotated[str, Field(min_length=1, max_length=120)] = Field(..., alias='name', description='Human-readable name for the record being created or updated.')
    description: Union[Annotated[str, Field(max_length=500)], None] = Field(None, alias='description', description='Human-readable summary that distinguishes this record from similarly named records.')
    authoring_instructions: Annotated[str, Field(max_length=4000)] = Field(..., alias='authoringInstructions', description='Presentation guidance for authors using this saved template; executable prompts or code are rejected.')
    config: CreateArtifactTemplateInputVariant5Config = Field(..., alias='config', description='Validated renderer configuration for the new immutable template version; arbitrary code is rejected.')


# Union schema: validate external payloads with TypeAdapter(CreateArtifactTemplateInput).
CreateArtifactTemplateInput = Union[CreateArtifactTemplateInputVariant1, CreateArtifactTemplateInputVariant2, CreateArtifactTemplateInputVariant3, CreateArtifactTemplateInputVariant4, CreateArtifactTemplateInputVariant5]


CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant1Config = TypedDict('CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant1Config', {
    'theme': Required[Literal['paper', 'ink', 'warm']],
    'density': Required[Literal['comfortable', 'compact']],
    'showSourceRail': Required[bool],
    'showGeneratedAt': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
})
CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant1Config.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant1 = TypedDict('CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant1', {
    'templateVersionId': Required[str],
    'templateId': Required[str],
    'version': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'rendererVersion': Required[Literal[1]],
    'inputContractVersion': Required[Literal[1]],
    'authoringInstructions': Required[Annotated[str, Field(max_length=4000)]],
    'createdAt': Required[str],
    'rendererKey': Required[Literal['editorial_reading_room_v1']],
    'config': Required[CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant1Config],
})
CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant2ConfigFeatureFlags = TypedDict('CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant2ConfigFeatureFlags', {
    'navigation': Required[bool],
    'socialLinks': Required[bool],
    'authority': Required[bool],
    'consultation': Required[bool],
    'learning': Required[bool],
    'services': Required[bool],
    'proof': Required[bool],
    'finalCta': Required[bool],
})
CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant2ConfigFeatureFlags.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant2Config = TypedDict('CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant2Config', {
    'theme': Required[Literal['blue', 'slate', 'monochrome']],
    'showGeneratedAt': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'featureFlags': Required[CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant2ConfigFeatureFlags],
})
CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant2Config.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant2 = TypedDict('CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant2', {
    'templateVersionId': Required[str],
    'templateId': Required[str],
    'version': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'rendererVersion': Required[Literal[1]],
    'inputContractVersion': Required[Literal[1]],
    'authoringInstructions': Required[Annotated[str, Field(max_length=4000)]],
    'createdAt': Required[str],
    'rendererKey': Required[Literal['personal_authority_v1']],
    'config': Required[CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant2Config],
})
CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant2.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3ConfigColors = TypedDict('CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3ConfigColors', {
    'accent': NotRequired[str],
    'background': NotRequired[str],
    'surface': NotRequired[str],
    'text': NotRequired[str],
})
CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3ConfigColors.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3ConfigTypography = TypedDict('CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3ConfigTypography', {
    'display': Required[Literal['editorial-serif', 'modern-sans', 'humanist-sans']],
    'body': Required[Literal['editorial-serif', 'modern-sans', 'humanist-sans']],
})
CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3ConfigTypography.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3ConfigFeatureFlags = TypedDict('CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3ConfigFeatureFlags', {
    'navigation': Required[bool],
    'socialLinks': Required[bool],
    'authority': Required[bool],
    'consultation': Required[bool],
    'learning': Required[bool],
    'services': Required[bool],
    'proof': Required[bool],
    'finalCta': Required[bool],
})
CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3ConfigFeatureFlags.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3Config = TypedDict('CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3Config', {
    'theme': Required[Literal['blue', 'terracotta', 'slate', 'monochrome']],
    'showGeneratedAt': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'colors': NotRequired[CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3ConfigColors],
    'typography': NotRequired[CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3ConfigTypography],
    'featureFlags': Required[CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3ConfigFeatureFlags],
})
CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3Config.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3 = TypedDict('CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3', {
    'templateVersionId': Required[str],
    'templateId': Required[str],
    'version': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'rendererVersion': Required[Literal[1]],
    'inputContractVersion': Required[Literal[1]],
    'authoringInstructions': Required[Annotated[str, Field(max_length=4000)]],
    'createdAt': Required[str],
    'rendererKey': Required[Literal['personal_authority_v2']],
    'config': Required[CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3Config],
})
CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant4ConfigFeatureFlags = TypedDict('CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant4ConfigFeatureFlags', {
    'breakingTicker': Required[bool],
    'navigation': Required[bool],
    'leadGrid': Required[bool],
    'latestNews': Required[bool],
    'categorySections': Required[bool],
    'newsletter': Required[bool],
    'pressRoom': Required[bool],
    'trustFooter': Required[bool],
})
CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant4ConfigFeatureFlags.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant4Config = TypedDict('CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant4Config', {
    'theme': Required[Literal['daily', 'journal', 'midnight']],
    'showGeneratedAt': Required[bool],
    'showBylines': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'featureFlags': Required[CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant4ConfigFeatureFlags],
})
CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant4Config.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant4 = TypedDict('CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant4', {
    'templateVersionId': Required[str],
    'templateId': Required[str],
    'version': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'rendererVersion': Required[Literal[1]],
    'inputContractVersion': Required[Literal[1]],
    'authoringInstructions': Required[Annotated[str, Field(max_length=4000)]],
    'createdAt': Required[str],
    'rendererKey': Required[Literal['newsroom_publisher_v1']],
    'config': Required[CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant4Config],
})
CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant4.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant5ConfigFeatureFlags = TypedDict('CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant5ConfigFeatureFlags', {
    'sidebarMedia': Required[bool],
    'disclosure': Required[bool],
    'stickyToc': Required[bool],
    'faq': Required[bool],
    'citation': Required[bool],
    'share': Required[bool],
    'authorCard': Required[bool],
})
CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant5ConfigFeatureFlags.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant5Config = TypedDict('CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant5Config', {
    'theme': Required[Literal['navy', 'slate', 'forest']],
    'showGeneratedAt': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'featureFlags': Required[CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant5ConfigFeatureFlags],
})
CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant5Config.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant5 = TypedDict('CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant5', {
    'templateVersionId': Required[str],
    'templateId': Required[str],
    'version': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'rendererVersion': Required[Literal[1]],
    'inputContractVersion': Required[Literal[1]],
    'authoringInstructions': Required[Annotated[str, Field(max_length=4000)]],
    'createdAt': Required[str],
    'rendererKey': Required[Literal['blog_article_v1']],
    'config': Required[CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant5Config],
})
CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant5.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant1Config = TypedDict('CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant1Config', {
    'theme': Required[Literal['paper', 'ink', 'warm']],
    'density': Required[Literal['comfortable', 'compact']],
    'showSourceRail': Required[bool],
    'showGeneratedAt': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
})
CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant1Config.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant1 = TypedDict('CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant1', {
    'templateVersionId': Required[str],
    'templateId': Required[str],
    'version': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'rendererVersion': Required[Literal[1]],
    'inputContractVersion': Required[Literal[1]],
    'authoringInstructions': Required[Annotated[str, Field(max_length=4000)]],
    'createdAt': Required[str],
    'rendererKey': Required[Literal['editorial_reading_room_v1']],
    'config': Required[CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant1Config],
})
CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant2ConfigFeatureFlags = TypedDict('CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant2ConfigFeatureFlags', {
    'navigation': Required[bool],
    'socialLinks': Required[bool],
    'authority': Required[bool],
    'consultation': Required[bool],
    'learning': Required[bool],
    'services': Required[bool],
    'proof': Required[bool],
    'finalCta': Required[bool],
})
CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant2ConfigFeatureFlags.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant2Config = TypedDict('CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant2Config', {
    'theme': Required[Literal['blue', 'slate', 'monochrome']],
    'showGeneratedAt': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'featureFlags': Required[CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant2ConfigFeatureFlags],
})
CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant2Config.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant2 = TypedDict('CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant2', {
    'templateVersionId': Required[str],
    'templateId': Required[str],
    'version': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'rendererVersion': Required[Literal[1]],
    'inputContractVersion': Required[Literal[1]],
    'authoringInstructions': Required[Annotated[str, Field(max_length=4000)]],
    'createdAt': Required[str],
    'rendererKey': Required[Literal['personal_authority_v1']],
    'config': Required[CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant2Config],
})
CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant2.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant3ConfigColors = TypedDict('CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant3ConfigColors', {
    'accent': NotRequired[str],
    'background': NotRequired[str],
    'surface': NotRequired[str],
    'text': NotRequired[str],
})
CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant3ConfigColors.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant3ConfigTypography = TypedDict('CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant3ConfigTypography', {
    'display': Required[Literal['editorial-serif', 'modern-sans', 'humanist-sans']],
    'body': Required[Literal['editorial-serif', 'modern-sans', 'humanist-sans']],
})
CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant3ConfigTypography.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant3ConfigFeatureFlags = TypedDict('CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant3ConfigFeatureFlags', {
    'navigation': Required[bool],
    'socialLinks': Required[bool],
    'authority': Required[bool],
    'consultation': Required[bool],
    'learning': Required[bool],
    'services': Required[bool],
    'proof': Required[bool],
    'finalCta': Required[bool],
})
CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant3ConfigFeatureFlags.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant3Config = TypedDict('CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant3Config', {
    'theme': Required[Literal['blue', 'terracotta', 'slate', 'monochrome']],
    'showGeneratedAt': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'colors': NotRequired[CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant3ConfigColors],
    'typography': NotRequired[CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant3ConfigTypography],
    'featureFlags': Required[CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant3ConfigFeatureFlags],
})
CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant3Config.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant3 = TypedDict('CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant3', {
    'templateVersionId': Required[str],
    'templateId': Required[str],
    'version': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'rendererVersion': Required[Literal[1]],
    'inputContractVersion': Required[Literal[1]],
    'authoringInstructions': Required[Annotated[str, Field(max_length=4000)]],
    'createdAt': Required[str],
    'rendererKey': Required[Literal['personal_authority_v2']],
    'config': Required[CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant3Config],
})
CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant3.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant4ConfigFeatureFlags = TypedDict('CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant4ConfigFeatureFlags', {
    'breakingTicker': Required[bool],
    'navigation': Required[bool],
    'leadGrid': Required[bool],
    'latestNews': Required[bool],
    'categorySections': Required[bool],
    'newsletter': Required[bool],
    'pressRoom': Required[bool],
    'trustFooter': Required[bool],
})
CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant4ConfigFeatureFlags.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant4Config = TypedDict('CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant4Config', {
    'theme': Required[Literal['daily', 'journal', 'midnight']],
    'showGeneratedAt': Required[bool],
    'showBylines': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'featureFlags': Required[CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant4ConfigFeatureFlags],
})
CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant4Config.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant4 = TypedDict('CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant4', {
    'templateVersionId': Required[str],
    'templateId': Required[str],
    'version': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'rendererVersion': Required[Literal[1]],
    'inputContractVersion': Required[Literal[1]],
    'authoringInstructions': Required[Annotated[str, Field(max_length=4000)]],
    'createdAt': Required[str],
    'rendererKey': Required[Literal['newsroom_publisher_v1']],
    'config': Required[CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant4Config],
})
CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant4.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant5ConfigFeatureFlags = TypedDict('CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant5ConfigFeatureFlags', {
    'sidebarMedia': Required[bool],
    'disclosure': Required[bool],
    'stickyToc': Required[bool],
    'faq': Required[bool],
    'citation': Required[bool],
    'share': Required[bool],
    'authorCard': Required[bool],
})
CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant5ConfigFeatureFlags.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant5Config = TypedDict('CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant5Config', {
    'theme': Required[Literal['navy', 'slate', 'forest']],
    'showGeneratedAt': Required[bool],
    'brandName': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'featureFlags': Required[CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant5ConfigFeatureFlags],
})
CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant5Config.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant5 = TypedDict('CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant5', {
    'templateVersionId': Required[str],
    'templateId': Required[str],
    'version': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'rendererVersion': Required[Literal[1]],
    'inputContractVersion': Required[Literal[1]],
    'authoringInstructions': Required[Annotated[str, Field(max_length=4000)]],
    'createdAt': Required[str],
    'rendererKey': Required[Literal['blog_article_v1']],
    'config': Required[CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant5Config],
})
CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant5.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateArtifactTemplateOutputVariant1Template = TypedDict('CreateArtifactTemplateOutputVariant1Template', {
    'templateId': Required[str],
    'name': Required[Annotated[str, Field(min_length=1, max_length=120)]],
    'description': Required[Annotated[str, Field(max_length=500)]],
    'currentVersionId': Required[str],
    'status': Required[Literal['active', 'archived']],
    'currentVersion': NotRequired[Union[CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant1, CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant2, CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant3, CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant4, CreateArtifactTemplateOutputVariant1TemplateCurrentVersionVariant5]],
    'versions': NotRequired[list[Union[CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant1, CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant2, CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant3, CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant4, CreateArtifactTemplateOutputVariant1TemplateVersionsItemVariant5]]],
    'createdAt': Required[str],
    'updatedAt': Required[str],
})
CreateArtifactTemplateOutputVariant1Template.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CreateArtifactTemplateOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    template: Union[CreateArtifactTemplateOutputVariant1Template, None] = Field(None, alias='template', description='')
    error: Union[Annotated[str, Field(min_length=1, max_length=500)], None] = Field(None, alias='error', description='')
    error_code: Union[Literal['invalid_request', 'not_found', 'conflict', 'template_archived', 'renderer_unavailable', 'artifact_unavailable', 'internal_error'], None] = Field(None, alias='errorCode', description='')
    request_id: Union[Annotated[str, Field(max_length=200)], None] = Field(None, alias='requestId', description='')


CreateArtifactTemplateOutputVariant2DeliveryArtifactsItem = TypedDict('CreateArtifactTemplateOutputVariant2DeliveryArtifactsItem', {
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
CreateArtifactTemplateOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateArtifactTemplateOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('CreateArtifactTemplateOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
CreateArtifactTemplateOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateArtifactTemplateOutputVariant2Delivery = TypedDict('CreateArtifactTemplateOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[CreateArtifactTemplateOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[CreateArtifactTemplateOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
CreateArtifactTemplateOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateArtifactTemplateOutputVariant2RecoveryOperation = TypedDict('CreateArtifactTemplateOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CreateArtifactTemplateOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateArtifactTemplateOutputVariant2Recovery = TypedDict('CreateArtifactTemplateOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[CreateArtifactTemplateOutputVariant2RecoveryOperation],
})
CreateArtifactTemplateOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CreateArtifactTemplateOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: CreateArtifactTemplateOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: CreateArtifactTemplateOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(CreateArtifactTemplateOutput).
CreateArtifactTemplateOutput = Union[CreateArtifactTemplateOutputVariant2, CreateArtifactTemplateOutputVariant1]

_CreateArtifactTemplateInputAdapter = TypeAdapter(CreateArtifactTemplateInput)
_CreateArtifactTemplateOutputAdapter = TypeAdapter(CreateArtifactTemplateOutput)