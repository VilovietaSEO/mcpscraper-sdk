export interface Input {
  /**
   * Authorized Analytics Site id.
   */
  siteId: string;
  /**
   * Owner-facing survey name.
   */
  name: string;
  /**
   * Customer-visible structured influence question; do not request contact data or free text.
   */
  question: string;
  /**
   * Whether a respondent may select one influence or several.
   */
  selectionMode: "single" | "multiple";
  /**
   * Authoritative outcome families eligible to receive an invitation.
   *
   * @minItems 1
   * @maxItems 20
   */
  eligibleOutcomeFamilies:
    | [string]
    | [string, string]
    | [string, string, string]
    | [string, string, string, string]
    | [string, string, string, string, string]
    | [string, string, string, string, string, string]
    | [string, string, string, string, string, string, string]
    | [string, string, string, string, string, string, string, string]
    | [string, string, string, string, string, string, string, string, string]
    | [string, string, string, string, string, string, string, string, string, string]
    | [string, string, string, string, string, string, string, string, string, string, string]
    | [string, string, string, string, string, string, string, string, string, string, string, string]
    | [string, string, string, string, string, string, string, string, string, string, string, string, string]
    | [string, string, string, string, string, string, string, string, string, string, string, string, string, string]
    | [
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string
      ]
    | [
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string
      ]
    | [
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string
      ]
    | [
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string
      ]
    | [
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string
      ]
    | [
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string
      ];
  /**
   * Short-lived merchant exchange-code lifetime.
   */
  exchangeTtlSeconds: number;
  /**
   * Hosted survey session lifetime after one-time exchange.
   */
  sessionTtlSeconds: number;
  /**
   * Versioned privacy disclosure approval. A draft may omit it; production publication may not.
   */
  approvedCopyId?: string | null;
  /**
   * Two to twenty stable structured influences.
   *
   * @minItems 2
   * @maxItems 20
   */
  options:
    | [
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        }
      ]
    | [
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        }
      ]
    | [
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        }
      ]
    | [
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        }
      ]
    | [
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        }
      ]
    | [
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        }
      ]
    | [
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        }
      ]
    | [
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        }
      ]
    | [
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        }
      ]
    | [
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        }
      ]
    | [
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        }
      ]
    | [
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        }
      ]
    | [
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        }
      ]
    | [
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        }
      ]
    | [
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        }
      ]
    | [
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        }
      ]
    | [
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        }
      ]
    | [
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        }
      ]
    | [
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        },
        {
          /**
           * Stable opaque option id; changing a label never changes this id.
           */
          optionId: string;
          /**
           * Bounded owner-authored influence label. Free-text customer testimony is not accepted.
           */
          label: string;
        }
      ];
  /**
   * Retry key; reuse only for this exact mutation.
   */
  idempotencyKey: string;
}

export interface Output {
  ok: true;
  operation: "create";
  survey: {
    surveyId: string;
    siteId: string;
    revision: number;
    state: "draft" | "published" | "paused" | "archived";
    name: string;
    question: string;
    selectionMode: "single" | "multiple";
    /**
     * @minItems 1
     */
    eligibleOutcomeFamilies: [string, ...string[]];
    exchangeTtlSeconds: number;
    sessionTtlSeconds: number;
    approvedCopyId: string | null;
    /**
     * @minItems 2
     */
    options: [
      {
        optionId: string;
        label: string;
        position: number;
      },
      {
        optionId: string;
        label: string;
        position: number;
      },
      ...{
        optionId: string;
        label: string;
        position: number;
      }[]
    ];
  };
  created?: boolean;
}
