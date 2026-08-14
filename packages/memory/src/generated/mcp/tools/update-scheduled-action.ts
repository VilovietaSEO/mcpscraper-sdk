export interface Input {
  /**
   * The scheduled action id.
   */
  id: string;
  /**
   * Human-readable summary that distinguishes this record from similarly named records.
   */
  description?: string;
  /**
   * Exact accessible Memory vault name; omit only when this tool documents a safe active-vault default.
   */
  vault?: string;
  /**
   * New execution cadence; omit to preserve the scheduled action cadence.
   */
  cadence?: "once" | "daily" | "weekly" | "monthly";
  /**
   * Local execution time in 24-hour HH:MM form; null clears the stored time.
   */
  timeOfDay?: string | null;
  /**
   * IANA timezone for schedule evaluation; omit to preserve the current timezone.
   */
  timezone?: string;
  /**
   * Explicit HTML artifact choice; omit to preserve the current selection.
   */
  artifactSelection?:
    | {
        /**
         * Operation mode selected for this nested request branch.
         */
        mode: "none";
      }
    | {
        /**
         * Operation mode selected for this nested request branch.
         */
        mode: "saved_template";
        /**
         * Opaque saved-template identifier returned by an artifact-template tool.
         */
        templateId: string;
        /**
         * Immutable saved-template version selected for rendering.
         */
        templateVersionId: string;
      };
}

export interface Output {
  ok: boolean;
  artifactSelection?:
    | {
        /**
         * Operation mode selected for this nested request branch.
         */
        mode: "none";
      }
    | {
        /**
         * Operation mode selected for this nested request branch.
         */
        mode: "saved_template";
        /**
         * Opaque saved-template identifier returned by an artifact-template tool.
         */
        templateId: string;
        /**
         * Immutable saved-template version selected for rendering.
         */
        templateVersionId: string;
      };
  error?: string;
  errorCode?: string;
}
