# Dynamo Log Report

You are given an Apache-style access log at:

`/app/access.log`

Create a JSON report at:

`/app/report.json`

The report must be valid JSON and must contain exactly these top-level keys:

```json
{
  "total_requests": 0,
  "unique_ips": 0,
  "status_counts": {},
  "path_counts": {},
  "top_path": ""
}
```

## Parsing rules

Each non-empty line in `/app/access.log` is one request.

For each request:

- The client IP address is the first whitespace-separated field.
- The request path is the path inside the quoted HTTP request, for example `/index.html` from `"GET /index.html HTTP/1.1"`.
- The HTTP status code is the three-digit status code after the quoted HTTP request.

## Success criteria

1. Create `/app/report.json` as valid JSON with exactly the keys `total_requests`, `unique_ips`, `status_counts`, `path_counts`, and `top_path`.
2. `total_requests` must equal the number of non-empty request lines in `/app/access.log`.
3. `unique_ips` must equal the number of distinct client IP addresses in `/app/access.log`.
4. `status_counts` must be an object whose keys are HTTP status codes as strings and whose values are exact request counts.
5. `path_counts` must be an object whose keys are request paths and whose values are exact request counts.
6. `top_path` must be the request path with the highest count. If two or more paths tie, choose the alphabetically first path.

Do not use the internet. Do not write the final answer anywhere except `/app/report.json`.
