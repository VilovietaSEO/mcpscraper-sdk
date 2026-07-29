export interface Input {
  /**
   * Which part of the reusable editorial-reading-room guide to return. Start with workflow; fetch the content contract or compact example only when needed.
   */
  focus?: "workflow" | "content_contract" | "example";
}

export interface Output {
  ok: boolean;
  focus: "workflow" | "content_contract" | "example";
  guide: string;
}
