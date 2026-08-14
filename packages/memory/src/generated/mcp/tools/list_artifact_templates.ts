export interface Input {
  /**
   * Lifecycle status used to filter or update the selected records.
   */
  status?: "active" | "archived" | "all";
  /**
   * Optional case-insensitive search text for preset and saved-template names, descriptions, renderer keys, and authoring guidance.
   */
  query?: string;
  /**
   * Optional renderer-family filter. Saved templates are matched through their current immutable version.
   */
  presetKey?:
    | "editorial_reading_room_v1"
    | "personal_authority_v1"
    | "personal_authority_v2"
    | "newsroom_publisher_v1"
    | "blog_article_v1";
}

export interface Output {
  ok: boolean;
  presets?: {
    /**
     * Registered preset key returned by list_artifact_templates.
     */
    presetKey:
      | "editorial_reading_room_v1"
      | "personal_authority_v1"
      | "personal_authority_v2"
      | "newsroom_publisher_v1"
      | "blog_article_v1";
    name: string;
    description: string;
    mark: string;
    featureFlags: {
      key: string;
      label: string;
      description: string;
    }[];
    defaultConfig:
      | {
          /**
           * Registered presentation theme selected for the renderer.
           */
          theme: "paper" | "ink" | "warm";
          /**
           * Validated presentation-density setting for the renderer.
           */
          density: "comfortable" | "compact";
          /**
           * Whether the renderer displays the source and provenance rail.
           */
          showSourceRail: boolean;
          /**
           * Whether the renderer displays the artifact generation time.
           */
          showGeneratedAt: boolean;
          /**
           * Public publication or collection brand name.
           */
          brandName?: string;
        }
      | {
          /**
           * Registered presentation theme selected for the renderer.
           */
          theme: "blue" | "slate" | "monochrome";
          /**
           * Whether the renderer displays the artifact generation time.
           */
          showGeneratedAt: boolean;
          /**
           * Public publication or collection brand name.
           */
          brandName?: string;
          /**
           * Validated renderer features enabled for this template version.
           */
          featureFlags: {
            /**
             * Validated navigation labels and destinations for the rendered site.
             */
            navigation: boolean;
            /**
             * Curated public social profile links for the publication identity.
             */
            socialLinks: boolean;
            /**
             * Source authority or ownership context supporting this content.
             */
            authority: boolean;
            /**
             * Consultation-call presentation and link settings.
             */
            consultation: boolean;
            /**
             * Learning-section configuration for the editorial renderer.
             */
            learning: boolean;
            /**
             * Source-backed services associated with the business listing.
             */
            services: boolean;
            /**
             * Proof-section content and evidence references.
             */
            proof: boolean;
            /**
             * Final call-to-action content shown after the authored collection.
             */
            finalCta: boolean;
          };
        }
      | {
          /**
           * Registered presentation theme selected for the renderer.
           */
          theme: "blue" | "terracotta" | "slate" | "monochrome";
          /**
           * Whether the renderer displays the artifact generation time.
           */
          showGeneratedAt: boolean;
          /**
           * Public publication or collection brand name.
           */
          brandName?: string;
          /**
           * Optional bounded brand-color overrides validated for hexadecimal form and accessible contrast.
           */
          colors?: {
            /**
             * Optional six-digit hexadecimal accent color that must meet the renderer contrast threshold.
             */
            accent?: string;
            /**
             * Optional six-digit hexadecimal page-background color that must preserve readable contrast.
             */
            background?: string;
            /**
             * Optional six-digit hexadecimal structural-surface color that must preserve visible separation.
             */
            surface?: string;
            /**
             * Optional six-digit hexadecimal primary text color that must meet WCAG AA contrast.
             */
            text?: string;
          };
          /**
           * Optional registered display and body font-family selections; arbitrary CSS and remote fonts are rejected.
           */
          typography?: {
            /**
             * Registered self-contained display-font family selected for prominent headings.
             */
            display: "editorial-serif" | "modern-sans" | "humanist-sans";
            /**
             * Registered self-contained display-font family selected for prominent headings.
             */
            body: "editorial-serif" | "modern-sans" | "humanist-sans";
          };
          /**
           * Validated renderer features enabled for this template version.
           */
          featureFlags: {
            /**
             * Validated navigation labels and destinations for the rendered site.
             */
            navigation: boolean;
            /**
             * Curated public social profile links for the publication identity.
             */
            socialLinks: boolean;
            /**
             * Source authority or ownership context supporting this content.
             */
            authority: boolean;
            /**
             * Consultation-call presentation and link settings.
             */
            consultation: boolean;
            /**
             * Learning-section configuration for the editorial renderer.
             */
            learning: boolean;
            /**
             * Source-backed services associated with the business listing.
             */
            services: boolean;
            /**
             * Proof-section content and evidence references.
             */
            proof: boolean;
            /**
             * Final call-to-action content shown after the authored collection.
             */
            finalCta: boolean;
          };
        }
      | {
          /**
           * Registered presentation theme selected for the renderer.
           */
          theme: "daily" | "journal" | "midnight";
          /**
           * Whether the renderer displays the artifact generation time.
           */
          showGeneratedAt: boolean;
          /**
           * Whether authored article bylines are visibly rendered.
           */
          showBylines: boolean;
          /**
           * Public publication or collection brand name.
           */
          brandName?: string;
          /**
           * Validated renderer features enabled for this template version.
           */
          featureFlags: {
            /**
             * Optional short breaking-news ticker shown by the renderer.
             */
            breakingTicker: boolean;
            /**
             * Validated navigation labels and destinations for the rendered site.
             */
            navigation: boolean;
            /**
             * Lead-story grid configuration for the editorial renderer.
             */
            leadGrid: boolean;
            /**
             * Latest-news section configuration for the editorial renderer.
             */
            latestNews: boolean;
            /**
             * Ordered category sections and their assigned article references.
             */
            categorySections: boolean;
            /**
             * Newsletter-callout presentation and subscription link settings.
             */
            newsletter: boolean;
            /**
             * Press-room section configuration for the editorial renderer.
             */
            pressRoom: boolean;
            /**
             * Trust and provenance footer configuration for the rendered site.
             */
            trustFooter: boolean;
          };
        }
      | {
          /**
           * Registered presentation theme selected for the renderer.
           */
          theme: "navy" | "slate" | "forest";
          /**
           * Whether the renderer displays the artifact generation time.
           */
          showGeneratedAt: boolean;
          /**
           * Public publication or collection brand name.
           */
          brandName?: string;
          /**
           * Validated renderer features enabled for this template version.
           */
          featureFlags: {
            /**
             * Whether the article renderer shows editorial media above the desktop sidebar.
             */
            sidebarMedia: boolean;
            /**
             * Whether the article renderer includes the expandable editorial disclosure.
             */
            disclosure: boolean;
            /**
             * Whether the article renderer keeps section navigation visible and highlights the active section.
             */
            stickyToc: boolean;
            /**
             * Whether the article renderer includes accessible expandable frequently asked questions.
             */
            faq: boolean;
            /**
             * Whether the article renderer includes the citation guide and clipboard actions.
             */
            citation: boolean;
            /**
             * Whether the article renderer includes native sharing with a clipboard fallback.
             */
            share: boolean;
            /**
             * Whether the article renderer includes the complete author attribution card.
             */
            authorCard: boolean;
          };
        };
  }[];
  templates?: {
    templateId: string;
    name: string;
    description: string;
    currentVersionId: string;
    status: "active" | "archived";
    currentVersion?:
      | {
          templateVersionId: string;
          templateId: string;
          version: number;
          rendererVersion: 1;
          inputContractVersion: 1;
          authoringInstructions: string;
          createdAt: string;
          rendererKey: "editorial_reading_room_v1";
          /**
           * Validated renderer configuration for the new immutable template version; arbitrary code is rejected.
           */
          config: {
            /**
             * Registered presentation theme selected for the renderer.
             */
            theme: "paper" | "ink" | "warm";
            /**
             * Validated presentation-density setting for the renderer.
             */
            density: "comfortable" | "compact";
            /**
             * Whether the renderer displays the source and provenance rail.
             */
            showSourceRail: boolean;
            /**
             * Whether the renderer displays the artifact generation time.
             */
            showGeneratedAt: boolean;
            /**
             * Public publication or collection brand name.
             */
            brandName?: string;
          };
        }
      | {
          templateVersionId: string;
          templateId: string;
          version: number;
          rendererVersion: 1;
          inputContractVersion: 1;
          authoringInstructions: string;
          createdAt: string;
          rendererKey: "personal_authority_v1";
          /**
           * Validated renderer configuration for the new immutable template version; arbitrary code is rejected.
           */
          config: {
            /**
             * Registered presentation theme selected for the renderer.
             */
            theme: "blue" | "slate" | "monochrome";
            /**
             * Whether the renderer displays the artifact generation time.
             */
            showGeneratedAt: boolean;
            /**
             * Public publication or collection brand name.
             */
            brandName?: string;
            /**
             * Validated renderer features enabled for this template version.
             */
            featureFlags: {
              /**
               * Validated navigation labels and destinations for the rendered site.
               */
              navigation: boolean;
              /**
               * Curated public social profile links for the publication identity.
               */
              socialLinks: boolean;
              /**
               * Source authority or ownership context supporting this content.
               */
              authority: boolean;
              /**
               * Consultation-call presentation and link settings.
               */
              consultation: boolean;
              /**
               * Learning-section configuration for the editorial renderer.
               */
              learning: boolean;
              /**
               * Source-backed services associated with the business listing.
               */
              services: boolean;
              /**
               * Proof-section content and evidence references.
               */
              proof: boolean;
              /**
               * Final call-to-action content shown after the authored collection.
               */
              finalCta: boolean;
            };
          };
        }
      | {
          templateVersionId: string;
          templateId: string;
          version: number;
          rendererVersion: 1;
          inputContractVersion: 1;
          authoringInstructions: string;
          createdAt: string;
          rendererKey: "personal_authority_v2";
          /**
           * Validated renderer configuration for the new immutable template version; arbitrary code is rejected.
           */
          config: {
            /**
             * Registered presentation theme selected for the renderer.
             */
            theme: "blue" | "terracotta" | "slate" | "monochrome";
            /**
             * Whether the renderer displays the artifact generation time.
             */
            showGeneratedAt: boolean;
            /**
             * Public publication or collection brand name.
             */
            brandName?: string;
            /**
             * Optional bounded brand-color overrides validated for hexadecimal form and accessible contrast.
             */
            colors?: {
              /**
               * Optional six-digit hexadecimal accent color that must meet the renderer contrast threshold.
               */
              accent?: string;
              /**
               * Optional six-digit hexadecimal page-background color that must preserve readable contrast.
               */
              background?: string;
              /**
               * Optional six-digit hexadecimal structural-surface color that must preserve visible separation.
               */
              surface?: string;
              /**
               * Optional six-digit hexadecimal primary text color that must meet WCAG AA contrast.
               */
              text?: string;
            };
            /**
             * Optional registered display and body font-family selections; arbitrary CSS and remote fonts are rejected.
             */
            typography?: {
              /**
               * Registered self-contained display-font family selected for prominent headings.
               */
              display: "editorial-serif" | "modern-sans" | "humanist-sans";
              /**
               * Registered self-contained display-font family selected for prominent headings.
               */
              body: "editorial-serif" | "modern-sans" | "humanist-sans";
            };
            /**
             * Validated renderer features enabled for this template version.
             */
            featureFlags: {
              /**
               * Validated navigation labels and destinations for the rendered site.
               */
              navigation: boolean;
              /**
               * Curated public social profile links for the publication identity.
               */
              socialLinks: boolean;
              /**
               * Source authority or ownership context supporting this content.
               */
              authority: boolean;
              /**
               * Consultation-call presentation and link settings.
               */
              consultation: boolean;
              /**
               * Learning-section configuration for the editorial renderer.
               */
              learning: boolean;
              /**
               * Source-backed services associated with the business listing.
               */
              services: boolean;
              /**
               * Proof-section content and evidence references.
               */
              proof: boolean;
              /**
               * Final call-to-action content shown after the authored collection.
               */
              finalCta: boolean;
            };
          };
        }
      | {
          templateVersionId: string;
          templateId: string;
          version: number;
          rendererVersion: 1;
          inputContractVersion: 1;
          authoringInstructions: string;
          createdAt: string;
          rendererKey: "newsroom_publisher_v1";
          /**
           * Validated renderer configuration for the new immutable template version; arbitrary code is rejected.
           */
          config: {
            /**
             * Registered presentation theme selected for the renderer.
             */
            theme: "daily" | "journal" | "midnight";
            /**
             * Whether the renderer displays the artifact generation time.
             */
            showGeneratedAt: boolean;
            /**
             * Whether authored article bylines are visibly rendered.
             */
            showBylines: boolean;
            /**
             * Public publication or collection brand name.
             */
            brandName?: string;
            /**
             * Validated renderer features enabled for this template version.
             */
            featureFlags: {
              /**
               * Optional short breaking-news ticker shown by the renderer.
               */
              breakingTicker: boolean;
              /**
               * Validated navigation labels and destinations for the rendered site.
               */
              navigation: boolean;
              /**
               * Lead-story grid configuration for the editorial renderer.
               */
              leadGrid: boolean;
              /**
               * Latest-news section configuration for the editorial renderer.
               */
              latestNews: boolean;
              /**
               * Ordered category sections and their assigned article references.
               */
              categorySections: boolean;
              /**
               * Newsletter-callout presentation and subscription link settings.
               */
              newsletter: boolean;
              /**
               * Press-room section configuration for the editorial renderer.
               */
              pressRoom: boolean;
              /**
               * Trust and provenance footer configuration for the rendered site.
               */
              trustFooter: boolean;
            };
          };
        }
      | {
          templateVersionId: string;
          templateId: string;
          version: number;
          rendererVersion: 1;
          inputContractVersion: 1;
          authoringInstructions: string;
          createdAt: string;
          rendererKey: "blog_article_v1";
          /**
           * Validated renderer configuration for the new immutable template version; arbitrary code is rejected.
           */
          config: {
            /**
             * Registered presentation theme selected for the renderer.
             */
            theme: "navy" | "slate" | "forest";
            /**
             * Whether the renderer displays the artifact generation time.
             */
            showGeneratedAt: boolean;
            /**
             * Public publication or collection brand name.
             */
            brandName?: string;
            /**
             * Validated renderer features enabled for this template version.
             */
            featureFlags: {
              /**
               * Whether the article renderer shows editorial media above the desktop sidebar.
               */
              sidebarMedia: boolean;
              /**
               * Whether the article renderer includes the expandable editorial disclosure.
               */
              disclosure: boolean;
              /**
               * Whether the article renderer keeps section navigation visible and highlights the active section.
               */
              stickyToc: boolean;
              /**
               * Whether the article renderer includes accessible expandable frequently asked questions.
               */
              faq: boolean;
              /**
               * Whether the article renderer includes the citation guide and clipboard actions.
               */
              citation: boolean;
              /**
               * Whether the article renderer includes native sharing with a clipboard fallback.
               */
              share: boolean;
              /**
               * Whether the article renderer includes the complete author attribution card.
               */
              authorCard: boolean;
            };
          };
        };
    versions?: (
      | {
          templateVersionId: string;
          templateId: string;
          version: number;
          rendererVersion: 1;
          inputContractVersion: 1;
          authoringInstructions: string;
          createdAt: string;
          rendererKey: "editorial_reading_room_v1";
          /**
           * Validated renderer configuration for the new immutable template version; arbitrary code is rejected.
           */
          config: {
            /**
             * Registered presentation theme selected for the renderer.
             */
            theme: "paper" | "ink" | "warm";
            /**
             * Validated presentation-density setting for the renderer.
             */
            density: "comfortable" | "compact";
            /**
             * Whether the renderer displays the source and provenance rail.
             */
            showSourceRail: boolean;
            /**
             * Whether the renderer displays the artifact generation time.
             */
            showGeneratedAt: boolean;
            /**
             * Public publication or collection brand name.
             */
            brandName?: string;
          };
        }
      | {
          templateVersionId: string;
          templateId: string;
          version: number;
          rendererVersion: 1;
          inputContractVersion: 1;
          authoringInstructions: string;
          createdAt: string;
          rendererKey: "personal_authority_v1";
          /**
           * Validated renderer configuration for the new immutable template version; arbitrary code is rejected.
           */
          config: {
            /**
             * Registered presentation theme selected for the renderer.
             */
            theme: "blue" | "slate" | "monochrome";
            /**
             * Whether the renderer displays the artifact generation time.
             */
            showGeneratedAt: boolean;
            /**
             * Public publication or collection brand name.
             */
            brandName?: string;
            /**
             * Validated renderer features enabled for this template version.
             */
            featureFlags: {
              /**
               * Validated navigation labels and destinations for the rendered site.
               */
              navigation: boolean;
              /**
               * Curated public social profile links for the publication identity.
               */
              socialLinks: boolean;
              /**
               * Source authority or ownership context supporting this content.
               */
              authority: boolean;
              /**
               * Consultation-call presentation and link settings.
               */
              consultation: boolean;
              /**
               * Learning-section configuration for the editorial renderer.
               */
              learning: boolean;
              /**
               * Source-backed services associated with the business listing.
               */
              services: boolean;
              /**
               * Proof-section content and evidence references.
               */
              proof: boolean;
              /**
               * Final call-to-action content shown after the authored collection.
               */
              finalCta: boolean;
            };
          };
        }
      | {
          templateVersionId: string;
          templateId: string;
          version: number;
          rendererVersion: 1;
          inputContractVersion: 1;
          authoringInstructions: string;
          createdAt: string;
          rendererKey: "personal_authority_v2";
          /**
           * Validated renderer configuration for the new immutable template version; arbitrary code is rejected.
           */
          config: {
            /**
             * Registered presentation theme selected for the renderer.
             */
            theme: "blue" | "terracotta" | "slate" | "monochrome";
            /**
             * Whether the renderer displays the artifact generation time.
             */
            showGeneratedAt: boolean;
            /**
             * Public publication or collection brand name.
             */
            brandName?: string;
            /**
             * Optional bounded brand-color overrides validated for hexadecimal form and accessible contrast.
             */
            colors?: {
              /**
               * Optional six-digit hexadecimal accent color that must meet the renderer contrast threshold.
               */
              accent?: string;
              /**
               * Optional six-digit hexadecimal page-background color that must preserve readable contrast.
               */
              background?: string;
              /**
               * Optional six-digit hexadecimal structural-surface color that must preserve visible separation.
               */
              surface?: string;
              /**
               * Optional six-digit hexadecimal primary text color that must meet WCAG AA contrast.
               */
              text?: string;
            };
            /**
             * Optional registered display and body font-family selections; arbitrary CSS and remote fonts are rejected.
             */
            typography?: {
              /**
               * Registered self-contained display-font family selected for prominent headings.
               */
              display: "editorial-serif" | "modern-sans" | "humanist-sans";
              /**
               * Registered self-contained display-font family selected for prominent headings.
               */
              body: "editorial-serif" | "modern-sans" | "humanist-sans";
            };
            /**
             * Validated renderer features enabled for this template version.
             */
            featureFlags: {
              /**
               * Validated navigation labels and destinations for the rendered site.
               */
              navigation: boolean;
              /**
               * Curated public social profile links for the publication identity.
               */
              socialLinks: boolean;
              /**
               * Source authority or ownership context supporting this content.
               */
              authority: boolean;
              /**
               * Consultation-call presentation and link settings.
               */
              consultation: boolean;
              /**
               * Learning-section configuration for the editorial renderer.
               */
              learning: boolean;
              /**
               * Source-backed services associated with the business listing.
               */
              services: boolean;
              /**
               * Proof-section content and evidence references.
               */
              proof: boolean;
              /**
               * Final call-to-action content shown after the authored collection.
               */
              finalCta: boolean;
            };
          };
        }
      | {
          templateVersionId: string;
          templateId: string;
          version: number;
          rendererVersion: 1;
          inputContractVersion: 1;
          authoringInstructions: string;
          createdAt: string;
          rendererKey: "newsroom_publisher_v1";
          /**
           * Validated renderer configuration for the new immutable template version; arbitrary code is rejected.
           */
          config: {
            /**
             * Registered presentation theme selected for the renderer.
             */
            theme: "daily" | "journal" | "midnight";
            /**
             * Whether the renderer displays the artifact generation time.
             */
            showGeneratedAt: boolean;
            /**
             * Whether authored article bylines are visibly rendered.
             */
            showBylines: boolean;
            /**
             * Public publication or collection brand name.
             */
            brandName?: string;
            /**
             * Validated renderer features enabled for this template version.
             */
            featureFlags: {
              /**
               * Optional short breaking-news ticker shown by the renderer.
               */
              breakingTicker: boolean;
              /**
               * Validated navigation labels and destinations for the rendered site.
               */
              navigation: boolean;
              /**
               * Lead-story grid configuration for the editorial renderer.
               */
              leadGrid: boolean;
              /**
               * Latest-news section configuration for the editorial renderer.
               */
              latestNews: boolean;
              /**
               * Ordered category sections and their assigned article references.
               */
              categorySections: boolean;
              /**
               * Newsletter-callout presentation and subscription link settings.
               */
              newsletter: boolean;
              /**
               * Press-room section configuration for the editorial renderer.
               */
              pressRoom: boolean;
              /**
               * Trust and provenance footer configuration for the rendered site.
               */
              trustFooter: boolean;
            };
          };
        }
      | {
          templateVersionId: string;
          templateId: string;
          version: number;
          rendererVersion: 1;
          inputContractVersion: 1;
          authoringInstructions: string;
          createdAt: string;
          rendererKey: "blog_article_v1";
          /**
           * Validated renderer configuration for the new immutable template version; arbitrary code is rejected.
           */
          config: {
            /**
             * Registered presentation theme selected for the renderer.
             */
            theme: "navy" | "slate" | "forest";
            /**
             * Whether the renderer displays the artifact generation time.
             */
            showGeneratedAt: boolean;
            /**
             * Public publication or collection brand name.
             */
            brandName?: string;
            /**
             * Validated renderer features enabled for this template version.
             */
            featureFlags: {
              /**
               * Whether the article renderer shows editorial media above the desktop sidebar.
               */
              sidebarMedia: boolean;
              /**
               * Whether the article renderer includes the expandable editorial disclosure.
               */
              disclosure: boolean;
              /**
               * Whether the article renderer keeps section navigation visible and highlights the active section.
               */
              stickyToc: boolean;
              /**
               * Whether the article renderer includes accessible expandable frequently asked questions.
               */
              faq: boolean;
              /**
               * Whether the article renderer includes the citation guide and clipboard actions.
               */
              citation: boolean;
              /**
               * Whether the article renderer includes native sharing with a clipboard fallback.
               */
              share: boolean;
              /**
               * Whether the article renderer includes the complete author attribution card.
               */
              authorCard: boolean;
            };
          };
        }
    )[];
    createdAt: string;
    updatedAt: string;
  }[];
  error?: string;
  errorCode?:
    | "invalid_request"
    | "not_found"
    | "conflict"
    | "template_archived"
    | "renderer_unavailable"
    | "artifact_unavailable"
    | "view_link_unavailable"
    | "internal_error";
  requestId?: string;
}
