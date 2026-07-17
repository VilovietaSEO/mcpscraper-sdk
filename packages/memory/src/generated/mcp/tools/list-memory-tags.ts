export interface Input {
  /**
   * Include deprecated tags as well as active tags. Defaults true so the AI sees the complete vocabulary; pass false only for an active-only display.
   */
  includeDeprecated?: boolean;
}

export interface Output {
  ok: boolean;
  tags?: {
    tag: string;
    description: string | null;
    aliases: string[];
    status: "active" | "deprecated";
    usageCount: number;
    vaultUsage: {
      [k: string]: number;
    };
  }[];
  error?: string;
}
