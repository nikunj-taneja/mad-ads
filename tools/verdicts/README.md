# Verdict report validator

**Maturity: working starter.** Dependency-free, synthetic-test covered, and intentionally decoupled from any dashboard or kill-list implementation.

Validate the media buyer's machine-readable handoff before another agent or tool consumes it:

```bash
python3 tools/verdicts/validate.py analysis/verdicts.json
```

Required fields are `generated` (`YYYY-MM-DD`), `period.since`, `period.until`, a non-empty `take`, and a non-empty `verdicts` list. Each verdict needs `ad`, `reason`, and one of `PAUSE`, `WAIT`, `KEEP`, `SCALE`, `ITERATE`, or `RESTRUCTURE`.

Optional `actions` entries accept the tags `pause`, `redirect`, `scale`, or `watch`. `budget_plan` and `data_flags` must be lists when present. This validates shape, not whether a recommendation is strategically correct or safe to execute.
