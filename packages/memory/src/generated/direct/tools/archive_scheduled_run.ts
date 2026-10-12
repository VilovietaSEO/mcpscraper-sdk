export interface Input {
  apiKey?: string;
  sessionId?: string;
  runId: string;
  /**
   * True to archive the result; false to restore it.
   */
  archived: boolean;
}

export type Output =
  | {
      ok: boolean;
      run?: {
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
      };
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
    }
  | {
      idempotencyKey?: string;
      operation?: {
        runId: string | null;
        idempotencyKey: string;
        state: string;
      };
      error_code: string;
      error_type: string;
      message: string;
      retryable: boolean;
      retry_after_seconds?: number;
      charge_status?: string;
      details?: {
        [k: string]: unknown;
      };
    };
