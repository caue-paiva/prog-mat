"""Empacota entregáveis e gera hashes, excluindo caches, ambientes e licenças."""
from pathlib import Path
import hashlib
import zipfile
ROOT=Path(__file__).resolve().parents[1]
paths=[]
for p in sorted(ROOT.rglob('*')):
    if not p.is_file(): continue
    rel=p.relative_to(ROOT)
    if any(part.startswith('.') or part in ('__pycache__','build','dist') or part.endswith('.egg-info') for part in rel.parts): continue
    if p.suffix in ('.pyc','.lic','.zip') or p.name=='SHA256SUMS.txt':continue
    paths.append(p)
manifest=ROOT/'SHA256SUMS.txt'
manifest.write_text(''.join(f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(ROOT)}\n' for p in paths))
output=ROOT.parent/'projeto_sobrevivencia.zip'
with zipfile.ZipFile(output,'w',zipfile.ZIP_DEFLATED) as z:
    for p in paths+[manifest]: z.write(p,Path('prog-mat')/p.relative_to(ROOT))
print(output)
