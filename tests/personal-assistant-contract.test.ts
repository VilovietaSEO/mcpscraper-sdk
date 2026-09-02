import assert from 'node:assert/strict'
import { readFile } from 'node:fs/promises'
import test from 'node:test'

type Schema = Record<string, any>

const EXPECTED_ASSISTANT_TOOLS = [
  'assistant_approval_decide', 'assistant_approvals_list', 'assistant_bulk_send', 'assistant_command',
  'assistant_conversation_get', 'assistant_delivery_test', 'assistant_diagnostics_get', 'assistant_execution_status',
  'assistant_grant_create', 'assistant_grant_revoke', 'assistant_grants_list', 'assistant_message_send',
  'assistant_number_purchase', 'assistant_number_release', 'assistant_number_search', 'assistant_number_status',
  'assistant_status',
].sort()

function successData(schema: Schema): Schema {
  const branch = (schema.anyOf as Schema[]).find(candidate => candidate.properties?.ok?.const === true && candidate.properties?.data)
  assert.ok(branch, 'tool output must include one inline success data branch')
  return branch.properties.data
}

test('Assistant MCP inventory and owner-safe contracts remain exact', async () => {
  const manifest = JSON.parse(await readFile('contracts/mcp.tools.json', 'utf8'))
  assert.equal(manifest.toolCount, 375)
  assert.deepEqual(manifest.tools.map((tool: Schema) => tool.name).filter((name: string) => name.startsWith('assistant_')).sort(), EXPECTED_ASSISTANT_TOOLS)

  const byName = new Map<string, Schema>(manifest.tools.map((tool: Schema) => [tool.name, tool]))
  const messageSend = byName.get('assistant_message_send')!
  const attachments = messageSend.inputSchema.properties.attachmentRefs
  assert.equal(attachments.maxItems, 10)
  assert.equal(attachments.items.type, 'string')
  assert.match(attachments.items.pattern, /A-Za-z0-9/)
  assert.equal(messageSend.inputSchema.additionalProperties, false)

  const diagnostics = successData(byName.get('assistant_diagnostics_get')!.outputSchema)
  assert.deepEqual(Object.keys(diagnostics.properties).sort(), ['checkedAt', 'checks', 'journeyState', 'supportRef'])
  assert.equal(diagnostics.additionalProperties, false)

  const delivery = byName.get('assistant_delivery_test')!
  assert.deepEqual([...delivery.inputSchema.required].sort(), ['confirmation', 'idempotencyKey', 'recipientRef', 'senderEndpointRef'])
  assert.equal(delivery.inputSchema.properties.confirmation.const, 'SEND TEST')
  assert.equal(delivery.inputSchema.additionalProperties, false)
  const deliveryData = successData(delivery.outputSchema)
  assert.deepEqual(Object.keys(deliveryData.properties).sort(), ['executionRef', 'nextActions', 'state'])
  assert.equal(deliveryData.properties.receiptRef, undefined)
  assert.equal(deliveryData.additionalProperties, false)
})

test('Assistant owner OpenAPI includes all generated routes and exact journey endpoints', async () => {
  const contract = JSON.parse(await readFile('contracts/assistant.openapi.yaml', 'utf8'))
  assert.equal(contract['x-source-route-count'], 77)
  for (const path of [
    '/api/v1/assistant/diagnostics', '/api/v1/assistant/delivery-tests', '/api/v1/assistant/schedules',
    '/api/v1/assistant/reminders', '/api/v1/assistant/consent/content', '/api/v1/assistant/lifecycle/previews',
  ]) assert.ok(contract.paths[path], `missing ${path}`)
})
