export interface Input {}

export interface Output {
  /**
   * True on success; false on auth error.
   */
  ok: boolean;
  /**
   * The schedule link. Present only the first time a link is minted for this identity.
   */
  url?: string;
  /**
   * True when a link already exists and was NOT re-shown. Use revoke-schedule-link then call this again to get a fresh one.
   */
  alreadyExists?: boolean;
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
