export interface Input {
  apiKey?: string;
  sessionId?: string;
  templateId: string;
}

export type Output =
  | {
      ok: true;
      template: {
        templateId: string;
        name: string;
        description: string;
        currentVersionId: string;
        status: "active" | "archived";
        currentVersion?: {
          templateVersionId: string;
          templateId: string;
          version: number;
          rendererKey: "editorial_reading_room_v1";
          rendererVersion: 1;
          inputContractVersion: 1;
          config: {
            theme: "paper" | "ink" | "warm";
            density: "comfortable" | "compact";
            showSourceRail: boolean;
            showGeneratedAt: boolean;
            brandName?: string;
          };
          authoringInstructions: string;
          createdAt: string;
        };
        versions?: {
          templateVersionId: string;
          templateId: string;
          version: number;
          rendererKey: "editorial_reading_room_v1";
          rendererVersion: 1;
          inputContractVersion: 1;
          config: {
            theme: "paper" | "ink" | "warm";
            density: "comfortable" | "compact";
            showSourceRail: boolean;
            showGeneratedAt: boolean;
            brandName?: string;
          };
          authoringInstructions: string;
          createdAt: string;
        }[];
        createdAt: string;
        updatedAt: string;
      };
    }
  | {
      ok: false;
      error: string;
      errorCode:
        | "invalid_request"
        | "not_found"
        | "conflict"
        | "template_archived"
        | "renderer_unavailable"
        | "artifact_unavailable"
        | "view_link_unavailable"
        | "internal_error";
      requestId?: string;
    };
