import assert from 'node:assert/strict'
import { execFileSync } from 'node:child_process'
import { mkdtempSync, readFileSync, rmSync, writeFileSync } from 'node:fs'
import { tmpdir } from 'node:os'
import { join } from 'node:path'
import test from 'node:test'

test('server-owned REST paths and errors project into the complete OpenAPI contract', () => {
  const source = JSON.parse(readFileSync('contracts/server-rest.v1.json', 'utf8'))
  const openapi = JSON.parse(readFileSync('contracts/scraper.openapi.generated.json', 'utf8'))
  assert.equal(openapi['x-server-rest-contract-sha256'], source.sourceContractSha256)
  assert.deepEqual(openapi.components.schemas.MapsSearchRequest.required, ['query'])
  assert.equal(openapi.paths['/maps/search'].post.operationId, 'mapsSearch')
  assert.ok(openapi.paths['/maps/search'].post.parameters.some((parameter: { name: string }) => parameter.name === 'Idempotency-Key'))
  assert.equal(openapi.paths['/directory/run'].post.responses['202'].content['application/json'].schema.$ref, '#/components/schemas/DirectoryJobResponse')
  assert.equal(openapi.paths['/directory/jobs/{jobId}'].get.responses['404'].content['application/json'].schema.$ref, '#/components/schemas/DirectoryJobNotFound')
  assert.ok(openapi.components.schemas.PublicErrorEnvelope.properties.error_code.enum.includes('directory_job_not_found'))
})

test('source parity rejects a changed server artifact with an unchanged digest', () => {
  const temp = mkdtempSync(join(tmpdir(), 'mcpscraper-rest-tamper-'))
  try {
    const source = JSON.parse(readFileSync('contracts/server-rest.v1.json', 'utf8'))
    source.operations[0].summary = 'Changed without regenerating the server digest'
    const file = join(temp, 'public-rest.v1.json')
    writeFileSync(file, JSON.stringify(source))
    assert.throws(() => execFileSync(process.execPath, [
      'scripts/project-public-rest-contract.mjs', '--check', `--source=${file}`,
    ], { stdio: 'pipe' }), /Command failed/)
  } finally {
    rmSync(temp, { recursive: true, force: true })
  }
})
