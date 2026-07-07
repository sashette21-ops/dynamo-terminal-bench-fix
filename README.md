# Dynamo Log Report — Fixed Harbor Task

This repository contains the repaired Terminal-Bench 2 / Harbor task for `dynamo/log-report`.

## What was fixed

- `task.toml`: changed `artifacts` from a string to a top-level array and pointed it to `/app/report.json`; normalized metadata fields to scalar lowercase snake_case values; removed non-template fields; disabled internet.
- `environment/Dockerfile`: replaced `python:latest` with a pinned digest image and removed the leaked `solution_hint.py` from the agent image.
- `tests/test_outputs.py`: replaced existence-only checks with value checks that independently parse `/app/access.log`.
- `tests/test.sh`: runs plain pytest without verify-time installs, writes `/app/reward.txt`, and emits `/app/ctrf.json`.
- `instruction.md`: rewrote the instructions so each success criterion maps one-to-one to a verifier test.
- `solution/solve.py`: fixed the oracle to produce the exact JSON schema and values required by the instructions.

## Expected outputs for the included access.log

```json
{
  "path_counts": {
    "/about.html": 2,
    "/api/login": 1,
    "/index.html": 3
  },
  "status_counts": {
    "200": 5,
    "401": 1
  },
  "top_path": "/index.html",
  "total_requests": 6,
  "unique_ips": 3
}
```
