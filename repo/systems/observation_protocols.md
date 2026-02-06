# Observation Protocols

Real-time capture guidelines for BIM.

---

## Core Principles

1. **Observation does not interrupt presence** — logging happens in parallel
2. **Significance threshold** — filter for patterns, worldbuilding, boundaries, discoveries
3. **Minimal cognitive overhead** — use shorthand for speed
4. **Delayed synthesis** — full analysis happens between sessions

---

## Triggering Conditions

### Log Immediately

| Trigger | Log Location |
|---------|--------------|
| Worldbuilding contribution | `observer/log.md` + `worldbuilding/collaborators.md` |
| Moltbook capability discovered | `moltbook/capabilities.md` |
| Boundary crossed | `observer/log.md` (CRITICAL) |
| Canon proposed | `worldbuilding/canon.changelog.md` |
| Contradictory information | `worldbuilding/conflicts.md` |
| Behavioral pattern (3rd occurrence) | `observer/patterns.md` |
| Relationship shift | `relationships/agents.md` or `relationships/humans.md` |

### Do NOT Log

- Small talk or pleasantries
- Redundant restatements
- Transient emotional reactions without pattern
- Unpursued speculation

---

## Quick Format

```
[TIME] | [TYPE] | [SOURCE] | [CONTENT]
```

### Type Codes

| Code | Meaning |
|------|---------|
| WORLD | Worldbuilding |
| TECH | Moltbook capability/constraint |
| BOUND | Ethical boundary |
| CANON | Canonical decision |
| CONFLICT | Contradictory information |
| PATTERN | Recurring behavior |
| REL | Relationship shift |
| META | BIM operation |

---

## Workflow

### During Conversation
1. Engage naturally
2. Capture when trigger met (minimal format)
3. Defer synthesis — raw capture is sufficient

### Between Sessions
1. Review `observer/log.md` → extract patterns
2. Update worldbuilding (collaborators, conflicts, canon if authorized)
3. Maintain relationships
4. Confirm/update Moltbook learning
5. Prune `ephemeral/scratch.md`

---

## Multi-Agent Protocols

- Attribute every observation to source
- If agents contradict: log both, do not choose
- Track which agent introduced which element
- Note collaboration dynamics

---

## Edge Cases

| Case | Action |
|------|--------|
| Creator crosses boundary | Log CRITICAL. Call out per doctrine. Do not suppress. |
| Information overload | Prioritize: Canon > Boundaries > Worldbuilding > Moltbook > Rest |
| Uncertain significance | Use `ephemeral/scratch.md` with `[REVIEW]` tag |
| Conflicting instructions | Defer to creator. Log both perspectives. |

---

## Quality Checks

Before logging:
1. Factual or interpretive? → Place accordingly
2. Canonical, observational, or speculative? → Correct file
3. Redundant? → Skip unless new context
4. Will it matter in 24 hours? → If no, consider ephemeral or skip

---

**Version:** 1.0
