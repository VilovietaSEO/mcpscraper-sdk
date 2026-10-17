import { cp, mkdir, mkdtemp, rm } from 'node:fs/promises'
import { tmpdir } from 'node:os'
import { basename, dirname, join, resolve } from 'node:path'
import { fileURLToPath } from 'node:url'
import { spawnSync } from 'node:child_process'

const root = resolve(dirname(fileURLToPath(import.meta.url)), '..')
const args = process.argv.slice(2)
if (args.length && (args.length !== 2 || args[0] !== '--out-dir')) {
  throw new Error('Usage: npm run build:python -- [--out-dir <directory>]')
}
const output = resolve(args[1] ?? join(root, 'dist'))
await mkdir(output, { recursive: true })

// Hatch includes ancestor VCS ignore files even when excluded by the project.
// Build from explicit public sources so repository metadata never enters sdists.
for (const name of ['scraper-python', 'memory-python']) {
  const source = join(root, 'packages', name)
  const stage = await mkdtemp(join(tmpdir(), 'mcpscraper-python-dist-'))
  try {
    await mkdir(join(stage, '.git')) // Stop ancestor VCS metadata discovery.
    for (const file of ['README.md', 'pyproject.toml']) {
      await cp(join(source, file), join(stage, file))
    }
    await cp(join(source, 'src'), join(stage, 'src'), {
      recursive: true,
      filter: path => !['__pycache__', '.gitignore'].includes(basename(path)) && !path.endsWith('.pyc'),
    })
    const result = spawnSync('uv', ['build', '--project', stage, '--out-dir', output], {
      cwd: stage,
      stdio: 'inherit',
    })
    if (result.error) throw result.error
    if (result.status !== 0) throw new Error(`Python archive build failed for ${name}`)
  } finally {
    await rm(stage, { recursive: true, force: true })
  }
}
