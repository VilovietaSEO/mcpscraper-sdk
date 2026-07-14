export interface Input {}

export interface Output {
  ok: boolean;
  tool: "browser_extension_list";
  session_id: null;
  /**
   * Every extension available to load via extension_names on browser_open.
   */
  extensions: {
    name: string;
    /**
     * Always "store" for extensions added via browser_extension_import.
     */
    source: string;
    source_url: string | null;
    size_bytes: number | null;
    created_at: string;
  }[];
  count: number;
}
