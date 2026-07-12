# Setup and environment guide

Mad Ads works locally without API credentials. Most tools inspect local files. The optional Meta auditor makes read-only requests, and the narrow uploader can create a paused link ad only after two explicit confirmation flags.

## Clean-clone setup

Requirements:

- Git;
- Python 3.11 or newer;
- Claude Code (the default) or Codex.

From a new clone:

```sh
git clone <repository-url> mad-ads
cd mad-ads
cp .env.example .env
python3 --version
python3 tools/privacy-scan.py .
python3 tools/run-tests.py
```

There are currently no third-party Python packages to install. `pyproject.toml` records the Python version and project metadata; the starter utilities use the standard library.

Confirm the repo-local skills are exposed to both supported agents:

```sh
test "$(readlink .claude/skills)" = ../skills
test "$(readlink .agents/skills)" = ../skills
```

Open the repository in Claude Code and ask:

> Read CLAUDE.md and onboard this workspace. Tell me the smallest set of template fields needed for my first workflow; do not invent missing facts.

Codex reads `AGENTS.md`, which points to the same canonical instructions. If a client does not discover a skill automatically, explicitly ask it to read `skills/<skill-name>/SKILL.md`.

## Safe local smoke test

No secrets, fixture, or network access is needed for the clean-clone test:

```sh
python3 tools/check-script-length/check.py templates/ad-brief.md
python3 tools/privacy-scan.py .
git status --short
```

To exercise the CSV parser, export a CSV from Meta Ads Manager into `data/` and run:

```sh
python3 tools/parse-meta-csv/parse.py data/<export>.csv
```

The parser requires an ad-name column and a spend column. It reports mappings; it does not upload or mutate anything.

Before using real data, confirm `git status --short` does not list the export or `.env`. If it does, stop and repair `.gitignore` before continuing.

## Environment variables

Copy `.env.example` to `.env`. Meta tools load it from the repository root, with exported shell variables taking precedence. Other integrations must document their behavior. Never paste token values into prompts, logs, Markdown, fixtures, or tracked configuration.

| Variable | Needed now? | Source and format |
|---|---:|---|
| `META_ACCESS_TOKEN` | No | Meta access token created for the intended Business portfolio and app. Prefer a system-user token for controlled server-side automation. |
| `META_AD_ACCOUNT_ID` | No | Ads Manager/Business Settings account ID, formatted as `act_<digits>` for Graph API calls. |
| `META_API_VERSION` | No | Graph API version selected and tested by the integration implementer. Pin it rather than silently using a moving default. |
| `META_PAGE_ID` | No | Numeric Facebook Page ID authorized for the ad account and app. |
| `META_INSTAGRAM_ACTOR_ID` | No | Instagram professional-account actor ID connected to the Page, when Instagram identity is used. |
| `SHOPIFY_STORE_DOMAIN` | No | The store's `*.myshopify.com` hostname, without a scheme or path. |
| `SHOPIFY_ACCESS_TOKEN` | No | Admin API token from a custom app with only the scopes required by the implemented reader. |
| `HIGGSFIELD_API_KEY` | No | API credential from the provider when direct generation is implemented. Prompt-sheet generation needs none. |

Blank values are intentional. Do not collect credentials in advance “just in case.” Check `tools/REGISTRY.md` and `docs/tool-status.md` before assuming an integration exists.

## Meta setup prerequisites

The repository supports Meta CSV inspection, a read-only access audit, and one narrow upload path for a paused link ad using an image hash already in Meta. It does not create campaigns/ad sets, upload media, activate ads, or support catalog/video/carousel formats. Before enabling these tools, establish:

1. A Meta Business portfolio with access to the target ad account.
2. A Meta developer app connected to that business and an appropriate Marketing API use case.
3. A system user or other token strategy suitable for the operating context, with the minimum permissions the tool actually uses. Common Marketing API work may require `ads_read` for reporting and `ads_management` for mutations; Page/Instagram creative operations can require additional asset permissions and assignments. Verify current requirements in Meta's official documentation when implementing because permissions and review rules change.
4. Explicit asset assignments for the ad account, Facebook Page, Instagram professional account, pixel/dataset, and catalog if the workflow uses them.
5. An approved app mode/review path for any use beyond assets owned by the app's business.
6. A pinned Graph API version and a recorded upgrade owner/date.
7. A human authorization model: which account may be changed, who approves budgets and creative, and what must remain read-only.

Safe implementation defaults:

- begin with an identity/access probe and read-only reporting;
- print the target business, account, Page, and actor before any mutation;
- support `--dry-run` and make it the default;
- create campaigns, ad sets, and ads paused unless the operator explicitly requests otherwise;
- require an explicit account ID on every mutation instead of choosing the first accessible account;
- make retries idempotent and record returned object IDs;
- never log tokens or full customer payloads;
- add the tool and its verified status to `tools/REGISTRY.md`.

An agent should ask the human for values by variable name and direct them to place the values in `.env`; it should not ask the human to paste secrets into chat.

## Credential validation sequence

When a live integration is added, validate it in this order:

1. Confirm all required variables are present without printing their values.
2. Call the provider's identity or token-debug endpoint.
3. List or fetch only the explicitly configured account and assets.
4. Run a read-only request with a narrow date range.
5. Run the tool's dry-run mode and inspect the proposed payload.
6. If a write is authorized, create a paused test object with an unmistakable test name.
7. Record how to remove/archive the test object and verify the result in the provider UI.

Do not treat a successful token check as authorization to spend money or publish creative.

## Troubleshooting

### A CSV column is reported missing

Run the parser and inspect its `columns` and `mapping` output. Meta export labels vary by locale and report preset. Re-export in English with ad name and amount spent, or ask an agent to add the exact header alias to `tools/parse-meta-csv/parse.py` and test it against a redacted fixture.

### A skill is not discovered

Check the symlinks with the two `readlink` commands above. On systems that checked out symlinks as plain text, recreate `.claude/skills` and `.agents/skills` as relative symlinks to `../skills`, or tell the agent to read the relevant `SKILL.md` directly.

### `.env` values are invisible to a tool

Run Meta tools inside the repository so they can find the root `.env`. Exported shell values override file values. Future integrations must document their own loading behavior.

### Meta returns an OAuth or permissions error

Check token expiry, app mode, asset assignment, requested permission, business ownership, and whether the token belongs to the expected system user/app. Test against the configured account rather than a broad account listing. Consult current official Meta documentation; do not weaken permissions or switch accounts until the mismatch is understood.

### Meta returns an invalid object or actor error

Confirm IDs belong to the same authorized business context and that the Page, Instagram professional account, pixel/dataset, or catalog is assigned to both the acting user and ad account as required. Numeric IDs are not interchangeable.

### A tool is missing or marked partial

That is expected for some integrations. Read `docs/tool-status.md`, then ask the agent to implement the smallest safe capability using a redacted fixture or official API contract. Require a dry run, loud failures, usage help, and a registry update before trusting it with live credentials.

## Before publishing a fork

Run the privacy scan, inspect Git's staged and tracked files, and use your Git host's secret scanner. Add brand names, domains, client names, email addresses, account IDs, and other identifiers to `.privacy-patterns` before scanning. Deleting a secret in a later commit does not remove it from Git history; rotate exposed credentials and clean history before publishing.
