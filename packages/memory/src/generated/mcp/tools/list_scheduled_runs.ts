export interface Input {
  view?: "inbox" | "all" | "archived";
  status?: "running" | "succeeded" | "no_output" | "partial" | "billing_stopped" | "failed";
  scheduleId?: string;
  templateId?: string;
  from?: string;
  to?: string;
  query?: string;
  cursor?: string;
  limit?: number;
}

export type Output = {
  [k: string]: unknown;
} & {
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
    /**
     * No rendered artifact, or one exact immutable saved template version. This does not disable Memory-note output.
     */
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
            rendererKey: "editorial_reading_room_v1";
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
            rendererKey: "editorial_reading_room_v1";
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
            rendererKey: "editorial_reading_room_v1";
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
            rendererKey: "editorial_reading_room_v1";
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
            rendererKey: "editorial_reading_room_v1";
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
            rendererKey: "editorial_reading_room_v1";
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
            rendererKey: "editorial_reading_room_v1";
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
            rendererKey: "editorial_reading_room_v1";
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
            rendererKey: "editorial_reading_room_v1";
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
            rendererKey: "editorial_reading_room_v1";
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
            rendererKey: "editorial_reading_room_v1";
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
            rendererKey: "editorial_reading_room_v1";
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
            rendererKey: "editorial_reading_room_v1";
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
            rendererKey: "editorial_reading_room_v1";
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
            rendererKey: "editorial_reading_room_v1";
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
            rendererKey: "editorial_reading_room_v1";
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
            rendererKey: "editorial_reading_room_v1";
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
            rendererKey: "editorial_reading_room_v1";
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
            rendererKey: "editorial_reading_room_v1";
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
            rendererKey: "editorial_reading_room_v1";
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
            rendererKey: "editorial_reading_room_v1";
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
            rendererKey: "editorial_reading_room_v1";
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
            rendererKey: "editorial_reading_room_v1";
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
            rendererKey: "editorial_reading_room_v1";
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
            rendererKey: "editorial_reading_room_v1";
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
            rendererKey: "editorial_reading_room_v1";
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
            rendererKey: "editorial_reading_room_v1";
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
            rendererKey: "editorial_reading_room_v1";
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
            rendererKey: "editorial_reading_room_v1";
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
            rendererKey: "editorial_reading_room_v1";
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
            rendererKey: "editorial_reading_room_v1";
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
            rendererKey: "editorial_reading_room_v1";
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
            rendererKey: "editorial_reading_room_v1";
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
            rendererKey: "editorial_reading_room_v1";
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
            rendererKey: "editorial_reading_room_v1";
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
            rendererKey: "editorial_reading_room_v1";
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
            rendererKey: "editorial_reading_room_v1";
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
            rendererKey: "editorial_reading_room_v1";
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
            rendererKey: "editorial_reading_room_v1";
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
            rendererKey: "editorial_reading_room_v1";
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
            rendererKey: "editorial_reading_room_v1";
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
            rendererKey: "editorial_reading_room_v1";
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
            rendererKey: "editorial_reading_room_v1";
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
            rendererKey: "editorial_reading_room_v1";
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
            rendererKey: "editorial_reading_room_v1";
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
            rendererKey: "editorial_reading_room_v1";
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
            rendererKey: "editorial_reading_room_v1";
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
            rendererKey: "editorial_reading_room_v1";
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
            rendererKey: "editorial_reading_room_v1";
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
            rendererKey: "editorial_reading_room_v1";
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
            rendererKey: "editorial_reading_room_v1";
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
            rendererKey: "editorial_reading_room_v1";
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
            rendererKey: "editorial_reading_room_v1";
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
            rendererKey: "editorial_reading_room_v1";
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
            rendererKey: "editorial_reading_room_v1";
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
};
