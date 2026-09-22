---
name: sdd-lite
description: "Run a lightweight, repository-native specification-driven workflow for MVPs and evolving systems: align and confirm requirements, maintain recoverable baselines, load implementation context by task references, route conforming bug fixes without artifact churn, govern semantic changes, and verify proportionally. Use when the user explicitly mentions SDD Lite, sdd-lite, 轻量 SDD, MVP 规格化, or asks to work from an SDD Lite baseline. Do not use for strict SDD governance, Manifest/hash approval, or ordinary edits that do not request SDD Lite."
---

# SDD Lite

Maintain a compact requirements-to-evidence chain that another AI can recover without chat history or Git commit boundaries. Optimize for one integrated current-system view, low drift, exact recovery of sealed artifact baselines, minimal sufficient hot context, and proportional process. SDD Lite is a decision and verification aid, not a requirement to produce documentation for every code change. Do not recreate the Manifest, hashes, review dossiers, question registry, or amendment machinery of strict SDD.

## Boundaries

- Activate for `$sdd-lite` or a clear natural-language request to use SDD Lite. Do not treat ordinary implementation, a bare mention of SDD, or generic MVP work as SDD Lite.
- Do not modify implementation merely because the user asks to inspect, discuss, align, plan, draft, audit, migrate, or restore artifacts.
- Existing code is implementation fact, not automatically intended behavior. Research, prototypes, reference designs, and discussion drafts are inputs, not automatically approved requirements.
- Only explicit confirmation that uniquely identifies a Spec version or `CHG-*` can change confirmed requirements. “可以”, “继续”, and similar phrases are not confirmation.
- Requirement confirmation, artifact migration, and implementation are separate authorizations unless the same message explicitly combines them.
- A direct request to implement or fix a stated defect is implementation authorization for that bounded scope. It does not authorize a semantic requirement change.
- Preserve user and concurrent workspace changes. Never reset, overwrite, delete legacy evidence, or silently reconcile unrelated work.

## Apply proportional governance

Classify the work before choosing artifacts:

- `conformance_fix`: code or tests deviate from unambiguous current requirements/contracts; repair implementation under the same sealed baseline;
- `implementation_work`: implement an approved task without changing observable semantics;
- `implementation_decision`: change a durable cross-cutting approach while preserving product behavior; use a design-only `CHG-*` when published Design changes, without bumping Spec;
- `semantic_change`: change observable behavior, acceptance, authority, data, UI meaning, or contract semantics; use `CHG-*` and seal a new baseline;
- `baseline_verification`: claim the complete baseline is implemented or ready; run full evidence closure and Gate B.

Do not promote a conformance fix into a semantic change merely because code changes. If expected behavior is absent, contradictory, or materially ambiguous, pause the fix at that decision boundary and propose alignment or `CHG-*` instead of guessing.

## Maintain one current system view

Use the repository's established documentation convention, or default to:

```text
docs/sdd/
├── spec.md
├── design.md
├── ui.md                     # only for UI-2 or an existing UI baseline
├── contracts/
│   ├── index.md
│   ├── CTR-001.md
│   └── ...
├── tasks.md
├── verification.md
├── changes.md
├── baselines.md
└── history/
    ├── specs/
    ├── designs/
    ├── ui/
    ├── contracts/
    ├── tasks/
    └── legacy/               # only for authorized migration preservation
```

Top-level artifacts are the integrated current working view. Split contracts only by stable boundary or authoritative ownership, never by delivery, feature, or change. A large legacy contract file may be read by referenced section until an authorized structural migration splits it. Do not create a full Spec/Design/UI/Contracts/Tasks/Verification suite for every increment.

While a confirmed change or migration is being materialized, `baselines.md` must distinguish the last sealed baseline from the pending working state. History, superseded plans, completed-task detail, and old ledger events are cold storage. Keep them recoverable, but do not duplicate their prose into current Design, Tasks, or navigation summaries.

### Artifact roles

- `spec.md`: current effective requirements and acceptance criteria; version `vN.N`.
- `design.md`: current effective architecture and decisions; independent revision `rN`.
- `ui.md`: optional project-level current visual/interaction contract for UI-2; independent revision `rN`.
- `contracts/`: current effective component/machine boundaries; version each stable contract independently.
- `tasks.md`: current execution/dependency state; use a lightweight revision and preserve supersession links.
- `verification.md`: mutable current summary plus append-only verification, audit, and invalidation events.
- `changes.md`: mutable current summary plus append-only `CHG-*` and `MIG-*` records/events.
- `baselines.md`: mutable active/pending summary plus append-only sealed `BL-*` version vectors.
- `history/`: immutable published revisions and baseline task snapshots. Never edit an archived revision; publish a new one.

For ledger files, summaries are derived navigation aids and may change in place; historical entries/events may only be appended or superseded by later events. Never rewrite an earlier event to make history appear current.

Current views must stay implementation-readable:

- Design emphasizes effective architecture and active decisions; revision notes point to history instead of replaying every change.
- Tasks emphasizes ready, active, blocked, and recently completed work; preserve older detail in baseline snapshots and keep only compact supersession/status links current.
- A current change proposal has one self-contained effective snapshot; later append-only proposal events record deltas rather than repeatedly restating the full proposal.
- Verification keeps a concise current acceptance/evidence summary; detailed command output lives in durable referenced test artifacts when available.
- Auxiliary documents declare their authority and last validated baseline. Treat stale or unversioned auxiliary prose as observed background, never as current normative truth.

Do not depend on Git to recover SDD artifacts. A commit may be optional implementation evidence, but mixed commits, rebases, or missing repository history must not prevent artifact restoration.

## Load detailed guidance only when relevant

- Read [artifact templates](references/artifact-templates.md) only for the artifact being created or updated.
- Read [artifact audit](references/artifact-audit.md) before publishing an immutable revision, sealing a baseline, marking a baseline verified, or restoring one.
- Read [maintenance and context loading](references/maintenance-and-context.md) for implementation, bug fixing, refactoring, or any project whose current artifacts are large.
- Read [documentation consolidation](references/documentation-consolidation.md) only when proposing or performing an authorized structural cleanup of authoritative artifacts.
- Read [legacy migration](references/legacy-migration.md) when old artifacts lack the current integrated view, ledgers, history, or baseline model.
- Read [UI governance](references/ui-governance.md) when the current action classifies, changes, publishes, or audits UI/page/screen/interaction scope, or when a supplied prototype/design/reference affects the work. An unrelated existing `ui.md` does not force full UI guidance into a non-UI task.

## Recover context cheaply

Reuse a recent project scan only after verifying material conclusions against accessible sources. Otherwise inspect the project, research, and SDD artifacts read-only. If multiple project roots are plausible, stop writes and ask for the target.

For ordinary continuation, obey the Hot Context Contract in [maintenance and context loading](references/maintenance-and-context.md) and use two passes:

1. **Index pass:** read only the active/pending summary and target vector in `baselines.md`; recovery/current status and the target task in `tasks.md`; version metadata and headings of current artifacts; active-change summary in `changes.md`; and current evidence summary in `verification.md`.
2. **Task pass:** follow the target task or defect references and read only the applicable `REQ-*`, `AC-*`, `DEC-*`, `UI-*`, `CTR-*`, recent `CHG-*`, verification events, code, and tests. Expand to adjacent sections only when a dependency, contradiction, or safety boundary requires it.

Use heading/ID search rather than reading large artifacts from start to finish. Never load full `history/`, all sealed baseline entries, all completed tasks, or entire append-only ledgers for ordinary implementation. Expand into cold history only for baseline recovery, authority conflict, chronology dispute, regression investigation, or an explicit user audit request. If the bounded context cannot be formed without broad reading, stop expanding and recommend documentation consolidation. If current metadata disagrees about the active vector or target, stop implementation and report the inconsistency.

Classify inputs as `confirmed`, `observed`, `assumption`, `candidate`, `open_question`, or `risk`. Old tests and prototypes establish history or feasibility, not current completion evidence.

## Choose the requested action

Do not collapse these actions without authorization.

### Inspect

Inspect read-only and report the project map, current/partial/unverified capabilities, research decisions and candidates, contradictions, risks, SDD compatibility, and likely alignment topics. If legacy artifacts exist, classify the likely migration as `compatible`, `bootstrap`, `consolidate`, or `blocked`; do not migrate.

### Align

Present a compact snapshot of goal, users, observable loop, scope, non-goals, constraints, success criteria, assumptions, and sources. Ask only decisions that can change scope, permissions, security/data boundaries, external contracts, feasibility, UI authority/fidelity, or acceptance, with at most three primary decisions per turn.

When UI signals exist, classify the current requirement as UI-0, UI-1, or UI-2 using [UI governance](references/ui-governance.md) and state the evidence. Do not infer a UI deliverable when the requirement omits UI; if the loop technically requires a UI change, flag it for scope confirmation.

Do not draft a Spec unless requested.

### Draft and confirm the initial Spec

Create or update the single `docs/sdd/spec.md`. Keep candidates and deferred ideas out of MUST requirements. An open question affecting goal, security/data/UI authority, external contract, or acceptance blocks confirmation.

Mark the draft with its proposed version and provide exact confirmation wording such as `确认 Spec v0.1`. On valid confirmation:

1. record confirmation metadata without adding requirements;
2. run the `pre_publish` Spec checks from [artifact audit](references/artifact-audit.md);
3. only on pass, publish an identical immutable copy at `history/specs/spec-v0.1.md`;
4. preserve requirement and acceptance IDs across revisions; never silently reuse an ID for different semantics.

Spec confirmation alone does not authorize implementation or imply that a complete baseline exists.

### Design, UI, contracts, and plan

After Spec confirmation, update the single current `design.md`, optional project-level `ui.md` for UI-2, relevant stable-boundary contracts, and `tasks.md`. Every material decision, UI rule, contract, and task traces to applicable `REQ-*` or `AC-*`.

- Publish a Design, UI, or Contract revision only after its `pre_publish` audit passes and it is accepted or implementation is explicitly authorized against it.
- Do not publish drafts merely because a version label was proposed.
- Snapshot Tasks only while sealing a baseline, not for every checkbox edit.
- Run Gate A before sealing; a failed Gate A leaves the candidate working set pending and blocks publication of remaining candidate revisions and `BL-*` sealing.
- On pass, publish audited candidates, snapshot Tasks, append the immutable baseline vector, and update the current summary.

### Propose and materialize changes

After a confirmed Spec exists, record material semantic proposals in `changes.md` before altering confirmed requirements, design, UI, or contracts. Each `CHG-*` identifies the source baseline, proposed target versions, exact old-to-new semantics, affected IDs/artifacts, risks, and verification impact.

Keep the latest proposal as one self-contained effective snapshot; older proposal events are cold deltas. After two self-review rounds, classify new findings as current behavior/security blockers, implementation detail, or deferred risk. Do not keep adding persistence, state, recovery, DTO, migration, or governance machinery for hypothetical cases unless confirmed user-visible behavior, a safety boundary, or acceptance evidence requires it. If mechanism grows without adding product capability or retiring a demonstrated risk, simplify the proposal. Wording, formatting, and non-semantic clarification do not create a new proposal revision; only an effective semantic snapshot or version-vector change does.

Classify before confirmation:

- goal, scope, observable behavior, requirement, acceptance, user flow, interaction meaning, visible permission behavior, or authoritative UI behavior: bump Spec and affected artifacts;
- implementation approach only: revise Design without bumping Spec;
- visual/layout contract only with no behavioral change: revise UI only, and Design only if architecture changes;
- contract semantics only with no product behavior change: bump affected Contracts and revise Design if needed;
- task ordering/status only: revise Tasks only;
- typo, formatting, or link repair with no semantic effect: append a non-material note; no published version required.

Request exact confirmation such as `确认 CHG-004，将 Spec 从 v0.3 更新到 v0.4`. On confirmation:

1. update the mutable change summary and append a confirmation event; do not implement unless separately authorized;
2. materialize only the confirmed delta into candidate current artifacts and keep the `CHG-*` pending;
3. run `pre_publish` checks and Gate A before immutable publication;
4. on failure, report blockers and keep the last sealed baseline active;
5. on pass, publish changed revisions, reuse unchanged revisions, snapshot Tasks, and seal the new baseline;
6. append the materialization event and update summaries.

Verification evidence remains historically valid for the baseline and implementation reference it originally proved. A new working state requires new evidence; do not rewrite an earlier PASS as a FAIL or erase it.

### Migrate legacy artifacts

When migration is requested, follow [legacy migration](references/legacy-migration.md): inventory read-only, classify, propose an explicit `MIG-*` mapping and recovery coverage, then wait for migration authorization. Preserve legacy evidence, do not invent history, separate semantic conflicts into `CHG-*`, and run Gate A before sealing the imported baseline. Migration does not authorize code changes.

### Consolidate documentation

When a compatible project needs only Contract splitting, Tasks compaction, indexes, or cold-history boundaries, follow [documentation consolidation](references/documentation-consolidation.md). Inspect and propose the exact structural scope first; do not edit until the user explicitly authorizes it. Preserve semantics, immutable history, and sealed-baseline recovery. Do not bump Spec for structural cleanup, and run Gate A only when the published vector or authoritative references change. This action never authorizes code changes.

### Maintain or fix defects

Follow [maintenance and context loading](references/maintenance-and-context.md).

When the active sealed baseline unambiguously defines the expected behavior and implementation deviates:

1. bind the repair to that baseline and the smallest relevant IDs;
2. reproduce and diagnose against current code and tests;
3. implement the smallest conforming repair and add or strengthen regression evidence;
4. run focused checks proportional to the affected boundary;
5. append one compact verification event only when the project actively uses the ledger or the user requests durable evidence.

Do not create `CHG-*`, bump Spec/Design/UI/Contracts, snapshot Tasks, seal a new baseline, or run Gate A for a pure conformance fix. Do not create a new `TASK-*` for a trivial repair; use one when coordination, dependencies, ownership, or multi-stage verification benefit from it. A durable cross-cutting design change, contract correction, or observable behavior change exits this lane and follows the applicable planning or semantic-change path.

### Implement

Modify code only after explicit implementation authorization. Verify the target baseline is sealed and current, inspect workspace changes, identify the bounded task or repair, and ensure no unresolved material decision blocks work. Construct a small runtime implementation packet containing the baseline, target task/defect, referenced IDs, affected ownership/files, required checks, and exclusions; do not require a new `implementation-packet.md`. Read only that packet's referenced artifact sections, then prioritize current code, executable schemas, tests, and observed failures over unrelated documentation. Implement the smallest useful vertical result and keep Tasks truthful when a task exists.

When parallel work is explicitly authorized, freeze shared contracts and foundational types first. Parallelize only dependency-ready tasks with non-overlapping write ownership; integrate and verify after prerequisites complete.

### Verify and finish

Choose the verification level from [maintenance and context loading](references/maintenance-and-context.md): focused repair/task checks, affected-boundary regression, or full baseline verification. Append factual events bound to one `BL-*`, implementation reference, environment, and time when durable evidence is required. Mocks do not prove a required real external loop.

Map only the affected `AC-*` for focused task or repair verification. Map every active `AC-*` and run Gate B from [artifact audit](references/artifact-audit.md) only when the user requests full baseline verification, release/readiness assessment, or a claim that the whole baseline is implemented. A focused PASS does not make the baseline `verified`; an outstanding unrelated acceptance item does not turn a correctly completed bounded task into a failed task.

### Restore or compare a baseline

Resolve its exact vector from the immutable baseline ledger, then run Gate C from [artifact audit](references/artifact-audit.md). Load only the matching immutable history files. Never infer missing revisions from later current files; report absent/inconsistent mappings as recoverability defects.

Restoring SDD artifacts is not the same as reproducing code. Behavioral reproduction additionally needs referenced machine-readable contracts, dependency locks, migrations, configuration examples, fixtures, startup/deployment instructions, and executable acceptance tests.

## Stable traceability

Maintain where applicable:

```text
CHG-* / MIG-* → BL-* → REQ-* / AC-* → DEC-* / UI-* / CTR-* → TASK-* → VER-*
```

- Preserve stable IDs while semantics remain the same.
- Use explicit old-to-new mappings, `replaces`, or `supersedes` when semantics change.
- A sealed baseline vector and ledger entry are immutable. Corrections append a superseding baseline; only current summaries change in place.
- Reuse unchanged artifact revisions across baselines.
- Current artifacts declare their own versions; `baselines.md` declares which revisions compose each system state.

## Escalate proportionally

Continue Lite when work consumes existing confirmed boundaries. Pause and recommend strict `$sdd`, or ask the user to choose stronger governance, when the work creates or materially changes identity/authorization/privacy boundaries, irreversible production data operations, payments or ledgers, long-lived credential scope, public compatibility commitments, authoritative data ownership, or formal multi-party approvals. State the exact trigger and scope.

## Artifact economy

The standard current set is Spec, Design, stable-boundary Contracts when needed, Tasks, Verification, Changes, and Baselines. Add one project-level UI artifact only for UI-2 or when an existing baseline already uses it. Historical copies exist only for published revisions, task checkpoints, and authorized legacy preservation.

Artifact size is a routing and maintenance signal, not a semantic correctness gate. Apply the overridable advisory thresholds in [maintenance and context loading](references/maintenance-and-context.md). When ordinary implementation requires reading extensive historical prose before relevant code, reduce the hot path without deleting history. Structural cleanup of existing authoritative artifacts follows [documentation consolidation](references/documentation-consolidation.md), requires explicit authorization, and must not rewrite append-only history or silently enter an implementation task.

Do not create per-feature artifact suites, a Manifest, hashes, question registry, amendment directory, review dossiers, a separate audit document, or per-task evidence directories. Use strict SDD when formal identity or approval chains are required.
