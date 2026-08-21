export interface Input {
  /**
   * Proposal id returned by commons_submit_entity, in the form commons-proposal-<uuid>.
   */
  proposalId: string;
}

export interface Output {
  ok: boolean;
  data?: unknown;
  error?: string;
  message?: string;
}
