import { McpToolsClient } from '../packages/memory/dist/index.js'

const {
  MCP_SCRAPER_API_KEY: apiKey,
  GMAIL_CONNECTION_ID: connectionId,
  GMAIL_THREAD_ID: threadId,
  GMAIL_PARENT_MESSAGE_ID: parentMessageId,
  GMAIL_REPLY_BODY: body,
  GMAIL_DRAFT_IDEMPOTENCY_KEY: idempotencyKey,
} = process.env
if (!apiKey || !connectionId || !threadId) {
  throw new Error('Set MCP_SCRAPER_API_KEY, GMAIL_CONNECTION_ID and GMAIL_THREAD_ID.')
}

const gmail = new McpToolsClient({ apiKey }).connections
const messages = []
let cursor
do {
  const { thread } = await gmail.gmailGetThread({ connectionId, threadId, cursor })
  if (!thread.providerCoverageComplete) throw new Error('Gmail did not provide the full conversation.')
  messages.push(...thread.messages)
  cursor = thread.nextCursor ?? undefined
} while (cursor)

for (const message of messages) {
  console.log(message.messageId, message.sentAt, message.bodyComplete ? 'body complete' : 'read the full artifact')
}

if (parentMessageId) {
  if (!messages.some(message => message.messageId === parentMessageId) || !body || !idempotencyKey) {
    throw new Error('Review the exact parent and provide GMAIL_REPLY_BODY and GMAIL_DRAFT_IDEMPOTENCY_KEY.')
  }
  const { draft } = await gmail.gmailCreateReplyDraft({ connectionId, threadId, parentMessageId, body, idempotencyKey, confirmed: true })
  if (draft.status !== 'draft_created' || draft.sent !== false || draft.parentMessageId !== parentMessageId) {
    throw new Error('Review Gmail Drafts before submitting another request.')
  }
  console.log('Verified unsent reply draft', draft.draftId)
}
