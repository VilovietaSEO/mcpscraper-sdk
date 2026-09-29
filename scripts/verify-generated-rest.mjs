import { execFileSync } from 'node:child_process'
import { mkdtempSync, readFileSync, rmSync } from 'node:fs'
import { tmpdir } from 'node:os'
import { join, resolve } from 'node:path'

const root = process.cwd()
execFileSync(process.execPath, ['scripts/project-public-rest-contract.mjs', '--check'], { stdio: 'inherit' })
const temp = mkdtempSync(join(tmpdir(), 'mcpscraper-rest-contract-'))
try {
  const nodeOutput = join(temp, 'schema.ts')
  const pythonOutput = join(temp, 'models.py')
  execFileSync(resolve('node_modules/.bin/openapi-typescript'), [
    'contracts/scraper.openapi.generated.json', '-o', nodeOutput,
  ], { stdio: 'inherit' })
  execFileSync(process.execPath, [
    'scripts/run-python-project.mjs', 'packages/scraper-python',
    'packages/scraper-python/scripts/generate-rest-python.py', pythonOutput,
  ], { stdio: 'inherit' })
  for (const [expected, actual] of [
    ['packages/scraper/src/schema.ts', nodeOutput],
    ['packages/scraper-python/src/mcpscraper/models.py', pythonOutput],
  ]) {
    if (readFileSync(expected, 'utf8') !== readFileSync(actual, 'utf8')) {
      throw new Error(`${expected} is stale; run npm run generate:rest`)
    }
  }
  console.log('Node and Python REST models match generated OpenAPI.')
} finally {
  rmSync(temp, { recursive: true, force: true })
}
