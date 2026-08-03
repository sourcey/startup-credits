# Contributing

Normal pull requests add or update one or more files under
`vendors/{shard}/`.

The shard is the first two characters of the vendor slug (or the whole slug
when it is shorter), and the filename is exactly `{slug}.yaml`; CI verifies
that identity-derived path.

Keep a data pull request data-only; do not mix vendor YAML with documentation or workflow edits.
For a new record, copy a nearby vendor file and preserve the shape:

- allocate fresh ULIDs with the existing `ent_`, `prg_`, and `off_` prefixes; never reuse an ID;
- use one opaque, stable file-local `source_id` for each public URL and reference it from the
  Programs and Offers it supports; a `source_id` does not encode or hash its URL;
- add a Program only when the vendor publicly names a real umbrella program; standalone Offers do
  not need one; and
- keep separate Offers for materially different economics, eligibility, duration, access, or
  terms. Do not split one application bundle into a card per benefit.
- Keep the vendor `description` to 200 characters and describe the vendor itself, not its offers.
- Keep each `summary` to 240 characters: it is the compact public synopsis used in listings and
  metadata. An Offer may use optional `description` for longer source-backed context. Economics,
  eligibility, and access still belong in their structured fields rather than repeated prose.

Generate fresh IDs with Node's built-in crypto support. The first command prints one Entity,
Program, and Offer ID; use only the IDs the record needs and rerun it for additional Offers.

```bash
node -e 'const{randomBytes}=require("node:crypto"),a="0123456789abcdefghjkmnpqrstvwxyz",e=(n,l)=>{let s="";while(l--)s=a[Number(n&31n)]+s,n>>=5n;return s},u=()=>e(BigInt(Date.now()),10)+e(BigInt("0x"+randomBytes(10).toString("hex")),16);for(const p of ["ent_","prg_","off_"])console.log(p+u())'
node -e 'console.log("src_"+require("node:crypto").randomBytes(32).toString("hex"))'
```

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

Before starting a new vendor, search the
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

The repository's `validate` check validates only the changed dependency closure
through the exact digest-pinned Sourcey Candidate Verifier and enforces the DCO.
It starts automatically when a pull request is opened or updated. A green `validate`
check means the submitted tree is structurally and semantically valid; contributors can
push corrections to the same branch and receive a fresh result without maintainer review.
External contributors do not need direct repository write access: GitHub may create a fork as the
source of their pull request, and subsequent pushes to that same source branch update it normally.
Sourcey's separate required `sourcey/admission` check proves that private,
replayable evidence and authority were admitted for the exact pull-request Git
tree; contributors never upload that private material. Once both checks pass and
the pull request is merged, publication and live activation are automatic.

For an exact local preflight, run this from a checkout with `origin/main` fetched:

```bash
base="$(git merge-base HEAD origin/main)"
digest="$(<.github/sourcey-candidate-verifier.sha256)"
work="$(mktemp -d)"
archive="sourcey-candidate-verifier-sha256-${digest}.tar.gz"
curl --fail --silent --show-error \
  "https://artifacts.sourcey.com/catalog/code/candidate-verifier/sha256-${digest}/${archive}" \
  --output "${work}/${archive}"
curl --fail --silent --show-error \
  "https://artifacts.sourcey.com/catalog/code/candidate-verifier/sha256-${digest}/${archive}.sha256" \
  --output "${work}/${archive}.sha256"
(cd "${work}" && shasum -a 256 --check "${archive}.sha256")
mkdir "${work}/verifier"
tar -xzf "${work}/${archive}" --strip-components=1 -C "${work}/verifier"
node "${work}/verifier/sourcey-candidate-verifier.js" \
  validate-change --repository "$PWD" --base "${base}" --head HEAD
rm -rf "${work}"
```

This is the same pinned executable used by CI, not a second validator.
