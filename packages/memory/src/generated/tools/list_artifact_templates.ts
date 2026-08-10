export interface Input {
  apiKey?: string;
  sessionId?: string;
  status?: "active" | "archived" | "all";
}

export type Output =
  | {
      ok: true;
      presets: (
        | {
            name: string;
            description: string;
            mark: string;
            featureFlags: {
              key: string;
              label: string;
              description: string;
            }[];
            presetKey: "editorial_reading_room_v1";
            defaultConfig: {
              theme: "paper" | "ink" | "warm";
              density: "comfortable" | "compact";
              showSourceRail: boolean;
              showGeneratedAt: boolean;
              brandName?: string;
            };
          }
        | {
            name: string;
            description: string;
            mark: string;
            featureFlags: {
              key: string;
              label: string;
              description: string;
            }[];
            presetKey: "personal_authority_v1";
            defaultConfig: {
              theme: "blue" | "slate" | "monochrome";
              showGeneratedAt: boolean;
              brandName?: string;
              featureFlags: {
                navigation: boolean;
                socialLinks: boolean;
                authority: boolean;
                consultation: boolean;
                learning: boolean;
                services: boolean;
                proof: boolean;
                finalCta: boolean;
              };
            };
          }
      )[];
      templates: {
        templateId: string;
        name: string;
        description: string;
        currentVersionId: string;
        status: "active" | "archived";
        currentVersion?:
          | {
              templateVersionId: string;
              templateId: string;
              version: number;
              rendererVersion: 1;
              inputContractVersion: 1;
              authoringInstructions: string;
              createdAt: string;
              rendererKey: "editorial_reading_room_v1";
              config: {
                theme: "paper" | "ink" | "warm";
                density: "comfortable" | "compact";
                showSourceRail: boolean;
                showGeneratedAt: boolean;
                brandName?: string;
              };
            }
          | {
              templateVersionId: string;
              templateId: string;
              version: number;
              rendererVersion: 1;
              inputContractVersion: 1;
              authoringInstructions: string;
              createdAt: string;
              rendererKey: "personal_authority_v1";
              config: {
                theme: "blue" | "slate" | "monochrome";
                showGeneratedAt: boolean;
                brandName?: string;
                featureFlags: {
                  navigation: boolean;
                  socialLinks: boolean;
                  authority: boolean;
                  consultation: boolean;
                  learning: boolean;
                  services: boolean;
                  proof: boolean;
                  finalCta: boolean;
                };
              };
            };
        versions?: (
          | {
              templateVersionId: string;
              templateId: string;
              version: number;
              rendererVersion: 1;
              inputContractVersion: 1;
              authoringInstructions: string;
              createdAt: string;
              rendererKey: "editorial_reading_room_v1";
              config: {
                theme: "paper" | "ink" | "warm";
                density: "comfortable" | "compact";
                showSourceRail: boolean;
                showGeneratedAt: boolean;
                brandName?: string;
              };
            }
          | {
              templateVersionId: string;
              templateId: string;
              version: number;
              rendererVersion: 1;
              inputContractVersion: 1;
              authoringInstructions: string;
              createdAt: string;
              rendererKey: "personal_authority_v1";
              config: {
                theme: "blue" | "slate" | "monochrome";
                showGeneratedAt: boolean;
                brandName?: string;
                featureFlags: {
                  navigation: boolean;
                  socialLinks: boolean;
                  authority: boolean;
                  consultation: boolean;
                  learning: boolean;
                  services: boolean;
                  proof: boolean;
                  finalCta: boolean;
                };
              };
            }
        )[];
        createdAt: string;
        updatedAt: string;
      }[];
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
