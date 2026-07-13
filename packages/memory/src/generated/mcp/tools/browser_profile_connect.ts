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

export type Output = unknown
