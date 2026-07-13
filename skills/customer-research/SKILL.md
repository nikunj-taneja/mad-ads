---
name: customer-research
description: Ingest customer evidence into a traceable registry, mine repeated signals into evidence-backed persona proposals, and preserve customer language without inventing demographics or strategy.
---

# Customer research

Turn calls, reviews, surveys, support messages, interviews, and operator notes into a structured evidence base. Then mine that base for targeting-grade customer clusters. This skill has two explicit modes and never edits `variables/` without approval.

## Boundaries

Use this skill to log customer evidence, backfill structured records, sharpen personas, or test whether an existing persona still fits. Do not use it to write ads, briefs, or media-buying verdicts. It may recommend existing angles and formats but must not invent new taxonomy entries.

## Inputs

Always read:

- `templates/customer-research.md`
- `variables/personas.md`
- `variables/angles.md`
- `variables/formats.md`
- `templates/products.md`
- every customer source the operator supplies under `data/` or by exact path

If a private registry does not exist, ask the operator to create or authorize one under `data/customer-profiles.md`. `data/` is gitignored. Never place real customer PII in a tracked example.

## Evidence discipline

- Every fact needs a source ID and date. Preserve exact quotes with quotation marks.
- Omit unknown fields. Do not write `unknown`, empty strings, or plausible guesses.
- Mark genuine inference as `(inferred from <evidence>)`; never turn inference into fact.
- Minimize PII. Prefer a stable anonymous customer ID over a name, email, phone number, or address.
- Reconcile conflicting evidence by retaining both claims with their sources. Do not average them.
- One vivid quote is a signal, not a segment. State sample size, source mix, recency, and selection bias.
- Demographics may only be recorded when explicitly supplied and relevant. Never infer age, income, gender, location, or identity from vocabulary or purchase behavior.

## Mode 1: ingest

Use when the operator supplies information about one or more customers.

### 1. Find or create the record

Search by stable customer ID, order ID, interview ID, and only then by name if names are present. Merge into an existing record rather than creating duplicates. Never overwrite a confirmed field silently.

### 2. Normalize the evidence

Use this schema. Include only fields supported by the source:

```yaml
---
customer_id: <anonymous stable ID>
source_id: <call/review/survey/support/order identifier>
source_date: <YYYY-MM-DD>
source_type: <call|review|survey|support|interview|operator-note|other>
purchase_context: <what happened before purchase>
products_purchased: [<customer-facing product name>]
prior_alternatives: [<product, brand, workaround, or status quo explicitly mentioned>]
discovery_channel: <explicit source>
situation: <observable context or job-to-be-done>
desired_outcomes: [<outcome in customer language>]
objections: [<objection in customer language>]
decision_triggers: [<event or proof that changed the decision>]
product_reaction: <positive and negative reaction>
repeat_intent: <explicit signal and wording>
price_signal: <exact or closely paraphrased evidence>
content_diet: [<explicit channels, creators, communities, or publications>]
comparators: [<explicit alternatives used as a benchmark>]
persona_match: <existing persona code or no-clean-match>
---
```

After the YAML, add 2–4 sentences capturing the language and context that the schema loses. Include the strongest exact quote and its source ID. Do not copy sensitive details that do not improve marketing understanding.

### 3. Reconcile and append

Record contradictions as separate sourced observations. Keep records ordered by `customer_id`. If importing a table, report rows read, records created, records updated, records skipped, and the reason for every skip.

### 4. Flag persona signal

If the record does not cleanly map to an existing persona, tell the operator. Offer mine mode; do not run it automatically.

### Ingest output

Report the registry path, records changed, fields omitted for lack of evidence, conflicts retained, and whether a persona gap appeared.

## Mode 2: mine

Use for persona refreshes, segmentation, corpus mining, or evaluation of a named persona.

### 1. Audit the corpus

Load all authorized customer sources. Backfill usable rows into the registry first if the operator has authorized writes. Record source counts, date range, missing fields, likely sampling bias, and duplicate handling.

### 2. Cluster on behavior and motivation

Use axes that actually occur in the evidence, such as:

- situation or job-to-be-done;
- prior alternative and comparator;
- desired outcome and emotional payoff;
- objection and perceived risk;
- decision trigger and proof needed;
- discovery channel and content diet;
- price sensitivity and willingness-to-pay signals;
- usage occasion and repeat behavior.

A working cluster requires at least three independent customer records sharing at least three meaningful axes. Below that threshold, label it `emerging signal`, not a persona. Do not force every record into a cluster.

### 3. Compare clusters with existing personas

- `CLEAN MATCH`: sharpen the existing persona with evidence-backed signals without changing its core motivation.
- `PARTIAL MATCH`: propose a split only when two groups have materially different situations, objections, or conversion triggers.
- `NO MATCH`: propose a new persona only when the cluster threshold is met.
- `CONTRADICTED`: document evidence that weakens or invalidates the current persona definition.

### 4. Build a creative and activation spec

Each proposed persona delta must contain:

**Creative spec**

- core situation and desired progress;
- incentive vector in one sentence;
- primary emotional trigger;
- language customers actually use;
- proof that unlocks belief;
- messages that create resistance;
- counter-evidence and unresolved uncertainty.

**Activation spec**

- observable acquisition signals supported by evidence;
- discovery channels and content diet;
- comparator and category affinities;
- relevant geography or demographics only when explicit and sufficiently represented;
- fields with no evidence written as `[NEEDS INPUT: <field>]`.

Do not claim that an interest or demographic field can directly target a platform audience without checking current platform capabilities.

### 5. Pair existing angles and formats

Recommend 2–3 entries from `variables/angles.md` and `variables/formats.md` only when their mechanism fits the cluster. Cite the evidence and explain why. If no entry fits, report a taxonomy gap and ask the operator whether they want a separate proposal.

### 6. Write the proposal

Save `creative-strategy/persona-update-YYMMDD.md`:

```markdown
# Persona update: YYYY-MM-DD

## Corpus audit
- Sources, sample size, date range, duplicates, and backfills
- Source bias and material missing evidence

## Summary
- Counts of sharpens, splits, new proposals, contradictions, and emerging signals

## Proposed persona deltas

### [SHARPEN|SPLIT|NEW|CONTRADICTED] CODE: descriptive name
**Evidence base:** customer/source IDs and count
**Current definition:** exact relevant text from `variables/personas.md`
**Proposed delta:** exact replacement or addition
**Creative spec:** situation, progress, trigger, language, proof, resistance
**Activation spec:** evidence-backed observable signals
**Angle and format pairings:** existing codes with rationale
**Counter-evidence:** what does not fit
**Confidence:** high, medium, or low, with reason

## Emerging signals
Signals below the clustering threshold.

## Unclustered evidence
Records intentionally left outside a persona.

## Decisions required
Exact approvals or missing inputs needed from the operator.
```

### 7. Stop at the approval gate

Never edit `variables/personas.md`, `variables/angles.md`, or `variables/formats.md`. Give the proposal path and exact changes awaiting approval.

## Quality check

Before finishing, verify that every claim traces to a source, exact quotes are unchanged, sample sizes are visible, counter-evidence is included, PII is minimized, and no persona is based on fewer than three independent records without an `emerging signal` label.
