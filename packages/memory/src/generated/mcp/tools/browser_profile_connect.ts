export interface Input {
  /**
   * Account email for the login. Derives a stable profile name and is recorded as a note. Does NOT import existing cookies — the user signs in fresh.
   */
  email?: string;
  /**
   * Profile to add this login to. Omit to derive from email. A single profile holds MANY logins — pass the same name with a different domain to stack accounts.
   */
  profile?: string;
  /**
   * Site to log into, e.g. chatgpt.com, claude.ai, reddit.com. Defaults to chatgpt.com.
   */
  domain?: string;
  /**
   * Login page for the domain. Defaults to https://<domain>/.
   */
  login_url?: string;
  /**
   * Deprecated alias for login_url.
   */
  url?: string;
  /**
   * Free-text note describing this login. Surfaced by browser_profile_list.
   */
  note?: string;
  /**
   * Optional human label for this sign-in setup session.
   */
  label?: string;
  /**
   * Sign-in session lifetime before auto-termination. Defaults to 600.
   */
  timeout_seconds?: number;
}

export interface Output {
  ok: boolean;
  tool: "browser_profile_connect";
  /**
   * The underlying live browser session id backing this sign-in.
   */
  session_id: string | null;
  auth_connection_id: string;
  /**
   * mcpscraper.dev sign-in link to give the user so they can complete this login.
   */
  watch_url: string;
  /**
   * Deprecated; always null. Open watch_url to view the sign-in.
   */
  live_view_url: string | null;
  /**
   * Profile this login was added to. Reuse it to stack more logins or to open a session.
   */
  profile: string;
  domain: string;
  setup_url: string;
  account_email: string | null;
  note: string | null;
  status: string;
  /**
   * Deprecated; always null.
   */
  flow_status: string | null;
  /**
   * Deprecated; always null.
   */
  flow_step: string | null;
  /**
   * Deprecated; always null.
   */
  flow_expires_at: string | null;
  /**
   * Deprecated; always null.
   */
  post_login_url: string | null;
  /**
   * Every login currently saved in this profile, so you can see what else is connected.
   */
  connected_logins: {
    /**
     * Auth connection id for this login.
     */
    connection_id: string | null;
    /**
     * Site this login is for, e.g. chatgpt.com.
     */
    domain: string;
    /**
     * Auth status, e.g. NEEDS_AUTH or AUTHENTICATED.
     */
    status: string;
    /**
     * Account email recorded for this login, when known.
     */
    account_email: string | null;
    /**
     * Free-text note describing this login.
     */
    note: string | null;
    /**
     * mcpscraper.dev sign-in link when this login still needs the user to authenticate.
     */
    watch_url: string | null;
    /**
     * When this login was last saved or refreshed.
     */
    last_connected_at: string | null;
  }[];
  next_steps: string[];
  raw?: {
    [k: string]: unknown;
  };
}
