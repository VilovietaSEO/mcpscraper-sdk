export interface Input {
  /**
   * Use search for topic/keyword requests. Use channel when the user provides @handle, channel ID, or channel URL.
   */
  mode: "search" | "channel";
  /**
   * Required when mode is search. The YouTube search topic in the user’s words.
   */
  query?: string;
  /**
   * YouTube channel handle, channel ID, or URL. Examples: @mkbhd, UC..., https://youtube.com/@mkbhd.
   */
  channelHandle?: string;
  /**
   * Number of videos to return. Default 50, maximum 500.
   */
  maxVideos?: number;
}

export type Output =
  | {
      mode: string;
      videoCount: number;
      channel: {
        title: string | null;
        subscriberCount: string | null;
      } | null;
      videos: {
        videoId: string;
        title: string;
        channelName: string | null;
        views: string | null;
        duration: string | null;
        url: string | null;
      }[];
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
