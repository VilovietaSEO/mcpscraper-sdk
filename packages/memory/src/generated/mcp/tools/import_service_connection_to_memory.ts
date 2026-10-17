export interface Input {
  /**
   * A tenant-owned connectionId from list_service_connections.
   */
  connectionId: string;
  /**
   * The exact providerConfigKey returned with that connection. It is matched together with connectionId against the authenticated caller.
   */
  providerConfigKey: string;
  /**
   * One exact current readTools entry for that connection. Actions, admin tools, and unlisted names are rejected.
   */
  tool: string;
  /**
   * JSON arguments for one bounded provider read. The serialized object may be at most 64 KiB.
   */
  args?: {
    [k: string]: unknown;
  };
  /**
   * An existing ordinary Memory vault the caller can write and index. Secure and channel vaults are rejected because this tool creates searchable RAG content.
   */
  vault: string;
  /**
   * Optional human-readable snapshot title. The server always chooses the stable storage path.
   */
  title?: string;
}

export type Output =
  | {
      ok: boolean;
      stored?: boolean;
      status?: "search_ready" | "stored_not_indexed";
      searchReady?: boolean;
      providerConfigKey?: string;
      connectionId?: string;
      tool?: string;
      vault?: string;
      path?: string;
      sourceBytes?: number;
      contentSha256?: string;
      indexedChunks?: number;
      importedAt?: string;
      untrustedContent?: true;
      warning?: string;
      errorCode?: string;
      retryable?: boolean;
      error: string | null;
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
