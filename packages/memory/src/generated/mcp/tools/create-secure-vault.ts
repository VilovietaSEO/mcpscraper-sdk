export interface Input {
  /**
   * Vault name. Must match ^[A-Za-z0-9 _-]{1,48}$. Defaults to a name like "Passwords" if the caller has no preference.
   */
  name: string;
}

export interface Output {
  /**
   * True when the vault was created; false on auth/scope/validation error.
   */
  ok: boolean;
  /**
   * The vault name. Present when ok is true.
   */
  vault?: string;
  /**
   * True if newly created; false if a vault with this name already existed for you (idempotent) — note this does NOT confirm the existing vault is secure-kind; check list-vaults if unsure.
   */
  created?: boolean;
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
