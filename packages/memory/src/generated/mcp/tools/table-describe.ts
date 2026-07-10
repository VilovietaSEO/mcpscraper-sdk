export interface Input {
  /**
   * Table name, from table-list.
   */
  tableName: string;
}

export interface Output {
  /**
   * True on success; false on auth or not-found error.
   */
  ok: boolean;
  /**
   * The table name.
   */
  tableName?: string;
  /**
   * Column names and their Postgres types, in table order.
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
