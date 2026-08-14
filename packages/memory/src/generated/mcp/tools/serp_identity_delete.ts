export interface Input {
  /**
   * Identity name returned by serp_identity_list.
   */
  name: string;
  /**
   * Must be true because deletion permanently removes the saved browser state and its fixed proxy.
   */
  confirm: true;
}

export interface Output {
  ok: boolean;
  tool: "serp_identity_delete";
  session_id: null;
  name: string;
  deleted: boolean;
}
