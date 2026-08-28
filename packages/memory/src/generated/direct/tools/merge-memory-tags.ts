export interface Input {
  apiKey?: string;
  sessionId?: string;
  /**
   * The duplicate tag to retire.
   */
  from: string;
  /**
   * The canonical tag to keep. Every note using "from" is retagged to this.
   */
  into: string;
}

export interface Output {
  ok: boolean;
  from?: string;
  into?: string;
  notesRetagged?: number;
  aliases?: string[];
  descriptionCopied?: boolean;
  error?: string;
}
