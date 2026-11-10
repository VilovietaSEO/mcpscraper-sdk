import { test } from 'node:test'
import assert from 'node:assert/strict'
import { MemoryClient } from '../src/client.js'
import { McpToolsClient } from '../src/mcp-client.js'

function fakeFetch(handler: (body: any) => unknown) {
  return (async (_url: string | URL, init?: RequestInit) => {
    const body = JSON.parse(String(init?.body))
    const payload = {
      jsonrpc: '2.0',
      id: body.id,
      result: { structuredContent: handler(body) },
    }
    return {
      ok: true,
      status: 200,
      json: async () => payload,
      text: async () => JSON.stringify(payload),
    } as Response
  }) as typeof globalThis.fetch
}

test('unified client excludes retired scheduling actions', () => {
  const client = new McpToolsClient({
    apiKey: 'sk_test',
    fetch: fakeFetch(() => { throw new Error('Unexpected request') }),
  })
  assert.equal('listScheduledRuns' in client.schedule, false)
  assert.equal('updateScheduledAction' in client.schedule, false)
})

test('unified client creates an immutable editorial artifact template', async () => {
  let capturedBody: any
  const input = {
    presetKey: 'editorial_reading_room_v1' as const,
    name: 'Weekly SEO briefing',
    description: 'Compact weekly review',
    config: {
      theme: 'paper' as const,
      density: 'comfortable' as const,
      showSourceRail: true,
      showGeneratedAt: true,
    },
    authoringInstructions: 'Lead with decisions and preserve every source label.',
  }
  const client = new McpToolsClient({
    apiKey: 'sk_test',
    fetch: fakeFetch(body => {
      capturedBody = body
      return { ok: true, template: { templateId: '00000000-0000-4000-8000-000000000001' } }
    }),
  })

  await client.schedule.createArtifactTemplate(input)

  assert.equal(capturedBody.params.name, 'create_artifact_template')
  assert.deepEqual(capturedBody.params.arguments, input)
})

test('direct Memory client uses hosted tool names for result and template contracts', async () => {
  const called: string[] = []
  const client = new MemoryClient({
    apiKey: 'sk_test',
    fetch: fakeFetch(body => {
      called.push(body.params.name)
      if (body.params.name === 'list_scheduled_runs') {
        return { ok: true, items: [], nextCursor: null }
      }
      return { ok: true, presets: [], templates: [] }
    }),
  })

  await client.schedule.listScheduledRuns({})
  await client.schedule.listArtifactTemplates({ status: 'all' })

  assert.deepEqual(called, ['list_scheduled_runs', 'list_artifact_templates'])
})
