# Dynamo Terminal-Bench Fix

This repository contains a corrected Harbor Terminal-Bench 2 task for `dynamo/log-report`.

## What was fixed

### Format
`task.toml` was corrected so `artifacts` is a top-level array, not a string. The task, verifier, metadata, and environment sections follow the required Harbor structure.

### Environment
The Dockerfile uses one environment image and installs verifier dependencies during the image build. The reference solution is not copied into the agent image. Replace `REPLACE_WITH_APPROVED_PINNED_DIGEST` with the approved pinned `sha256` digest required by your Harbor environment.

### Verifier
The original verifier was gameable because it only checked whether an output file existed. The corrected verifier parses `access.log` independently and checks each required value exactly.

### Instruction
`instruction.md` now has five clear success criteria. The verifier has exactly one test per criterion and no extra checks.

## Files

```text
dynamo-terminal-bench-fix/
├── README.md
├── task.toml
├── instruction.md
├── access.log
├── environment/
│   └── Dockerfile
├── solution/
│   └── solve.sh
└── tests/
    ├── test.sh
    └── test_outputs.py
```

## Expected verifier behavior

- Oracle solution should produce `reward.txt = 1`.
- Nop agent should produce `reward.txt = 0`.
- A bugged solution with an incorrect count should produce `reward.txt = 0`.

## Note

Before final submission, run the task in your Terminal-Bench environment and paste the real `reward.txt` and `ctrf.json` summaries from your machine.
