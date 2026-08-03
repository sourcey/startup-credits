# Repository boundary

This is `sourcey/startup-credits`: the thin public YAML contribution
repository. “Startup Credits” is only this GitHub repository's name.

Allowed:

- `vendors/**/*.yaml`;
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

Pull-request CI processes only changed vendor files and their exact identity
dependency closure. It must never rebuild the full catalog. Merge is the sole
human activation and every live surface advances from the same resulting live
head.

The public `validate` check must start automatically for an opened or updated
data pull request, use the exact digest-pinned workspace-owned verifier, and
return actionable field errors before private review. `sourcey/admission` is a
separate Sourcey-owned evidence gate and never contributor-authored work.

`vendors/` is the only public data collection. Offers, programs, links, and
sources are nested in their owning vendor document. Do not add a generic
`data/` wrapper or another top-level collection unless Kam explicitly approves
a genuinely independent public authoring surface.
