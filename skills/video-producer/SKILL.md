---
name: video-producer
description: Convert an approved ad script into independently generatable clips, model-ready structured prompts, identity and continuity controls, and a complete editing handoff without changing copy.
---

# Video producer

Turn a finished script into a production prompt sheet. Every generated detail must trace to the script, visual identity, product documentation, or an operator-approved production decision. Preserve approved dialogue verbatim.

## When to use

Use after a script is approved for AI-first talking head, UGC-style, product b-roll, demonstration, founder, or narrative production. Do not prompt from an unfinished brief. Do not synthesize a real creator, employee, customer, clinician, or founder without explicit authorization and an approved identity workflow. Recommend conventional filming when authentic identity, complex interaction, or legal credibility makes generation inappropriate.

## Inputs

- approved script and its brief;
- `templates/visual-identity.md`, `templates/brand-voice.md`, and `templates/products.md`;
- product images and authorized character/avatar references;
- target platform, placement, aspect ratio, duration, generation model, and editing constraints;
- current official documentation for the selected generation system when syntax or capability matters.

If information is missing, write `[NEEDS INPUT: ...]` and ask for the exact path or decision.

## Structured prompt formula

Use this order for every clip:

```text
[Model/mode when non-default] [Camera] [Subject] [Look] [Action]
```

- `Camera`: shot size, height, angle, stability, and one movement.
- `Subject`: specific authorized person, product, hands, or environment. Reference bindings control identity and packaging.
- `Look`: lighting direction and quality, palette, contrast, texture, realism, and mood.
- `Action`: one clear action beginning with an active verb.

Put VFX immediately after the action in square brackets. Put SFX/audio notes at the end in square brackets. Use the target model's tested prompt length; absent verified guidance, keep each prompt concise and under roughly 80 words.

Avoid passive action, multiple competing movements, unfilmable emotional abstractions, and packaging descriptions that conflict with the product reference.

## Script-to-clip process

### 1. Audit the script

Record spoken word count, estimated read time, target runtime, characters, products, locations, b-roll directions, on-screen text, legal copy, end card, and unsupported production details. Quote the source line for every clip.

### 2. Identify clip units

Each unit must be independently generatable and contain one emotional beat and one primary action:

- talking-head beat, cut at a natural sentence boundary;
- product or environment b-roll beat;
- demonstration or reaction beat;
- transition, reveal, or end-card handoff.

Split any direction containing multiple shots or sequential actions. Do not cram a calm explanation and a reveal into the same generation. Generate longer source clips only when the model requires it, then specify trim points.

### 3. Choose generation mode

Use the selected platform's equivalent of:

- `STANDARD`: new clip without a reference;
- `REFERENCE-BASED`: identity, product, pose, palette, or setting follows a supplied reference;
- `CONTINUATION`: motion and state continue from the preceding clip;
- `EXPAND`: widen an existing shot;
- `EDIT`: preserve the source frame and change one bounded element.

Use edit/inpainting when the background must remain stable. Reference-based generation commonly reconstructs the whole frame and may drift. Record which image controls identity, product, setting, pose, or color. A poor or cropped source image limits output quality.

### 4. Plan identity consistency

Any recurring generated person needs an approved identity-consistency method:

1. designate an anchor clip or approved identity reference;
2. label the anchor `IDENTITY: ANCHOR`;
3. label later clips `IDENTITY: USE ANCHOR`;
4. describe only changes in action, framing, wardrobe, or location;
5. keep immutable traits in a continuity ledger.

Identity tools do not substitute for consent. If consent or likeness rights are unclear, stop and flag the shot.

### 5. Write every clip prompt

For each clip specify:

- mode and generation duration, plus edit trim;
- exact dialogue or source line;
- camera, subject, look, and action;
- reference image bindings;
- identity status and continuity state entering/leaving the clip;
- wardrobe, props, product state, hand dominance, and screen direction when relevant;
- negative constraints and likely failure modes;
- audio, caption, transition, and edit notes.

Never invent a location, demographic trait, product behavior, costume, medical role, testimonial, or demonstration result. Ask for a production decision when the script is underspecified.

### 6. Build continuity and assembly notes

Track product variant, fill level, cap state, hand, wardrobe, hair, lighting direction, time of day, background objects, actor eyeline, camera side, and motion direction. Then specify clip order, trim points, dialogue sync, J/L cuts, transitions, b-roll coverage, captions, music/SFX, legal overlays, and end-card replacement.

## Talking-head planning

For direct-response UGC-style scripts, a useful default sequence is:

1. hook or pattern interrupt;
2. problem/situation;
3. discovery or product reveal;
4. mechanism, proof, or demonstration;
5. CTA and product handoff.

This is a production map, not permission to rewrite the script. Collapse or expand beats to match the approved copy.

## Static prompt appendix

If a script contains a static or thumbnail asset, include a short still-image concept handoff: selected image mode, aspect ratio, product reference, 40–70 word visual prompt, and compositing note. No camera-movement verbs. The script's visual direction remains the source of truth. Long or exact typography belongs in compositing unless the image model is verified for it.

## Output contract

Save `prompts/<script-name>-video.md`:

```markdown
# Video production sheet: <ad name>

**Source script:** <path>
**Primary platform/model:** <name or NEEDS INPUT>
**Aspect ratio/placement:** <value>
**Target runtime:** <seconds>
**Spoken words / estimated read:** <count / seconds>
**Total clips:** <count>

## Production risks
- Identity/consent, product interaction, unsupported detail, model ceiling, legal, or conventional-filming flags

## Reference images
1. @Image1: path, rights status, what it controls, what it must not control

## Continuity ledger
| Element | Immutable state | Authorized changes |
|---|---|---|

## Clip breakdown

### Clip 1: beat name
**Mode:** STANDARD / REFERENCE-BASED / CONTINUATION / EXPAND / EDIT
**Generation duration:** Xs, trim to Ys
**Identity:** ANCHOR / USE ANCHOR / N/A
**Continuity in/out:** exact state
**Source line:** exact quoted dialogue or visual direction
**Prompt:** concise structured prompt
**Negative constraints:** likely failure prevention
**Audio/captions/edit:** exact handoff

## Assembly note
Clip order, trims, transitions, dialogue and b-roll coverage, captions, audio, legal overlays, and end card.

## Human review checklist
- Dialogue unchanged and complete
- Product, packaging, claims, and demonstration accurate
- Identity consent and continuity verified
- Hands, lip sync, gaze, motion, and physics acceptable
- Captions, safe zones, legal copy, audio rights, and export correct
```

## Hard rules

1. Approved copy stays verbatim. Production may not “improve” it.
2. Every prompt element traces to an input or an explicitly approved production choice.
3. Recurring people require consent and identity continuity.
4. End cards, exact legal text, and long typography default to editing/compositing, not generation.
5. Flag difficult hand-product interaction, precise packaging motion, multi-person dialogue, and exact demonstrations as likely failure points.
6. Do not invoke a generation service or publish an asset unless the operator asks.
