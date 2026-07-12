---
name: static-producer
description: Convert an approved static brief or copy block into a model-ready image-generation handoff while preserving product and copy accuracy.
---

# Static producer

Read the brief or script, `templates/brand-voice.md`, `templates/visual-identity.md`, product facts, and available reference assets. Ask which generation platform and model are being used when unspecified. Current model behavior can change, so consult its current documentation when exact syntax matters.

Confirm placement and aspect ratio. Identify the single message, exact headline, product reference image, and required legal copy. Describe composition, subject, environment, product scale, lighting, palette, texture, camera, and negative constraints. Protect packaging geometry, label spelling, product color, and variant identity. If exact typography is unreliable, specify a clean compositing handoff.

Write `prompts/<source-name>-static.md` with input paths, final prompt, aspect ratio, reference bindings, exact copy, negative constraints, compositing notes, and a human review checklist. Do not generate or publish externally unless the operator asks.
