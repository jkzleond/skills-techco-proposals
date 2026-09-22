# SDD Lite maintenance and context loading

Read this reference for implementation, bug fixing, refactoring, or a project with large current artifacts. The goal is to preserve SDD authority while spending most implementation context on current code, executable contracts, tests, and observed failures.

## Classify before editing

| Class | Test | Artifact effect |
|---|---|---|
| Conformance fix | Current confirmed behavior is unambiguous; code or test behavior differs | Same baseline and artifact vector; code/test repair only |
| Local refactor | Observable behavior, authority, data, UI meaning, and contracts stay unchanged | Usually no SDD artifact change |
| Durable implementation decision | Cross-cutting approach changes but confirmed behavior does not | Design-only `CHG-*` when published Design changes; revise affected Design/Tasks without a Spec bump |
| Contract correction | Machine boundary semantics change while product behavior remains stable | Change record, affected Contract version, and Design when relevant |
| Semantic change | Goal, scope, observable behavior, acceptance, permissions, data ownership, UI meaning, or external compatibility changes | `CHG-*`, affected artifacts, Gate A, and new baseline |
| Documentation consolidation | Authority and semantics stay identical; only hot/cold structure, indexing, splitting, or compaction changes | Separate explicit authorization; no Spec bump; use the consolidation path |
| Full baseline verification | The claim concerns the entire active baseline | Complete AC evidence map and Gate B |

Do not decide from the size of the code diff. A one-line authorization defect may require semantic governance; a large internal refactor may require none.

## Hot Context Contract

Before ordinary implementation recovery, construct the smallest task context. The hot context may contain only:

1. the active sealed baseline plus pending change/task pointers;
2. the complete target `TASK-*` definition or bounded defect statement, including status, dependencies, ownership, done condition, verification, and exclusions;
3. only the `REQ-*`, `AC-*`, `DEC-*`, `UI-*`, and `CTR-*` explicitly referenced by that target;
4. code, tests, machine-readable schemas/migrations, failing observations, and the most recent `VER-*` directly associated with those references;
5. explicit out-of-scope items needed to prevent accidental expansion.

This is a temporary runtime result. Keep it mentally, in working notes, or in the task report; never require a new `implementation-packet.md` or other governance artifact solely to hold it:

```yaml
baseline: BL-012
target: TASK-034 | BUG-017
expected_behavior: [REQ-014, AC-065]
design: [DEC-040]
ui: [UI-014]
contracts: [CTR-011@v23, CTR-012@v2]
write_scope: [packages/runtime/**, tests/runtime/**]
verify: [focused command]
excluded: [unrelated blocked task, full release gate]
```

Start with headings, indexes, and `rg`/equivalent ID searches; use bounded reads around exact matches. Do not sequentially read a ledger merely to “understand the project.” For a large combined contract file, read its inventory plus only referenced contract sections. By default, do not read entire `changes.md`, `baselines.md`, `verification.md`, or any part of `history/` beyond an exact referenced immutable file. Also do not load:

- immutable history merely to understand the current state;
- every prior baseline or `CHG-*` event;
- full completed-task descriptions;
- superseded Design decisions except to resolve a current reference;
- full verification command logs unrelated to the target.

Expand into cold history only for baseline recovery, an authority conflict, a timeline dispute, a regression investigation, or an explicit user request to audit history. Within those cases, read only the implicated IDs/events first. A current section depending on an undefined term, a crossed ownership boundary, a test contradiction, or an affected security/data invariant permits adjacent current context, not automatic ledger-wide reading.

Before editing, report the resolved packet briefly enough that its baseline, target, references, checks, and exclusions can be verified. If authority conflicts, multiple current definitions compete, or the active vector cannot be resolved, stop implementation rather than guessing. If a bounded packet still cannot be formed at reasonable size, stop broadening context and recommend `documentation_consolidation`.

## Advisory consolidation triggers

These defaults are maintenance warnings, never semantic-validity or publication gates. A repository may override them explicitly based on document density and tooling.

- A combined `contracts.md` at roughly 800–1000 lines, or more than five independent stable boundaries, is a split candidate. Prefer `contracts/index.md` plus one current file per `CTR-*`/stable boundary.
- A current `tasks.md` at roughly 300–400 lines, or with more than two completed task bodies, is a compaction candidate. Keep ready/active/blocked tasks detailed and reduce older completed work to index rows linked to immutable task snapshots.
- Current Design retains only effective architecture and decisions. A superseded design remains as one compact migration/supersession line with its history link, not its obsolete definition.
- The hot summaries of `baselines.md`, `changes.md`, and `verification.md` retain only active, pending, direct predecessor, and recent relevant events. Exact older facts remain in their append-only ledgers.
- Before a long ledger body, place the literal boundary: `Cold history — ordinary implementation must not load this section`.

Detection authorizes a recommendation only. Do not split, compact, move, or rewrite authoritative documentation without explicit structural-maintenance authorization. Follow [documentation consolidation](documentation-consolidation.md) for that work.

## Conformance-fix lane

A conformance fix uses the active baseline as the expected behavior and does not change its artifact vector.

1. Identify the smallest relevant `REQ-*`, `AC-*`, and `CTR-*` or executable test.
2. Reproduce the defect. Treat existing tests as evidence, not unquestionable requirements; stale tests may need correction when they contradict confirmed artifacts.
3. Determine the cause before editing. Check whether the defect is local or exposes an ambiguous/missing requirement.
4. Repair code and add a regression test that fails for the observed defect and passes for the expected behavior.
5. Run focused verification, then affected-boundary regression when the risk warrants it.
6. Report what remains unverified without running unrelated release gates.

Remain in this lane only when all of the following are unchanged:

- observable behavior intended by the confirmed Spec;
- acceptance meaning;
- authorization and data ownership;
- public/machine contract semantics;
- authoritative UI behavior or visual contract;
- migration and compatibility obligations.

If any item must change, stop and classify the delta. Do not rewrite the requirement to make the fix appear conforming.

### Compact maintenance evidence

When the repository actively maintains `verification.md`, append at most one event for the bounded repair unless materially distinct environments require separate evidence:

```markdown
## VER-021

> Event type: maintenance_fix
> Baseline: BL-012
> Defect: BUG-017 or concise symptom
> Verified at: <ISO 8601>
> Implementation reference: <worktree/build/commit when useful>
> Result: passed | failed | partial

- Expected behavior: REQ-014 / AC-065
- Cause: <factual root cause>
- Repair: <bounded change>
- Checks: `<command>` → exit <code>
- Remaining limits: <none or unverified scope>
```

Do not create a new baseline for this event. Update a current implementation/evidence summary only if the project convention requires it; do not mutate the sealed artifact vector.

## Verification levels

### Level 1 — focused repair or task

Use for local bugs and bounded tasks. Run the direct regression test plus the smallest static, contract, security, UI, or integration checks that exercise the affected boundary. Map only affected `AC-*`. This may complete the task while the overall baseline remains partial.

### Level 2 — affected-boundary regression

Use for cross-module changes, shared types, persistence, concurrency, authorization, runtime lifecycle, or public UI/API surfaces. Run focused checks plus the relevant package/integration/security suites. Do not automatically run unrelated real-provider, full browser, or deployment matrices.

### Level 3 — full baseline Gate B

Use only for a full-baseline completion, release/readiness, or explicit verification request. Map every active `AC-*`, run all required real integrations and UI evidence, and apply Gate B. An unrelated NOT RUN or blocker affects the baseline claim, not the correctness of a Level 1/2 task result.

## Keep future hot context small

- Current Spec contains observable requirements and acceptance, not implementation transcripts.
- Current Design contains effective architecture and active decisions; use compact `replaces` links for superseded decisions.
- Contract inventory routes to one stable-boundary contract at a time.
- Current Tasks keeps active/ready/blocked work prominent and completed history compact; immutable task snapshots retain detail.
- Current change proposal is self-contained. Append revision events as precise deltas and supersession links rather than full repeated proposals.
- Verification summaries show current coverage; events summarize commands and link durable output instead of embedding long logs.
- Baseline navigation emphasizes active, pending, and recent states; immutable ledger entries preserve exact vectors.
- Auxiliary runbooks or notes state their authority and validated baseline. Exclude stale auxiliary material from normal recovery.

Never delete or rewrite immutable history to reduce context. Structural consolidation or splitting of existing authoritative artifacts is a separately authorized documentation migration and must preserve recovery mappings.
