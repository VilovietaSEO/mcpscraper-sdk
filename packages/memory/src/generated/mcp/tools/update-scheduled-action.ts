export interface Input {
  /**
   * The scheduled action id.
   */
  id: string;
  description?: string;
  vault?: string;
  cadence?: "once" | "daily" | "weekly" | "monthly";
  timeOfDay?: string | null;
  timezone?: string;
  artifactSelection?:
    | {
        mode: "none";
      }
    | {
        mode: "saved_template";
        templateId: string;
        templateVersionId: string;
      };
}

export interface Output {
  ok: boolean;
  artifactSelection?:
    | {
        mode: "none";
      }
    | {
        mode: "saved_template";
        templateId: string;
        templateVersionId: string;
      };
  error?: string;
  errorCode?: string;
}
