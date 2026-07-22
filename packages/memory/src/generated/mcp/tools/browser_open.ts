export interface Input {
  /**
   * Optional human label for this session, shown in the watch console.
   */
  label?: string;
  /**
   * Optional URL to navigate to immediately after opening.
   */
  url?: string;
  /**
   * Optional saved hosted profile name to load a logged-in session for a site.
   */
  profile?: string;
  /**
   * Persist cookies/storage back to the named profile on close. Avoid parallel sessions writing to the same profile.
   */
  save_profile_changes?: boolean;
  /**
   * Session lifetime before auto-termination. Defaults to 600.
   */
  timeout_seconds?: number;
  /**
   * Names of extensions previously added with browser_extension_import (see browser_extension_list for what's available) to load into this session. Loading extensions restarts the browser, adding a few seconds to startup.
   */
  extension_names?: string[];
}

export interface Output {
  ok: boolean;
  tool: "browser_open";
  /**
   * Session id returned by browser_open. Use only this exact value in later browser_* calls; do not construct one yourself.
   */
  session_id: string;
  /**
   * Human watch/takeover URL for this browser session on mcpscraper.dev.
   */
  watch_url: string;
  /**
   * Deprecated; always null. Open watch_url to view the live session.
   */
  live_view_url: string | null;
  /**
   * Initial URL requested by the caller, when provided.
   */
  url: string | null;
  hint: string;
  raw?: {
    [k: string]: unknown;
  };
}
