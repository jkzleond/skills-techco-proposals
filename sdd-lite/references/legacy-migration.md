# SDD Lite legacy artifact migration

Read this reference when existing SDD artifacts do not follow the current integrated-view, ledger, history, and baseline model. Migration is a documentation operation, not implementation authorization.

If the project already follows that model and only needs Contract splitting, Tasks compaction, indexing, or cold-history boundaries, use [documentation consolidation](documentation-consolidation.md) instead of legacy migration.

## Start read-only

Inventory before writing:

- artifact roots and competing conventions;
- Spec/Design/Contract/Task/Verification files and their stated versions/statuses;
- explicit confirmations and version relationships;
- per-feature or per-increment artifact suites;
- oversized hot artifacts, repeated historical prose in current views, and combined contracts that prevent task-scoped loading;
- auxiliary documents whose authority or last validated baseline is unclear;
- current code/tests and research that can establish observed facts but not approved intent;
- missing history, conflicting semantics, ambiguous current versions, and broken references;
- existing UI artifacts, prototypes, screenshots, and the authority assigned to them.

Classify the project:

- `compatible`: already follows the current model; audit only;
- `bootstrap`: one integrated current set exists but ledgers/history/baseline are missing;
- `consolidate`: multiple increment or feature sets must be resolved into one current system view;
- `blocked`: the effective requirements or authority cannot be determined without user decisions.

Report the classification, proposed target paths, semantic conflicts, expected recovery coverage, and exact write scope. Do not migrate until the user explicitly requests or approves the migration.

## Migration invariants

- Copy or preserve original artifacts before normalizing them; do not delete or overwrite legacy evidence.
- Store preserved imports under `history/legacy/<MIG-ID>/` when a durable local copy is authorized and needed. Otherwise keep stable links to their original paths.
- A format, directory, ID-mapping, or ledger migration does not bump the Spec, Design, UI, or Contract version when semantics are unchanged.
- Splitting a combined Contract by existing stable boundaries, compacting derived summaries, or moving already snapshotted completed-task detail out of the hot view is structural when content and IDs remain identical. Preserve an explicit mapping and do not rewrite append-only events.
- Preserve reliable versions, confirmations, timestamps, stable IDs, and source paths.
- Do not invent missing confirmation, chronology, versions, or historical snapshots.
- Observed code behavior cannot silently resolve conflicts between confirmed requirements.
- Any semantic change discovered during migration becomes a separate `CHG-*` proposal and follows normal confirmation.
- If confirmation of the imported Spec cannot be established, mark it `imported-unconfirmed`; request confirmation before sealing a confirmed baseline.
- Migration never authorizes code changes.

## Recovery coverage

Declare the honest result:

```yaml
recovery_coverage:
  current_baseline: full | partial | unavailable
  historical_baselines: full | partial | unavailable
  recovery_starts_at: BL-001 | unknown
  known_gaps:
    - <missing or ambiguous artifact/version>
```

`full` requires exact artifact files and a complete version vector. If only the current state survives, state that exact restoration begins at the imported baseline; do not claim earlier baselines are recoverable.

## Migration flow

1. Reserve a `MIG-*` ID and append a proposed migration record to `changes.md` without treating it as a product change.
2. Preserve legacy originals or stable references.
3. Build the candidate integrated current view: one Spec, one Design, stable-boundary Contracts, optional UI, one Tasks view, and ledgers.
4. Create an explicit old-path/old-ID to new-path/new-ID mapping.
5. Resolve structural conflicts directly; return semantic conflicts to alignment.
6. Run Gate A from [artifact audit](artifact-audit.md).
7. On pass, publish the recoverable revisions, seal the bootstrap baseline, and append the `materialized` migration event.

## `MIG-*` record template

Add migration records to the append-only ledger in `changes.md`; include them in its mutable summary.

```markdown
## MIG-001 — Import legacy SDD artifacts

> Proposed at: <ISO 8601>
> Source layout: <paths/convention>
> Target layout: docs/sdd

### Classification and scope

- Classification: compatible | bootstrap | consolidate | blocked
- Semantic change intended: no
- Preserved originals: <paths>

### Mapping

| Legacy artifact or ID | Current artifact or ID | Confidence | Note |
|---|---|---|---|
| <old path/ID> | <new path/ID> | confirmed / observed / uncertain | <reason> |

### Recovery coverage

<Coverage block and known gaps.>

### Event history

- MIG-001-E01 — `<time>` — `proposed`; scope: <summary>
- MIG-001-E02 — `<time>` — `authorized`; exact text: `<authorization>`
- MIG-001-E03 — `<time>` — `audited`; Gate A: VER-014 passed
- MIG-001-E04 — `<time>` — `materialized`; result baseline: BL-001
```

Correct a migration record with a later event or superseding `MIG-*`; never rewrite preserved legacy evidence or claim a broader recovery range than the files support.
