# SDD Lite documentation consolidation

Read this reference only to propose or perform a structural cleanup of authoritative SDD Lite artifacts. This path reduces hot context without changing approved product semantics and without authorizing implementation.

## Boundaries

- Treat size thresholds from [maintenance and context loading](maintenance-and-context.md) as advisory warnings; project-specific overrides are allowed.
- Obtain explicit user authorization for the exact structural write scope before editing.
- Do not bump Spec, Design, UI, or Contract semantics for formatting, indexing, splitting, or compaction alone.
- Never delete, rewrite, or resequence append-only ledger events or immutable history files.
- Preserve stable IDs, current versions, confirmations, exact baseline recovery, and old-to-new path mappings.
- Separate any discovered semantic disagreement into alignment or `CHG-*`; do not resolve it as cleanup.

## Allowed consolidation

- Split a combined Contract by existing stable boundaries into `contracts/index.md` and one current effective file per Contract.
- Compact `tasks.md` so ready, active, and blocked tasks retain full definitions while older completed task bodies become index rows linked to existing immutable task snapshots.
- Remove superseded prose from a current Design while retaining one-line `replaces`/migration links to immutable revisions.
- Reduce mutable ledger summaries to active, pending, direct predecessor, and recent relevant events.
- Add indexes, stable headings, path mappings, and the cold-history boundary: `Cold history — ordinary implementation must not load this section`.

Do not copy all unchanged Contract revisions when sealing a later baseline. `contracts/index.md` records the current version vector, ownership, file, consumers, and requirement/acceptance trace; the baseline reuses each unchanged immutable Contract revision.

## Flow

1. Inspect headings, indexes, sizes, current vector, and exact target sections read-only; do not begin by reading every ledger event.
2. Report the consolidation candidates, intended paths, preserved history, mapping, expected hot-context reduction, and exact write scope.
3. Wait for explicit authorization such as `授权 documentation_consolidation，范围：...`.
4. Apply structural changes without changing normative sentences or stable-ID meanings. Keep the last sealed baseline recoverable throughout.
5. Record the result as one compact maintenance/migration event in the existing `changes.md` ledger, including authorization, mapping, semantic-change result (`none`), and affected authoritative references. Do not create a new governance document.
6. Run targeted reference/path checks. Run Gate A only when the published version vector or authoritative references change; mere line movement, index addition, or hot-summary compaction does not trigger it.

If exact semantic preservation cannot be demonstrated, stop the consolidation and report the conflicting IDs or definitions. Do not choose which definition is current.
