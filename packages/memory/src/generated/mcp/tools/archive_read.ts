export interface Input {
  /**
   * Preferred: private artifactId returned by check_site_export. The server reauthorizes ownership on every read.
   */
  artifactId?: string;
  /**
   * Fallback: bounded public HTTPS ZIP URL. Use artifactId for MCP Scraper-owned exports.
   */
  url?: string;
  /**
   * Exact ZIP entry path to read. Omit to list the archive. Use a path returned by a previous archive_read listing.
   */
  path?: string;
  /**
   * Byte offset for a text-file read. Continue from nextOffset until it is null. Ignored when path is omitted.
   */
  offset?: number;
  /**
   * Maximum UTF-8 bytes to return from the selected text file. Default 50,000; maximum 200,000.
   */
  maxBytes?: number;
  /**
   * Maximum entry rows returned when listing. The server still validates the complete archive. Default 200; maximum 1,000.
   */
  maxEntries?: number;
  /**
   * Store the complete selected text file in the tenant Library vault through library-ingest. Requires path. Preserves the ZIP URL and entry path as source provenance.
   */
  depositToLibrary?: boolean;
}

export type Output =
  | {
      mode: "list" | "read";
      /**
       * Public ZIP URL or private artifactId used for this read.
       */
      archiveUrl: string;
      artifactId?: string;
      compressedBytes: number;
      entryCount: number;
      totalUncompressedBytes: number;
      entries?: {
        path: string;
        directory: boolean;
        compressedBytes: number;
        uncompressedBytes: number;
        contentType: string | null;
        readable: boolean;
        modifiedAt: string | null;
      }[];
      entriesTruncated?: boolean;
      path?: string;
      contentType?: string;
      fileBytes?: number;
      offset?: number;
      content?: string;
      nextOffset?: number | null;
      memory?: {
        deposited: boolean;
        vault?: string;
        noteId?: string;
        path?: string;
        chunks?: number;
        error?: string;
      };
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
