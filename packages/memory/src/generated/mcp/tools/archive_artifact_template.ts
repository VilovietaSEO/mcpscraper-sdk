export interface Input {
  /**
   * Opaque saved-template identifier returned by an artifact-template tool.
   */
  templateId: string;
  /**
   * Set true to archive the record or false to restore it.
   */
  archived: boolean;
}

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
