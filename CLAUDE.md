# Mad Ads agent instructions

This is an agent-operated marketing workspace for a D2C brand or agency. Claude Code is the default harness. Codex follows the same rules through `AGENTS.md`.

## Start every task here

1. Read `.memory/MEMORY.md`.
2. Read the relevant files in `templates/` and `variables/`.
3. Check `tools/REGISTRY.md` before writing a recurring data transformation.
4. State missing inputs. Ask the operator to fill a file when the repository does not contain the facts.

Never invent product claims, customer quotes, prices, performance data, or brand facts. Write `[NEEDS INPUT: description]` when evidence is missing.

## Operating rules

- Define the requested outcome and verify it before reporting completion.
- Read callers and contracts before modifying code.
- Prefer the smallest working change. Partial tools are allowed, but label limitations visibly.
- Preserve unrelated work and generated artifacts.
- Keep credentials in `.env`, never in tracked files.
- Use scripts for deterministic work and model judgment for interpretation, strategy, and writing.
- Put reusable project skills in `skills/<name>/SKILL.md`. Do not install project skills into a user's home directory.
- Outputs move through files. Do not silently change an upstream contract while producing a downstream artifact.

## Human handoffs

Agents may ask the operator to:

- export Meta Ads data into `data/`;
- complete a fill-in template;
- authorize an API action;
- provide product imagery or customer research;
- review claims, budgets, and creative before publication.

Give the exact path and expected columns or format.

## Source-of-truth folders

- `templates/`: brand facts and blank handoff contracts
- `variables/`: controlled marketing taxonomy and targets
- `data/`: private local inputs, gitignored
- `analysis/`: media analysis outputs
- `creative-strategy/`: concept queues and research updates
- `ads/`: lifecycle folders for briefs and scripts
- `prompts/`: production prompt sheets
- `skills/`: reusable agent workflows
- `tools/`: deterministic utilities
- `.memory/`: durable project rules and decisions

## Workflow

`data export -> media-buyer -> analysis -> creative-strategist -> brief -> copywriter -> script -> static-producer/video-producer -> prompt sheet -> human review -> launch`

Customer research can update persona proposals at any time. An agent must request approval before changing `variables/` because those files affect every downstream task.

Competitor research and swipe files are optional. Never block the core workflow because they do not exist. When external references are used, record their source and licensing or usage constraints.

## Skill loading

Claude Code discovers the repository skills through `.claude/skills`, a relative symlink to `../skills`. Codex can discover `skills/` directly from this repository and is also instructed by `AGENTS.md`. If a harness does not auto-discover them, ask it to read the relevant `skills/<name>/SKILL.md` explicitly.

## Writing

Write plainly. Avoid fabricated certainty and generic marketing filler. Match `templates/brand-voice.md`. Claims must trace to a repository file or operator-provided source.
