# Hook-rate tracker

**Maturity: working starter.** Dependency-free and synthetic-test covered. Meta export column availability varies, so inspect exports when the required-column error appears.

Rank video ads across one or more Meta Ads CSV exports:

```bash
python3 tools/hook-rate/track.py data/meta-week-1.csv data/meta-week-2.csv
python3 tools/hook-rate/track.py data/meta-week-1.csv --min-impressions 1000 --json
```

Required columns: `Ad name`, `Impressions`, `3-second video plays` (or `Video plays at 3 seconds`), and `Hook Rate`. Optional columns include `Hold Rate (50%)`, `Amount spent`, and `Purchases`.

Duplicate ad names across files are combined. Hook rate is weighted by impressions; 50% hold rate is weighted by 3-second plays. Both `0.35` and `35%` are accepted. This tool deliberately does not impose universal “good/bad” thresholds—put account-specific benchmarks in `variables/` and interpret adequate sample sizes in context.
