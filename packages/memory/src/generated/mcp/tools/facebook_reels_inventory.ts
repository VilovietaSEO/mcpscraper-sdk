export interface Input {
  /**
   * Public Facebook profile or Page URL whose Reel URLs should be collected. Do not pass an individual Reel, video, post, share, group, or event URL.
   */
  url: string;
  /**
   * Maximum Reel URLs requested. Logged-out collection is capped at 60 even when this is higher; a valid saved Facebook browser profile can continue toward the requested maximum.
   */
  maxUrls?: number;
  /**
   * Optional saved hosted browser profile name containing a Facebook login. Set one up with browser_profile_connect first. An expired or logged-out profile falls back to the anonymous 60-URL cap.
   */
  profile?: string;
  /**
   * Save browser changes back to the hosted profile. Leave unset unless intentionally updating the saved Facebook login.
   */
  saveProfileChanges?: boolean;
  /**
   * Previously returned Reel URLs to retain and deduplicate while continuing an interrupted collection.
   *
   * @maxItems 2000
   */
  resumeUrls?: string[];
  /**
   * Safety ceiling for pagination attempts. Default 250; collection normally stops earlier at maxUrls or a Facebook access boundary.
   */
  maxScrolls?: number;
  /**
   * Delay after each scroll before collecting the next DOM batch.
   */
  scrollDelayMs?: number;
  /**
   * Stop after this many consecutive pagination attempts add no Reel URLs.
   */
  stableScrollLimit?: number;
}

export type Output =
  | {
      sourceUrl: string;
      profileUrl: string;
      pageUrl: string;
      profileName: string | null;
      browser: {
        mode: "hosted";
        requestedMode: "hosted";
        profileName: string | null;
        profileSource: "hosted";
      };
      requestedMaxUrls: number;
      effectiveMaxUrls: number;
      anonymousCap: 60;
      anonymousCapApplied: boolean;
      savedProfileRequested: boolean;
      authenticationStatus: "authenticated" | "logged_out" | "unknown";
      collectedUrlCount: number;
      resumedUrlCount: number;
      newlyCollectedUrlCount: number;
      complete: boolean;
      partial: boolean;
      stoppedReason:
        | "max_urls"
        | "anonymous_cap"
        | "deadline"
        | "login_wall"
        | "stable_scrolls"
        | "max_scrolls"
        | "no_scrolls"
        | "navigation_error"
        | "browser_error";
      pagination: {
        maxScrolls: number;
        attemptedScrolls: number;
        stableScrolls: number;
        stableScrollLimit: number;
        scrollDelayMs: number;
        stages: {
          stage: string;
          itemCount: number;
          addedCount: number;
          scrollY: number | null;
          scrollHeight: number | null;
          loginWallVisible: boolean;
          dismissibleLoginOverlayVisible: boolean;
        }[];
      };
      items: {
        url: string;
        reelId: string;
        viewCountText: string | null;
        anchorText: string | null;
        firstSeenStage: string;
      }[];
      limitations: string[];
      recoverableError: {
        stage: string;
        message: string;
      } | null;
      extractedAt: string;
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
