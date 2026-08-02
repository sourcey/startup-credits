# Contributing

Normal pull requests add or update one or more files under
`vendors/{shard}/`.

The shard is the first two characters of the vendor slug (or the whole slug
when it is shorter), and the filename is exactly `{slug}.yaml`; CI verifies
that identity-derived path.

Keep a data pull request data-only; do not mix vendor YAML with documentation or workflow edits.
For a new record, copy a nearby vendor file and preserve the shape:

- allocate fresh ULIDs with the existing `ent_`, `prg_`, and `off_` prefixes; never reuse an ID;
- use a stable file-local `source_id` for each public URL and reference it from the Programs and
  Offers it supports;
- add a Program only when the vendor publicly names a real umbrella program; standalone Offers do
  not need one; and
- keep separate Offers for materially different economics, eligibility, duration, access, or
  terms. Do not split one application bundle into a card per benefit.

- Describe only public vendor, program, and offer facts supported by the URLs
  in the record.
- Keep stable IDs stable. Correct or end an offer instead of deleting its
  history.
- Do not claim Sourcey verification, vendor signatures, freshness, or
  provenance tiers in YAML. Sourcey's independent evidence and authority
  pipeline derives those properties.
- Do not add executable code, schemas, generated output, evidence objects,
  scanner state, package files, or release controls.
- Sign off commits using `Signed-off-by: Name <email>` to certify the
  [Developer Certificate of Origin](https://developercertificate.org/).

The repository's `validate` check validates only the changed dependency closure
through the exact digest-pinned Sourcey Candidate Verifier and enforces the DCO.
Sourcey's separate required `sourcey/admission` check proves that private,
replayable evidence and authority were admitted for the exact pull-request Git
tree; contributors never upload that private material. Once both checks pass and
the pull request is merged, publication and live activation are automatic.
