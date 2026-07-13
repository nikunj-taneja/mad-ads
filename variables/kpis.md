# KPI and decision configuration

Fill this before running the media-buyer skill. Use business economics, not generic benchmarks. Values marked `[NEEDS INPUT]` prevent an agent from making the affected recommendation.

## Account context

- Currency: [NEEDS INPUT]
- Account timezone: [NEEDS INPUT]
- Reporting timezone: [NEEDS INPUT]
- Meta attribution setting/window: [NEEDS INPUT]
- Commerce revenue definition (gross/net, tax, shipping, refunds): [NEEDS INPUT]
- Average order value (AOV): [NEEDS INPUT]
- Contribution margin before advertising: [NEEDS INPUT]

## Economics

- Target CPA/CAC: [NEEDS INPUT]
- Maximum acceptable CPA/CAC: [NEEDS INPUT]
- Break-even CPA/CAC: [NEEDS INPUT]
- Target blended ROAS: [NEEDS INPUT]
- Break-even ROAS: [NEEDS INPUT]
- Target Meta-attributed ROAS: [NEEDS INPUT]

## Evidence floors

- Automatic WAIT below spend: [NEEDS INPUT; suggested expression: `1.0 × AOV`]
- Verdict-ready spend: [NEEDS INPUT; suggested expression: `1.5 × AOV`]
- High-confidence spend: [NEEDS INPUT; suggested expression: `3.0 × AOV`]
- Minimum purchases for KEEP: [NEEDS INPUT]
- Minimum purchases for SCALE: [NEEDS INPUT]
- Decay evaluation period and spend floor: [NEEDS INPUT]
- Lifetime lookback source/path: [NEEDS INPUT]

## Creative and funnel attention bands

Definitions must match the export/parser.

- Minimum acceptable Hook Rate: [NEEDS INPUT]
- Strong Hook Rate: [NEEDS INPUT]
- Minimum acceptable Hold Rate: [NEEDS INPUT]
- Strong Hold Rate: [NEEDS INPUT]
- Minimum acceptable link/outbound CTR: [NEEDS INPUT]
- Strong link/outbound CTR: [NEEDS INPUT]
- Minimum CVR and denominator: [NEEDS INPUT]
- Maximum cost per ATC: [NEEDS INPUT]
- Minimum ATC → Checkout rate: [NEEDS INPUT]
- Maximum cost per checkout: [NEEDS INPUT]
- Minimum Checkout → Purchase rate: [NEEDS INPUT]
- CVR sharp-drop threshold: [NEEDS INPUT; suggested: `>40%`]
- Fatigue warning frequency: [NEEDS INPUT]
- Severe saturation frequency: [NEEDS INPUT]

## Reach and audience

- Feeder/Star CPMR band: [NEEDS INPUT; suggested: `<0.7 × active median`]
- Converter/Saturated CPMR band: [NEEDS INPUT; suggested: `>1.3 × active median`]
- Maximum existing-customer spend share in prospecting: [NEEDS INPUT]
- Minimum audience-segment coverage for decisions: [NEEDS INPUT]

## Budget controls

- Maximum same-day budget change: [NEEDS INPUT; common ceiling: `50%`]
- Proven-campaign raise step: [NEEDS INPUT]
- ABO viable daily floor: [NEEDS INPUT; suggested expression: `0.5 × AOV`]
- Desired days for a new test to reach verdict-ready spend: [NEEDS INPUT]
- Maximum concurrent creatives per shared-budget ad set: [NEEDS INPUT; common range: `3–4`]
- Cap utilisation below which budget is non-binding: [NEEDS INPUT; suggested: `<80%`]
- Recent/long-window divergence that blocks a raise: [NEEDS INPUT; suggested: `3d < 0.75 × 7d`]
- Per-ad campaign-spend share that makes decay campaign-blocking: [NEEDS INPUT; suggested: `≥30%`]
- Seasonality/month-phase factors: [NEEDS INPUT or NOT USED]

## Campaign map

- Creative-testing campaign(s): [NEEDS INPUT]
- Scaling/automated-shopping campaign(s): [NEEDS INPUT]
- Bid-cap campaign(s): [NEEDS INPUT or NOT USED]
- Default graduation destination: [NEEDS INPUT]
- Graduation criteria overrides: [NEEDS INPUT or use economics/evidence floors above]

## Execution safety

- Default external action mode: DRY RUN
- Require explicit human confirmation before account mutation: YES
- Require all newly created entities to start paused: YES
