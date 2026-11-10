export interface Input {}

export type Output =
  | {
      /**
       * True on success; false on auth error.
       */
      ok: boolean;
      /**
       * Notes shared with you and accepted. Present when ok is true.
       */
      notes?: {
        /**
         * Pass this as shareId to memory-get/memory-put/delete-note/unlink-share.
         */
        shareId: string;
        /**
         * Identity who shared the note.
         */
        owner: string;
        /**
         * Note title.
         */
        title: string;
        /**
         * Your permissions on this note.
         */
        permissions: {
          read: boolean;
          edit: boolean;
          delete: boolean;
          reshare: boolean;
        };
        /**
         * Current revision (pass as baseRevision when editing).
         */
        revision: number;
        /**
         * Last update timestamp.
         */
        updatedAt: string;
      }[];
      /**
       * Human-readable failure reason when ok is false.
       */
      error?: string;
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
