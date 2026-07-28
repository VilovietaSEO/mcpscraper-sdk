import { existsSync } from 'node:fs'
import { spawnSync } from 'node:child_process'
import { resolve } from 'node:path'

const [project, ...args] = process.argv.slice(2)

if (!project || args.length === 0) {
  console.error('Usage: node scripts/run-python-project.mjs <project> <python arguments...>')
  process.exit(2)
}

const python = resolve(
  project,
  process.platform === 'win32' ? '.venv/Scripts/python.exe' : '.venv/bin/python',
)

if (!existsSync(python)) {
  console.error(`Missing project virtual environment: ${python}`)
  console.error(`Create it first with: UV_CACHE_DIR=.cache/uv uv sync --project ${project}`)
  process.exit(2)
}

const result = spawnSync(python, args, {
  cwd: process.cwd(),
  stdio: 'inherit',
})

if (result.error) {
  throw result.error
}

process.exit(result.status ?? 1)
