export interface Input {
  /**
   * The question to ask. It is sent as a real message and should need current information so the assistant searches the web. Required unless session_id is given.
   */
  prompt?: string;
  /**
   * Which assistant to ask when the tool opens the browser itself. ChatGPT and Gemini need no sign-in. Claude needs a saved signed-in profile.
   */
  platform?: "chatgpt" | "claude" | "gemini";
  /**
   * Saved profile name from browser_profile_connect, to ask as a signed-in account. Leave out for ChatGPT and Gemini: they answer signed-out visitors, so no sign-in or setup is needed.
   */
  profile?: string;
  /**
   * Leave out: the tool then opens a browser, asks the prompt, captures and closes the browser in one call. Pass a session id from browser_open only to capture inside a browser you are already driving on chatgpt.com, claude.ai or gemini.google.com.
   */
  session_id?: string;
  /**
   * Longest wait for the answer to finish; the tool returns as soon as the answer ends. Defaults to 150000 when a prompt is sent, 8000 without one. A signed-in answer with web research often takes about a minute.
   */
  wait_ms?: number;
  /**
   * The site being tracked, e.g. example.com. Sources on it are tagged First-party/vendor, and site_outcome says whether it was cited, only looked at, or absent.
   */
  first_party_domain?: string;
  /**
   * Competitor sites, e.g. ["ridgeway.example"]. Sources on them are tagged Competitor, and competitor_sites gives each one's outcome.
   *
   * @maxItems 25
   */
  competitor_domains?: string[];
  /**
   * Brand or product names to look for in the answer text, yours and competitors, e.g. ["Acme", "Ridgeway"]. Each comes back in brand_mentions with whether it was named, how often, and how early.
   *
   * @maxItems 25
   */
  brands?: string[];
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
      platform: "ChatGPT" | "Claude" | "Gemini";
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
       * The text of the answer the assistant gave, with citation markers and layout tags removed; at most 20,000 characters. Empty when the text could not be read.
       */
      answer_text: string;
      /**
       * One entry per name passed in brands. Empty when brands was not passed.
       */
      brand_mentions: {
        brand: string;
        /**
         * Whether the name appears in the answer text as a whole word, ignoring case.
         */
        mentioned: boolean;
        count: number;
        /**
         * Character offset of the first mention in answer_text.
         */
        first_position: number | null;
        /**
         * 1 for the brand named first among the brands passed, 2 for the next, and so on.
         */
        order: number | null;
        /**
         * The words around the first mention.
         */
        context: string;
      }[];
      /**
       * Every web-search sub-query issued, in capture order.
       */
      queries: string[];
      /**
       * Products the assistant looked up to show as product cards. These are shopping lookups, not web searches.
       */
      product_lookups: string[];
      /**
       * Image searches the assistant ran for pictures shown in the answer.
       */
      image_queries: string[];
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
         * URL category: First-party/vendor, Competitor, Government, Education, News/media, Reddit, Forum, Social/video, Encyclopedia, Review site, Local/directory, Retailer, Docs, or Other.
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
         * URL category: First-party/vendor, Competitor, Government, Education, News/media, Reddit, Forum, Social/video, Encyclopedia, Review site, Local/directory, Retailer, Docs, or Other.
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
         * URL category: First-party/vendor, Competitor, Government, Education, News/media, Reddit, Forum, Social/video, Encyclopedia, Review site, Local/directory, Retailer, Docs, or Other.
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
       * For first_party_domain: cited in the answer, researched (looked at but not cited), or absent. Null when first_party_domain was not passed.
       */
      site_outcome: ("cited" | "researched" | "absent") | null;
      /**
       * One entry per domain passed in competitor_domains.
       */
      competitor_sites: {
        domain: string;
        outcome: "cited" | "researched" | "absent";
        times_cited: number;
      }[];
      /**
       * True when the sources include the tracked site, a listed competitor, or a known retailer. False means the assistant leaned only on non-commercial sources as far as these lists can tell.
       */
      commercial_sites_listed: boolean;
      /**
       * True when this call opened its own browser and closed it afterwards, so no browser time keeps running.
       */
      browser_closed?: boolean;
      /**
       * mention_check for a signed-out run, full_fanout for a run through a saved profile. Present when the tool opened its own browser.
       */
      check_type?: ("mention_check" | "full_fanout") | null;
      /**
       * Credits charged for this run: the flat price for its check_type. Present when the tool opened its own browser.
       */
      charged_credits?: number | null;
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
