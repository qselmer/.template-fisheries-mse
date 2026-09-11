from pathlib import Path

import yaml

root = Path(__file__).resolve().parents[2]
missing = []
errors = []

# La documentación principal del template es en español.
# Los archivos .en.md existentes son complementarios y no son obligatorios.
for d in [p for p in root.rglob('*') if p.is_dir() and '.git' not in p.parts]:
    rel = d.relative_to(root)
    if rel == Path('.github'):
        if not (d / 'ABOUT.md').exists():
            missing.append(str((d / 'ABOUT.md').relative_to(root)))
        continue
    if not (d / 'README.md').exists():
        missing.append(str((d / 'README.md').relative_to(root)))

required = [
    'README.md',
    'template.yml',
    'repo.yml',
    'species_profile.yml',
    'publication.yml',
    'CITATION.cff',
    'VERSION',
    'config/operating_model.yml',
    'config/observation_model.yml',
    'config/estimation_model.yml',
    'config/implementation_model.yml',
]

for f in required:
    if not (root / f).exists():
        missing.append(f)

for path in sorted(list(root.rglob('*.yml')) + list(root.rglob('*.yaml'))):
    if '.git' in path.parts:
        continue
    try:
        with path.open('r', encoding='utf-8') as handle:
            yaml.safe_load(handle)
    except Exception as exc:
        errors.append(f'{path.relative_to(root)}: YAML inválido ({exc})')


def load_yaml(relative_path):
    path = root / relative_path
    if not path.exists():
        return {}
    with path.open('r', encoding='utf-8') as handle:
        return yaml.safe_load(handle) or {}


if (root / 'template.yml').exists():
    meta = load_yaml('template.yml').get('template', {})
    expected = {
        'repository': '.template-mse',
        'type': 'type-template',
        'produces': 'type-project',
        'version': '1.0.0',
        'language': 'es',
    }
    for key, value in expected.items():
        if str(meta.get(key)) != value:
            errors.append(f'template.yml: {key} debe ser {value!r}')

if (root / 'repo.yml').exists():
    contract = load_yaml('repo.yml')
    if contract.get('schema_version') != 2:
        errors.append('repo.yml: schema_version debe ser 2')

    repo = contract.get('repository', {})
    expected = {
        'owner': 'qselmer',
        'name': '.template-mse',
        'type': 'type-template',
        'status': 'active',
        'stage': 'stable',
        'visibility': 'public',
        'version': '1.0.0',
    }
    for key, value in expected.items():
        if str(repo.get(key)) != value:
            errors.append(f'repo.yml: repository.{key} debe ser {value!r}')

    topics = repo.get('topics', []) or []
    type_topics = [topic for topic in topics if str(topic).startswith('type-')]
    if type_topics != ['type-template']:
        errors.append("repo.yml: debe existir exactamente un topic 'type-template'")

    integration = contract.get('integration', {}) or {}
    profile = integration.get('profile', {}) or {}
    if profile.get('include') is not True:
        errors.append('repo.yml: integration.profile.include debe ser true')

    expected_url = 'https://github.com/qselmer/.template-mse'
    if integration.get('repository_url') != expected_url:
        errors.append(f'repo.yml: integration.repository_url debe ser {expected_url!r}')

version_file = root / 'VERSION'
if version_file.exists() and version_file.read_text(encoding='utf-8').strip() != '1.0.0':
    errors.append('VERSION debe ser 1.0.0')

if missing or errors:
    print('Repository check: FAIL')
    if missing:
        print('\nArchivos faltantes:')
        print('\n'.join(f'- {item}' for item in sorted(set(missing))))
    if errors:
        print('\nErrores:')
        print('\n'.join(f'- {item}' for item in errors))
    raise SystemExit(1)

print('Repository check: PASS')
