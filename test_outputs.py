import json
import re
from collections import Counter
from pathlib import Path

LOG_PATH = Path("/app/access.log")
REPORT_PATH = Path("/app/report.json")
EXPECTED_KEYS = {"total_requests", "unique_ips", "status_counts", "path_counts", "top_path"}
REQUEST_RE = re.compile(r'"[A-Z]+\s+(?P<path>\S+)\s+HTTP/[^\"]+"\s+(?P<status>\d{3})\b')


def parse_access_log():
    ips = set()
    status_counts = Counter()
    path_counts = Counter()
    total_requests = 0

    for line in LOG_PATH.read_text().splitlines():
        line = line.strip()
        if not line:
            continue

        total_requests += 1
        ips.add(line.split()[0])

        match = REQUEST_RE.search(line)
        assert match is not None, f"Could not parse log line: {line}"
        status_counts[match.group("status")] += 1
        path_counts[match.group("path")] += 1

    top_path = sorted(path_counts.items(), key=lambda item: (-item[1], item[0]))[0][0]

    return {
        "total_requests": total_requests,
        "unique_ips": len(ips),
        "status_counts": dict(sorted(status_counts.items())),
        "path_counts": dict(sorted(path_counts.items())),
        "top_path": top_path,
    }


def load_report():
    assert REPORT_PATH.exists(), "Missing required artifact: /app/report.json"
    return json.loads(REPORT_PATH.read_text())


def test_report_exists_valid_json_and_exact_keys():
    """Verifies instruction.md success criterion 1: create /app/report.json as valid JSON with exactly the required keys."""
    report = load_report()
    assert set(report.keys()) == EXPECTED_KEYS


def test_total_requests_matches_access_log():
    """Verifies instruction.md success criterion 2: total_requests equals the number of non-empty request lines."""
    report = load_report()
    expected = parse_access_log()
    assert report["total_requests"] == expected["total_requests"]


def test_unique_ips_matches_access_log():
    """Verifies instruction.md success criterion 3: unique_ips equals the number of distinct client IP addresses."""
    report = load_report()
    expected = parse_access_log()
    assert report["unique_ips"] == expected["unique_ips"]


def test_status_counts_match_access_log():
    """Verifies instruction.md success criterion 4: status_counts has exact counts by HTTP status code."""
    report = load_report()
    expected = parse_access_log()
    assert report["status_counts"] == expected["status_counts"]


def test_path_counts_match_access_log():
    """Verifies instruction.md success criterion 5: path_counts has exact counts by request path."""
    report = load_report()
    expected = parse_access_log()
    assert report["path_counts"] == expected["path_counts"]


def test_top_path_matches_access_log():
    """Verifies instruction.md success criterion 6: top_path is the highest-count path, alphabetically first on ties."""
    report = load_report()
    expected = parse_access_log()
    assert report["top_path"] == expected["top_path"]
