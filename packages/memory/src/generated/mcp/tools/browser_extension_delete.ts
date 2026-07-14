export interface Input {
  /**
   * Name of the extension to remove, as returned by browser_extension_list.
   */
  name: string;
}

export interface Output {
  ok: boolean;
  tool: "browser_extension_delete";
  session_id: null;
  name: string;
  deleted: boolean;
}
