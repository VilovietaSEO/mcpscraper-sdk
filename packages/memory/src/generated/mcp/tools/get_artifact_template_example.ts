export interface Input {
  /**
   * Registered preset key returned by list_artifact_templates.
   */
  presetKey:
    | "editorial_reading_room_v1"
    | "personal_authority_v1"
    | "personal_authority_v2"
    | "newsroom_publisher_v1"
    | "blog_article_v1";
}

export type Output =
  | {
      ok: boolean;
      example?: {
        presetKey:
          | "editorial_reading_room_v1"
          | "personal_authority_v1"
          | "personal_authority_v2"
          | "newsroom_publisher_v1"
          | "blog_article_v1";
        name: string;
        description: string;
        rendererKey:
          | "editorial_reading_room_v1"
          | "personal_authority_v1"
          | "personal_authority_v2"
          | "newsroom_publisher_v1"
          | "blog_article_v1";
        rendererVersion: 1;
        inputContractVersion: 1;
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
        recommendedAuthoringInstructions: string;
        /**
         * @minItems 1
         * @maxItems 8
         */
        previewPages:
          | [
              {
                label: string;
                url: string;
                description: string;
              }
            ]
          | [
              {
                label: string;
                url: string;
                description: string;
              },
              {
                label: string;
                url: string;
                description: string;
              }
            ]
          | [
              {
                label: string;
                url: string;
                description: string;
              },
              {
                label: string;
                url: string;
                description: string;
              },
              {
                label: string;
                url: string;
                description: string;
              }
            ]
          | [
              {
                label: string;
                url: string;
                description: string;
              },
              {
                label: string;
                url: string;
                description: string;
              },
              {
                label: string;
                url: string;
                description: string;
              },
              {
                label: string;
                url: string;
                description: string;
              }
            ]
          | [
              {
                label: string;
                url: string;
                description: string;
              },
              {
                label: string;
                url: string;
                description: string;
              },
              {
                label: string;
                url: string;
                description: string;
              },
              {
                label: string;
                url: string;
                description: string;
              },
              {
                label: string;
                url: string;
                description: string;
              }
            ]
          | [
              {
                label: string;
                url: string;
                description: string;
              },
              {
                label: string;
                url: string;
                description: string;
              },
              {
                label: string;
                url: string;
                description: string;
              },
              {
                label: string;
                url: string;
                description: string;
              },
              {
                label: string;
                url: string;
                description: string;
              },
              {
                label: string;
                url: string;
                description: string;
              }
            ]
          | [
              {
                label: string;
                url: string;
                description: string;
              },
              {
                label: string;
                url: string;
                description: string;
              },
              {
                label: string;
                url: string;
                description: string;
              },
              {
                label: string;
                url: string;
                description: string;
              },
              {
                label: string;
                url: string;
                description: string;
              },
              {
                label: string;
                url: string;
                description: string;
              },
              {
                label: string;
                url: string;
                description: string;
              }
            ]
          | [
              {
                label: string;
                url: string;
                description: string;
              },
              {
                label: string;
                url: string;
                description: string;
              },
              {
                label: string;
                url: string;
                description: string;
              },
              {
                label: string;
                url: string;
                description: string;
              },
              {
                label: string;
                url: string;
                description: string;
              },
              {
                label: string;
                url: string;
                description: string;
              },
              {
                label: string;
                url: string;
                description: string;
              },
              {
                label: string;
                url: string;
                description: string;
              }
            ];
        machineReadableExampleUrl: string;
        exampleInput: {
          [k: string]: unknown;
        };
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
