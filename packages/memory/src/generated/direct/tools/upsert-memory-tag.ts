export interface Input {
  apiKey?: string;
  sessionId?: string;
  tag: string;
  description?: string;
  aliases?: string[];
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
