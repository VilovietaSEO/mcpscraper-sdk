export interface Input {
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
