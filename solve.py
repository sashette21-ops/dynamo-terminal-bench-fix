import json
import re
from collections import Counter
from pathlib import Path

LOG_PATH = Path("/app/access.log")
REPORT_PATH = Path("/app/report.json")

REQUEST_RE = re.compile(r'"[A-Z]+\s+(?P<path>\S+)\s+HTTP/[^\"]+"\s+(?P<status>\d{3})\b')

ips = set()
status_counts = Counter()
path_counts = Counter()
total_requests = 0

for line in LOG_PATH.read_text().splitlines():
    line = line.strip()
    if not line:
        continue

    total_requests += 1
    parts = line.split()
    ips.add(parts[0])

    match = REQUEST_RE.search(line)
    if not match:
        raise ValueError(f"Could not parse log line: {line}")

    status_counts[match.group("status")] += 1
    path_counts[match.group("path")] += 1

top_path = sorted(path_counts.items(), key=lambda item: (-item[1], item[0]))[0][0]

report = {
    "total_requests": total_requests,
    "unique_ips": len(ips),
    "status_counts": dict(sorted(status_counts.items())),
    "path_counts": dict(sorted(path_counts.items())),
    "top_path": top_path,
}

REPORT_PATH.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
