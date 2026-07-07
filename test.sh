#!/usr/bin/env bash
set -uo pipefail

cd /app
pytest /tests/test_outputs.py -rA 2>&1 | tee /tmp/pytest-output.txt
status=${PIPESTATUS[0]}

if [ "$status" -eq 0 ]; then
  echo 1 > /app/reward.txt
else
  echo 0 > /app/reward.txt
fi

python3 - <<'PY'
import json
import re
from pathlib import Path

text = Path('/tmp/pytest-output.txt').read_text()
summary = {
    'tests': 0,
    'passed': 0,
    'failed': 0,
    'skipped': 0,
    'pending': 0,
    'other': 0,
}

patterns = {
    'passed': r'(\d+) passed',
    'failed': r'(\d+) failed',
    'skipped': r'(\d+) skipped',
    'pending': r'(\d+) pending',
}

for key, pattern in patterns.items():
    match = re.search(pattern, text)
    if match:
        summary[key] = int(match.group(1))

summary['tests'] = summary['passed'] + summary['failed'] + summary['skipped'] + summary['pending'] + summary['other']

ctrf = {
    'results': {
        'tool': {'name': 'pytest'},
        'summary': summary,
        'tests': []
    }
}

Path('/app/ctrf.json').write_text(json.dumps(ctrf, indent=2) + '\n')
PY

exit 0
