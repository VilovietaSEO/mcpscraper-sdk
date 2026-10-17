export interface Input {
  /**
   * Human-readable title for the proposed record or authored content.
   */
  title: string;
  /**
   * Complete content to route, validate, or store; do not substitute a partial excerpt when full content is required.
   */
  content: string;
  /**
   * Optional source or provenance constraint appropriate to this tool; omit when no source restriction is intended.
   */
  source?: string;
  /**
   * Governed content or record type used for routing and validation.
   */
  type?: string;
  /**
   * Exact accessible Memory vault name; omit only when this tool documents a safe active-vault default.
   */
  vault?: string;
  /**
   * Proposed listing or memory tags to resolve against the live canonical vocabulary.
   *
   * @maxItems 20
   */
  tagCandidates?:
    | []
    | [
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        }
      ]
    | [
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        }
      ]
    | [
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        }
      ]
    | [
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        }
      ]
    | [
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        }
      ]
    | [
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        }
      ]
    | [
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        }
      ]
    | [
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        }
      ]
    | [
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        }
      ]
    | [
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        }
      ]
    | [
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        }
      ]
    | [
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        }
      ]
    | [
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        }
      ]
    | [
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        }
      ]
    | [
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        }
      ]
    | [
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        }
      ]
    | [
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        }
      ]
    | [
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        }
      ]
    | [
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        }
      ]
    | [
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        }
      ];
  /**
   * Maximum related-note candidates to return from the planning pass.
   */
  maxLinks?: number;
}

export type Output =
  | {
      ok: boolean;
      route?: {
        [k: string]: unknown;
      };
      contract?: {
        [k: string]: unknown;
      };
      tagResolutions?: {
        [k: string]: unknown;
      }[];
      linkOpportunities?: {
        [k: string]: unknown;
      }[];
      instructions?: string[];
      error?: string;
    }
  | {
      delivery: {
        mode: "artifact";
        status: "complete" | "partial" | "unavailable";
        retainedRepresentation: "formatted-tool-result";
        sourceIsError: boolean;
        artifacts: {
          artifactId: string;
          filename: string;
          contentType: string;
          bytes: number;
          sha256: string;
          expiresAt: string;
          capabilities: string[];
          downloadUrl: string | null;
          downloadUrlExpiresAt: string | null;
          downloadState: "available" | "local" | "unavailable";
        }[];
        availableExports?: {
          artifactId: string;
          sourceArtifactId: string;
          filename: "result.md";
          contentType: "text/markdown; charset=utf-8";
          state: "on-demand";
        }[];
        downloadLinksOmitted: boolean;
        scopeOmittedFields: number;
        storageFailure: {
          artifactId: string | null;
          outcome: "unknown" | "bytes-stored-metadata-pending" | "failed";
        } | null;
        nextAction: string;
      };
      preview: string;
      scope: {
        [k: string]: string | number | boolean | null;
      };
      recovery: {
        idempotencyKey?: string;
        operationId?: string;
        runId?: string;
        jobId?: string;
        operation?: {
          runId: string | null;
          idempotencyKey: string;
          state: string;
        };
      };
    };
