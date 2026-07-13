# Mad Ads

An open, fill-in-the-blanks marketing operating system for D2C founders and agencies working with coding agents.

Mad Ads gives Claude Code and Codex a shared workspace for performance analysis, customer research, creative strategy, and ad copy. It is designed for technical D2C operators who want repeatable marketing work instead of disconnected chat threads, while keeping creative production in human hands.

The repository starts intentionally empty of brand and customer information. Your agent will tell you which file to complete, what export to add, or which decision needs human approval.

## What you get

- one canonical set of project instructions for Claude Code and Codex;
- repo-local skills that travel with the project;
- fill-in templates for products, offers, voice, customers, and KPIs;
- a file-based creative pipeline with clear handoffs;
- starter tools for validating Meta exports and script duration;
- safe defaults that keep exports, credentials, and customer data out of git.

The default path is deliberately short: fill in brand truth, add performance data, produce briefs and scripts, then hand approved work to production. Optional research and integrations can be added without making the basic workflow harder to start.

## Quick start

Requirements: Git, Python 3.11+, and either Claude Code or Codex.

```sh
git clone <your-fork-url> mad-ads
cd mad-ads
cp .env.example .env
python3 tools/run-tests.py
```

Then open the repository in Claude Code (the default) and say:

> Onboard this brand. Read CLAUDE.md, inspect the fill-in templates, and ask me only for the inputs required to complete the first useful workflow.

Codex reads `AGENTS.md`, which points to the same canonical instructions.

Start by filling:

1. `templates/brand.md`
2. `templates/products.md`
3. `templates/offers.md`
4. `templates/brand-voice.md`
5. `variables/kpis.md`

Detailed credential and integration setup lives in `docs/setup.md`. Credentials are unnecessary for onboarding, file-based analysis, briefing, or copy.

For performance analysis, place a Meta CSV export in `data/` and invoke the `media-buyer` skill. The export remains untracked. Run `python tools/doctor.py` at any time to see what is ready, missing, or optional.

## Workflow

```text
Meta export                         customer calls / reviews
    |                                       |
media-buyer                         customer-research
    |                                       |
analysis/<date>-analysis.md       persona proposal
    |                                       |
    +-------------- creative-strategist ----+
                           |
                    ads/briefed/*.md
                           |
                       copywriter
                           |
                    ads/scripted/*.md
                           |
          human design, filming, editing + launch
```

Each stage writes a file. This makes work inspectable, resumable, and portable between agent harnesses.

## Repository layout

| Path | Purpose |
|---|---|
| `skills/` | Agent workflows, stored in the project |
| `templates/` | Brand facts and handoff contracts |
| `variables/` | Personas, angles, formats, and KPI targets |
| `data/` | Private exports and research, ignored by git |
| `analysis/` | Performance analysis contracts |
| `creative-strategy/` | Ranked concept queues and proposals |
| `ads/` | Brief and script lifecycle |
| `tools/` | Reusable deterministic utilities |
| `.memory/` | Project rules and durable decisions |

## Using project skills

Skills live in `skills/<skill-name>/SKILL.md`. `.claude/skills` is a relative symlink, so Claude Code can load the same files without duplicating them. Codex reads the repo instructions and local skill folder. You can also invoke a workflow explicitly:

> Read `skills/creative-strategist/SKILL.md` and create briefs from the latest analysis.

Included skills:

- `media-buyer`: analyze paid-social exports and issue evidence-based verdicts;
- `customer-research`: structure reviews, calls, and support messages into persona proposals;
- `creative-strategist`: turn evidence and coverage gaps into ranked briefs;
- `copywriter`: write direct-response copy through Schwartz awareness and sophistication, LF8 desire mapping, Sugarman sentence mechanics, proof, hooks, and format-specific contracts;

Production skills are intentionally excluded. The copywriter supplies inline visual direction and asset requirements; human designers, creators, editors, and creative directors decide how the work is produced.

Customer research and external inspiration are optional inputs. The core workflow does not assume you already have a swipe library.

These are full operating skills, not short persona prompts. The strategy and copy layers include the diagnostic frameworks, decision gates, evidence rules, and downstream contracts needed to produce consistent work. See `docs/framework-map.md` for what is implemented where.

## Books and frameworks behind the skills

The system translates several established direct-response frameworks into agent-operable checklists and handoff contracts:

| Source | Used in | What it contributes |
|---|---|---|
| Eugene M. Schwartz, *Breakthrough Advertising* | `creative-strategist`, `copywriter` | Awareness stages, market sophistication, mass desire, headline verbalization, belief building, mechanism, identification, and copy intensification |
| Joseph Sugarman, *The Adweek Copywriting Handbook* | `copywriter` | Slippery-slide sentence mechanics, fifteen operating axioms, psychological triggers, curiosity, specificity, objection handling, satisfaction conviction, editing, and direct-response doctrine |
| Drew Eric Whitman, *Cashvertising* | `creative-strategist`, `copywriter` | Life-Force 8 desire mapping, means-end chains, Mental Movie, Four Walls, fear-appeal sequencing, inoculation, and learned-want laddering |

The media-buyer and customer-research skills also contain original operating methods developed from practical campaign analysis and research discipline.

Mad Ads is an independent implementation and is not affiliated with or endorsed by these authors or publishers. It summarizes and operationalizes ideas; it does not include the books themselves.

## Privacy and publishing

`data/`, `.env`, generated media, and local memory are ignored. Before publishing a fork, run:

```sh
python tools/privacy-scan.py .
```

Add your brand names, domains, client names, and known identifiers to `.privacy-patterns.example`, copy it to `.privacy-patterns`, then scan again. Secret scanning in your Git host is still recommended.

## What this project will not do silently

Agents may prepare recommendations, drafts, files, and dry runs. They must request explicit approval before changing live budgets, creating ads, publishing assets, deploying pages, or modifying a store. New Meta ads should be created paused unless the operator deliberately overrides that safeguard.

## Adapting the system

Keep brand truth in templates, controlled taxonomies in variables, judgment workflows in skills, and deterministic transformations in tools. When an integration is missing, ask the agent to inspect the API or export shape and patch the smallest useful tool. Record it in `tools/REGISTRY.md`.

## License

MIT. See `LICENSE`.
