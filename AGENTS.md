## Owner correction, 30 September 2026

Before selecting work, state the whole user or customer job and the useful result needed. For paid products, say who buys and why. Find the missing behaviour that prevents that result, and prioritise it. A narrow feature, polished screen or passing test count does not prove that the product is useful or complete. Keep the original product promise and the owner's chosen design sources visible while building and verifying the actual journey.

Use dated evidence about intended users, their current setups and the likely release date. Where compatibility matters, a supported minimum is a regression boundary, not the primary development target. Choose this product's current versions with the highest relevant adoption first, then relevant adjacent release series, and then its declared minimum. Check actual version compatibility and lifecycle support against the launch horizon and user environments before choosing or retaining a minimum.

Never borrow version numbers or compatibility floors from another product. Separate public adoption statistics from actual user and buyer evidence. Separate distributions for different platforms do not establish a combined customer cohort. Do not invent coverage, multiply separate shares into a market claim, or claim unexecuted compatibility. Record missing or stale evidence and untested target versions as open release gates.

This correction governs prioritisation and evidence within this repository's authorised scope. Existing scope, approval, privacy, managed instruction blocks and writing rules still apply. Preserve those rules, including any Lovable block, restrictions on exposing tool traces and restrictions on dashes in copy.

# Repository boundary

This is `sourcey/startup-credits`: the thin public YAML contribution
repository. “Startup Credits” is only this GitHub repository's name.

Allowed:

- `entities/**/*.yaml`;
- concise contributor, legal, and repository-boundary documentation; and
- minimal GitHub metadata and YAML workflows that invoke digest-pinned tools
  owned by the private Sourcey workspace.

Forbidden:

- executable code, packages, applications, scripts, CLIs, tests, fixtures, or
  build systems;
- contracts, schemas, OpenAPI/MCP generators, scanners, evidence operations,
  captures, trust material, authority objects, prompts, source inventories, or
  internal state;
- generated catalog or release snapshots, manual live selectors, compatibility
  layers, shims, duplicated definitions, or consumer-specific copies; and
- semantic-version changes, `v2` shapes, or product/package naming decisions
  without Kam's explicit approval.

Pull-request CI processes only changed Entity files and their exact identity
dependency closure. It must never rebuild the full catalog. Merge is the sole
human activation and every live surface advances from the same resulting live
head.

The public `sourcey/validation` status must start automatically for an opened or updated
data pull request, use the exact digest-pinned workspace-owned verifier, and
return actionable field errors before private review. `sourcey/admission` is a
separate Sourcey-owned evidence gate and never contributor-authored work.

Evidence review is semantic, not a verbatim-copy test. Published factual values
need located source support; neutral Sourcey titles, summaries, descriptions,
and taxonomy classifications may faithfully express cited facts in different
words. Sourcey-owned IDs, encodings, and capture metadata are not claims that a
vendor page must literally contain. The private Catalog policy and evaluator
are the sole authority for that distinction; this repository does not restate
or implement it.

`entities/` is the only public data collection. Programs and Offers are nested
in their owning Entity document; repository evidence remains in that same
document but outside the shared `entity` envelope. Do not add a generic
`data/` wrapper or another top-level collection unless Kam explicitly approves
a genuinely independent public authoring surface.
