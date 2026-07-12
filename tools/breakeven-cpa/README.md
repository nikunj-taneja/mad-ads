# Breakeven CPA calculator

**Maturity: working starter.** Dependency-free and covered by synthetic tests. Its output is only as accurate as the cost inputs; an operator should confirm tax and contribution-margin treatment with their accountant.

Breakeven CPA is CM2 per order: net revenue less COGS, payment fees, returns allowance, shipping, and packaging. It is not a recommended bid or budget.

Use an aggregate JSON:

```json
{"gross_revenue":10000,"tax":1000,"cogs":2500,"payment_fees":300,"returns_allowance":200,"shipping":500,"packaging":100,"orders":10}
```

```bash
python3 tools/breakeven-cpa/compute.py --summary data/unit-economics.json --current-cpa 450
```

Or use a one-row-per-order CSV. `gross_revenue` is required; optional columns are `tax,cogs,payment_fees,returns_allowance,shipping,packaging`. Empty optional cells use rates or per-order values from `--defaults`:

```json
{"tax_rate":0.1,"cogs_rate":0.25,"payment_fee_rate":0.03,"returns_rate":0.02,"shipping_per_order":5,"packaging_per_order":1}
```

Add `--json` for machine-readable output. Keep real exports in `data/`, which is gitignored.
