export interface Input {}

export interface Output {
  ok: boolean;
  tool: "serp_identity_list";
  session_id: null;
  identities: {
    name: string;
    country: string;
    proxy_type: "static_isp";
    profile_persistence: "cookies_and_storage";
    ip_persistence: "fixed_for_identity_lifetime";
    status: "ready" | "deleting" | "error";
    created_at: string;
    last_used_at: string | null;
  }[];
  count: number;
}
