# Tool registry

| Tool | Purpose | Typical caller | Status |
|---|---|---|---|
| `parse-meta-csv/parse.py` | Inspect a Meta CSV and report usable column mappings | media-buyer | working starter |
| `check-script-length/check.py` | Estimate spoken duration from a Markdown script | sugarman | working starter |
| `privacy-scan.py` | Scan tracked-style text for secrets and operator-defined identifiers | maintainer | working starter |
| `doctor.py` | Report missing core inputs and optional integrations | onboarding agent/operator | working starter |
| `meta-ads-auditor/audit.py` | Validate Meta access and optionally list campaigns | operator/agent | working starter, live unverified |
| `meta-ads-uploader/upload.py` | Dry-run or create one PAUSED link ad from an existing image hash | operator/agent | partial, live unverified |
| `breakeven-cpa/compute.py` | Calculate contribution before acquisition and breakeven CPA | media-buyer | working local tool |
| `hook-rate/track.py` | Aggregate weighted video hook and hold metrics | media-buyer | working local tool |
| `verdicts/validate.py` | Validate an ad-verdict JSON contract | media-buyer | working local tool |
| `run-tests.py` | Run dependency-free unit tests | maintainer/agent | working |

Add one row whenever a reusable tool is added, renamed, or retired.
