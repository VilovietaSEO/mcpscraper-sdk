export interface Input {
  /**
   * Optional category whose required canonical tag and contract details should be selected.
   */
  category?: "home" | "professional" | "restaurants" | "financial" | "realestate" | "auto" | "wellness";
}

export interface Output {
  [k: string]: unknown;
}
