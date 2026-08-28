import type { Input as ApprovalDecisionInput } from './generated/mcp/tools/assistant_approval_decide.js'
import type { Input as ApprovalsListInput } from './generated/mcp/tools/assistant_approvals_list.js'
import type { Input as CommandInput } from './generated/mcp/tools/assistant_command.js'

/** Opaque continuation values must be passed back unchanged. */
export type AssistantCursor = NonNullable<ApprovalsListInput['cursor']>

/** Shared bounded-page fields used by assistant list operations. */
export type AssistantPageRequest = Pick<ApprovalsListInput, 'cursor' | 'pageSize'>

/** Stable retry identity for one exact assistant mutation. */
export type AssistantIdempotencyKey = CommandInput['idempotencyKey']

/** Exact immutable approval-decision contract generated from the MCP manifest. */
export type AssistantApprovalDecision = ApprovalDecisionInput

/** Exact command-submission contract generated from the MCP manifest. */
export type AssistantCommand = CommandInput
