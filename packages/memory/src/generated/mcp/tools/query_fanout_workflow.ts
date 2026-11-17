export interface Input {
  /**
   * The question to ask. It is sent as a real message and should need current information so the assistant searches the web. Required unless session_id is given.
   */
  prompt?: string;
  /**
   * Which assistant to ask when the tool opens the browser itself. Claude needs a saved signed-in profile.
   */
  platform?: "chatgpt" | "claude";
  /**
   * Saved profile name from browser_profile_connect, to ask as a signed-in account. Leave out for ChatGPT: it answers signed-out visitors, so no sign-in or setup is needed.
   */
  profile?: string;
  /**
   * Leave out: the tool then opens a browser, asks the prompt, captures and closes the browser in one call. Pass a session id from browser_open only to capture inside a browser you are already driving on chatgpt.com or claude.ai.
   */
  session_id?: string;
  /**
   * Longest wait for the answer to finish; the tool returns as soon as the answer ends. Defaults to 90000 when a prompt is sent, 8000 without one.
   */
  wait_ms?: number;
  /**
   * The brand/site being researched, e.g. example.com — sources on this domain are tagged First-party/vendor.
   */
  first_party_domain?: string;
  /**
   * Clear any previously buffered stream for this page before capturing.
   */
  reset?: boolean;
  /**
   * When using the installed local MCP server, write JSON/CSV/TSV/HTML exports to MCP_SCRAPER_OUTPUT_DIR/fanout. Hosted clients such as ChatGPT always receive the complete structured result inline and leave exports null.
   */
  export?: boolean;
}

export type Output =
  | {
      /**
       * Whether the browser-agent action succeeded.
       */
      ok: boolean;
      tool: "query_fanout_workflow";
      /**
       * Browser session id when the response is scoped to a session.
       */
      session_id: string | null;
      /**
       * Which AI-search surface the fan-out was captured from.
       */
      platform: "ChatGPT" | "Claude";
      captured_at: string;
      /**
       * The user prompt that triggered the captured fan-out, when recoverable.
       */
      prompt: string;
      meta: {
        model: string;
        finishType: string;
        title: string;
        rounds: number;
      };
      /**
       * Every web-search sub-query issued, in capture order.
       */
      queries: string[];
      /**
       * Every researched URL, cited first.
       */
      browsed_urls: {
        url: string;
        domain: string;
        title: string;
        cited: boolean;
        timesCited: number;
        snippet: string;
        round: number | null;
        /**
         * URL category: First-party/vendor, News/media, Reddit, Social/video, Encyclopedia, Review site, Docs, or Blog.
         */
        siteType: string;
      }[];
      /**
       * Researched URLs cited in the final answer.
       */
      cited_urls: {
        url: string;
        domain: string;
        title: string;
        cited: boolean;
        timesCited: number;
        snippet: string;
        round: number | null;
        /**
         * URL category: First-party/vendor, News/media, Reddit, Social/video, Encyclopedia, Review site, Docs, or Blog.
         */
        siteType: string;
      }[];
      /**
       * Researched URLs pulled but not cited.
       */
      browsed_only: {
        url: string;
        domain: string;
        title: string;
        cited: boolean;
        timesCited: number;
        snippet: string;
        round: number | null;
        /**
         * URL category: First-party/vendor, News/media, Reddit, Social/video, Encyclopedia, Review site, Docs, or Blog.
         */
        siteType: string;
      }[];
      snippets: {
        url: string;
        domain: string;
        title: string;
        text: string;
      }[];
      counts: {
        subQueries: number;
        browsed: number;
        cited: number;
        browsedOnly: number;
      };
      /**
       * Objective aggregates: top sourced sites by frequency, citation order, and URL-category counts.
       */
      aggregates: {
        topSites: {
          domain: string;
          count: number;
          cited: boolean;
          timesCited: number;
          siteType: string;
        }[];
        citationOrder: {
          rank: number;
          domain: string;
          url: string;
          timesCited: number;
        }[];
        byCategory: {
          [k: string]: number;
        };
      };
      first_party_domain: string | null;
      /**
       * True when this call opened its own browser and closed it afterwards, so no browser time keeps running.
       */
      browser_closed?: boolean;
      /**
       * Non-fatal local export failure. The inline capture remains complete when this is present.
       */
      export_error?: string | null;
      /**
       * Local-only export paths when export=true, otherwise null. Hosted clients receive the complete structured result inline instead of inaccessible server paths.
       */
      exports: {
        relativeTo: string;
        dir: string;
        json: string;
        queriesCsv: string;
        queriesTsv: string;
        citationsCsv: string;
        sourcesCsv: string;
        browsedOnlyCsv: string;
        snippetsCsv: string;
        domainsCsv: string;
        report: string;
      } | null;
      debug?: {
        interceptorReady: boolean;
        rawBytes: number;
        unmappedKeys: string[];
        note: string;
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
