import assert from 'node:assert/strict'
import test from 'node:test'
import { readFile } from 'node:fs/promises'

const paths = {
  contract: 'contracts/mcp.tools.json',
  node: 'packages/memory/src/generated/mcp/tools/analytics_list_journeys.ts',
  nodeVisitor: 'packages/memory/src/generated/mcp/tools/analytics_get_visitor_journey.ts',
  scraperPython: 'packages/scraper-python/src/mcpscraper/mcp_models/analytics_list_journeys.py',
  scraperPythonVisitor: 'packages/scraper-python/src/mcpscraper/mcp_models/analytics_get_visitor_journey.py',
  memoryPython: 'packages/memory-python/src/mcpscraper_memory/mcp_models/analytics_list_journeys.py',
  memoryPythonVisitor: 'packages/memory-python/src/mcpscraper_memory/mcp_models/analytics_get_visitor_journey.py',
  cli: 'packages/cli/src/generated-tools.ts',
  curl: 'docs/curl-tools.md',
  example: 'examples/xray-journeys.mjs',
} as const

test('analytics_list_journeys projects its selector, evidence tier, null branches, and pagination everywhere', async () => {
  const files = Object.fromEntries(await Promise.all(
    Object.entries(paths).map(async ([name, path]) => [name, await readFile(path, 'utf8')]),
  )) as Record<keyof typeof paths, string>
  const manifest = JSON.parse(files.contract) as { toolCount: number; tools: Array<Record<string, any>> }
  const tool = manifest.tools.find(candidate => candidate.name === 'analytics_list_journeys')
  assert.ok(tool)
  assert.equal(manifest.toolCount, 369)
  assert.deepEqual(tool.inputSchema.properties.journeyTier.enum, ['confirmed', 'best_guess', 'all'])
  assert.equal(tool.inputSchema.properties.journeyTier.default, 'confirmed')
  assert.equal(tool.outputSchema.properties.bestGuess.anyOf[0].properties.journeyTier.const, 'candidate_assisted')
  assert.ok(tool.outputSchema.required.includes('confirmed'))
  assert.ok(tool.outputSchema.required.includes('bestGuess'))
  assert.deepEqual(tool.outputSchema.properties.confirmed.anyOf[0].properties.pageInfo.required, ['nextCursor', 'hasNextPage'])

  assert.match(files.node, /journeyTier\?: "confirmed" \| "best_guess" \| "all"/)
  assert.match(files.node, /journeyTier: "candidate_assisted"/)
  assert.match(files.node, /nextCursor: string \| null/)
  for (const python of [files.scraperPython, files.memoryPython]) {
    assert.match(python, /Literal\['confirmed', 'best_guess', 'all'\]/)
    assert.match(python, /best_guess: Any/)
  }
  assert.match(files.cli, /"name": "analytics_list_journeys"/)
  assert.match(files.curl, /`analytics_list_journeys` — List X-Ray Journeys/)
  assert.match(files.example, /journeyTier: 'confirmed'/)
  assert.match(files.example, /journeyTier: 'best_guess'/)
  assert.match(files.example, /candidate_assisted/)
})

test('enhanced journey windows and complete confirmed output project into every client surface', async () => {
  const files = Object.fromEntries(await Promise.all(
    Object.entries(paths).map(async ([name, path]) => [name, await readFile(path, 'utf8')]),
  )) as Record<keyof typeof paths, string>
  const manifest = JSON.parse(files.contract) as { tools: Array<Record<string, any>> }

  for (const name of ['analytics_get_session_timeline', 'analytics_get_visitor_journey']) {
    const tool = manifest.tools.find(candidate => candidate.name === name)
    assert.ok(tool)
    assert.equal(tool.inputSchema.properties.from.format, 'date-time')
    assert.match(tool.inputSchema.properties.from.description, /90 days/)
    assert.equal(tool.inputSchema.properties.to.format, 'date-time')
    assert.match(tool.inputSchema.properties.to.description, /366 days/)
    assert.deepEqual(tool.outputSchema.required, ['ok', 'data'])
    assert.equal(tool.outputSchema.properties.data.properties.journeyTier.const, 'confirmed')
    assert.equal(tool.outputSchema.properties.data.properties.candidateAssisted.type, 'null')
    for (const field of ['subject', 'range', 'summary', 'commonPages', 'acquisition', 'eventBreakdown', 'sessions', 'items', 'pageInfo']) {
      assert.ok(tool.outputSchema.properties.data.required.includes(field), `${name}.${field}`)
    }
  }

  assert.match(files.nodeVisitor, /from\?: string/)
  assert.match(files.nodeVisitor, /to\?: string/)
  assert.match(files.nodeVisitor, /candidateAssisted: null/)
  assert.match(files.nodeVisitor, /commonPages:/)
  assert.match(files.nodeVisitor, /eventBreakdown:/)
  assert.match(files.nodeVisitor, /occurredAt: string/)
  for (const python of [files.scraperPythonVisitor, files.memoryPythonVisitor]) {
    assert.match(python, /from_: str \| None/)
    assert.match(python, /alias="from"/)
    assert.match(python, /to: str \| None/)
  }
  assert.match(files.cli, /"name": "analytics_get_visitor_journey"/)
  assert.match(files.curl, /`analytics_get_visitor_journey` — Get Visitor Journey/)
  assert.match(files.example, /getVisitorJourney/)
  assert.match(files.example, /commonPages/)
  assert.match(files.example, /chronology/)
})
