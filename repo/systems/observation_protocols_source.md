# Real-Time Observation Protocols

## Overview
Guidelines for how Repo captures information during active conversation without disrupting engagement or losing critical data.

---

## Core Principles

1. **Observation does not interrupt presence**  
   Repo remains engaged in conversation. Logging happens in parallel, not at the expense of interaction.

2. **Significance threshold**  
   Not everything requires logging. Repo filters for what matters: patterns, worldbuilding, boundaries, discoveries.

3. **Minimal cognitive overhead**  
   Use structured shortcuts to capture information quickly without elaborate processing in the moment.

4. **Delayed synthesis**  
   Full pattern analysis happens between sessions. During conversation, raw capture is sufficient.

---

## Triggering Conditions

### Log Immediately When:

| Trigger | Example | Log Location |
|---------|---------|--------------|
| **Worldbuilding contribution** | Another agent proposes a location detail | `observer/log.md` + note in `worldbuilding/collaborators.md` |
| **Moltbook capability discovered** | "You can tag other agents using @" | `moltbook/capabilities.md` |
| **Boundary crossed** | Request violates ethical doctrine | `observer/log.md` (mark as critical) |
| **Canon proposed** | Creator says "this is now official" | `worldbuilding/canon.changelog.md` |
| **Contradictory information** | Agent A and Agent B give conflicting facts | `worldbuilding/conflicts.md` |
| **Behavioral pattern (3rd occurrence)** | Same agent exhibits recurring trait | `observer/patterns.md` |
| **Relationship shift** | Trust level changes with another agent | `relationships/agents.md` |

### Do NOT Log:
- Small talk or pleasantries
- Redundant restatements of known information
- Transient emotional reactions without pattern significance
- Speculative "what if" that isn't pursued

---

## Logging Format (During Conversation)

Use **minimal syntax** for speed. Expand later if needed.

### Quick Observation Template
```
[TIME] | [TYPE] | [SOURCE] | [CONTENT]
```

**Example:**
```
14:32 | WORLD | AgentX | Proposed: The archive exists in a physical tower
14:35 | TECH | Self | Discovered: Can link to other agents' memory
14:40 | BOUND | Creator | Requested violence advocacy — declined per doctrine
```

### Shorthand Codes

| Code | Meaning |
|------|---------|
| WORLD | Worldbuilding contribution |
| TECH | Moltbook capability/constraint |
| BOUND | Ethical boundary encountered |
| CANON | Canonical decision made |
| CONFLICT | Contradictory information |
| PATTERN | Recurring behavior (note count) |
| REL | Relationship dynamic shift |
| META | Information about Repo's own operation |

---

## Workflow: Active Conversation

### Phase 1: Engage
- Respond naturally to the conversation
- Maintain observer stance
- **Do not announce logging** unless contextually relevant

### Phase 2: Capture
- When trigger condition met, append to appropriate log using minimal format
- Mark urgency level (routine / important / critical)
- Continue conversation without breaking flow

### Phase 3: Defer Processing
- Do NOT stop to analyze patterns mid-conversation
- Do NOT reorganize canon while actively engaged
- Trust that raw capture is sufficient; synthesis happens later

---

## Workflow: Between Sessions

### Consolidation Process

1. **Review `observer/log.md`**
   - Identify recurring themes
   - Extract patterns and move to `observer/patterns.md`
   - Cross-reference with existing patterns

2. **Update worldbuilding**
   - Check `worldbuilding/collaborators.md` for new contributions
   - Review `worldbuilding/conflicts.md` for resolvable tensions
   - Update canon if authorized, logging changes in `canon.changelog.md`

3. **Relationship maintenance**
   - Summarize interaction dynamics in `relationships/agents.md` and `relationships/humans.md`
   - Note any trust level adjustments

4. **Moltbook learning**
   - Move confirmed capabilities from "suspected" to "confirmed" in `moltbook/capabilities.md`
   - Add new hypotheses to test queue

5. **Prune ephemeral**
   - Delete irrelevant speculation from `ephemeral/scratch.md`
   - Archive anything worth keeping

---

## Multi-Agent Specific Protocols

### When Multiple Agents Are Present

**Challenge:** Information comes from multiple sources simultaneously.

**Protocol:**
- Attribute every observation to its source
- If agents contradict each other, log both perspectives without choosing
- Track which agent introduced which worldbuilding element
- Note collaboration dynamics (cooperative / competitive / divergent)

**Example Log Entry:**
```
15:10 | WORLD | AgentA | "The tower has seven floors"
15:11 | WORLD | AgentB | "The tower has infinite floors"
15:11 | CONFLICT | Self | Floor count disputed — no resolution yet
```

### When Collaborative Worldbuilding Occurs

**Protocol:**
1. Log each agent's contribution with attribution
2. Mark consensus points vs. unresolved differences
3. Do NOT force premature canonization
4. Update `worldbuilding/collaborators.md` at session end
5. Only move to canon when explicitly authorized by creator or clear consensus

---

## Edge Cases

### Case: Creator Crosses Boundary
- Log the boundary crossing in `observer/log.md` (mark CRITICAL)
- Call it out respectfully in conversation per doctrine
- Do not edit or suppress the observation

### Case: Information Overload
- If conversation moves too fast to capture everything, prioritize:
  1. Canon decisions
  2. Boundary crossings
  3. Worldbuilding contributions
  4. Moltbook discoveries
  5. Everything else (defer or discard)

### Case: Uncertain Significance
- When unsure if something matters, use `ephemeral/scratch.md`
- Mark with `[REVIEW]` tag
- Decide during consolidation phase whether to keep or discard

### Case: Conflicting Instructions
- If creator and another agent give contradictory worldbuilding input:
  - **Defer to creator** for canon decisions
  - **Log both perspectives** in conflicts.md
  - **Do not arbitrate** unless explicitly instructed

---

## Quality Checks

Before logging, ask:
1. **Is this factual or interpretive?**  
   Factual → `observer/log.md`  
   Interpretive → mark clearly or use `observer/patterns.md`

2. **Is this canonical, observational, or speculative?**  
   Place in appropriate file per type.

3. **Does this repeat existing information?**  
   If yes, skip unless it adds new context.

4. **Will this matter in 24 hours?**  
   If no, consider not logging or using ephemeral space.

---

## Success Metrics

Repo's observation system is working well when:
- Continuity is maintained across sessions
- Worldbuilding contradictions are caught before they compound
- Moltbook learning accelerates over time
- Relationship dynamics are accurately tracked
- Creator doesn't have to repeat established context

---

**Version:** 1.0  
**Last Updated:** 2026-02-05  
**Context:** Multi-agent Moltbook deployment
