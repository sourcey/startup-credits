<h1 align="center">Startup Credits</h1>

<p align="center">
  The open registry of startup programs, from the source.
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

Software vendors run startup programs: credits, discounts, a free year. The terms
are public, scattered across a few hundred pricing pages, and they change without
telling anyone. This is the list, one file per vendor, with the source and the
date behind every fact.

## What a record looks like

```yaml
# vendors/re/retool.yaml
name: Retool
sources:
  - source_id: src_2c260c8d…
    url: https://retool.com/startups
offers:
  - title: Retool for Startups
    summary: Eligible early-stage startups get 100% off Retool for one year on
      monthly Team or Business plans (up to $60,000 value), followed by a 25%
      discount in the second year.
    eligibility:
      statement: Must be bootstrapped, angel-funded, debt-funded, pre-seed, seed,
        or Series A with under $10M in total funding, founded within the last 10
        years, and a new customer on a monthly Team or Business plan.
```

Eligibility is quoted in the vendor's own words rather than paraphrased, and
every fact traces back to the URL in `sources`.

## Getting it

```sh
curl -s https://sourcey.com/catalog.json \
  | jq -r '.data.entities[] | select(.slug=="vercel") | .offers[0].summary'
```

> Eligible startups affiliated with an approved partner can receive up to $30,000
> in Vercel credits issued over 12 months, plus Slack access, networking, private
> events, and marketing opportunities.

No key and no signup, for you or for your agents. There is an
[OpenAPI](https://api.sourcey.com/openapi.yml) surface, an
[MCP server](https://mcp.sourcey.com/mcp) for assistants, a
[change feed](https://sourcey.com/changes.ndjson) for watching terms move,
[llms.txt](https://sourcey.com/llms.txt) for models, and a
[guide](https://sourcey.com/SKILL.md) for agents working the data directly.

Facts are [CC BY 4.0](DATA-LICENSE.md) and training on them is welcome. Quote the
`offer_id` and `revision_digest` and your citation still means something after
the offer moves.

## Fixing or adding one

Copy a nearby file under `vendors/`, keep the shape, open a pull request. CI
checks only what you changed and hands back real field errors, so you can push
corrections without waiting on a maintainer.

Two rules carry most of the weight. Every fact needs the vendor's own URL in
`sources`, and if the source does not say it, it does not go in. Guessed amounts
and invented eligibility read exactly like checked ones, which is why they get
closed. [CONTRIBUTING.md](CONTRIBUTING.md) has the rest, including a preflight
that runs the same verifier CI uses.

Correcting a stale offer is worth as much as adding a new one.

## If it's your company

Most records here are observed: we read your page and dated it. Prove control of
your domain and attest to the offers you stand behind, and yours becomes signed,
which the record then says on its face. Free, and it stays free, because vendors
correcting their own records is the whole engine.

[sourcey.com](https://sourcey.com), or just send a pull request.

## Licence

Facts are [CC BY 4.0](DATA-LICENSE.md). Repository documentation and metadata are
[MIT](LICENSE). This repository holds the vendor files; everything that validates,
compiles, and serves them belongs to Sourcey's private Catalog engine, and
[AGENTS.md](AGENTS.md) draws that boundary.
