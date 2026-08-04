<h1 align="center">Startup Credits</h1>

<p align="center">
  <b>The open registry of startup programs</b><br>
  <sub><em>Never pay the stranger price</em></sub>
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
  <img alt="vendors on record" src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fsourcey.com%2Fcatalog.json&query=%24.data.entities.length&label=vendors%20on%20record&style=flat-square&labelColor=0a0908&color=d0231c">
  <img alt="last change" src="https://img.shields.io/github/last-commit/sourcey/startup-credits?style=flat-square&labelColor=0a0908&color=176b45&label=last%20change">
  <img alt="changes per month" src="https://img.shields.io/github/commit-activity/m/sourcey/startup-credits?style=flat-square&labelColor=0a0908&color=176b45&label=changes%2Fmonth">
  <img alt="data licence CC BY 4.0" src="https://img.shields.io/badge/data-CC%20BY%204.0-6a645d?style=flat-square&labelColor=0a0908">
</p>

---

Every tool has two prices. The one on the pricing page, and the one startups
actually pay once somebody tells them the program exists.

The second price isn't a secret. It's just spread across a few hundred vendor
pages, worded differently every time, and quietly revised whenever the vendor
feels like it. So we write it down. One file per vendor, every fact carrying the
page it came from and the day we read it.

Nothing here is for sale. Tiers come from evidence and are never influenced by
payment, and the [rules](https://sourcey.com/policies) are published as catalog
records with their own revision digests, exactly like the data they govern.

## What a record looks like

```yaml
# vendors/at/atlassian.yaml
name: Atlassian
sources:
  - source_id: src_0ae96c1d…
    url: https://www.atlassian.com/software/startups
offers:
  - title: Atlassian for Startups
    summary: Eligible startups can get Atlassian Cloud products (including Premium
      editions of Jira, Confluence, Loom, Bitbucket, and more) for $0 for 12 months
      for up to 50 users.
    eligibility:
      statement: Must not be an existing Atlassian paid customer, must be VC funded
        or associated with a partner accelerator/incubator, and must not have raised
        more than $10 million in external funding.
```

Eligibility is quoted in the vendor's own words rather than paraphrased, and
every fact traces back to the URL in `sources`.

## Getting it

Browse it at [sourcey.com](https://sourcey.com), by vendor or by category. Or ask
for one record and get that same offer back:

```sh
curl -s https://api.sourcey.com/v1/entities/by-slug/atlassian \
  | jq -r '.data.offers[0].summary'
```

> Eligible startups can get Atlassian Cloud products (including Premium editions
> of Jira, Confluence, Loom, Bitbucket, and more) for $0 for 12 months for up to
> 50 users.

No key and no signup, for you or for your agents. There is an
[OpenAPI](https://api.sourcey.com/openapi.yml) surface, an
[MCP server](https://mcp.sourcey.com/mcp) for assistants, a
[change feed](https://sourcey.com/changes.ndjson) for watching terms move,
[llms.txt](https://sourcey.com/llms.txt) for models, and a
[guide](https://sourcey.com/SKILL.md) for agents working the data directly.

Terms move. Confirm with the vendor before you rely on it.

Facts are [CC BY 4.0](DATA-LICENSE.md) and training on them is welcome. Quote the
`offer_id` and `revision_digest` and your citation still means something after
the offer moves:

    sourcey.com · <offer_id> @ <revision_digest> · CC BY 4.0

## Fixing or adding one

Copy a nearby file under `vendors/`, keep the shape, open a pull request. CI
checks only what you changed and hands back real field errors, so you can push
corrections without waiting on a maintainer.

Two rules carry most of the weight. Every fact needs the vendor's own URL in
`sources`, and if the source does not say it, it does not go in. Guessed amounts
and invented eligibility read exactly like checked ones, which is why they get
closed. [CONTRIBUTING.md](CONTRIBUTING.md) has the rest, including a preflight
that runs the same verifier CI uses. Correcting a stale offer is worth as much as
adding a new one.

## If it's your company

Claim it and the record carries your signature instead of our reading of your
page. Prove the domain whichever way suits you: DNS, a file on your site, a role
address, or a reply from any mailbox on your domain. Claiming establishes who you
are and never signs your offers for you; you attest to those separately, by exact
revision.

Free, now and later. Start at `sourcey.com/claim/<your-slug>`.

## Licence

Facts are [CC BY 4.0](DATA-LICENSE.md). Documentation and metadata are [MIT](LICENSE).

---

<p align="center">Know a program that isn't here yet? <a href="CONTRIBUTING.md">Add it.</a></p>
