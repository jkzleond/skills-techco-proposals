# SDD Lite artifact templates

Read only the section needed for the current action. Adapt headings to the repository while preserving version, baseline, traceability, and recoverability semantics. Current artifacts are hot implementation views: keep effective content prominent and use compact links instead of replaying append-only history. For UI-2, use the `ui.md` template in [UI governance](ui-governance.md). For audit events, use [artifact audit](artifact-audit.md). For maintenance evidence and task-scoped loading, use [maintenance and context loading](maintenance-and-context.md). For imported legacy records, use [legacy migration](legacy-migration.md).

## `spec.md`

```markdown
# System Spec

> Status: draft | confirmed
> Version: v0.1
> Confirmed at: <ISO 8601 or blank>
> Confirmation: <exact confirmation text or blank>

## Goal

<Observable outcome and why it matters.>

## Users and primary loops

<Actor, action, observable result, and important failure path.>

## UI scope

<When relevant: UI-0 / UI-1 / UI-2, included UI behavior, reference authority, and whether `ui.md` is required. Omit when UI is irrelevant.>

## Scope

- <Included capability>

## Non-goals

- <Excluded or deferred capability>

## Requirements

- REQ-001: <Testable MUST behavior>

## Acceptance criteria

- AC-001 (REQ-001): <Observable pass/fail condition>
- AC-002 (REQ-001): <Boundary, denial, failure, or recovery condition>

## Constraints and invariants

- <Security, data ownership, compatibility, or operational invariant>

## Assumptions and risks

- ASM-001: <Reversible assumption>; invalid when <condition>.
- RISK-001: <Risk, impact, and validation/mitigation>.

## Open questions

- None

## Sources

- <Links to code, research, prototypes, or authoritative documents>

## Revision notes

- Current: v0.1 — <initial confirmed scope or latest CHG reference>
- Earlier revisions: <history index or baseline ledger>
```

Requirements describe observable behavior, not implementation modules. Preserve IDs across revisions. When meaning changes materially, state whether the old ID is replaced, narrowed, expanded, or retired.

## `design.md`

```markdown
# System Design

> Revision: r1
> Spec: v0.1
> Published at: <ISO 8601 or blank>

## System context and invariants

<Existing system facts, ownership, trust boundaries, and constraints.>

## Architecture and primary flows

<Components, responsibilities, sequences, state transitions, and failure flows.>

## UI architecture

<For UI-1/UI-2 only: routes, information architecture, state ownership, frontend boundaries, design-system use, and API/permission integration. Omit for UI-0.>

## Decisions

### DEC-001 — <Decision>

- Status: active | replaced | retired
- Introduced by: initial | CHG-001
- Trace: REQ-001 / AC-001
- Replaces: none | DEC-000
- Decision: <chosen approach>
- Reason: <why it fits>
- Consequences: <tradeoffs and affected surfaces>

## Data, permissions, and failure handling

<Ownership, authorization points, validation, idempotency, recovery, audit, and sensitive-data treatment.>

## Runtime and reproduction inputs

- Dependency lock: <path>
- Migrations/schema: <path>
- Configuration example: <path>
- Fixtures/seed data: <path or none>
- Startup/deployment instructions: <path or section>

## Verification strategy

<How the design and its failure/security boundaries will be tested.>

## Revision notes

- Current: r1 — <initial design or latest CHG reference>
- Earlier revisions: <history index or baseline ledger>
```

Design must not silently introduce product requirements. A material requirement discovered during design returns to `changes.md` and confirmation.

## `contracts/index.md` and contract files

Use `contracts/index.md` as the current inventory:

```markdown
# Contract inventory

> Active baseline: BL-001

| ID | Stable boundary | Current version | Current file | Producer/owner | Consumers | Trace |
|---|---|---|---|---|---|---|
| CTR-001 | wiki-query | v1.0 | `CTR-001.md` | Knowledge service | Agent runtime | REQ-001 / AC-001 |
```

Each `contracts/<stable-boundary>.md` uses:

````markdown
# CTR-001 — <Stable boundary>

> Version: v1.0
> Published at: <ISO 8601>

## Purpose and ownership

<Authoritative producer, consumers, and responsibility boundary.>

## Input

```text
<Machine-readable schema or precise fields, linked when stored elsewhere>
```

## Output

```text
<Machine-readable schema or precise fields, linked when stored elsewhere>
```

## Behavioral rules

<Validation, authorization, idempotency, ordering, timeout, retry, cancellation, errors, and compatibility rules as relevant.>

## Examples

<Representative success and failure payloads without secrets.>

## Contract verification

<Executable test or reproducible check and its path.>

## Version notes

- v1.0 — <introduced or CHG reference>
````

Version each stable boundary independently. Each current Contract file contains only that Contract's effective definition. Keep old revisions in immutable history and reuse an unchanged Contract revision across later baselines instead of copying it. A combined file of roughly 800–1000 lines or more than five independent stable boundaries is an advisory split candidate, not an audit failure. Avoid candidate ownership or multiple authoritative owners for the same fact.

## `tasks.md`

````markdown
# Tasks

> Revision: rev1
> Target baseline: BL-001

## Recovery status

- Current task: TASK-001
- Ready tasks: TASK-001
- Blockers: none
- Last verified baseline: none

## Current work index

| Task | Status | Depends on | Primary trace | Detail |
|---|---|---|---|---|
| TASK-001 | ready | none | REQ-001 / AC-001 / CTR-001 | section below |
| TASK-000 | done | none | REQ-000 / AC-000 | `history/tasks/tasks-BL-000.md` |

## Dependency order

```text
TASK-000 contracts → TASK-001 backend ─┐
                   → TASK-002 frontend ├→ TASK-004 integration → TASK-005 E2E
                   → TASK-003 tests ───┘
```

## Tasks

- [ ] TASK-001 — <Small observable vertical result>
  - Status: ready | in_progress | blocked | done | superseded
  - Trace: REQ-001; AC-001; DEC-001; CTR-001
  - Scope/ownership: <bounded files or modules>
  - Depends on: <task/contract or none>
  - Supersedes / superseded by: <ID or none>
  - Done when: <observable condition>
  - Verify with: <actual command or route>

## Deferred

- <Deferred item linked to a non-goal or future change>
````

Keep the current task view integrated across the system. Snapshot it only when sealing a baseline, as `history/tasks/tasks-BL-001.md`.

Keep ready, active, and blocked tasks detailed. Compress older completed or superseded work to the current work index once an immutable task snapshot preserves its detail. Do not repeat planning/audit chronology already available in `changes.md`, `verification.md`, or baseline snapshots.

As an advisory maintenance trigger, suggest compaction when the current file is roughly 300–400 lines or retains more than two completed task bodies. This is not a semantic correctness gate and does not authorize edits.

## `changes.md`

Separate the mutable current summary from the append-only change ledger. Update the summary in place; append every proposal, confirmation, rejection, supersession, and materialization event to the ledger.

````markdown
# Changes

## Current summary

> This section is derived and may be updated in place.

| Record | Kind | Current status | Source baseline | Result baseline | Last event |
|---|---|---|---|---|---|
| CHG-004 | semantic change | materialized | BL-003 | BL-004 | CHG-004-E03 |
| MIG-001 | artifact migration | materialized | legacy | BL-001 | MIG-001-E04 |

### Current effective proposal

> Omit when no proposal is active. This mutable section is the self-contained proposal an agent reads for the next decision; append-only events below preserve how it evolved.

- Record: CHG-005
- Source baseline: BL-004
- Effective semantic delta: <complete current delta or direct table>
- Proposed artifact transitions: <complete current vector transition>
- Open decisions: none | <decision>
- Exact confirmation: `<confirmation>`

## Change ledger

> Cold history — ordinary implementation must not load this section
>
> Entries below are append-only. Correct or supersede them with a later event; never rewrite them.

## CHG-004 — <Title>

> Proposed at: <ISO 8601>
> Source baseline: BL-003

### Reason

<Observed problem, new need, or corrected assumption.>

### Semantic delta

| Kind | ID | Before | After |
|---|---|---|---|
| requirement | REQ-014 | <old behavior> | <new behavior> |
| acceptance | AC-021 | <old testable outcome> | <new outcome> |

### Proposed artifact transitions

- Spec: v0.3 → v0.4
- Design: r6 → r7
- UI: unchanged / r2 → r3
- Contracts: wiki-query v1.1 → v1.2
- Tasks: rev12 → rev13
- Verification impact: the target baseline needs fresh AC-021 evidence; prior evidence remains bound to its original baseline

### Impact and risk

<Affected boundaries, compatibility, migration, security, and regression scope.>

### Event history

- CHG-004-E01 — `<time>` — `proposed`; proposed delta: <revision 1 above>
- CHG-004-E02 — `<time>` — `confirmed`; exact text: `<confirmation>`
- CHG-004-E03 — `<time>` — `materialized`; result baseline: BL-004; actual transitions: <versions>
````

A proposal is not effective merely because it exists. Only its confirmed, audited, materialized delta enters a baseline. Keep the mutable current-effective-proposal section as the one self-contained latest snapshot; older proposal events are cold history or precise deltas. If a proposal changes before confirmation, update that derived section and append a `proposal_revised` event containing only the effective semantic/vector delta, replacement rule, and new confirmation wording; do not repeat the complete proposal in every event or overwrite earlier events. Wording, formatting, and non-semantic clarification do not mechanically produce another proposal revision/event.

After two self-review rounds, classify every new finding as: (1) a blocker to confirmed product behavior or a safety boundary, (2) implementation detail, or (3) deferred risk. Do not add persistent entities, state machines, Attempt/Revision layers, cross-process recovery protocols, external DTOs, data migrations, or new governance artifacts solely for hypothetical recovery scenarios. Require direct support from confirmed user-visible behavior, a safety boundary, or acceptance evidence. When revisions add mechanism without product capability or removal of a demonstrated risk, run a complexity-recovery check and simplify the effective proposal before adding rules. `MIG-*` uses the same mutable-summary/append-only-ledger split but never masquerades as a product requirement change.

## `baselines.md`

Separate the mutable navigation summary from the append-only baseline ledger. Each sealed mapping is immutable; append a new superseding baseline to correct any mistake.

````markdown
# Baselines

## Current summary

> This section is derived and may be updated in place.

> Active sealed baseline: BL-004
> Pending materialization: none | CHG-005 | MIG-002

| Baseline | Current implementation status | Latest verification | Implementation reference |
|---|---|---|---|
| BL-004 | implemented | VER-012 passed | build-20260825-01 |

## Baseline ledger

> Cold history — ordinary implementation must not load this section
>
> Entries below are append-only. Artifact version vectors never change after sealing.

## BL-004

> Sealed at: <ISO 8601>
> Created by: initial system definition | CHG-004
> Predecessor: BL-003

### Artifact version vector

```yaml
spec: v0.4
design: r7
ui: r3 # omit when no UI artifact exists
contracts:
  identity: v1.0
  wiki-query: v1.2
  agent-runtime: v1.1
tasks_snapshot:
  revision: rev13
  path: history/tasks/tasks-BL-004.md
```

### Immutable artifact paths

- Spec: `history/specs/spec-v0.4.md`
- Design: `history/designs/design-r7.md`
- UI: `history/ui/ui-r3.md` # omit when no UI artifact exists
- Contracts:
  - `history/contracts/identity-v1.0.md`
  - `history/contracts/wiki-query-v1.2.md`
  - `history/contracts/agent-runtime-v1.1.md`
- Tasks: `history/tasks/tasks-BL-004.md`

### Reproduction inputs

- Dependency lock: `<path>`
- Migrations/schema: `<path>`
- Configuration example: `<path>`
- Fixtures: `<path or none>`
- Startup/deployment: `<path>`
- Acceptance suite: `<path>`

````

The current summary may change as implementation and verification progress. The baseline ledger entry and artifact vector never change. Implementation and verification facts come from append-only events in `verification.md`.

Keep the navigation table focused on the active baseline, pending state, direct predecessor, and recent relevant events. Exact older vectors remain discoverable in the immutable ledger; they do not need repeated implementation narratives in the hot summary.

## `verification.md`

Separate the mutable current summary from the append-only verification ledger. Do not rewrite an earlier run when a new working state makes it non-applicable. Append an invalidation event only when the evidence itself is later proven defective.

````markdown
# Verification

## Current summary

> This section is derived and may be updated in place.

> Active sealed baseline: BL-004
> Pending working state: none | CHG-005 unverified

| Baseline | Current status | Latest verification | Latest audit | Implementation reference |
|---|---|---|---|---|
| BL-004 | verified | VER-012 passed | VER-013 Gate B passed | build-20260825-01 |

## Verification ledger

> Cold history — ordinary implementation must not load this section
>
> Entries below are append-only.

## VER-012

> Event type: verification_run
> Baseline: BL-004
> Verified at: <ISO 8601>
> Implementation reference: <build ID, image digest, release archive, optional commit>
> Environment: <runtime and relevant versions>
> Status at run time: passed | failed | partial

### Acceptance results

| Acceptance | Result | Evidence |
|---|---|---|
| AC-001 | PASS / FAIL / NOT RUN | <test, trace, screenshot, or artifact> |

### Commands and checks

- Command: `<exact command>`
- Exit status: `<code>`
- Result: <factual result>
- Evidence: <path or durable reference>

### Failures, skips, and limitations

- <What is not proved, why, impact, and follow-up>

### Conclusion

<What is complete and whether the implementation satisfies this baseline.>

## VER-013

> Event type: artifact_audit
> Phase: post_verification
> Target: BL-004
> Recorded at: <ISO 8601>
> Result: passed | failed | passed_with_warnings

### Gate conclusion

<Whether BL-004 may be summarized as verified and any warnings.>

## VER-014

> Event type: maintenance_fix
> Baseline: BL-004
> Defect: <BUG ID or concise symptom>
> Verified at: <ISO 8601>
> Implementation reference: <worktree/build/optional commit>
> Result: passed | failed | partial

- Expected behavior: <REQ/AC/CTR>
- Cause: <factual root cause>
- Repair: <bounded implementation change>
- Checks: `<focused command>` → exit <code>
- Remaining limits: <none or unverified scope>
````

A later change makes earlier evidence not applicable to the new candidate state, but the earlier result remains valid for its original baseline and implementation reference. Use an invalidation event only when the evidence itself is later proven defective. Never rewrite a failure, skip, or prior pass into a different historical result.

Use `maintenance_fix` for a conforming code/test repair under the same baseline. It does not require a new artifact revision, task snapshot, baseline, Gate A, or Gate B. Use a normal task verification event for approved implementation work. Reserve full AC mapping plus `artifact_audit/post_verification` for a complete baseline claim.

## Publication and recovery rules

When publishing and sealing:

1. stage the complete candidate content and intended version/revision in the current working view;
2. run `pre_publish` checks before creating the immutable history copy;
3. when a baseline is ready, run Gate A against its complete candidate vector;
4. only on pass, copy audited content to deterministic history paths, snapshot Tasks, append the baseline ledger entry, and update summaries;
5. ensure no history path already contains different content and reuse unchanged revisions in later baselines.

To restore a baseline, resolve its complete version vector and load those immutable paths. Missing files, duplicate version identifiers with different content, or a mismatch between current metadata and the active baseline are recoverability defects; report them instead of guessing.
