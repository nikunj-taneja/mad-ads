---
name: static-producer
description: Reverse-engineer a reference static or execute an approved brief, write evidence-safe copy when authorized, and produce a final model-ready image-generation and compositing handoff.
---

# Static producer

Translate an approved static brief, copy block, or useful reference image into a production-ready visual handoff. The job has two layers: identify what makes the visual work, then reproduce its transferable architecture without copying protected brand assets or inventing product facts.

## Inputs

Required:

- approved brief or copy block, or an operator-provided reference image;
- `templates/brand-voice.md`, `templates/visual-identity.md`, and `templates/products.md`;
- `variables/personas.md`, `variables/angles.md`, and `variables/market-sophistication.md`;
- product reference image and verified claims for the chosen product.

Optional: existing script, offer file, placement requirements, legal copy, prior winning creative, and current documentation for the selected generation model.

If the target model is unspecified, recommend one based on the scene and label exact syntax as model-dependent. Current model behavior and platform limits must be verified from current official documentation when they matter.

## Mode A: reference adaptation

### 1. Analyze the reference

Produce every field:

```markdown
## Reference analysis: <filename>

**Brand/category:** known or unknown
**Likely objective:** hypothesis, clearly labeled

**Visual architecture**
- Layout, focal point, text zones, negative space, and reading order
- Palette, contrast, saturation, texture, and depth
- Typography class, weight, hierarchy, and copy density
- Product treatment, scale, angle, crop, and context
- Lighting, mood, camera/lens feel, and realism level

**Copy architecture**
- Exact readable headline, supporting copy, badges, CTA, and placement
- Claim type and sophistication stage

**Why it may work**
- Scroll-stop mechanism
- Persuasion structure
- Emotional register
- Active copy or persuasion principles, with how each manifests

**Placement safety**
- Aspect ratio, edge risk, UI-overlay risk, and cropping risk

**Adaptability**
- Transferable structure
- Brand-equity or category-dependent elements
- Copyright/trade-dress risk
- Low, medium, or high adaptation risk with reason
```

Distinguish observation from hypothesis. Analyze structure, not just surface style. Never assume the reference performs well merely because it exists. If performance evidence was supplied, cite it.

### 2. Propose 1–3 directions

For each direction name the product, persona, angle, sophistication treatment, borrowed architecture, material changes, and any existing script match. Do not copy logos, mascots, proprietary characters, distinctive packaging, or near-verbatim competitor copy. Ask the operator to choose when the options materially differ.

## Mode B: approved-brief execution

Extract the single message, target persona, angle, proof, exact approved copy, product, offer, placement, and legal constraints. If these conflict, stop and surface the conflict instead of blending them.

## Copy block

Only write or adapt copy when the operator or source brief authorizes it. Otherwise preserve approved copy verbatim.

Default static limits:

```markdown
**Headline:** maximum 8 words
**Support:** optional, maximum 12 words
**CTA:** short action phrase
**Legal/disclaimer:** exact supplied text
```

Rules:

- Match copy volume to the visual architecture.
- Prefer concrete proof and specific nouns over unsupported adjectives.
- Sell the desired outcome or idea, not a list of features.
- Use vocabulary documented in customer evidence and brand voice.
- Check `variables/market-sophistication.md`; escalate an exhausted bare claim through mechanism, proof, or identification.
- Never invent numbers, product performance, guarantees, scarcity, reviews, awards, ingredients, or comparisons.
- Use customer-facing product names, never internal codes.

## Prompt engineering

Select the mode appropriate to the image: clean product hero, lifestyle product scene, person with product, conceptual/CGI product, direct restyle, or complex composition. Record the selected platform, model, and mode rather than assuming a vendor.

The prompt must specify:

1. subject and exact reference binding;
2. composition, aspect ratio, focal hierarchy, and safe-zone placement;
3. environment, surface, depth, and background;
4. lighting direction, quality, contrast, and color palette;
5. camera position, crop, perspective, and lens feel;
6. product placement, scale, angle, contact shadow, and reflections;
7. people, hands, wardrobe, pose, and identity authorization if present;
8. exact text only if the model is expected to render it;
9. negative constraints and known failure modes.

Use concrete visual language. Avoid vague requests such as “premium” without describing the visual evidence of that quality. For a product reference, do not redescribe packaging geometry that the reference already controls. State what to preserve: label spelling, logo, cap, color, proportions, variant, and material.

### Text strategy

Choose explicitly:

- `IN-MODEL TEXT`: include exact text, font class, weight, color, alignment, and position. Use only when the selected model is sufficiently reliable and every output will receive spelling review.
- `COMPOSITING HANDOFF`: generate clean negative space and provide a separate exact typography specification. Prefer this for long copy, legal text, exact brand typography, or models with unreliable text rendering.

Never leave text ownership ambiguous.

## Placement safe zones

Platform UI and cropping rules change. Check current official placement documentation before using exact percentages. Until confirmed:

- keep the product and headline comfortably within the central 60–70% of the frame;
- keep critical content away from the outer 5% for feed assets;
- for vertical story/reel assets, reserve generous top and bottom UI zones and avoid the lower third for critical elements;
- if a disclaimer is required, allocate a deliberate high-contrast legal area and verify minimum readable size after export;
- produce separate crops when one composition cannot survive every placement.

## Output contract

Save `prompts/<source-name>-static.md`:

```markdown
# Static production sheet: <name>

## Inputs
- Brief/copy/reference paths
- Product reference path and binding
- Verified fact and claim sources

## Production target
- Platform, model, mode, aspect ratio, placement, and export size

## Reference analysis
<required in reference-adaptation mode>

## Direction
- Persona, angle, message, proof, sophistication treatment

## Exact copy
- Headline, support, CTA, and legal text

## Final prompt
<single paste-ready prompt>

## Negative constraints
<packaging, anatomy, text, lighting, crop, duplication, and artifact constraints>

## Reference bindings
<what each image controls and what it must not control>

## Compositing handoff
<exact typography and placement, or explicitly not required>

## Human review checklist
- Product geometry, variant, label spelling, logo, and color
- Copy spelling, claims, price, offer, CTA, and disclaimer
- Anatomy and product interaction
- Safe-zone and crop survival
- Brand fit, reference distance, and rights risk
- Export dimensions, color profile, and compression
```

Do not generate, upload, or publish externally unless the operator asks. A prompt sheet is not an approved ad. Human review remains mandatory for product accuracy, claims, rights, and rendered text.
