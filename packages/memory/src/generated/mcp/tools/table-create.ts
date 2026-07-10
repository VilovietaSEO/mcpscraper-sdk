export interface Input {
  /**
   * Table name: lowercase letters, numbers, underscores, starting with a letter (e.g. rank_tracker).
   */
  tableName: string;
  /**
   * Columns to create, in addition to the automatic id/created_at/updated_at.
   *
   * @minItems 1
   */
  columns: [
    {
      /**
       * Column name: lowercase letters, numbers, underscores, starting with a letter. Cannot be id, created_at, or updated_at.
       */
      name: string;
      /**
       * Column type.
       */
      type: "text" | "number" | "integer" | "boolean" | "date" | "timestamp" | "json";
    },
    ...{
      /**
       * Column name: lowercase letters, numbers, underscores, starting with a letter. Cannot be id, created_at, or updated_at.
       */
      name: string;
      /**
       * Column type.
       */
      type: "text" | "number" | "integer" | "boolean" | "date" | "timestamp" | "json";
    }[]
  ];
}

export interface Output {
  /**
   * True on success; false on auth/scope/validation error.
   */
  ok: boolean;
  /**
   * The table name.
   */
  tableName?: string;
  /**
   * True if the table was newly created; false if it already existed.
   */
  created?: boolean;
  /**
   * The columns requested (existing tables are not altered to match).
   */
  columns?: {
    name: string;
    type: string;
  }[];
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
