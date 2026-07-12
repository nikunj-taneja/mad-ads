# Repository skills

Each skill has one canonical file at `skills/<name>/SKILL.md`. Relative discovery links expose this folder to both supported harnesses:

- `.claude/skills -> ../skills`
- `.agents/skills -> ../skills`

If symlinks are unavailable, tell the agent to read the relevant `SKILL.md` explicitly or create per-skill links supported by the local harness. Do not copy these skills into a home directory because project rules should travel with the repository.

Skills contain judgment workflows. Recurring parsing, validation, rendering, and API behavior belongs in `tools/` and must be registered in `tools/REGISTRY.md`.
