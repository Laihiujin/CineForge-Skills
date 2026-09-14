#!/usr/bin/env python3
from pathlib import Path
import sys, shutil, re
if len(sys.argv)!=2 or not re.fullmatch(r'[a-z0-9][a-z0-9-]*',sys.argv[1]):
    raise SystemExit('usage: python3 scripts/new_project.py <lowercase-slug>')
root=Path(__file__).resolve().parents[1]
p=root/'projects'/sys.argv[1]
for d in ['00-brief','01-story','02-script','03-canon/characters','03-canon/locations','04-assets/characters','04-assets/locations','04-assets/props','04-assets/style','05-shotlist','06-prompts','07-generations','08-audio','09-edit','10-qc','11-delivery']:
    (p/d).mkdir(parents=True,exist_ok=True)
for src,dst in [('creative-brief.md','00-brief/creative-brief.md'),('shotlist.csv','05-shotlist/shotlist.csv'),('qc-report.md','10-qc/qc-report.md')]:
    shutil.copy(root/'templates'/src,p/dst)
(p/'README.md').write_text(f'# {sys.argv[1]}\n\nStart with `00-brief/creative-brief.md`, then route through the director skill.\n')
print(p)
