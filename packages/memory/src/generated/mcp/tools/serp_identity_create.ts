export interface Input {
  /**
   * Stable caller-facing name, e.g. google-us-primary.
   */
  name: string;
  /**
   * Two-letter country for the static network identity. Defaults to US.
   */
  country?: string;
}

export interface Output {
  ok: boolean;
  tool: "serp_identity_create";
  /**
   * Live Google takeover session opened on the new persistent identity.
   */
  session_id: string;
  /**
   * Give this URL to the user so they can clear consent or CAPTCHA directly on google.com.
   */
  watch_url: string;
  url: "https://www.google.com/";
  identity: {
    name: string;
    country: string;
    proxy_type: "static_isp";
    profile_persistence: "cookies_and_storage";
    ip_persistence: "fixed_for_identity_lifetime";
    status: "ready" | "deleting" | "error";
    created_at: string;
    last_used_at: string | null;
  };
  next_steps: string[];
}
