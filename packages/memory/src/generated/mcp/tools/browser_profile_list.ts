export interface Input {
  /**
   * Profile whose saved logins to list. Omit to derive from email.
   */
  profile?: string;
  /**
   * Account email used to derive the profile name when profile is not given.
   */
  email?: string;
  /**
   * Restrict to one site login, e.g. chatgpt.com. Use this to poll a single login until its status reads AUTHENTICATED.
   */
  domain?: string;
  /**
   * A specific login connection id returned by browser_profile_connect, to poll just that one.
   */
  connection_id?: string;
}

export interface Output {
  ok: boolean;
  tool: "browser_profile_list";
  session_id: null;
  /**
   * Profile these logins belong to.
   */
  profile: string;
  /**
   * All site logins saved in this profile, each with its current auth status and note.
   */
  connections: {
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
  count: number;
}
