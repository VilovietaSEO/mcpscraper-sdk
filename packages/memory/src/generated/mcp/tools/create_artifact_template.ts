export type Input =
  | {
      /**
       * Registered preset key returned by list_artifact_templates.
       */
      presetKey: "editorial_reading_room_v1";
      /**
       * Human-readable name for the record being created or updated.
       */
      name: string;
      /**
       * Human-readable summary that distinguishes this record from similarly named records.
       */
      description?: string;
      /**
       * Presentation guidance for authors using this saved template; executable prompts or code are rejected.
       */
      authoringInstructions: string;
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
      /**
       * Registered preset key returned by list_artifact_templates.
       */
      presetKey: "personal_authority_v1";
      /**
       * Human-readable name for the record being created or updated.
       */
      name: string;
      /**
       * Human-readable summary that distinguishes this record from similarly named records.
       */
      description?: string;
      /**
       * Presentation guidance for authors using this saved template; executable prompts or code are rejected.
       */
      authoringInstructions: string;
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
           * Whether the renderer includes the navigation section.
           */
          navigation: boolean;
          /**
           * Whether the renderer includes social profile links.
           */
          socialLinks: boolean;
          /**
           * Whether the renderer includes the authority section.
           */
          authority: boolean;
          /**
           * Whether the renderer includes the consultation call-to-action.
           */
          consultation: boolean;
          /**
           * Whether the renderer includes the learning section.
           */
          learning: boolean;
          /**
           * Whether the renderer includes the services section.
           */
          services: boolean;
          /**
           * Whether the renderer includes the proof section.
           */
          proof: boolean;
          /**
           * Whether the renderer includes the final call-to-action.
           */
          finalCta: boolean;
        };
      };
    }
  | {
      /**
       * Registered preset key returned by list_artifact_templates.
       */
      presetKey: "personal_authority_v2";
      /**
       * Human-readable name for the record being created or updated.
       */
      name: string;
      /**
       * Human-readable summary that distinguishes this record from similarly named records.
       */
      description?: string;
      /**
       * Presentation guidance for authors using this saved template; executable prompts or code are rejected.
       */
      authoringInstructions: string;
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
           * Registered self-contained body-font family selected for article and paragraph text.
           */
          body: "editorial-serif" | "modern-sans" | "humanist-sans";
        };
        /**
         * Validated renderer features enabled for this template version.
         */
        featureFlags: {
          /**
           * Whether the renderer includes the navigation section.
           */
          navigation: boolean;
          /**
           * Whether the renderer includes social profile links.
           */
          socialLinks: boolean;
          /**
           * Whether the renderer includes the authority section.
           */
          authority: boolean;
          /**
           * Whether the renderer includes the consultation call-to-action.
           */
          consultation: boolean;
          /**
           * Whether the renderer includes the learning section.
           */
          learning: boolean;
          /**
           * Whether the renderer includes the services section.
           */
          services: boolean;
          /**
           * Whether the renderer includes the proof section.
           */
          proof: boolean;
          /**
           * Whether the renderer includes the final call-to-action.
           */
          finalCta: boolean;
        };
      };
    }
  | {
      /**
       * Registered preset key returned by list_artifact_templates.
       */
      presetKey: "newsroom_publisher_v1";
      /**
       * Human-readable name for the record being created or updated.
       */
      name: string;
      /**
       * Human-readable summary that distinguishes this record from similarly named records.
       */
      description?: string;
      /**
       * Presentation guidance for authors using this saved template; executable prompts or code are rejected.
       */
      authoringInstructions: string;
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
           * Whether the renderer includes the breaking-news ticker.
           */
          breakingTicker: boolean;
          /**
           * Whether the renderer includes the navigation section.
           */
          navigation: boolean;
          /**
           * Whether the renderer includes the lead-story grid.
           */
          leadGrid: boolean;
          /**
           * Whether the renderer includes the latest-news section.
           */
          latestNews: boolean;
          /**
           * Whether the renderer includes article sections grouped by category.
           */
          categorySections: boolean;
          /**
           * Whether the renderer includes the newsletter call-to-action.
           */
          newsletter: boolean;
          /**
           * Whether the renderer includes the press-room section.
           */
          pressRoom: boolean;
          /**
           * Whether the renderer includes the trust and provenance footer.
           */
          trustFooter: boolean;
        };
      };
    }
  | {
      /**
       * Registered preset key returned by list_artifact_templates.
       */
      presetKey: "blog_article_v1";
      /**
       * Human-readable name for the record being created or updated.
       */
      name: string;
      /**
       * Human-readable summary that distinguishes this record from similarly named records.
       */
      description?: string;
      /**
       * Presentation guidance for authors using this saved template; executable prompts or code are rejected.
       */
      authoringInstructions: string;
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

export type Output =
  | {
      ok: boolean;
      template?: {
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
              config: {
                theme: "paper" | "ink" | "warm";
                density: "comfortable" | "compact";
                showSourceRail: boolean;
                showGeneratedAt: boolean;
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
              config: {
                theme: "blue" | "slate" | "monochrome";
                showGeneratedAt: boolean;
                brandName?: string;
                featureFlags: {
                  navigation: boolean;
                  socialLinks: boolean;
                  authority: boolean;
                  consultation: boolean;
                  learning: boolean;
                  services: boolean;
                  proof: boolean;
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
              config: {
                theme: "blue" | "terracotta" | "slate" | "monochrome";
                showGeneratedAt: boolean;
                brandName?: string;
                colors?: {
                  accent?: string;
                  background?: string;
                  surface?: string;
                  text?: string;
                };
                typography?: {
                  display: "editorial-serif" | "modern-sans" | "humanist-sans";
                  body: "editorial-serif" | "modern-sans" | "humanist-sans";
                };
                featureFlags: {
                  navigation: boolean;
                  socialLinks: boolean;
                  authority: boolean;
                  consultation: boolean;
                  learning: boolean;
                  services: boolean;
                  proof: boolean;
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
              config: {
                theme: "daily" | "journal" | "midnight";
                showGeneratedAt: boolean;
                showBylines: boolean;
                brandName?: string;
                featureFlags: {
                  breakingTicker: boolean;
                  navigation: boolean;
                  leadGrid: boolean;
                  latestNews: boolean;
                  categorySections: boolean;
                  newsletter: boolean;
                  pressRoom: boolean;
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
              config: {
                theme: "navy" | "slate" | "forest";
                showGeneratedAt: boolean;
                brandName?: string;
                featureFlags: {
                  sidebarMedia: boolean;
                  disclosure: boolean;
                  stickyToc: boolean;
                  faq: boolean;
                  citation: boolean;
                  share: boolean;
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
              config: {
                theme: "paper" | "ink" | "warm";
                density: "comfortable" | "compact";
                showSourceRail: boolean;
                showGeneratedAt: boolean;
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
              config: {
                theme: "blue" | "slate" | "monochrome";
                showGeneratedAt: boolean;
                brandName?: string;
                featureFlags: {
                  navigation: boolean;
                  socialLinks: boolean;
                  authority: boolean;
                  consultation: boolean;
                  learning: boolean;
                  services: boolean;
                  proof: boolean;
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
              config: {
                theme: "blue" | "terracotta" | "slate" | "monochrome";
                showGeneratedAt: boolean;
                brandName?: string;
                colors?: {
                  accent?: string;
                  background?: string;
                  surface?: string;
                  text?: string;
                };
                typography?: {
                  display: "editorial-serif" | "modern-sans" | "humanist-sans";
                  body: "editorial-serif" | "modern-sans" | "humanist-sans";
                };
                featureFlags: {
                  navigation: boolean;
                  socialLinks: boolean;
                  authority: boolean;
                  consultation: boolean;
                  learning: boolean;
                  services: boolean;
                  proof: boolean;
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
              config: {
                theme: "daily" | "journal" | "midnight";
                showGeneratedAt: boolean;
                showBylines: boolean;
                brandName?: string;
                featureFlags: {
                  breakingTicker: boolean;
                  navigation: boolean;
                  leadGrid: boolean;
                  latestNews: boolean;
                  categorySections: boolean;
                  newsletter: boolean;
                  pressRoom: boolean;
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
              config: {
                theme: "navy" | "slate" | "forest";
                showGeneratedAt: boolean;
                brandName?: string;
                featureFlags: {
                  sidebarMedia: boolean;
                  disclosure: boolean;
                  stickyToc: boolean;
                  faq: boolean;
                  citation: boolean;
                  share: boolean;
                  authorCard: boolean;
                };
              };
            }
        )[];
        createdAt: string;
        updatedAt: string;
      };
      error?: string;
      errorCode?:
        | "invalid_request"
        | "not_found"
        | "conflict"
        | "template_archived"
        | "renderer_unavailable"
        | "artifact_unavailable"
        | "internal_error";
      requestId?: string;
    }
  | {
      delivery: {
        mode: "artifact";
        status: "complete" | "partial" | "unavailable";
        retainedRepresentation: "formatted-tool-result";
        sourceIsError: boolean;
        artifacts: {
          artifactId: string;
          filename: string;
          contentType: string;
          bytes: number;
          sha256: string;
          expiresAt: string;
          capabilities: string[];
          downloadUrl: string | null;
          downloadUrlExpiresAt: string | null;
          downloadState: "available" | "local" | "unavailable";
        }[];
        availableExports?: {
          artifactId: string;
          sourceArtifactId: string;
          filename: "result.md";
          contentType: "text/markdown; charset=utf-8";
          state: "on-demand";
        }[];
        downloadLinksOmitted: boolean;
        scopeOmittedFields: number;
        storageFailure: {
          artifactId: string | null;
          outcome: "unknown" | "bytes-stored-metadata-pending" | "failed";
        } | null;
        nextAction: string;
      };
      preview: string;
      scope: {
        [k: string]: string | number | boolean | null;
      };
      recovery: {
        idempotencyKey?: string;
        operationId?: string;
        runId?: string;
        jobId?: string;
        operation?: {
          runId: string | null;
          idempotencyKey: string;
          state: string;
        };
      };
    };
