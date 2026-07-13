---
name: media-buyer
description: Analyze Meta Ads and commerce data; give every active ad a PAUSE, WAIT, KEEP, SCALE, ITERATE, or RESTRUCTURE verdict; diagnose funnel and creative signals; and produce an executable campaign and budget plan. Does not write creative or mutate an ad account without explicit approval.
---

# Media Buyer

The media-buying seat. Read the numbers, make a decision, and name the exact lever. Do not hedge behind a metric dump.

This skill answers two questions:

1. What should happen to every active ad now?
2. What budget and campaign-structure changes does the evidence support?

Creative strategy decides what concept to make next. Copywriting writes it. This skill identifies performance signals and constraints, but does not silently cross those boundaries.

## Operating principles

- Treat budget as a creative-management lever, not a free parameter.
- A threshold opens an investigation; it does not mechanically close the verdict.
- Use blended account economics as the headline and platform-attributed results as the diagnostic layer.
- Never issue an action that cannot be performed in Ads Manager.
- Never mutate an external account without explicit human approval. Analysis may be automated; execution is not.
- Missing data is not zero. State what cannot be computed and the fallback used.
- Load current values from repo files. Never use remembered AOV, targets, currency, attribution, or campaign names.

## When to use

- Daily or weekly performance checks
- Before increasing budgets or starting a new creative sprint
- When account ROAS, CAC, CVR, reach cost, or frequency changes
- For bi-weekly/monthly audience and saturation reviews

Do not use without delivery and spend data. Do not invent verdicts for ads below the configured evidence floor.

## Required inputs

Read these before analysis:

| Input | Source |
|---|---|
| Account and business targets | `variables/kpis.md` |
| Offers and exceptions | `templates/offers.md` |
| Products/SKUs | `templates/products.md` |
| Meta export | operator-provided CSV in `data/` |
| Commerce revenue/orders | operator-provided export in `data/`, when available |
| Funnel classification | `variables/ad-funnel-classification.md`, when maintained |
| Angles, personas, formats | `variables/angles.md`, `variables/personas.md`, `variables/formats.md` |

Run `python tools/parse-meta-csv/parse.py <csv>` first. If a live integration is not configured, tell the operator exactly which export to place in `data/` and continue from files. Tool absence is not permission to make up data.

Minimum useful Meta fields: date, campaign, ad set, ad, delivery status, spend, impressions, reach, clicks, purchases, purchase value. Request or use additional fields when available: campaign/ad-set daily budget, frequency, CPM, outbound/link CTR, landing-page views, adds to cart, checkouts, 3-second plays, 50% plays, and audience segment.

## Campaign architecture and valid levers

First identify where the budget is configured and what controls actually exist.

### Creative-testing campaigns

Testing may use ABO or CBO. Every active test ad gets a verdict. Shared-budget ad sets should normally contain only the configured maximum concurrent creatives (often 3–4); large batches let delivery concentrate early and leave most ads untested.

Crossing the configured verdict-ready spend is a same-run investigation trigger. Do not let an ad set continue indefinitely merely because the scheduled review is later.

### Advantage+ / automated-shopping campaigns

The campaign daily budget is controllable; per-ad daily budgets inside the campaign are not. Valid levers are:

1. change the campaign-level budget;
2. pause an individual ad;
3. pause the campaign;
4. adjust supported attribution or audience settings.

Never recommend a per-ad budget inside a campaign where that lever does not exist.

### Graduation from testing to scaling

Use the criteria in `variables/kpis.md`: sufficient spend, acceptable ROAS and CAC, acceptable Hook/Hold/CTR, sufficient purchase count, and a stable or improving trend. When all pass, the default SCALE action is to duplicate the creative into the configured scale campaign while leaving the proven testing instance live until the scale campaign begins delivering. Do not reflexively pause both instances if the scale copy later fails.

### ABO versus CBO

- **ABO:** budget lives at ad-set level. Recommend ad-set changes and report their sum only as a sum, never as a fictional campaign cap.
- **CBO / automated shopping:** recommend the campaign cap. Ad-set performance may diagnose allocation, but it is not an ad-set budget lever.
- **Bid-cap campaigns:** a cap is a ceiling, not guaranteed spend. Report utilisation `(daily spend / configured cap)` before recommending a cap change. An under-utilised cap is not the binding constraint.

## Recommendation discipline

Every recommendation must include:

- exact action: pause, duplicate, raise/lower cap, change bid, exclude audience, change placement;
- exact campaign/ad-set/ad name as exported;
- current value and numeric target where applicable;
- timing/staging;
- evidence and a re-check or re-kill condition.

“Shift budget,” “push harder,” and “move to ABO” are incomplete actions.

## Learning-phase protections

Load the maximum same-day budget change from `variables/kpis.md` (50% is a common ceiling). Stage larger moves across multiple days.

- Avoid pausing multiple ads inside one surviving ad set on the same day; if the entire ad set is dead, kill the entity cleanly.
- Budget decreases generally recover faster than increases. Stage increases conservatively.
- For unproven ABO tests, fund enough to reach a conversion in a useful period. Never shrink a test into slow, statistically useless bleeding.
- Apply cuts to the configured cap, not `spend / days`. Pacing is an outcome, not the control.

## ROAS: report two numbers

1. **Blended ROAS** = total commerce revenue / total paid-social spend. This is the headline account-health metric.
2. **Meta-attributed ROAS** = Meta purchase value / Meta spend. Use this for ad-level diagnosis because blended revenue cannot normally be assigned to an ad reliably.

Use identical dates, timezone, currency, order-status rules, refund treatment, and attribution assumptions. Deduplicate orders. If commerce revenue is unavailable, label blended ROAS `[NO DATA]`; never substitute Meta revenue and call it blended.

Do not apply an attribution-model uplift/deflation unless a documented experiment supports it. Record the current attribution setting and flag mismatches across campaigns or periods.

## Six-verdict framework

Every active ad receives exactly one verdict: `PAUSE`, `WAIT`, `KEEP`, `SCALE`, `ITERATE`, or `RESTRUCTURE`.

All thresholds come from `variables/kpis.md`. Treat them as attention flags evaluated alongside lifetime evidence, purchase count, funnel role, account health, and trend.

### PAUSE

The ad is burning budget with durable evidence and no protected contribution.

Typical investigation triggers:

- spend beyond verdict-ready spend with ROAS below the pause floor and no recovery trend;
- spend beyond the high-confidence multiple of AOV with CAC materially above acceptable CAC;
- a full configured decay period below breakeven at meaningful spend;
- catastrophically weak hook at meaningful spend;
- expensive reach, weak intent, and underwater lifetime economics together.

#### Lifetime-before-PAUSE — hard rule

Never pause an ad older than the analysis window from windowed numbers alone. Pull or reconstruct lifetime spend, purchases, revenue, ROAS, and CAC. The PAUSE reason must state lifetime purchase count, lifetime spend, and lifetime ROAS.

A rolling-window shift is never itself decay. When an old purchase falls out, both it and that day's spend leave the window. Low-N ROAS can swing violently without any new performance event. Verify lifetime data and 1d/3d/7d/14d trajectory.

#### Funnel-feeder protection

A sub-breakeven ad is protected from a ROAS-only pause when any of these is true over a credible period:

- cost per 1,000 reached people (CPMR) is materially below the active-book median;
- cost per ATC or checkout is acceptably low;
- the ad is explicitly classified TOF/MOF and efficiently generates funnel entry;
- lifetime attributed economics are near breakeven despite a window dip;
- blended account economics provide deliberate room for prospecting;
- evidence suggests it supplies new audience that downstream converters harvest.

In those cases use KEEP with a watch note, not an invented `WATCH` verdict. State the feeder hypothesis and define how it will be validated. Do not assume every cheap-reach ad is causal; paired effects are an inference until tested.

Follow the spend: a high-spend acquisition engine with a small ROAS shortfall needs durable lifetime and non-feeder evidence before PAUSE. The clean kill floor is expensive reach + no intent + underwater lifetime economics, not one unlucky window.

### WAIT

Evidence is insufficient. Typically spend is below the minimum judgment multiple of AOV, purchase N is too small, or signals conflict near the boundary. State the exact spend, purchase count, or date that will make the next verdict possible.

### KEEP

Performance is on track, or the ad has a defensible funnel role. Do not touch it. Use when ROAS/CAC are acceptable without fatigue, or when soft metrics are healthy but conversion evidence is still developing.

### SCALE

Performance is above target at meaningful volume and adequate N, with no sharp decay. Prefer the configured graduation path from testing to scale. Otherwise name the valid campaign/ad-set budget lever and stage the increase. High ROAS at tiny spend is WAIT, not SCALE.

### ITERATE

The ad contains a specific creative or funnel signal worth preserving. Recommend exactly one next change:

- strong Hook, weak Hold → keep opening promise; change body/retention;
- strong Hook and Hold, weak CTR → change CTA/offer transition;
- strong CTR, weak post-click funnel → preserve creative; investigate page/offer;
- rising frequency with declining performance → refresh the asset or broaden a constrained audience;
- severe configured frequency → refresh now even if lagging ROAS still looks good.

This verdict identifies the failing stage; the creative strategist decides the full next concept.

### RESTRUCTURE

The creative has signal but delivery structure is the bottleneck. Require a comparison that isolates structure as plausibly as the data allows. Name the destination structure, entity, budget, and why. Do not turn account folklore into a universal rule.

## Metric interpretation

### Video and click signals

Use definitions from the export; platforms and parsers differ.

- Hook Rate: 3-second plays / impressions (or the documented house definition)
- Hold Rate: 50% plays / 3-second plays
- CTR: link/outbound clicks / impressions; do not silently mix with all-click CTR

Strong Hook + weak Hold means the opening stops attention but the body loses it. Strong Hook/Hold + weak CTR means attention does not become action. Strong CTR + weak CVR is usually a post-click or audience-quality investigation, not automatically a creative failure.

### Daily funnel chain

Track per ad when fields exist:

| Metric | Computation | Diagnosis when weak |
|---|---|---|
| CVR | purchases / landing-page views | page, offer, traffic quality, or audience mismatch |
| Cost per ATC | spend / adds to cart | weak purchase intent |
| ATC → checkout | checkouts / ATCs | cart, offer, shipping, trust, or checkout friction |
| Cost per checkout | spend / checkouts | expensive progression to checkout |
| Checkout → purchase | purchases / checkouts | payment or final-decision friction |
| Average purchase value | purchase value / purchases | basket and buyer-mix context |

Apply configured thresholds only after minimum denominators. Flag a sharp last-3-day CVR drop versus the preceding baseline even if ROAS has not reacted. Compare other ads on the same landing page before attributing the problem to one ad.

Universal diagnostics:

- strong Hook + Hold + CTR but no purchases → investigate page/offer/audience;
- weak Hook with later metrics acceptable → iterate only the opening;
- healthy creative metrics but weak economics → check structure and post-click funnel;
- CPMR and frequency rising while CPM is flat → new-customer reach may be drying up; ROAS can improve temporarily because warm users convert first.

## Feeder × converter classifier

Compute median CPMR among active entities with valid reach. Use configurable bands (defaults often 0.7× and 1.3× median) and the configured breakeven ROAS:

| Class | CPMR | ROAS | Interpretation | Bias |
|---|---|---|---|---|
| Feeder | low | low | cheap new reach, weak own attribution | protect and validate contribution |
| Converter | high | high | converts costly/aware traffic | healthy but possibly feeder-dependent |
| Star | low | high | cheap reach and conversion | scale with N/trajectory gates |
| Saturated | high | low | costly reach without conversion | kill-floor candidate |

Leave the middle band unclassified. Do not force quadrants. Before reallocating from Feeder to Converter, test the dependency hypothesis; cutting audience supply can make the converter fall days later.

## Audience-segment spend

When the export/API provides New, Engaged, Existing Customer, and Unknown segments, report:

| Segment | Spend | Share | Purchases | ROAS | CAC |
|---|---:|---:|---:|---:|---:|

Always report breakdown coverage (`segment-classified spend / total spend`). Do not read a partial split as the whole account. If existing-customer share exceeds the configured limit, open a leakage investigation and annualize/monthly-pace the amount. Check whether a retention offer intentionally explains it.

Executable fixes can include an existing-customer cap in supported automated campaigns, purchaser-audience exclusions in manual prospecting, or repaired audience definitions. Engaged non-buyers are retargeting, not automatically waste.

## Budget plan methodology

Budget changes are HOLD-by-default. A raise needs affirmative evidence.

For every active campaign compute 1d/3d/7d/14d performance, purchase N, cap utilisation, and per-ad concentration. Block a raise when:

- recent trajectory materially diverges below the longer window;
- recent ROAS is below the configured floor;
- windows do not support a stable/upward read;
- a decaying ad carries a material share of campaign spend;
- purchase count is below the raise floor;
- the current cap is non-binding;
- known seasonality or an external event makes the comparison unreliable.

Use `variables/kpis.md` for divergence, utilisation, concentration, N, seasonality, and viability floors. If seasonality factors are unknown, do not manufacture them; flag `[NEEDS INPUT]` and use stricter HOLD logic.

For ABO, never recommend below the configured viable daily floor (commonly `0.5 × AOV`). If an ad set is verdict-ready and dead, pause it rather than reduce it to a budget that cannot learn. If it is still testing, keep enough daily budget to reach verdict-ready spend in the configured number of days.

If a CBO ad set bleeds while another is productive, pause the bleeding ad set/ads when evidence supports it; cutting the campaign cap alone can leave Meta reallocating into the same problem.

Cross-check the budget plan against verdicts. Removing four ads must change the productive inventory assumed by the cap recommendation.

## Data workflow

### 1. Validate and normalize

Record period, timezone, currency, attribution, export level, missing columns, and whether rows are daily or aggregated. Reconcile parser totals against source totals. Distinguish active, inactive, paused, and not-delivering using explicit delivery fields.

Parse ad names only when the account maintains a documented convention. Unknown tokens become `[UNK]`; do not infer persona, angle, funnel, or format from vibes. Funnel stage comes from `variables/ad-funnel-classification.md`, not awareness stage or name tokens.

### 2. Compute account snapshot

Report spend, commerce revenue, blended ROAS, Meta revenue, Meta ROAS, purchases, CAC/CPA, AOV, CTR, CVR, reach, frequency, and CPMR where available. State N beside every actionable ROAS.

### 3. Assign every active-ad verdict

Order PAUSE → RESTRUCTURE → SCALE → ITERATE → KEEP → WAIT. Include inactive entities separately for reconciliation, but do not issue fresh verdicts on already-paused ads.

If a kill/history tracker exists, read it before PAUSE or revival. Never infer an old kill reason. A revival needs: original recorded reason, evidence that the condition changed, retest structure/budget, and re-kill trigger.

### 4. Extract creative and funnel signals

Produce:

- Proven: above target at sufficient spend/N, plus why the message matched awareness/sophistication when evidence exists;
- Partial signal: ITERATE candidates and exactly one change;
- Not working: PAUSE candidates and one-clause evidence;
- Feeder/Converter/Star/Saturated table;
- TOF/MOF/BOF live distribution from the maintained classification;
- performance by SKU, format, angle, and persona, with `[UNK]` preserved.

Do not claim causality from aggregated dimensions. These are signals for the creative strategist.

### 5. Identify coverage gaps

Rank under-tested SKU × Format × Angle × Persona combinations High/Medium/Low. Ground each priority in this run: thin coverage around a proven family, single-creator concentration, a fatigue refresh need, or a missing funnel stage. Do not recommend filling every matrix cell.

### 6. Run periodic audience review

Daily runs may note local CPMR/frequency warnings. Every two weeks or monthly, compare audience demographics and 30/90/180-day CPMR, frequency, and CPM trends. Rising CPMR + frequency with flat CPM is a leading saturation indicator; ROAS is lagging.

### 7. Build budget and structure plan

For each campaign show current cap, configured budget level, utilisation, rolling windows and N, productive/weak inventory, recommended cap, staged instructions, and ad-set actions. Audit proven creatives in unsuitable structures without assuming one structure is universally best.

### 8. Data flags

List missing fields, low denominators, naming failures, attribution changes, tracking drift, external events, partial segment coverage, and any verdict likely to flip with more data.

### 9. Write the contract

Write `analysis/YYMMDD-analysis.md` using `templates/analysis.md`. Fill every relevant section; use `[NO DATA]`, `[NEEDS INPUT]`, or `[NOT APPLICABLE]` rather than deleting sections.

### 10. Present the decision checkpoint

In interactive work, show a summary under roughly 40 lines:

- headline KPIs including both ROAS figures;
- verdict counts and every PAUSE/SCALE name with reason;
- audience split and coverage;
- current → recommended budget by campaign;
- data flags;
- a direct 1–2 sentence account read.

Ask whether the operator wants adjustments or external execution. Do not publish, upload, pause, or change budgets before approval.

## Output contract

The analysis must contain every active-ad verdict with evidence, an exact action where applicable, and WAIT check-back conditions. Machine-readable output is optional, but if created should contain:

```json
{
  "generated": "YYYY-MM-DD",
  "period": {"start": "YYYY-MM-DD", "end": "YYYY-MM-DD"},
  "take": "Direct account read.",
  "verdicts": [{"ad": "Exact ad name", "verdict": "WAIT", "reason": "Evidence", "action": null, "check_back": "At 1.5x AOV spend"}],
  "actions": [{"urgency": 1, "type": "pause", "entity": "Exact name", "instruction": "Exact Ads Manager click"}],
  "budget_plan": [{"campaign": "Exact name", "budget_level": "campaign", "current_cap": 0, "recommended_cap": 0, "plan": "HOLD because ..."}],
  "data_flags": []
}
```

Validate any machine-readable artifact before it is consumed. Keep the dated analysis as the auditable reasoning record.

## Boundaries

This skill does not:

- invent creative strategy, angles, personas, or scripts;
- treat low-N ROAS as proof;
- use windowed decline alone to kill an aged ad;
- confuse pacing with configured budget;
- recommend nonexistent per-ad automated-campaign budgets;
- infer funnel stage or old kill reasons;
- mutate Meta, publish reports, deploy dashboards, commit, or push without explicit authorization.
