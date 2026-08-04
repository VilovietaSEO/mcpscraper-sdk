export interface Input {
  /**
   * New-listing identity returned by prepare-local-sourcebook-write.
   */
  identity?: {
    category: "home" | "professional" | "restaurants" | "financial" | "realestate" | "auto" | "wellness";
    state: string;
    businessName: string;
    websiteUrl: string;
    slug?: string;
    /**
     * @maxItems 20
     */
    tags?:
      | []
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
    idempotencyKey: string;
  };
  /**
   * Complete replacement listing draft for an existing owner-scoped submission.
   */
  listing?: {
    [k: string]: unknown;
  };
  /**
   * Existing owner-scoped submission being revised. Omit for a new capture.
   */
  submissionId?: string;
  /**
   * Required current draft revision for an edit, preventing silent overwrites.
   */
  baseRevision?: number;
  /**
   * @maxItems 20
   */
  tagCandidates?:
    | []
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ];
  /**
   * @maxItems 20
   */
  tagDecisions?:
    | []
    | [
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        }
      ]
    | [
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        }
      ]
    | [
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        }
      ]
    | [
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        }
      ]
    | [
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        }
      ]
    | [
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        }
      ]
    | [
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        }
      ]
    | [
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        }
      ]
    | [
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        }
      ]
    | [
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        }
      ]
    | [
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        }
      ]
    | [
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        }
      ]
    | [
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        }
      ]
    | [
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        }
      ]
    | [
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        }
      ]
    | [
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        }
      ]
    | [
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        }
      ]
    | [
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        }
      ]
    | [
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        }
      ]
    | [
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        }
      ];
  /**
   * Stable retry key for a new capture. Required for new listings; omit only when revising an existing submissionId.
   */
  idempotencyKey?: string;
}

export type Output = unknown
