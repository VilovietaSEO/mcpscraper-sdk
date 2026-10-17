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

export type Output =
  | {
      ok: boolean;
      presets?: {
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
              theme: "paper" | "ink" | "warm";
              density: "comfortable" | "compact";
              showSourceRail: boolean;
              showGeneratedAt: boolean;
              brandName?: string;
            }
          | {
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
            }
          | {
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
            }
          | {
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
            }
          | {
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
      }[];
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
