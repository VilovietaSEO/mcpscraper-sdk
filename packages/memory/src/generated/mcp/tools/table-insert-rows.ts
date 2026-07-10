export interface Input {
  /**
   * Table name, from table-list.
   */
  tableName: string;
  /**
   * Rows to insert, each an object of column name to value.
   *
   * @minItems 1
   * @maxItems 500
   */
  rows: [
    {
      [k: string]: unknown;
    },
    ...{
      [k: string]: unknown;
    }[]
  ];
}

export interface Output {
  /**
   * True on success; false on auth/scope/validation error.
   */
  ok: boolean;
  /**
   * Number of rows inserted.
   */
  inserted?: number;
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
