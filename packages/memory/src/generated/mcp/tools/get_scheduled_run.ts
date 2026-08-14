export interface Input {
  /**
   * Opaque scheduled-run identifier returned by a scheduled-results tool.
   */
  runId: string;
}

export interface Output {
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
            /**
             * Registered preset key returned by list_artifact_templates.
             */
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
            /**
             * Registered preset key returned by list_artifact_templates.
             */
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
            /**
             * Registered preset key returned by list_artifact_templates.
             */
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
            /**
             * Registered preset key returned by list_artifact_templates.
             */
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
            /**
             * Registered preset key returned by list_artifact_templates.
             */
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
            /**
             * Registered preset key returned by list_artifact_templates.
             */
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
            /**
             * Registered preset key returned by list_artifact_templates.
             */
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
            /**
             * Registered preset key returned by list_artifact_templates.
             */
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
            /**
             * Registered preset key returned by list_artifact_templates.
             */
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
            /**
             * Registered preset key returned by list_artifact_templates.
             */
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
            /**
             * Registered preset key returned by list_artifact_templates.
             */
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
            /**
             * Registered preset key returned by list_artifact_templates.
             */
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
            /**
             * Registered preset key returned by list_artifact_templates.
             */
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
            /**
             * Registered preset key returned by list_artifact_templates.
             */
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
            /**
             * Registered preset key returned by list_artifact_templates.
             */
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
            /**
             * Registered preset key returned by list_artifact_templates.
             */
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
            /**
             * Registered preset key returned by list_artifact_templates.
             */
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
            /**
             * Registered preset key returned by list_artifact_templates.
             */
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
            /**
             * Registered preset key returned by list_artifact_templates.
             */
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
            /**
             * Registered preset key returned by list_artifact_templates.
             */
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
            /**
             * Registered preset key returned by list_artifact_templates.
             */
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
            /**
             * Registered preset key returned by list_artifact_templates.
             */
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
            /**
             * Registered preset key returned by list_artifact_templates.
             */
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
            /**
             * Registered preset key returned by list_artifact_templates.
             */
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
            /**
             * Registered preset key returned by list_artifact_templates.
             */
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
            /**
             * Registered preset key returned by list_artifact_templates.
             */
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
            /**
             * Registered preset key returned by list_artifact_templates.
             */
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
            /**
             * Registered preset key returned by list_artifact_templates.
             */
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
            /**
             * Registered preset key returned by list_artifact_templates.
             */
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
            /**
             * Registered preset key returned by list_artifact_templates.
             */
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
            /**
             * Registered preset key returned by list_artifact_templates.
             */
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
            /**
             * Registered preset key returned by list_artifact_templates.
             */
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
            /**
             * Registered preset key returned by list_artifact_templates.
             */
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
            /**
             * Registered preset key returned by list_artifact_templates.
             */
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
            /**
             * Registered preset key returned by list_artifact_templates.
             */
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
            /**
             * Registered preset key returned by list_artifact_templates.
             */
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
            /**
             * Registered preset key returned by list_artifact_templates.
             */
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
            /**
             * Registered preset key returned by list_artifact_templates.
             */
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
            /**
             * Registered preset key returned by list_artifact_templates.
             */
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
            /**
             * Registered preset key returned by list_artifact_templates.
             */
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
            /**
             * Registered preset key returned by list_artifact_templates.
             */
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
            /**
             * Registered preset key returned by list_artifact_templates.
             */
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
            /**
             * Registered preset key returned by list_artifact_templates.
             */
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
            /**
             * Registered preset key returned by list_artifact_templates.
             */
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
            /**
             * Registered preset key returned by list_artifact_templates.
             */
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
            /**
             * Registered preset key returned by list_artifact_templates.
             */
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
            /**
             * Registered preset key returned by list_artifact_templates.
             */
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
            /**
             * Registered preset key returned by list_artifact_templates.
             */
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
            /**
             * Registered preset key returned by list_artifact_templates.
             */
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
            /**
             * Registered preset key returned by list_artifact_templates.
             */
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
            /**
             * Registered preset key returned by list_artifact_templates.
             */
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
            /**
             * Registered preset key returned by list_artifact_templates.
             */
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
            /**
             * Registered preset key returned by list_artifact_templates.
             */
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
            /**
             * Registered preset key returned by list_artifact_templates.
             */
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
            /**
             * Registered preset key returned by list_artifact_templates.
             */
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
