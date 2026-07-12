# Marketing operations field notes

Transferable lessons for agents working in this repository. These are defaults, not universal facts. Validate them against the operator's account, attribution, economics, and production constraints.

## Evidence and measurement

- Use the same complete date window across ad-platform and commerce data. Exclude an incomplete current day unless the task is explicitly intraday.
- Record attribution settings and data freshness. Recent platform data can change as conversions arrive.
- Treat low-purchase ROAS as noisy. Before judging a creative, inspect lifetime history, absolute conversions, spend maturity, and recent trajectory.
- Never attribute an account-wide basket-size change to one creative when order data has no ad-level join.
- Separate platform-attributed return from blended revenue divided by spend. Define both before using either.
- Funnel stages need stage-appropriate metrics. A prospecting ad and a retargeting offer should not be judged by one undifferentiated threshold.
- Sanity-check new parser metrics against the source UI. For rates and averages, document weighting rather than taking a convenient maximum.
- A configured budget or bid cap is not the same as realized daily spend. Show both and compute utilization before recommending a change.
- Compare short and long windows as a trajectory. Seasonality and attribution lag can make one rolling average misleading.
- Keep contribution-margin definitions explicit. Never mix two CM1/CM2/CM3 conventions in one analysis.

## Decision records

- Every pause recommendation needs a numeric reason and a condition that would justify revival.
- Media recommendations should name the exact entity, lever, target value, and evidence. Avoid vague instructions such as “optimize spend.”
- Preserve the analysis document as the canonical record. Generated dashboards must agree with it.
- Store unusual investigation exports under descriptive filenames so they cannot overwrite scheduled inputs.
- Use actual creation dates in asset filenames. Do not backdate work to fit a campaign narrative.

## Creative strategy

- One ad should have one dominant persona and one dominant proposition. Split competing ideas into separate tests.
- Treat the funnel role as a judgment based on the ad's hypothesis and body, not as a mechanical consequence of format or audience label.
- Measure creative coverage across persona, angle, and format, but do not confuse a competitor swipe library with a representative coverage sample.
- Ground iterations in a named source asset and state what is retained, what changes, and why.
- A problem-aware prospecting static often benefits from opening on the customer's situation before product specifications or promotion. Treat this as a hypothesis to test.
- Founder credentials can follow the hook. The first frame still needs immediate relevance.
- Do not create a persona from a single anecdote. Keep weak clusters on a watch list until repeated evidence appears.
- Market sophistication belongs to a claim territory, not automatically to a geography or broad category. Track it as evidence changes.

## Copy and production

- Build a script skeleton before polishing a long script when strategic approval is still pending.
- Interleave visual or b-roll directions with spoken copy so editors understand the intended evidence and pacing.
- Static concepts need explicit photo or visual direction. Carry it from brief to script without quietly reinventing it.
- Put required headline text in the final image prompt when the generation workflow expects a finished ad. If exact rendering is unreliable, specify a compositing step.
- Use exact product reference images instead of redescribing packaging from memory.
- Never present an actor as a real customer or partnership creator without permission and accurate disclosure.
- Savings claims must use the real compare-at price and exact arithmetic. Do not round savings upward.
- Keep customer-facing language natural. Internal taxonomy labels do not automatically belong in ad copy.

## Tools and reliability

- Render and inspect a live web page before claiming what a visitor can see. Raw HTML can contain hidden or stale elements.
- Commit or otherwise durably checkpoint expensive generated outputs as soon as they land. Check status before clearing temporary directories.
- Decouple expensive media transcription, frame extraction, and model interpretation so partial results can resume.
- Use separate credentials and access paths for owned-account operations and public competitor research. Do not assume one token or API covers both.
- Default external mutations to dry-run or paused state. Require an operator's explicit authorization before spend, upload, deployment, or theme changes.
- Keep source data, calculation logic, and generated presentation separate. A dashboard is replaceable; the evidence and analysis contract are not.

## Memory hygiene

- Save durable, project-wide corrections in `.memory/project/` and link them from `.memory/MEMORY.md`.
- Mark superseded guidance instead of blending old and new rules.
- Keep brand-specific prices, claims, names, and thresholds in templates or variables, not in reusable skills or field notes.
