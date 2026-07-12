export interface Input {
  /**
   * Chrome Web Store URL of the extension to add, e.g. https://chromewebstore.google.com/detail/<slug>/<id>.
   */
  store_url: string;
  /**
   * Short name to save this extension under, e.g. "ani-ai". Reuse it later in extension_names on browser_open.
   */
  name: string;
}

export interface Output {
  ok: boolean;
  tool: "browser_extension_import";
  session_id: null;
  /**
   * The name this extension was saved under.
   */
  name: string;
  /**
   * The store URL this extension was imported from.
   */
  source_url: string;
  /**
   * Size of the extension package in bytes.
   */
  size_bytes: number | null;
}
