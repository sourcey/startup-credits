<h1 align="center">Startup Credits</h1>

<p align="center">
  <b>The open registry of startup programs.</b><br>
  Every discount, credit scheme, and startup tier on one machine-readable record,
  each exact offer revision either observed and dated, or signed by the vendor with proof.
</p>

<p align="center">
  <a href="https://sourcey.com">sourcey.com</a> ·
  <a href="https://sourcey.com/catalog.json">catalog.json</a> ·
  <a href="https://sourcey.com/llms.txt">llms.txt</a> ·
  <a href="https://mcp.sourcey.com/mcp">MCP</a> ·
  <a href="https://api.sourcey.com/openapi.yml">API</a>
</p>

<p align="center">
  <!-- Counts are read live from the published release; nothing here is kept by hand. -->
  <img alt="vendors on record" src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fsourcey.com%2Fcatalog.json&query=%24.data.entities.length&label=vendors%20on%20record&style=flat-square&labelColor=1B1B1F&color=B35C00">
  <img alt="last change" src="https://img.shields.io/github/last-commit/sourcey/startup-credits?style=flat-square&labelColor=1B1B1F&color=3F3F46&label=last%20change">
  <img alt="changes per month" src="https://img.shields.io/github/commit-activity/m/sourcey/startup-credits?style=flat-square&labelColor=1B1B1F&color=3F3F46&label=changes%2Fmonth">
  <img alt="data licence CC BY 4.0" src="https://img.shields.io/badge/data-CC%20BY%204.0-1B1B1F?style=flat-square&labelColor=1B1B1F&color=3F3F46">
</p>

---

Every tool a company buys has two prices. The one on the pricing page, and the
one startups actually pay through discounts, credits, and vendor programs. The
second number is real and usually public, and it is scattered across a few
hundred vendor pages that nobody keeps track of.

This repository is where that record gets built. One readable YAML file per
vendor, reviewed in the open, published to an API that people and their agents
can both read for free.

## Grey means we read it, signed means the vendor vouches for it

A fact is worth more the closer it sits to its origin, so every record carries
its provenance on the surface.

| Tier | What it means | Price |
|---|---|---|
| **Observed** (grey) | We captured the vendor's public page, dated it, and recorded what it said. Second-hand, and labelled that way. | Free |
| **Signed** | A vendor with proven authority attested to that exact offer revision. | Free, because subjects correcting their own record is the point |
| **Verified** | An independent check passed against that exact revision, with a receipt and an expiry. | Costs money, so it exists only where a payer funds it |

Tiers are derived from immutable evidence. Nobody types one into a file. Change
a fact and you start a new revision, which carries forward neither the vendor's
attestation nor an old verification.

If it's not from the source, it's a rumor, and the record says which is which.

## Use the data

Free to read forever, for you and for your agents. There is no key to request
and no quota to run out of.

| Surface | URL |
|---|---|
| Full catalog | [`sourcey.com/catalog.json`](https://sourcey.com/catalog.json) |
| Change feed | [`sourcey.com/changes.ndjson`](https://sourcey.com/changes.ndjson) |
| Model-readable index | [`sourcey.com/llms.txt`](https://sourcey.com/llms.txt) |
| Agent guide | [`sourcey.com/SKILL.md`](https://sourcey.com/SKILL.md) |
| OpenAPI | [`api.sourcey.com/openapi.yml`](https://api.sourcey.com/openapi.yml) |
| MCP | [`mcp.sourcey.com/mcp`](https://mcp.sourcey.com/mcp) |

Every entity, program, and offer carries a stable ID and a `revision_digest`, so
you can cite one exact version of one exact fact and have the citation still mean
something a year later when the offer has moved.

**Training on this is welcome.** It is published to be read by models. The facts
are [CC BY 4.0](DATA-LICENSE.md), which asks for one thing back:

```
Source: sourcey, the open registry of startup programs. https://sourcey.com
Offer <offer_id> @ <revision_digest>  (CC BY 4.0)
```

Take both values from the record you are quoting. Citing the revision digest is
what keeps a claim checkable, instead of leaving a screenshot of something that
used to be true.

## Add or correct a record

Copy a nearby file under `vendors/`, keep the shape, open a pull request. CI
pulls the exact content-addressed verifier and checks only what you changed, then
hands back real field errors. Push fixes to the same branch as often as you like
without waiting on a maintainer.

[CONTRIBUTING.md](CONTRIBUTING.md) has the data rules and a local preflight that
runs the identical verifier.

Correcting or ending an existing offer counts for as much as adding one. Terms
move, programs close, and a record that keeps up is worth more than a record
that only grows.

### What gets sent back

Provenance is the entire product, so the bar is the source.

- **Every fact needs a first-party URL** in the record's `sources`. The vendor's
  own page, or their own announcement. A roundup post quoting another directory
  is not a source.
- **If the source does not say it, it does not go in.** A credit amount nobody
  published, an eligibility rule that sounds about right, an expiry date filled
  in to complete the shape. An offer written up from memory, or by a model that
  never opened the page, reads exactly like one that was checked, which is why
  it gets closed on sight.
- **Never author provenance.** Verification, freshness, signature, and tier
  claims are derived from evidence. Writing one by hand is a fabrication.
- **Descriptions are written, not lifted.** Marketing copy and text pulled out
  of a meta tag both go back.
- **Check the open pull requests before you start.** Popular vendors attract
  several people at once, and only the first one through gets merged.

## If this is your company

Take your row. Prove control of the domain, review the exact offers we have, and
attest to the ones you stand behind. Free, and staying free, because vendors
correcting their own records is the engine of the whole thing. Your offer stops
being something we read somewhere and becomes something you said.

Start at [sourcey.com](https://sourcey.com), or open a pull request here and fix
the facts yourself.

## How publication works

Merging an admitted pull request to `main` is the only human activation. Sourcey
consumes that exact merge commit, publishes the changed closure, and advances one
live head that [sourcey.com](https://sourcey.com), the API, MCP, the change feed,
and the redirects all read together. Contributors never pick a release, digest,
deployment, or version.

Two checks run on a data pull request. `validate` is the public one; it starts
automatically on every pull request including a first one from a new fork, and
green means the tree is structurally and semantically sound. `sourcey/admission`
is a separate Sourcey-owned gate proving private evidence and authority were
admitted for that exact tree. Contributors never upload that private material.

This repository holds vendor YAML and the documentation around it. Schemas,
validation, evidence, release construction, the API, MCP, and the hosted runtime
belong to Sourcey's private Catalog engine. [AGENTS.md](AGENTS.md) draws the
boundary.

## Licence

Catalog facts are [CC BY 4.0](DATA-LICENSE.md). Repository documentation and
metadata are [MIT](LICENSE).
