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

export type Output = unknown
