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

export type Output = unknown
