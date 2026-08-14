export interface Input {
  /**
   * Proposed concepts to resolve against the canonical vocabulary.
   *
   * @minItems 1
   * @maxItems 20
   */
  candidates:
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
   * Confirm a candidate returned by an earlier review, as {proposedTag: canonicalTag}. The proposed spelling is recorded as an alias of the canonical tag so the same judgement is never re-litigated.
   */
  accept?: {
    [k: string]: string;
  };
}

export interface Output {
  ok: boolean;
  resolutions?: {
    candidate: string;
    normalized: string;
    action: "reuse" | "review" | "create" | "omit";
    tag?: string;
    matchedBy?: "exact" | "alias" | "near";
    matchedVia?: "key" | "alias" | "stem" | "trigram" | "embedding";
    score?: number;
    /**
     * Ranked existing tags to choose from when action is review. Nothing is merged automatically.
     */
    candidates?: {
      tag: string;
      matchedVia: "key" | "alias" | "stem" | "trigram" | "embedding";
      score: number;
      description: string | null;
    }[];
    reason: string;
  }[];
  error?: string;
}
