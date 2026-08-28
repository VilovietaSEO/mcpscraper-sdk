import { McpToolsClient } from '../packages/memory/dist/index.js'

const apiKey = process.env.MCP_SCRAPER_API_KEY
const connectionId = process.env.GMAIL_CONNECTION_ID
const query = process.env.GMAIL_QUERY ?? 'has:attachment newer_than:30d'

if (!apiKey || !connectionId) {
  throw new Error('Set MCP_SCRAPER_API_KEY and GMAIL_CONNECTION_ID before running this example.')
}

const tools = new McpToolsClient({ apiKey })
const gmail = tools.connections

const search = await gmail.gmailSearchMessages({ connectionId, query, limit: 25 })
if (!search.ok || !search.messages?.length) throw new Error(search.error ?? 'No matching Gmail messages found.')

// Full message reads expose every MIME part and opaque attachmentRef. Opening an
// attachment stores exact bytes as an owner-scoped artifact and can return a
// bounded text window when the observed MIME is text-readable.
const fullMessage = await gmail.gmailGetMessage({
  connectionId,
  messageId: search.messages[0].messageId,
  includeRawArtifact: true,
})
if (!fullMessage.ok || !fullMessage.message) throw new Error(fullMessage.error ?? 'Full message read failed.')
for (const attachment of fullMessage.message.attachments) {
  const opened = await gmail.gmailGetAttachment({ attachmentRef: attachment.attachmentRef })
  if (!opened.ok || !opened.artifact) throw new Error(opened.error ?? `Attachment ${attachment.filename} failed.`)
  console.log('attachment', opened.filename, opened.observedMime, opened.sha256, opened.artifact.artifactId)
}

// Freeze the query once. The reviewed count and digest must stay together for
// every later plan, export, mutation, or import call.
const prepared = await gmail.gmailPrepareSelection({
  connectionId,
  purpose: 'memory_import',
  source: { kind: 'query', query },
})
if (!prepared.ok || !prepared.selection) throw new Error(prepared.error ?? 'Selection preparation failed.')
console.log('selection preview', prepared.selection.preview)

const planResult = await gmail.gmailPrepareMemoryImport({
  connectionId,
  selectionId: prepared.selection.selectionId,
  selectionSha256: prepared.selection.selectionSha256,
  filingPolicy: 'source_archive',
  destination: { mode: 'auto' },
  attachmentPolicy: 'preserve_all',
})
if (!planResult.ok || !planResult.plan) throw new Error(planResult.error ?? 'Memory import planning failed.')
if (planResult.plan.refusals.length) {
  throw new Error(`Review the ${planResult.plan.refusals.length} refused attachment(s) before importing.`)
}
console.log('Memory plan', {
  messages: planResult.plan.messageCount,
  attachments: planResult.plan.attachmentCount,
  bytes: planResult.plan.attachmentBytes,
  routes: planResult.plan.routes,
})

const idempotencyKey = process.env.GMAIL_IMPORT_IDEMPOTENCY_KEY ?? `gmail-example-${planResult.plan.importPlanId}`
let run = await gmail.gmailImportToMemory({ importPlanId: planResult.plan.importPlanId, idempotencyKey })
if (!run.ok || !run.ingest) throw new Error(run.error ?? 'Memory import failed to start.')

// Status is observation-only. Resume work only by replaying gmail_import_to_memory
// with the same import plan and idempotency key when nextAction asks for it.
for (let attempt = 0; attempt < 120 && !run.ingest.complete; attempt += 1) {
  if (run.ingest.nextAction === 'call_gmail_import_to_memory') {
    run = await gmail.gmailImportToMemory({ importPlanId: planResult.plan.importPlanId, idempotencyKey })
  } else {
    await new Promise(resolve => setTimeout(resolve, 1_000))
    run = await gmail.gmailImportStatus({ ingestId: run.ingest.ingestId })
  }
  if (!run.ok || !run.ingest) throw new Error(run.error ?? 'Memory import continuation failed.')
  if (run.ingest.status === 'failed' || run.ingest.status === 'partial') break
}

console.log('final import status', run.ingest)
if (!run.ingest?.complete) throw new Error(`Import ended without complete status: ${run.ingest?.status ?? 'unknown'}`)

