# SDD Lite artifact audit

Read this reference before publishing an immutable artifact revision, sealing a baseline, marking a baseline verified, or restoring a baseline. Audit structure and traceability deterministically where possible; use semantic review for intent and boundary consistency. Do not invent missing evidence.

## Audit event model

Record durable audit results in the append-only ledger of `verification.md` with a `VER-*` ID and `Event type: artifact_audit`. The mutable summary may point to the latest result. A single materialization may use one consolidated audit event with clearly separated `pre_publish` and `pre_seal` results; do not create one event per artifact or per mechanical check unless their timing or result must remain independently addressable.

Use one of these phases:

- `pre_publish`: validates a candidate Spec, Design, UI, or Contract revision before copying it into `history/`;
- `pre_seal`: Gate A, validates the complete candidate artifact vector before sealing `BL-*`;
- `post_verification`: Gate B, validates the evidence closure before the baseline summary becomes `verified`;
- `restore`: Gate C, validates exact recoverability of a historical baseline.

For a read-only restore or inspection, report the audit without writing an event unless the user also authorizes recording it.

Classify findings as:

- `error`: breaks identity, consistency, traceability, recoverability, or required evidence; blocks the gate;
- `warning`: credible limitation that does not invalidate the baseline; record it and continue only when acceptance is unaffected;
- `note`: explanatory context.

Never repair a semantic error silently. Structural corrections may be made within the authorized documentation scope before publication; requirement, UI-scope, security/data-boundary, or contract-semantic changes return to alignment or `CHG-*` confirmation.

## Pre-publication check

Run before creating or replacing any immutable history file.

- Candidate metadata contains the intended version/revision and publication status.
- Stable IDs are unique and retain their prior meanings, or explicitly replace/retire earlier IDs.
- All material references resolve to existing or concurrently staged IDs and sources.
- The candidate contains no unresolved question that blocks its scope.
- A history path with the same version does not already contain different content.
- UI and contract references use stable repository paths where exact restoration matters; an unstable external URL is not the sole exact-recovery source.
- The candidate header version/revision agrees with the proposed transition and every vector/reference that already names it.
- Current normative sections do not cite superseded Design, UI, Contract, or Task revisions as current authority, and do not embed copied historical definitions.
- One mechanism has only one current authoritative definition. Historical sections and revision notes cannot define current behavior.
- Any difference between an artifact claimed as the active/reused revision and its immutable snapshot is either absent or explicitly registered as a pending candidate transition.

On failure, keep the artifact as a candidate, append or report the failed audit, and do not publish that revision.

## Gate A — pre-seal baseline audit

Run after candidate Spec, Design, applicable UI, Contracts, and Tasks are mutually ready, but before publishing remaining revisions and sealing the baseline.

### Structure and version vector

- The target `BL-*` is unique and its predecessor/source record is explicit.
- The vector names one confirmed Spec, one effective Design, every applicable Contract, optional UI revision, and one Tasks snapshot.
- Every immutable path is deterministic, exists already without conflicting content, or is ready to be published from an audited candidate.
- No vector entry points to a draft, missing file, ambiguous version, or overwritten historical revision.
- Unchanged artifact revisions are reused instead of duplicated.
- The candidate vector agrees with each current artifact header and `contracts/index.md`; every artifact claimed unchanged agrees with its immutable revision, while every changed artifact has an explicit pending transition.
- Mutable summaries identify only the active state, pending state, direct predecessor, and recent relevant events; older ledger material is behind an explicit cold-history boundary.

### Trace and semantic closure

- Every active MUST `REQ-*` has at least one observable `AC-*`.
- Material `DEC-*`, `CTR-*`, optional UI flows/states, and `TASK-*` trace to applicable `REQ-*` or `AC-*`.
- Design, UI, and Contracts do not introduce behavior or authority that contradicts the confirmed Spec.
- Authoritative ownership, permission enforcement, failure behavior, and externally visible compatibility are unambiguous.
- Task dependencies are acyclic enough to identify ready work; shared contracts or foundational types precede dependent parallel tasks.
- Referenced reproduction inputs exist or are explicitly recorded as limitations.
- Current normative sections contain no superseded `CTR-*`, Design, UI, or Task reference and no copied historical prose that competes with the current definition.
- Every `TASK-*` dependency and trace resolves to the current or explicitly staged revision; no dependency silently points to an old version.
- There is no unregistered drift between the last sealed vector, current headers, immutable snapshots, and declared pending transitions.

If current artifacts, summaries, and immutable revisions disagree about authority, stop the gate and implementation. Report the competing definitions and required decision; never infer the winner from chronology, code behavior, or document length.

### Gate result

If any error remains, do not publish the remaining candidate revisions, snapshot Tasks, or seal the baseline. Keep `Pending materialization` visible and return to the affected artifact or alignment decision.

If the audit passes:

1. publish audited candidate revisions into immutable history paths;
2. snapshot Tasks;
3. append the immutable baseline ledger entry and update the current summary;
4. append the `materialized` event to the originating `CHG-*` or `MIG-*` record.

## Gate B — post-verification evidence audit

Run only after implementation checks for the complete baseline and before marking that baseline `verified`. Do not run Gate B merely to finish a bounded task, conformance fix, or affected-boundary regression. Those operations record only their affected evidence and may pass while the overall baseline remains partial.

- Every active `AC-*` has fresh PASS/FAIL/NOT RUN evidence bound to the same `BL-*` and implementation reference.
- Required real integrations are not represented as passed by mocks alone.
- Commands, environment, time, exit status, artifacts, failures, skips, and limitations are recorded factually.
- Contract, security, UI interaction, visual, responsive, accessibility, and failure-path evidence exists when required by the baseline.
- The current summaries of `verification.md` and `baselines.md` are derivable from append-only events.
- Prior evidence remains attached to its original baseline. A later change may make it `not applicable` to the new working state, but does not rewrite the historical result.

An error blocks the `verified` summary state, not the existence of the sealed baseline. Append corrective or later verification events; never edit an earlier run. Unrelated `NOT RUN` acceptance items belong in a full-baseline result and must not be restated as a failure of an otherwise passing bounded task.

## Gate C — restore audit

Run when restoring or comparing a historical `BL-*`.

- Resolve the complete version vector from the immutable baseline ledger entry.
- Confirm every referenced history file and reproduction input exists.
- Confirm internal versions/revisions and stable IDs match the vector.
- Confirm the Tasks snapshot and optional UI revision are the ones named by the baseline.
- Report duplicate version identifiers with different content, missing paths, broken references, or non-derivable summaries as recoverability defects.

Pass means the SDD artifact set can be restored exactly. It does not by itself prove that source code, external services, credentials, or production data can be reconstructed.

## `artifact_audit` event template

```markdown
## VER-014

> Event type: artifact_audit
> Phase: pre_publish | pre_seal | post_verification | restore
> Target: spec v0.4 | candidate BL-004 | BL-004
> Recorded at: <ISO 8601>
> Result: passed | failed | passed_with_warnings

### Checks

| Check | Result | Evidence |
|---|---|---|
| Version and identity | PASS / FAIL | <paths and versions> |
| Traceability | PASS / FAIL | <coverage or broken references> |
| Recoverability | PASS / FAIL | <history paths or missing items> |

### Findings

- ERROR / WARNING / NOTE — <finding and affected IDs or paths>

### Gate conclusion

<What is allowed next and what remains blocked.>
```
