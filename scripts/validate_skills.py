#!/usr/bin/env python3
from pathlib import Path
import re, sys, json
root=Path(__file__).resolve().parents[1]
errs=[]
for p in sorted((root/'skills').glob('*/SKILL.md')):
    t=p.read_text()
    if not t.startswith('---\n'): errs.append(f'{p}: missing YAML frontmatter')
    for key in ('name:','description:','version:','stage:'):
        if key not in t[:1000]: errs.append(f'{p}: missing {key}')
    if '## Handoff' not in t: errs.append(f'{p}: missing handoff contract')
manifest=json.loads((root/'skills/manifest.json').read_text())
paths={x['path'] for x in manifest['skills']}
actual={str(p.relative_to(root)) for p in (root/'skills').glob('*/SKILL.md')}
if paths != actual:
    errs.append(f'manifest mismatch: manifest={len(paths)} actual={len(actual)}')
if errs:
    print('\n'.join(errs)); sys.exit(1)
print(f'OK: {len(actual)} skills validated')
