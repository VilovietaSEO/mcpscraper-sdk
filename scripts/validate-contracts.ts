import { spawnSync } from 'node:child_process'

function run(label: string, command: string, args: string[]): boolean {
  console.log(`\n--- ${label} ---`)
  const result = spawnSync(command, args, { stdio: 'inherit' })
  return result.status === 0
}

function main(): void {
  const openapiOk = run('OpenAPI lint', 'npx', ['-y', '@redocly/cli', 'lint', 'contracts/scraper.openapi.yaml'])
  const manifestOk = run('Memory manifest drift check', 'npx', ['tsx', 'scripts/sync-memory-manifest.ts'])

  console.log(`\nOpenAPI lint: ${openapiOk ? 'PASS' : 'FAIL'}`)
  console.log(`Memory manifest drift: ${manifestOk ? 'PASS' : 'FAIL'}`)

  process.exitCode = openapiOk && manifestOk ? 0 : 1
}

main()
