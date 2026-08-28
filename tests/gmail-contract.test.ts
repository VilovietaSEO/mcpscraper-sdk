import assert from 'node:assert/strict'
import { createHash } from 'node:crypto'
import { readFile } from 'node:fs/promises'
import test from 'node:test'

const GMAIL_TOOLS = [
  'gmail_search_messages',
  'gmail_get_message',
  'gmail_get_attachment',
  'gmail_prepare_selection',
  'gmail_export_selection',
  'gmail_bulk_manage_messages',
  'gmail_bulk_delete_messages',
  'gmail_prepare_memory_import',
  'gmail_import_to_memory',
  'gmail_import_status',
] as const

function canonicalJson(value: unknown): string {
  if (Array.isArray(value)) return `[${value.map(canonicalJson).join(',')}]`
  if (value && typeof value === 'object') {
    const entries = Object.entries(value as Record<string, unknown>).sort(([left], [right]) => left.localeCompare(right))
    return `{${entries.map(([key, child]) => `${JSON.stringify(key)}:${canonicalJson(child)}`).join(',')}}`
  }
  return JSON.stringify(value)
}

test('the complete Gmail family has exact generated fingerprints and safe annotations', async () => {
  const manifest = JSON.parse(await readFile('contracts/mcp.tools.json', 'utf8'))
  const fingerprints = JSON.parse(await readFile('contracts/gmail.tools.fingerprints.json', 'utf8'))
  const gmail = manifest.tools.filter((tool: { name: string }) => GMAIL_TOOLS.includes(tool.name as never))
  assert.deepEqual(gmail.map((tool: { name: string }) => tool.name).sort(), [...GMAIL_TOOLS].sort())
  assert.equal(fingerprints.toolCount, GMAIL_TOOLS.length)
  assert.equal(fingerprints.sourceContractSha256, manifest.sourceContractSha256)

  for (const tool of gmail) {
    const contract = {
      name: tool.name,
      description: tool.description,
      inputSchema: tool.inputSchema,
      outputSchema: tool.outputSchema,
      annotations: tool.annotations,
    }
    const expected = createHash('sha256').update(canonicalJson(contract)).digest('hex')
    assert.equal(fingerprints.tools.find((entry: { name: string }) => entry.name === tool.name)?.sha256, expected)
    assert.equal(tool.category, 'connections')
    assert.equal(tool.outputSchemaProvided, true)
  }

  const deletion = gmail.find((tool: { name: string }) => tool.name === 'gmail_bulk_delete_messages')
  assert.equal(deletion.annotations.destructiveHint, true)
  assert.deepEqual(deletion.inputSchema.properties.confirmPermanentDelete, {
    type: 'boolean',
    const: true,
    description: 'Required literal boolean proving the caller selected irreversible deletion rather than reversible trash.',
  })
  const status = gmail.find((tool: { name: string }) => tool.name === 'gmail_import_status')
  assert.equal(status.annotations.readOnlyHint, true)
})

test('runnable examples cover attachment access, resumable Memory import, and reversible management', async () => {
  const complete = await readFile('examples/gmail-complete-workflow.mjs', 'utf8')
  for (const method of [
    'gmailSearchMessages',
    'gmailGetMessage',
    'gmailGetAttachment',
    'gmailPrepareSelection',
    'gmailPrepareMemoryImport',
    'gmailImportToMemory',
    'gmailImportStatus',
  ]) assert.match(complete, new RegExp(method))
  assert.match(complete, /attachmentPolicy: 'preserve_all'/)
  assert.match(complete, /same import plan and idempotency key/)

  const bulk = await readFile('examples/gmail-bulk-manage.mjs', 'utf8')
  assert.match(bulk, /addLabelIds/)
  assert.match(bulk, /removeLabelIds/)
  assert.match(bulk, /Permanent deletion is intentionally absent/)
})

