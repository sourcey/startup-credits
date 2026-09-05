# Contributing

Normal pull requests add or update one or more files under
`entities/{shard}/`.

The shard is the first two characters of the Entity slug (or the whole slug
when it is shorter), and the filename is exactly `{slug}.yaml`; CI verifies
that identity-derived path.

Keep a data pull request data-only; do not mix Entity YAML with documentation or workflow edits.
For a new record, copy a nearby Entity file and preserve the shape:

- allocate fresh ULIDs with the existing `ent_`, `prg_`, and `off_` prefixes; never reuse an ID;
- use one opaque, stable file-local `source_id` for each public URL and reference it from the
  Programs and Offers it supports; a `source_id` does not encode or hash its URL;
- add a Program only when the Entity publicly names a real umbrella program; standalone Offers do
  not need one; and
- keep separate Offers for materially different economics, eligibility, duration, access, or
  terms. Do not split one application bundle into a card per benefit.
- Use only a category from the exact `taxonomy.json` bundled with the pinned Catalog Verifier.
  The local preflight downloads that file, and both local and CI failures print the complete
  current list; a nearby legacy record is not taxonomy authority.
- Give every Entity a `profile.summary`: one or two plain sentences about what the company does.
  Machine admission requires it; a submission without it is asked to add one.
- Keep `profile.description` to 200 characters and describe the Entity itself, not its Offers.
- Keep each `summary` (`profile.summary` and every Offer `summary`) to 240 characters: it is the
  compact public synopsis used in listings and metadata. An Offer may use optional `description` for longer source-backed context. Economics,
  eligibility, and access still belong in their structured fields rather than repeated prose.

Generate fresh IDs with Node's built-in crypto support. The first command prints one Entity,
Program, and Offer ID; use only the IDs the record needs and rerun it for additional Offers.

```bash
node -e 'const{randomBytes}=require("node:crypto"),a="0123456789abcdefghjkmnpqrstvwxyz",e=(n,l)=>{let s="";while(l--)s=a[Number(n&31n)]+s,n>>=5n;return s},u=()=>e(BigInt(Date.now()),10)+e(BigInt("0x"+randomBytes(10).toString("hex")),16);for(const p of ["ent_","prg_","off_"])console.log(p+u())'
node -e 'console.log("src_"+require("node:crypto").randomBytes(32).toString("hex"))'
```

- Describe only public vendor, program, and offer facts supported by the URLs
  in the record.
- Cite only canonical sources: pages published by the party that controls the
  fact. Vendor facts and vendor-run offers cite the vendor's own domains. A
  page on any other host counts only when that host belongs to an entity the
  offer's `roles` name, which is the channel-operator case: a perks platform's
  own page is canonical for a perk that platform grants to its members, and the
  record then names that platform as `access_operator_entity_id` and models the
  membership in `eligibility` and `access`. Directory and aggregator listings
  that describe someone else's program are never evidence; admission ignores
  them entirely, and a subject whose only sources are such listings is
  rejected before review. Do not name a role-holder the party does not
  actually hold: evidence review checks that the cited operator page shows the
  operator granting or gating the offer, not merely describing it.
- Keep stable IDs stable. Correct or end an offer instead of deleting its
  history.
- Do not claim Sourcey verification, vendor signatures, freshness, or
  provenance tiers in YAML. Declared offers (vendor-signed offers with no
  public source) are a hosted vendor-authority lane, never a contribution;
  every offer in this repository carries `source_ids`. Sourcey's
  independent evidence and authority
  pipeline derives those properties.
- Do not add executable code, schemas, generated output, evidence objects,
  scanner state, package files, or release controls.
- Sign off commits using `Signed-off-by: Name <email>` to certify the
  [Developer Certificate of Origin](https://developercertificate.org/).

## What evidence review checks

The public `sourcey/validation` status proves the YAML shape and changed identity closure. Sourcey's separate
admission result then checks the submitted facts against the record's public source URLs:

- published economics, eligibility, lifecycle, domains, links, and access facts must be supported
  by cited source material;
- support only counts from canonical sources: the vendor's own domains, or the domains of an
  entity the offer's `roles` name. Text on any other host is ignored no matter how well it
  matches, and the failure names the ignored hosts;
- Sourcey-written titles, summaries, descriptions, and taxonomy labels may faithfully paraphrase
  those cited facts and do not need to appear verbatim on the vendor page;
- opaque Sourcey IDs and canonical encodings such as money units are not expected to appear in
  vendor copy, but the real actor or value they encode must be supported; and
- Sourcey-owned metadata such as capture time and internal criterion IDs is not treated as a claim
  the vendor published.

If admission cannot cover a submitted fact, its result names the uncovered field and explains what
evidence is accepted. Correct the YAML or cite a better public source on the same pull request; do
not rewrite a supported fact merely to make it match a source sentence word for word.

Before starting a new Entity, search the
[open pull requests](https://github.com/sourcey/startup-credits/pulls) and
[missing-record issues](https://github.com/sourcey/startup-credits/issues?q=is%3Aissue+is%3Aopen).
If it is not already covered, open a missing-record issue and comment there before doing the work;
that issue is the lightweight reservation surface.

If DCO fails only on the latest commit, add the sign-off and update the same pull request:

```bash
git commit --amend --no-edit --signoff
git push --force-with-lease
```

If several commits need sign-off, rebase them and then update the same branch:

```bash
git fetch origin
git rebase --signoff origin/main
git push --force-with-lease
```

The repository's `sourcey/validation` status validates only the changed dependency closure
through the exact lockfile-pinned public `@sourcey/catalog-verifier` package and enforces the DCO.
It starts automatically when a pull request is opened or updated. A green `sourcey/validation`
status means the submitted tree passed the deterministic public structure, closure, and DCO
rules. It does not claim the submitted facts are true. Contributors can push corrections to the
same branch and receive a fresh result without maintainer review.
External contributors do not need direct repository write access: GitHub may create a fork as the
source of their pull request, and subsequent pushes to that same source branch update it normally.
Sourcey's separate required `sourcey/admission` check proves that private,
replayable evidence and authority were admitted for the exact pull-request Git
tree; contributors never upload that private material. Once both statuses pass and
the pull request is merged, publication and live activation are automatic.

For an exact local preflight, run this from a checkout with `origin/main` fetched:

```bash
base="$(git merge-base HEAD origin/main)"
work="$(mktemp -d)"
npm ci --prefix .github/catalog-verifier --ignore-scripts --no-audit --no-fund
verifier=".github/catalog-verifier/node_modules/.bin/sourcey-catalog-verify"
taxonomy=".github/catalog-verifier/node_modules/@sourcey/catalog-verifier/taxonomy.json"
curl --fail-with-body --silent --show-error https://api.sourcey.com/v1/release \
  --output "${work}/release.json"
release_id="$(jq -er '.release_id' "${work}/release.json")"
root_digest="$(<.github/sourcey-root-set.digest)"
test "$(jq -er '.descriptor.snapshot_core.root_set_digest' "${work}/release.json")" = "$root_digest"
"$verifier" identity-context-request startup-credits \
  --repository "$PWD" --base "$base" --head HEAD --taxonomy "$taxonomy" \
  --live-parent-release-id "$release_id" > "${work}/query.json"
curl --fail-with-body --silent --show-error -H 'content-type: application/json' \
  --data-binary @"${work}/query.json" \
  https://api.sourcey.com/v1/catalog-verifier/identity-contexts \
  | jq -e '.data' > "${work}/identity-context.json"
"$verifier" validate startup-credits \
  --repository "$PWD" --base "$base" --head HEAD --taxonomy "$taxonomy" \
  --identity-context "${work}/identity-context.json" \
  --root-set .github/sourcey-root-set.json --trusted-root-digest "$root_digest" \
  --verified-at "$(node -p 'new Date().toISOString()')" --format human
```

This is the same public npm package, signed identity-context protocol, and rooted trust input used
by CI—not a second validator. The command makes its one network-dependent context issuance explicit;
the final validation is offline over the saved bytes.
