#!/usr/bin/env bash
# Install the actual skill tree into a disposable project, never user directories.
set -euo pipefail

repo_root=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
test_root=$(mktemp -d)
trap 'rm -rf "$test_root"' EXIT
node_executable=$(node -p 'process.execPath')
export DISABLE_TELEMETRY=1

npm install --prefix "$test_root/tooling" --ignore-scripts --no-package-lock \
  --no-audit --no-fund skills@1.7.6
mkdir -p "$test_root/source" "$test_root/project"
cp -R "$repo_root/skills" "$test_root/source/skills"

# A future skill in another category must be included without an explicit list.
fixture="$test_root/source/skills/life/travel/distribution-fixture"
mkdir -p "$fixture/assets"
cat > "$fixture/SKILL.md" <<'EOF'
---
name: distribution-fixture
description: Synthetic skill used only by the distribution smoke test.
---
Read assets/checklist.txt when preparing the fictional trip.
EOF
printf 'A synthetic packing checklist.\n' > "$fixture/assets/checklist.txt"

cd "$test_root/project"
"$node_executable" "$test_root/tooling/node_modules/skills/bin/cli.mjs" \
  add "$test_root/source" --skill '*' \
  --agent claude-code codex cursor gemini-cli --full-depth --yes

python3 - "$test_root/source/skills" <<'PY'
import sys
from pathlib import Path

source = Path(sys.argv[1])
skills = sorted(source.rglob('SKILL.md'))
assert len(skills) >= 2, 'Expected real skills plus the future-skill fixture'
names = [skill.parent.name for skill in skills]
assert len(names) == len(set(names)), 'Skill names must be unique across categories'

for skill in skills:
    name = skill.parent.name
    canonical = Path('.agents/skills') / name
    claude = Path('.claude/skills') / name
    assert canonical.is_dir(), f'{name} was not installed to the shared directory'
    assert claude.is_symlink(), f'Claude Code is missing its link for {name}'
    assert claude.resolve() == canonical.resolve(), f'{name} has divergent installs'
    for original in skill.parent.rglob('*'):
        if original.is_file():
            relative = original.relative_to(skill.parent)
            assert (canonical / relative).read_bytes() == original.read_bytes(), (
                f'{name}/{relative} missing or changed during installation'
            )

installed = {path.name for path in Path('.agents/skills').iterdir()}
assert installed == set(names), f'Unexpected installed skill directories: {installed}'
assert Path('skills-lock.json').is_file(), 'Project installation was not recorded'
print(f'PASS: {len(skills)} skills installed, with complete payloads and shared Claude links')
PY
