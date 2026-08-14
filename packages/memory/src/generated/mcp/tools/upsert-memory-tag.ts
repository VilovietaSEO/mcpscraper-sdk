export interface Input {
  /**
   * Canonical tag name to create or curate.
   */
  tag: string;
  /**
   * Human-readable summary that distinguishes this record from similarly named records.
   */
  description?: string;
  /**
   * Alternative spellings that should resolve to this canonical value.
   */
  aliases?: string[];
  /**
   * Lifecycle status used to filter or update the selected records.
   */
  status?: "active" | "deprecated";
}

export interface Output {
  ok: boolean;
  tag?: {
    tag: string;
    description: string | null;
    aliases: string[];
    status: "active" | "deprecated";
  };
  error?: string;
}
