# SDD Lite UI governance

Read this reference when the requirement mentions a page, screen, interface, visual behavior, interaction, or UI, when a prototype/design/reference is supplied, or when an existing baseline already contains `ui.md`.

## Classify the current requirement, not the whole project

Use two signals:

1. Does the current requirement explicitly include UI behavior or a UI deliverable?
2. Does it provide or invoke a prototype, design file, screenshot, reference product, design system, or visual-fidelity acceptance?

Classify:

- `UI-0`: no UI scope and no relevant authoritative reference. Do not invent a UI deliverable or visual redesign.
- `UI-1`: UI behavior is in scope, but no authoritative visual reference or independent fidelity target exists. Put observable UI behavior in `spec.md` and implementation structure in `design.md`; normally do not create `ui.md`.
- `UI-2`: UI is in scope and a relevant prototype/design/reference or explicit visual-fidelity requirement exists. Create or update the single project-level `ui.md`, version it independently, archive published revisions, and include it in baselines.

If a reference is present but its relevance or authority is unclear, classify it as a candidate/open question. Distinguish `must match`, `directional reference`, and `exploration only`; a reference never silently overrides a confirmed Spec.

If UI is not mentioned but completing the requested observable loop appears to require a UI change, report the dependency and ask whether UI is in scope. Do not silently expand the work. Explicit user direction overrides the default classification.

An existing `ui.md` remains part of the system view. A later `UI-0` change reuses its current revision rather than deleting it or forcing a new UI revision.

## Where UI information belongs

### UI-1

- `spec.md`: actors, observable flows, controls and results, permission behavior, loading/empty/error/denied states, and required responsive/accessibility outcomes.
- `design.md`: routes, information architecture, state ownership, frontend component boundaries, design-system use, and API/permission integration.
- `tasks.md`: verifiable vertical user flows, not isolated styling paperwork.
- `verification.md`: E2E behavior and required UI states.

### UI-2

Use the same coverage plus one current `ui.md` containing the exact visual/interaction contract that would otherwise overload Design. Do not create one UI file per feature or change.

Default history path: `history/ui/ui-rN.md`. Baseline vectors include `ui: rN`; unchanged revisions are reused.

## UI semantic version rules

- User flow, interaction meaning, visible permission behavior, information architecture, or acceptance behavior changes: create `CHG-*`, bump Spec, and revise UI.
- Visual layout, component composition, or design-system treatment changes without behavior change: revise UI; revise Design only when architecture changes; do not bump Spec.
- Copy changes that alter business meaning or acceptance: bump Spec. Cosmetic copy corrections do not.
- API or error-model changes: revise applicable Contracts and verify UI state handling.
- UI implementation refactors with no visible/design-contract change: no UI revision.

## UI checks in artifact audits

### Gate A

- Every UI-scoped `REQ-*` and `AC-*` maps to a flow, screen/route, and required state.
- Role/action visibility matches backend authorization; the UI is not the authority for access control.
- Success, loading, empty, validation, error, denied, cancellation/retry, and destructive confirmation states are covered when applicable.
- UI references have stated authority and durable repository paths when exact restoration matters.
- Responsive, accessibility, localization, and design-system constraints are explicit when required.
- The baseline names the correct UI revision and immutable path for UI-2.

### Gate B

- Required user flows pass against the target baseline and implementation reference.
- Visual comparison is used only when fidelity is required, with reference, viewport, and result recorded.
- Required responsive viewports, keyboard paths, accessibility checks, permission states, and real API failures are evidenced.

### Gate C

- The historical UI revision and referenced local assets exist.
- The UI revision matches the baseline vector and retains its requirement/acceptance trace.
- Missing external-only references are reported as a recoverability limitation.

## `ui.md` template

````markdown
# UI Design

> Classification: UI-2
> Revision: r1
> Spec: v0.1
> Published at: <ISO 8601 or blank>

## Reference authority

| Reference | Authority | Durable source | Scope |
|---|---|---|---|
| <prototype/design/screenshot> | must_match / directional / exploration | <repository path or limitation> | <screens/flows> |

## Routes, screens, and flows

| ID | Route/screen | Actor | Purpose | Trace |
|---|---|---|---|---|
| UI-001 | <route/screen> | <role> | <observable outcome> | REQ-001 / AC-001 |

## State matrix

| Surface | Success | Loading | Empty | Error | Denied | Other required state |
|---|---|---|---|---|---|---|
| UI-001 | <state> | <state> | <state> | <state> | <state> | <retry/cancel/etc.> |

## Interaction and permission rules

<Navigation, actions, validation, destructive confirmation, focus/keyboard behavior, and the backend authority enforcing permissions.>

## Visual and responsive constraints

<Design system, tokens, layout, breakpoints/viewports, accessibility, localization, and required fidelity.>

## Component and data boundaries

<Component/state ownership and links to applicable `DEC-*` and `CTR-*`.>

## Verification references

<E2E, visual comparison, responsive, and accessibility tests or routes.>

## Revision notes

- r1 — <initial definition or CHG reference>
````

Do not copy restricted external design assets without authorization. When an exact local snapshot is unavailable, record the external reference and the resulting restoration limitation rather than claiming exact visual recoverability.
