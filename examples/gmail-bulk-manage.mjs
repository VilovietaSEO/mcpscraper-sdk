import { McpToolsClient } from '../packages/memory/dist/index.js'

const apiKey = process.env.MCP_SCRAPER_API_KEY
const connectionId = process.env.GMAIL_CONNECTION_ID
const query = process.env.GMAIL_BULK_QUERY
const labelId = process.env.GMAIL_TEST_LABEL_ID

if (!apiKey || !connectionId || !query || !labelId) {
  throw new Error('Set MCP_SCRAPER_API_KEY, GMAIL_CONNECTION_ID, GMAIL_BULK_QUERY, and GMAIL_TEST_LABEL_ID.')
}
if (process.env.CONFIRM_GMAIL_BULK_EXAMPLE !== 'yes') {
  throw new Error('Review the frozen selection, then set CONFIRM_GMAIL_BULK_EXAMPLE=yes to run the reversible example.')
}

const tools = new McpToolsClient({ apiKey })
const gmail = tools.connections
const prepared = await gmail.gmailPrepareSelection({
  connectionId,
  purpose: 'mailbox_action',
  source: { kind: 'query', query },
})
if (!prepared.ok || !prepared.selection) throw new Error(prepared.error ?? 'Selection preparation failed.')

const receipt = {
  connectionId,
  selectionId: prepared.selection.selectionId,
  selectionSha256: prepared.selection.selectionSha256,
  expectedCount: prepared.selection.count,
  confirmed: true,
}
console.log('approved selection', prepared.selection.preview)

const added = await gmail.gmailBulkManageMessages({
  ...receipt,
  operation: { kind: 'labels', addLabelIds: [labelId] },
  idempotencyKey: `gmail-label-add-${prepared.selection.selectionSha256.slice(0, 24)}`,
})
if (!added.ok || added.status === 'failed') throw new Error(added.error ?? 'Adding the label failed.')
console.log('label added', added)

const removed = await gmail.gmailBulkManageMessages({
  ...receipt,
  operation: { kind: 'labels', removeLabelIds: [labelId] },
  idempotencyKey: `gmail-label-remove-${prepared.selection.selectionSha256.slice(0, 24)}`,
})
if (!removed.ok || removed.status === 'failed') throw new Error(removed.error ?? 'Removing the label failed.')
console.log('label restored', removed)

// Permanent deletion is intentionally absent. gmail_bulk_delete_messages is
// irreversible and should only target messages created expressly as disposable
// fixtures after a separate, exact-count confirmation.

