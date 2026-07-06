# Dynamo Log Report

You are given an access log at:

`/app/access.log`

Create a JSON file at:

`/app/report.json`

The JSON file must contain exactly these top-level keys:

```json
{
  "total_requests": 0,
  "status_counts": {},
  "top_endpoint": "",
  "average_latency_ms": 0.0
}
```

## Success criteria

1. Create `/app/report.json` as valid JSON.
2. `total_requests` must equal the number of parsed request log entries in `/app/access.log`.
3. `status_counts` must be an object whose keys are HTTP status codes as strings and whose values are exact counts.
4. `top_endpoint` must be the endpoint path that appears most often. If there is a tie, choose the alphabetically first endpoint.
5. `average_latency_ms` must be the arithmetic mean of all parsed request latencies in milliseconds, rounded to exactly 2 decimal places.

Do not use the internet. Do not write the answer anywhere except `/app/report.json`.
