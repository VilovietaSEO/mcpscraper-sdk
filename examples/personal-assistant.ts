import {
  McpToolsClient,
  type AssistantApprovalDecision,
  type AssistantCursor,
  type AssistantIdempotencyKey,
} from '../packages/memory/src/index.js'

export async function submitAndReview(
  client: McpToolsClient,
  assistantRef: string,
  idempotencyKey: AssistantIdempotencyKey,
): Promise<void> {
  await client.assistant.command({
    assistantRef,
    instruction: 'Draft a reply, but do not send it without my approval.',
    idempotencyKey,
  })

  let cursor: AssistantCursor | undefined
  do {
    const page = await client.assistant.approvalsList({ state: 'pending', cursor, pageSize: 25 })
    cursor = typeof page.data === 'object' && page.data !== null && 'nextCursor' in page.data
      ? String(page.data.nextCursor)
      : undefined
  } while (cursor)
}

export async function decideApproval(
  client: McpToolsClient,
  decision: AssistantApprovalDecision,
): Promise<void> {
  await client.assistant.approvalDecide(decision)
}
