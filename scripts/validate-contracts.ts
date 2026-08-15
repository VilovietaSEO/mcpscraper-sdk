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
  const publicProductContractOk = run(
    'Public product contract convergence',
    'node',
    ['--import', 'tsx', 'scripts/check-public-product-contract.ts'],
  )
  const openapiOk = run('OpenAPI lint', 'npx', ['-y', '@redocly/cli', 'lint', 'contracts/scraper.openapi.yaml'])
  const manifestOk = run('Memory manifest drift check', 'npx', ['tsx', 'scripts/sync-memory-manifest.ts'])
  const unifiedManifestOk = run('Unified manifest drift check', 'npx', ['tsx', 'scripts/sync-mcp-manifest.ts'])
  const parityOk = run('All SDK/CLI/cURL parity', 'npm', ['run', 'verify:parity'])

  console.log(`\nScheduled results contract: ${scheduledResultsOk ? 'PASS' : 'FAIL'}`)
  console.log(`Public product contract: ${publicProductContractOk ? 'PASS' : 'FAIL'}`)
  console.log(`\nOpenAPI lint: ${openapiOk ? 'PASS' : 'FAIL'}`)
  console.log(`Memory manifest drift: ${manifestOk ? 'PASS' : 'FAIL'}`)
  console.log(`Unified manifest drift: ${unifiedManifestOk ? 'PASS' : 'FAIL'}`)
  console.log(`All-surface parity: ${parityOk ? 'PASS' : 'FAIL'}`)

  process.exitCode = scheduledResultsOk && publicProductContractOk && openapiOk && manifestOk && unifiedManifestOk && parityOk ? 0 : 1
}

main()
