export interface Input {
  /**
   * Scheduled-results view to return, such as inbox, all unarchived, or archived.
   */
  view?: "inbox" | "all" | "archived";
  /**
   * Optional scheduled-run execution status filter.
   */
  status?: "running" | "succeeded" | "no_output" | "partial" | "billing_stopped" | "failed";
  /**
   * Optional scheduled-action identifier used to restrict results to one schedule.
   */
  scheduleId?: string;
  /**
   * Opaque saved-template identifier returned by an artifact-template tool.
   */
  templateId?: string;
  /**
   * Inclusive ISO 8601 lower bound for scheduled-run creation time.
   */
  from?: string;
  /**
   * Exclusive ISO 8601 upper bound for scheduled-run creation time.
   */
  to?: string;
  /**
   * Text matched against scheduled-run titles and searchable metadata.
   */
  query?: string;
  /**
   * Opaque continuation cursor returned by the previous page; omit for the first page.
   */
  cursor?: string;
  /**
   * Maximum rows or records to return on this page; use the returned cursor for more.
   */
  limit?: number;
}

export type Output =
  | {
      ok: boolean;
      items?: {
        runId: string;
        scheduleId: string;
        scheduleDescription: string;
        executionMode: "agent" | "connection_sync";
        status: "running" | "succeeded" | "no_output" | "partial" | "billing_stopped" | "failed";
        summary: string;
        errorCode: string | null;
        errorMessage: string | null;
        scheduledFor: string;
        startedAt: string;
        completedAt: string | null;
        openedAt: string | null;
        archivedAt: string | null;
        artifactSelection:
          | {
              mode: "none";
            }
          | {
              mode: "saved_template";
              templateId: string;
              templateVersionId: string;
            };
        /**
         * @maxItems 100
         */
        noteOutputs: {
          vault: string;
          path: string;
          title?: string;
          sourceRef?: string;
        }[];
        /**
         * @maxItems 10
         */
        artifactOutputs:
          | []
          | [
              {
                artifactId: string;
                templateId: string;
                templateVersionId: string;
                rendererKey:
                  | "editorial_reading_room_v1"
                  | "personal_authority_v1"
                  | "personal_authority_v2"
                  | "newsroom_publisher_v1"
                  | "blog_article_v1";
                rendererVersion: 1;
                mimeType: "text/html";
                title: string;
                bytes: number;
                sha256: string;
                createdAt: string;
                viewerPath: string;
              }
            ]
          | [
              {
                artifactId: string;
                templateId: string;
                templateVersionId: string;
                rendererKey:
                  | "editorial_reading_room_v1"
                  | "personal_authority_v1"
                  | "personal_authority_v2"
                  | "newsroom_publisher_v1"
                  | "blog_article_v1";
                rendererVersion: 1;
                mimeType: "text/html";
                title: string;
                bytes: number;
                sha256: string;
                createdAt: string;
                viewerPath: string;
              },
              {
                artifactId: string;
                templateId: string;
                templateVersionId: string;
                rendererKey:
                  | "editorial_reading_room_v1"
                  | "personal_authority_v1"
                  | "personal_authority_v2"
                  | "newsroom_publisher_v1"
                  | "blog_article_v1";
                rendererVersion: 1;
                mimeType: "text/html";
                title: string;
                bytes: number;
                sha256: string;
                createdAt: string;
                viewerPath: string;
              }
            ]
          | [
              {
                artifactId: string;
                templateId: string;
                templateVersionId: string;
                rendererKey:
                  | "editorial_reading_room_v1"
                  | "personal_authority_v1"
                  | "personal_authority_v2"
                  | "newsroom_publisher_v1"
                  | "blog_article_v1";
                rendererVersion: 1;
                mimeType: "text/html";
                title: string;
                bytes: number;
                sha256: string;
                createdAt: string;
                viewerPath: string;
              },
              {
                artifactId: string;
                templateId: string;
                templateVersionId: string;
                rendererKey:
                  | "editorial_reading_room_v1"
                  | "personal_authority_v1"
                  | "personal_authority_v2"
                  | "newsroom_publisher_v1"
                  | "blog_article_v1";
                rendererVersion: 1;
                mimeType: "text/html";
                title: string;
                bytes: number;
                sha256: string;
                createdAt: string;
                viewerPath: string;
              },
              {
                artifactId: string;
                templateId: string;
                templateVersionId: string;
                rendererKey:
                  | "editorial_reading_room_v1"
                  | "personal_authority_v1"
                  | "personal_authority_v2"
                  | "newsroom_publisher_v1"
                  | "blog_article_v1";
                rendererVersion: 1;
                mimeType: "text/html";
                title: string;
                bytes: number;
                sha256: string;
                createdAt: string;
                viewerPath: string;
              }
            ]
          | [
              {
                artifactId: string;
                templateId: string;
                templateVersionId: string;
                rendererKey:
                  | "editorial_reading_room_v1"
                  | "personal_authority_v1"
                  | "personal_authority_v2"
                  | "newsroom_publisher_v1"
                  | "blog_article_v1";
                rendererVersion: 1;
                mimeType: "text/html";
                title: string;
                bytes: number;
                sha256: string;
                createdAt: string;
                viewerPath: string;
              },
              {
                artifactId: string;
                templateId: string;
                templateVersionId: string;
                rendererKey:
                  | "editorial_reading_room_v1"
                  | "personal_authority_v1"
                  | "personal_authority_v2"
                  | "newsroom_publisher_v1"
                  | "blog_article_v1";
                rendererVersion: 1;
                mimeType: "text/html";
                title: string;
                bytes: number;
                sha256: string;
                createdAt: string;
                viewerPath: string;
              },
              {
                artifactId: string;
                templateId: string;
                templateVersionId: string;
                rendererKey:
                  | "editorial_reading_room_v1"
                  | "personal_authority_v1"
                  | "personal_authority_v2"
                  | "newsroom_publisher_v1"
                  | "blog_article_v1";
                rendererVersion: 1;
                mimeType: "text/html";
                title: string;
                bytes: number;
                sha256: string;
                createdAt: string;
                viewerPath: string;
              },
              {
                artifactId: string;
                templateId: string;
                templateVersionId: string;
                rendererKey:
                  | "editorial_reading_room_v1"
                  | "personal_authority_v1"
                  | "personal_authority_v2"
                  | "newsroom_publisher_v1"
                  | "blog_article_v1";
                rendererVersion: 1;
                mimeType: "text/html";
                title: string;
                bytes: number;
                sha256: string;
                createdAt: string;
                viewerPath: string;
              }
            ]
          | [
              {
                artifactId: string;
                templateId: string;
                templateVersionId: string;
                rendererKey:
                  | "editorial_reading_room_v1"
                  | "personal_authority_v1"
                  | "personal_authority_v2"
                  | "newsroom_publisher_v1"
                  | "blog_article_v1";
                rendererVersion: 1;
                mimeType: "text/html";
                title: string;
                bytes: number;
                sha256: string;
                createdAt: string;
                viewerPath: string;
              },
              {
                artifactId: string;
                templateId: string;
                templateVersionId: string;
                rendererKey:
                  | "editorial_reading_room_v1"
                  | "personal_authority_v1"
                  | "personal_authority_v2"
                  | "newsroom_publisher_v1"
                  | "blog_article_v1";
                rendererVersion: 1;
                mimeType: "text/html";
                title: string;
                bytes: number;
                sha256: string;
                createdAt: string;
                viewerPath: string;
              },
              {
                artifactId: string;
                templateId: string;
                templateVersionId: string;
                rendererKey:
                  | "editorial_reading_room_v1"
                  | "personal_authority_v1"
                  | "personal_authority_v2"
                  | "newsroom_publisher_v1"
                  | "blog_article_v1";
                rendererVersion: 1;
                mimeType: "text/html";
                title: string;
                bytes: number;
                sha256: string;
                createdAt: string;
                viewerPath: string;
              },
              {
                artifactId: string;
                templateId: string;
                templateVersionId: string;
                rendererKey:
                  | "editorial_reading_room_v1"
                  | "personal_authority_v1"
                  | "personal_authority_v2"
                  | "newsroom_publisher_v1"
                  | "blog_article_v1";
                rendererVersion: 1;
                mimeType: "text/html";
                title: string;
                bytes: number;
                sha256: string;
                createdAt: string;
                viewerPath: string;
              },
              {
                artifactId: string;
                templateId: string;
                templateVersionId: string;
                rendererKey:
                  | "editorial_reading_room_v1"
                  | "personal_authority_v1"
                  | "personal_authority_v2"
                  | "newsroom_publisher_v1"
                  | "blog_article_v1";
                rendererVersion: 1;
                mimeType: "text/html";
                title: string;
                bytes: number;
                sha256: string;
                createdAt: string;
                viewerPath: string;
              }
            ]
          | [
              {
                artifactId: string;
                templateId: string;
                templateVersionId: string;
                rendererKey:
                  | "editorial_reading_room_v1"
                  | "personal_authority_v1"
                  | "personal_authority_v2"
                  | "newsroom_publisher_v1"
                  | "blog_article_v1";
                rendererVersion: 1;
                mimeType: "text/html";
                title: string;
                bytes: number;
                sha256: string;
                createdAt: string;
                viewerPath: string;
              },
              {
                artifactId: string;
                templateId: string;
                templateVersionId: string;
                rendererKey:
                  | "editorial_reading_room_v1"
                  | "personal_authority_v1"
                  | "personal_authority_v2"
                  | "newsroom_publisher_v1"
                  | "blog_article_v1";
                rendererVersion: 1;
                mimeType: "text/html";
                title: string;
                bytes: number;
                sha256: string;
                createdAt: string;
                viewerPath: string;
              },
              {
                artifactId: string;
                templateId: string;
                templateVersionId: string;
                rendererKey:
                  | "editorial_reading_room_v1"
                  | "personal_authority_v1"
                  | "personal_authority_v2"
                  | "newsroom_publisher_v1"
                  | "blog_article_v1";
                rendererVersion: 1;
                mimeType: "text/html";
                title: string;
                bytes: number;
                sha256: string;
                createdAt: string;
                viewerPath: string;
              },
              {
                artifactId: string;
                templateId: string;
                templateVersionId: string;
                rendererKey:
                  | "editorial_reading_room_v1"
                  | "personal_authority_v1"
                  | "personal_authority_v2"
                  | "newsroom_publisher_v1"
                  | "blog_article_v1";
                rendererVersion: 1;
                mimeType: "text/html";
                title: string;
                bytes: number;
                sha256: string;
                createdAt: string;
                viewerPath: string;
              },
              {
                artifactId: string;
                templateId: string;
                templateVersionId: string;
                rendererKey:
                  | "editorial_reading_room_v1"
                  | "personal_authority_v1"
                  | "personal_authority_v2"
                  | "newsroom_publisher_v1"
                  | "blog_article_v1";
                rendererVersion: 1;
                mimeType: "text/html";
                title: string;
                bytes: number;
                sha256: string;
                createdAt: string;
                viewerPath: string;
              },
              {
                artifactId: string;
                templateId: string;
                templateVersionId: string;
                rendererKey:
                  | "editorial_reading_room_v1"
                  | "personal_authority_v1"
                  | "personal_authority_v2"
                  | "newsroom_publisher_v1"
                  | "blog_article_v1";
                rendererVersion: 1;
                mimeType: "text/html";
                title: string;
                bytes: number;
                sha256: string;
                createdAt: string;
                viewerPath: string;
              }
            ]
          | [
              {
                artifactId: string;
                templateId: string;
                templateVersionId: string;
                rendererKey:
                  | "editorial_reading_room_v1"
                  | "personal_authority_v1"
                  | "personal_authority_v2"
                  | "newsroom_publisher_v1"
                  | "blog_article_v1";
                rendererVersion: 1;
                mimeType: "text/html";
                title: string;
                bytes: number;
                sha256: string;
                createdAt: string;
                viewerPath: string;
              },
              {
                artifactId: string;
                templateId: string;
                templateVersionId: string;
                rendererKey:
                  | "editorial_reading_room_v1"
                  | "personal_authority_v1"
                  | "personal_authority_v2"
                  | "newsroom_publisher_v1"
                  | "blog_article_v1";
                rendererVersion: 1;
                mimeType: "text/html";
                title: string;
                bytes: number;
                sha256: string;
                createdAt: string;
                viewerPath: string;
              },
              {
                artifactId: string;
                templateId: string;
                templateVersionId: string;
                rendererKey:
                  | "editorial_reading_room_v1"
                  | "personal_authority_v1"
                  | "personal_authority_v2"
                  | "newsroom_publisher_v1"
                  | "blog_article_v1";
                rendererVersion: 1;
                mimeType: "text/html";
                title: string;
                bytes: number;
                sha256: string;
                createdAt: string;
                viewerPath: string;
              },
              {
                artifactId: string;
                templateId: string;
                templateVersionId: string;
                rendererKey:
                  | "editorial_reading_room_v1"
                  | "personal_authority_v1"
                  | "personal_authority_v2"
                  | "newsroom_publisher_v1"
                  | "blog_article_v1";
                rendererVersion: 1;
                mimeType: "text/html";
                title: string;
                bytes: number;
                sha256: string;
                createdAt: string;
                viewerPath: string;
              },
              {
                artifactId: string;
                templateId: string;
                templateVersionId: string;
                rendererKey:
                  | "editorial_reading_room_v1"
                  | "personal_authority_v1"
                  | "personal_authority_v2"
                  | "newsroom_publisher_v1"
                  | "blog_article_v1";
                rendererVersion: 1;
                mimeType: "text/html";
                title: string;
                bytes: number;
                sha256: string;
                createdAt: string;
                viewerPath: string;
              },
              {
                artifactId: string;
                templateId: string;
                templateVersionId: string;
                rendererKey:
                  | "editorial_reading_room_v1"
                  | "personal_authority_v1"
                  | "personal_authority_v2"
                  | "newsroom_publisher_v1"
                  | "blog_article_v1";
                rendererVersion: 1;
                mimeType: "text/html";
                title: string;
                bytes: number;
                sha256: string;
                createdAt: string;
                viewerPath: string;
              },
              {
                artifactId: string;
                templateId: string;
                templateVersionId: string;
                rendererKey:
                  | "editorial_reading_room_v1"
                  | "personal_authority_v1"
                  | "personal_authority_v2"
                  | "newsroom_publisher_v1"
                  | "blog_article_v1";
                rendererVersion: 1;
                mimeType: "text/html";
                title: string;
                bytes: number;
                sha256: string;
                createdAt: string;
                viewerPath: string;
              }
            ]
          | [
              {
                artifactId: string;
                templateId: string;
                templateVersionId: string;
                rendererKey:
                  | "editorial_reading_room_v1"
                  | "personal_authority_v1"
                  | "personal_authority_v2"
                  | "newsroom_publisher_v1"
                  | "blog_article_v1";
                rendererVersion: 1;
                mimeType: "text/html";
                title: string;
                bytes: number;
                sha256: string;
                createdAt: string;
                viewerPath: string;
              },
              {
                artifactId: string;
                templateId: string;
                templateVersionId: string;
                rendererKey:
                  | "editorial_reading_room_v1"
                  | "personal_authority_v1"
                  | "personal_authority_v2"
                  | "newsroom_publisher_v1"
                  | "blog_article_v1";
                rendererVersion: 1;
                mimeType: "text/html";
                title: string;
                bytes: number;
                sha256: string;
                createdAt: string;
                viewerPath: string;
              },
              {
                artifactId: string;
                templateId: string;
                templateVersionId: string;
                rendererKey:
                  | "editorial_reading_room_v1"
                  | "personal_authority_v1"
                  | "personal_authority_v2"
                  | "newsroom_publisher_v1"
                  | "blog_article_v1";
                rendererVersion: 1;
                mimeType: "text/html";
                title: string;
                bytes: number;
                sha256: string;
                createdAt: string;
                viewerPath: string;
              },
              {
                artifactId: string;
                templateId: string;
                templateVersionId: string;
                rendererKey:
                  | "editorial_reading_room_v1"
                  | "personal_authority_v1"
                  | "personal_authority_v2"
                  | "newsroom_publisher_v1"
                  | "blog_article_v1";
                rendererVersion: 1;
                mimeType: "text/html";
                title: string;
                bytes: number;
                sha256: string;
                createdAt: string;
                viewerPath: string;
              },
              {
                artifactId: string;
                templateId: string;
                templateVersionId: string;
                rendererKey:
                  | "editorial_reading_room_v1"
                  | "personal_authority_v1"
                  | "personal_authority_v2"
                  | "newsroom_publisher_v1"
                  | "blog_article_v1";
                rendererVersion: 1;
                mimeType: "text/html";
                title: string;
                bytes: number;
                sha256: string;
                createdAt: string;
                viewerPath: string;
              },
              {
                artifactId: string;
                templateId: string;
                templateVersionId: string;
                rendererKey:
                  | "editorial_reading_room_v1"
                  | "personal_authority_v1"
                  | "personal_authority_v2"
                  | "newsroom_publisher_v1"
                  | "blog_article_v1";
                rendererVersion: 1;
                mimeType: "text/html";
                title: string;
                bytes: number;
                sha256: string;
                createdAt: string;
                viewerPath: string;
              },
              {
                artifactId: string;
                templateId: string;
                templateVersionId: string;
                rendererKey:
                  | "editorial_reading_room_v1"
                  | "personal_authority_v1"
                  | "personal_authority_v2"
                  | "newsroom_publisher_v1"
                  | "blog_article_v1";
                rendererVersion: 1;
                mimeType: "text/html";
                title: string;
                bytes: number;
                sha256: string;
                createdAt: string;
                viewerPath: string;
              },
              {
                artifactId: string;
                templateId: string;
                templateVersionId: string;
                rendererKey:
                  | "editorial_reading_room_v1"
                  | "personal_authority_v1"
                  | "personal_authority_v2"
                  | "newsroom_publisher_v1"
                  | "blog_article_v1";
                rendererVersion: 1;
                mimeType: "text/html";
                title: string;
                bytes: number;
                sha256: string;
                createdAt: string;
                viewerPath: string;
              }
            ]
          | [
              {
                artifactId: string;
                templateId: string;
                templateVersionId: string;
                rendererKey:
                  | "editorial_reading_room_v1"
                  | "personal_authority_v1"
                  | "personal_authority_v2"
                  | "newsroom_publisher_v1"
                  | "blog_article_v1";
                rendererVersion: 1;
                mimeType: "text/html";
                title: string;
                bytes: number;
                sha256: string;
                createdAt: string;
                viewerPath: string;
              },
              {
                artifactId: string;
                templateId: string;
                templateVersionId: string;
                rendererKey:
                  | "editorial_reading_room_v1"
                  | "personal_authority_v1"
                  | "personal_authority_v2"
                  | "newsroom_publisher_v1"
                  | "blog_article_v1";
                rendererVersion: 1;
                mimeType: "text/html";
                title: string;
                bytes: number;
                sha256: string;
                createdAt: string;
                viewerPath: string;
              },
              {
                artifactId: string;
                templateId: string;
                templateVersionId: string;
                rendererKey:
                  | "editorial_reading_room_v1"
                  | "personal_authority_v1"
                  | "personal_authority_v2"
                  | "newsroom_publisher_v1"
                  | "blog_article_v1";
                rendererVersion: 1;
                mimeType: "text/html";
                title: string;
                bytes: number;
                sha256: string;
                createdAt: string;
                viewerPath: string;
              },
              {
                artifactId: string;
                templateId: string;
                templateVersionId: string;
                rendererKey:
                  | "editorial_reading_room_v1"
                  | "personal_authority_v1"
                  | "personal_authority_v2"
                  | "newsroom_publisher_v1"
                  | "blog_article_v1";
                rendererVersion: 1;
                mimeType: "text/html";
                title: string;
                bytes: number;
                sha256: string;
                createdAt: string;
                viewerPath: string;
              },
              {
                artifactId: string;
                templateId: string;
                templateVersionId: string;
                rendererKey:
                  | "editorial_reading_room_v1"
                  | "personal_authority_v1"
                  | "personal_authority_v2"
                  | "newsroom_publisher_v1"
                  | "blog_article_v1";
                rendererVersion: 1;
                mimeType: "text/html";
                title: string;
                bytes: number;
                sha256: string;
                createdAt: string;
                viewerPath: string;
              },
              {
                artifactId: string;
                templateId: string;
                templateVersionId: string;
                rendererKey:
                  | "editorial_reading_room_v1"
                  | "personal_authority_v1"
                  | "personal_authority_v2"
                  | "newsroom_publisher_v1"
                  | "blog_article_v1";
                rendererVersion: 1;
                mimeType: "text/html";
                title: string;
                bytes: number;
                sha256: string;
                createdAt: string;
                viewerPath: string;
              },
              {
                artifactId: string;
                templateId: string;
                templateVersionId: string;
                rendererKey:
                  | "editorial_reading_room_v1"
                  | "personal_authority_v1"
                  | "personal_authority_v2"
                  | "newsroom_publisher_v1"
                  | "blog_article_v1";
                rendererVersion: 1;
                mimeType: "text/html";
                title: string;
                bytes: number;
                sha256: string;
                createdAt: string;
                viewerPath: string;
              },
              {
                artifactId: string;
                templateId: string;
                templateVersionId: string;
                rendererKey:
                  | "editorial_reading_room_v1"
                  | "personal_authority_v1"
                  | "personal_authority_v2"
                  | "newsroom_publisher_v1"
                  | "blog_article_v1";
                rendererVersion: 1;
                mimeType: "text/html";
                title: string;
                bytes: number;
                sha256: string;
                createdAt: string;
                viewerPath: string;
              },
              {
                artifactId: string;
                templateId: string;
                templateVersionId: string;
                rendererKey:
                  | "editorial_reading_room_v1"
                  | "personal_authority_v1"
                  | "personal_authority_v2"
                  | "newsroom_publisher_v1"
                  | "blog_article_v1";
                rendererVersion: 1;
                mimeType: "text/html";
                title: string;
                bytes: number;
                sha256: string;
                createdAt: string;
                viewerPath: string;
              }
            ]
          | [
              {
                artifactId: string;
                templateId: string;
                templateVersionId: string;
                rendererKey:
                  | "editorial_reading_room_v1"
                  | "personal_authority_v1"
                  | "personal_authority_v2"
                  | "newsroom_publisher_v1"
                  | "blog_article_v1";
                rendererVersion: 1;
                mimeType: "text/html";
                title: string;
                bytes: number;
                sha256: string;
                createdAt: string;
                viewerPath: string;
              },
              {
                artifactId: string;
                templateId: string;
                templateVersionId: string;
                rendererKey:
                  | "editorial_reading_room_v1"
                  | "personal_authority_v1"
                  | "personal_authority_v2"
                  | "newsroom_publisher_v1"
                  | "blog_article_v1";
                rendererVersion: 1;
                mimeType: "text/html";
                title: string;
                bytes: number;
                sha256: string;
                createdAt: string;
                viewerPath: string;
              },
              {
                artifactId: string;
                templateId: string;
                templateVersionId: string;
                rendererKey:
                  | "editorial_reading_room_v1"
                  | "personal_authority_v1"
                  | "personal_authority_v2"
                  | "newsroom_publisher_v1"
                  | "blog_article_v1";
                rendererVersion: 1;
                mimeType: "text/html";
                title: string;
                bytes: number;
                sha256: string;
                createdAt: string;
                viewerPath: string;
              },
              {
                artifactId: string;
                templateId: string;
                templateVersionId: string;
                rendererKey:
                  | "editorial_reading_room_v1"
                  | "personal_authority_v1"
                  | "personal_authority_v2"
                  | "newsroom_publisher_v1"
                  | "blog_article_v1";
                rendererVersion: 1;
                mimeType: "text/html";
                title: string;
                bytes: number;
                sha256: string;
                createdAt: string;
                viewerPath: string;
              },
              {
                artifactId: string;
                templateId: string;
                templateVersionId: string;
                rendererKey:
                  | "editorial_reading_room_v1"
                  | "personal_authority_v1"
                  | "personal_authority_v2"
                  | "newsroom_publisher_v1"
                  | "blog_article_v1";
                rendererVersion: 1;
                mimeType: "text/html";
                title: string;
                bytes: number;
                sha256: string;
                createdAt: string;
                viewerPath: string;
              },
              {
                artifactId: string;
                templateId: string;
                templateVersionId: string;
                rendererKey:
                  | "editorial_reading_room_v1"
                  | "personal_authority_v1"
                  | "personal_authority_v2"
                  | "newsroom_publisher_v1"
                  | "blog_article_v1";
                rendererVersion: 1;
                mimeType: "text/html";
                title: string;
                bytes: number;
                sha256: string;
                createdAt: string;
                viewerPath: string;
              },
              {
                artifactId: string;
                templateId: string;
                templateVersionId: string;
                rendererKey:
                  | "editorial_reading_room_v1"
                  | "personal_authority_v1"
                  | "personal_authority_v2"
                  | "newsroom_publisher_v1"
                  | "blog_article_v1";
                rendererVersion: 1;
                mimeType: "text/html";
                title: string;
                bytes: number;
                sha256: string;
                createdAt: string;
                viewerPath: string;
              },
              {
                artifactId: string;
                templateId: string;
                templateVersionId: string;
                rendererKey:
                  | "editorial_reading_room_v1"
                  | "personal_authority_v1"
                  | "personal_authority_v2"
                  | "newsroom_publisher_v1"
                  | "blog_article_v1";
                rendererVersion: 1;
                mimeType: "text/html";
                title: string;
                bytes: number;
                sha256: string;
                createdAt: string;
                viewerPath: string;
              },
              {
                artifactId: string;
                templateId: string;
                templateVersionId: string;
                rendererKey:
                  | "editorial_reading_room_v1"
                  | "personal_authority_v1"
                  | "personal_authority_v2"
                  | "newsroom_publisher_v1"
                  | "blog_article_v1";
                rendererVersion: 1;
                mimeType: "text/html";
                title: string;
                bytes: number;
                sha256: string;
                createdAt: string;
                viewerPath: string;
              },
              {
                artifactId: string;
                templateId: string;
                templateVersionId: string;
                rendererKey:
                  | "editorial_reading_room_v1"
                  | "personal_authority_v1"
                  | "personal_authority_v2"
                  | "newsroom_publisher_v1"
                  | "blog_article_v1";
                rendererVersion: 1;
                mimeType: "text/html";
                title: string;
                bytes: number;
                sha256: string;
                createdAt: string;
                viewerPath: string;
              }
            ];
        createdAt: string;
        updatedAt: string;
      }[];
      nextCursor?: string | null;
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
