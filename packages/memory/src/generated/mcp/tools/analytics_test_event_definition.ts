export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * Event definition id returned by analytics_list_event_definitions.
   */
  definitionId: string;
  /**
   * Bare hostname observed by the browser.
   */
  hostname: string;
  /**
   * URL path observed by the browser.
   */
  path: string;
  /**
   * Trigger interaction being previewed.
   */
  triggerKind: "page" | "click" | "form" | "semantic";
  /**
   * Validated data-xray-event name observed by the browser.
   */
  tagEventName?: string;
  /**
   * The browser-reported match result. The server never receives HTML or evaluates a selector.
   */
  selectorMatched?: boolean;
}

export interface Output {
  ok: boolean;
}
