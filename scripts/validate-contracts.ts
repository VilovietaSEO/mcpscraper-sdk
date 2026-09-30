import { spawnSync } from 'node:child_process'

function run(label: string, command: string, args: string[]): boolean {
  console.log(`\n--- ${label} ---`)
  const result = spawnSync(command, args, { stdio: 'inherit' })
  return result.status === 0
}

function main(): void {
  const scheduledResultsOk = run(
    'Scheduled results contract source check',
    'node',
    ['--import', 'tsx', 'scripts/check-scheduled-results-contract.ts'],
  )
  const restProjectionOk = run('REST source and generated-model drift', 'npm', ['run', 'verify:rest-contract'])
  const serverRestSource = process.env.MCP_REST_CONTRACT_PATH
  const restSourceOk = serverRestSource
    ? run('Server-to-SDK REST source parity', 'npm', ['run', 'verify:rest-source-contract', '--', `--source=${serverRestSource}`])
    : false
  if (!serverRestSource) console.error('MCP_REST_CONTRACT_PATH is required for server-to-SDK REST source parity.')
  const openapiOk = run('Generated REST OpenAPI lint', 'npx', ['-y', '@redocly/cli', 'lint', 'contracts/scraper.openapi.generated.json'])
  const manifestOk = run('Memory manifest drift check', 'npx', ['tsx', 'scripts/sync-memory-manifest.ts'])
  const unifiedManifestOk = run('Unified manifest drift check', 'npx', ['tsx', 'scripts/sync-mcp-manifest.ts'])
  const parityOk = run('All SDK/CLI/cURL parity', 'npm', ['run', 'verify:parity'])

  console.log(`\nScheduled results contract: ${scheduledResultsOk ? 'PASS' : 'FAIL'}`)
  console.log(`\nREST source and generated-model drift: ${restProjectionOk ? 'PASS' : 'FAIL'}`)
  console.log(`Server-to-SDK REST source parity: ${restSourceOk ? 'PASS' : 'FAIL'}`)
  console.log(`Generated REST OpenAPI lint: ${openapiOk ? 'PASS' : 'FAIL'}`)
  console.log(`Memory manifest drift: ${manifestOk ? 'PASS' : 'FAIL'}`)
  console.log(`Unified manifest drift: ${unifiedManifestOk ? 'PASS' : 'FAIL'}`)
  console.log(`All-surface parity: ${parityOk ? 'PASS' : 'FAIL'}`)

  process.exitCode = scheduledResultsOk && restProjectionOk && restSourceOk && openapiOk
    && manifestOk && unifiedManifestOk && parityOk ? 0 : 1
}

main()
