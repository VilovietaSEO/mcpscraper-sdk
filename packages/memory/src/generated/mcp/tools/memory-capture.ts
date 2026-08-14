export interface Input {
  /**
   * Exact accessible Memory vault name; omit only when this tool documents a safe active-vault default.
   */
  vault: string;
  /**
   * Optional governed folder override inside the selected vault.
   */
  folder?: string;
  /**
   * Exact path value used by this tool; preserve its leading slash or vault-relative form as required.
   */
  path: string;
  /**
   * Human-readable title for the proposed record or authored content.
   */
  title: string;
  /**
   * Complete content to route, validate, or store; do not substitute a partial excerpt when full content is required.
   */
  content: string;
  /**
   * Complete governed note properties required by the target vault contract.
   */
  props: {
    /**
     * Status enum value from the target vault contract.
     */
    status?: string;
    /**
     * Short retrieval-ready description.
     */
    summary?: string;
    /**
     * AI-generated keyword tags, not vault names.
     */
    tags?: string[];
    /**
     * Recall boost for important notes.
     */
    pinned?: boolean;
    /**
     * Attribution kind: user, person, url, file, channel, thread, or note.
     */
    source_type?: string;
    /**
     * Attribution reference (URL, path, channel, thread, or source note).
     */
    source_ref?: string;
    /**
     * Same-vault links (wiki [[ ]] targets).
     */
    related?: string[];
    /**
     * Cross-vault references in "Vault Name::relative/path.md" form.
     */
    related_vault_notes?: string[];
    /**
     * Whether Smart RAG should index the note.
     */
    embed?: boolean;
    /**
     * Embedding priority.
     */
    embed_priority?: "low" | "normal" | "high";
    /**
     * Optional retrieval-specific summary.
     */
    embedding_summary?: string;
    /**
     * Note type from the target vault contract (also used to route the note).
     */
    type?: string;
    /**
     * Domain folder for Library/Knowledge (AI, SEO, Copywriting & Ads, Business, Spirituality).
     */
    domain?: string;
    /**
     * Explicit sub-folder within the vault; overrides routing-derived folder.
     */
    folder?: string;
    /**
     * Skills only: one or more Obsidian/internal paths under scripts/.
     */
    script_links?: string[];
    /**
     * Skills only: optional Obsidian/internal paths under references/.
     */
    reference_links?: string[];
    /**
     * Skills only: optional Obsidian/internal paths under templates/.
     */
    template_links?: string[];
    /**
     * Channel messages only: the path of the top-level message this is a reply to. Absent on top-level messages.
     */
    parentMessageId?: string;
    [k: string]: unknown;
  };
  /**
   * Last revision read by the caller; supply it to reject an update if the record changed meanwhile.
   */
  baseRevision?: number;
  /**
   * Required justification for any tag that does not already exist. Tags resolve against the account's existing vocabulary; new tags require a one-line description.
   *
   * @maxItems 8
   */
  tagDecisions?:
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
          central: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
          /**
           * Reuse this existing tag instead of the proposed one, confirming a candidate returned by an earlier review. The proposed spelling is recorded as its alias.
           */
          acceptCanonical?: string;
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
          central: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
          /**
           * Reuse this existing tag instead of the proposed one, confirming a candidate returned by an earlier review. The proposed spelling is recorded as its alias.
           */
          acceptCanonical?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
          /**
           * Reuse this existing tag instead of the proposed one, confirming a candidate returned by an earlier review. The proposed spelling is recorded as its alias.
           */
          acceptCanonical?: string;
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
          central: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
          /**
           * Reuse this existing tag instead of the proposed one, confirming a candidate returned by an earlier review. The proposed spelling is recorded as its alias.
           */
          acceptCanonical?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
          /**
           * Reuse this existing tag instead of the proposed one, confirming a candidate returned by an earlier review. The proposed spelling is recorded as its alias.
           */
          acceptCanonical?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
          /**
           * Reuse this existing tag instead of the proposed one, confirming a candidate returned by an earlier review. The proposed spelling is recorded as its alias.
           */
          acceptCanonical?: string;
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
          central: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
          /**
           * Reuse this existing tag instead of the proposed one, confirming a candidate returned by an earlier review. The proposed spelling is recorded as its alias.
           */
          acceptCanonical?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
          /**
           * Reuse this existing tag instead of the proposed one, confirming a candidate returned by an earlier review. The proposed spelling is recorded as its alias.
           */
          acceptCanonical?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
          /**
           * Reuse this existing tag instead of the proposed one, confirming a candidate returned by an earlier review. The proposed spelling is recorded as its alias.
           */
          acceptCanonical?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
          /**
           * Reuse this existing tag instead of the proposed one, confirming a candidate returned by an earlier review. The proposed spelling is recorded as its alias.
           */
          acceptCanonical?: string;
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
          central: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
          /**
           * Reuse this existing tag instead of the proposed one, confirming a candidate returned by an earlier review. The proposed spelling is recorded as its alias.
           */
          acceptCanonical?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
          /**
           * Reuse this existing tag instead of the proposed one, confirming a candidate returned by an earlier review. The proposed spelling is recorded as its alias.
           */
          acceptCanonical?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
          /**
           * Reuse this existing tag instead of the proposed one, confirming a candidate returned by an earlier review. The proposed spelling is recorded as its alias.
           */
          acceptCanonical?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
          /**
           * Reuse this existing tag instead of the proposed one, confirming a candidate returned by an earlier review. The proposed spelling is recorded as its alias.
           */
          acceptCanonical?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
          /**
           * Reuse this existing tag instead of the proposed one, confirming a candidate returned by an earlier review. The proposed spelling is recorded as its alias.
           */
          acceptCanonical?: string;
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
          central: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
          /**
           * Reuse this existing tag instead of the proposed one, confirming a candidate returned by an earlier review. The proposed spelling is recorded as its alias.
           */
          acceptCanonical?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
          /**
           * Reuse this existing tag instead of the proposed one, confirming a candidate returned by an earlier review. The proposed spelling is recorded as its alias.
           */
          acceptCanonical?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
          /**
           * Reuse this existing tag instead of the proposed one, confirming a candidate returned by an earlier review. The proposed spelling is recorded as its alias.
           */
          acceptCanonical?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
          /**
           * Reuse this existing tag instead of the proposed one, confirming a candidate returned by an earlier review. The proposed spelling is recorded as its alias.
           */
          acceptCanonical?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
          /**
           * Reuse this existing tag instead of the proposed one, confirming a candidate returned by an earlier review. The proposed spelling is recorded as its alias.
           */
          acceptCanonical?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
          /**
           * Reuse this existing tag instead of the proposed one, confirming a candidate returned by an earlier review. The proposed spelling is recorded as its alias.
           */
          acceptCanonical?: string;
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
          central: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
          /**
           * Reuse this existing tag instead of the proposed one, confirming a candidate returned by an earlier review. The proposed spelling is recorded as its alias.
           */
          acceptCanonical?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
          /**
           * Reuse this existing tag instead of the proposed one, confirming a candidate returned by an earlier review. The proposed spelling is recorded as its alias.
           */
          acceptCanonical?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
          /**
           * Reuse this existing tag instead of the proposed one, confirming a candidate returned by an earlier review. The proposed spelling is recorded as its alias.
           */
          acceptCanonical?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
          /**
           * Reuse this existing tag instead of the proposed one, confirming a candidate returned by an earlier review. The proposed spelling is recorded as its alias.
           */
          acceptCanonical?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
          /**
           * Reuse this existing tag instead of the proposed one, confirming a candidate returned by an earlier review. The proposed spelling is recorded as its alias.
           */
          acceptCanonical?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
          /**
           * Reuse this existing tag instead of the proposed one, confirming a candidate returned by an earlier review. The proposed spelling is recorded as its alias.
           */
          acceptCanonical?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
          /**
           * Reuse this existing tag instead of the proposed one, confirming a candidate returned by an earlier review. The proposed spelling is recorded as its alias.
           */
          acceptCanonical?: string;
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
          central: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
          /**
           * Reuse this existing tag instead of the proposed one, confirming a candidate returned by an earlier review. The proposed spelling is recorded as its alias.
           */
          acceptCanonical?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
          /**
           * Reuse this existing tag instead of the proposed one, confirming a candidate returned by an earlier review. The proposed spelling is recorded as its alias.
           */
          acceptCanonical?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
          /**
           * Reuse this existing tag instead of the proposed one, confirming a candidate returned by an earlier review. The proposed spelling is recorded as its alias.
           */
          acceptCanonical?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
          /**
           * Reuse this existing tag instead of the proposed one, confirming a candidate returned by an earlier review. The proposed spelling is recorded as its alias.
           */
          acceptCanonical?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
          /**
           * Reuse this existing tag instead of the proposed one, confirming a candidate returned by an earlier review. The proposed spelling is recorded as its alias.
           */
          acceptCanonical?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
          /**
           * Reuse this existing tag instead of the proposed one, confirming a candidate returned by an earlier review. The proposed spelling is recorded as its alias.
           */
          acceptCanonical?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
          /**
           * Reuse this existing tag instead of the proposed one, confirming a candidate returned by an earlier review. The proposed spelling is recorded as its alias.
           */
          acceptCanonical?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
          /**
           * Reuse this existing tag instead of the proposed one, confirming a candidate returned by an earlier review. The proposed spelling is recorded as its alias.
           */
          acceptCanonical?: string;
        }
      ];
}

export interface Output {
  ok: boolean;
  valid?: boolean;
  errors?: string[];
  warnings?: string[];
  tagResolutions?: {
    candidate: string;
    action: "reuse" | "review" | "create" | "omit";
    tag?: string;
    candidates?: {
      tag: string;
      matchedVia: string;
      score: number;
      description: string | null;
    }[];
    reason: string;
  }[];
  note?: {
    path: string;
    title: string;
    updatedAt: string;
    revision: number;
  };
  indexed?: number;
  verified?: {
    contentBytes: number;
    propsPersisted: boolean;
    revision: number;
  };
  conflict?: boolean;
  code?: string;
  error?: string;
}
