# Workflow guide

The default path is deliberately simple. It begins with files the operator can export today and adds live integrations only when they create clear value.

```text
Meta CSV + brand files -> media-buyer -> analysis -> creative-strategist
    -> brief -> sugarman -> script -> static-producer or video-producer
    -> prompt sheet -> human review -> launch
```

Customer research can feed persona proposals into creative strategy at any point. A competitor swipe file is optional, not an onboarding prerequisite.

## 1. Brand onboarding

Ask the agent to read `CLAUDE.md` and identify only the fields required for the next useful output. Brand facts belong in `templates/`; controlled personas, angles, formats, and KPIs belong in `variables/`. Missing facts should remain visibly marked rather than fabricated.

Minimum files for most work:

- `templates/brand.md`;
- `templates/products.md`;
- `templates/offers.md`;
- `templates/brand-voice.md`;
- `variables/kpis.md`.

## 2. Performance analysis

Export an ad-level CSV from Meta Ads Manager into `data/`. Include at least ad name and amount spent; purchases and purchase value make the analysis more useful. Validate it locally:

```sh
python3 tools/parse-meta-csv/parse.py data/<export>.csv
```

Then ask the agent to use `skills/media-buyer/SKILL.md`. The current workflow is file-based: live Meta reads are not shipped.

## 3. Customer research

Put redacted reviews, interview notes, survey responses, or support themes in `data/`, then invoke `skills/customer-research/SKILL.md`. Customer quotes should retain a source pointer. The skill proposes changes; a human approves edits to shared `variables/` files.

## 4. Strategy and copy

Use `skills/creative-strategist/SKILL.md` to turn evidence and coverage gaps into briefs. Approved briefs move through `skills/sugarman/SKILL.md`. Estimate a drafted script's duration with:

```sh
python3 tools/check-script-length/check.py ads/scripted/<script>.md
```

Adjust `--wpm` only when the intended creator's speaking rate is known.

## 5. Production handoff

Use `skills/static-producer/SKILL.md` or `skills/video-producer/SKILL.md` to create model-ready prompt sheets. The repository hands prompts to the operator; it does not call Higgsfield or another generation API. The human reviews claims, likeness rights, product accuracy, and platform suitability before generation or publication.

## 6. Launch and feedback

Launch remains human-controlled. The optional Meta uploader creates only a paused link ad from an image hash that already exists in Meta, and requires two explicit execution flags. Export the next reporting window back into `data/`, run performance analysis again, and let evidence update the following concept queue.

Any expansion of the uploader must preserve the prerequisites and validation sequence in `docs/setup.md`, default dry-run behavior, paused creation, explicit account targeting, and registry/status documentation.

## Choosing the first workflow

- Have an ad export? Start with performance analysis.
- Have customer language but little spend data? Start with customer research.
- Have approved evidence and need ads? Start with strategy and copy.
- Have a finished script? Start with production prompting.

The system does not require every input lane to exist. Start with the strongest available evidence, preserve its source, and leave unsupported fields for the operator to fill.
