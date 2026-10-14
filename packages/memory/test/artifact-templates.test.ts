import { test } from 'node:test'
import assert from 'node:assert/strict'
import { MemoryClient } from '../src/client.js'
import { McpToolsClient } from '../src/mcp-client.js'

function fakeFetch(handler: (body: any) => unknown) {
  return (async (_url: string | URL, init?: RequestInit) => {
    const body = JSON.parse(String(init?.body))
    const payload = { jsonrpc: '2.0', id: body.id, result: { structuredContent: handler(body) } }
    return { ok: true, status: 200, json: async () => payload, text: async () => JSON.stringify(payload) } as Response
  }) as typeof globalThis.fetch
}

test('unified artifacts client creates an immutable editorial template', async () => {
  let capturedBody: any
  const input = {
    presetKey: 'editorial_reading_room_v1' as const,
    name: 'SEO briefing',
    config: { theme: 'paper' as const, density: 'comfortable' as const, showSourceRail: true, showGeneratedAt: true },
    authoringInstructions: 'Lead with decisions and preserve every source label.',
  }
  const client = new McpToolsClient({ apiKey: 'sk_test', fetch: fakeFetch(body => {
    capturedBody = body
    return { ok: true, template: { templateId: '00000000-0000-4000-8000-000000000001' } }
  }) })
  await client.artifacts.createArtifactTemplate(input)
  assert.equal(capturedBody.params.name, 'create_artifact_template')
  assert.deepEqual(capturedBody.params.arguments, input)
  assert.equal('schedule' in client, false)
})

test('direct Memory artifacts client preserves the hosted template wire name', async () => {
  const called: string[] = []
  const client = new MemoryClient({ apiKey: 'sk_test', fetch: fakeFetch(body => {
    called.push(body.params.name)
    return { ok: true, presets: [], templates: [] }
  }) })
  await client.artifacts.listArtifactTemplates({ status: 'all' })
  assert.deepEqual(called, ['list_artifact_templates'])
  assert.equal('schedule' in client, false)
})
