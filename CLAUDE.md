# ADORE.software Hugo Migration — Plan

## Overview

This repo is a Hugo reimplementation of the WordPress site at https://adore.software.
Theme: [Hugo Blox Builder](https://docs.hugoblox.com/) (`blox-bootstrap/v5`), hosted on Netlify.

The goal is to achieve full content and layout parity with the live WordPress site, then switch DNS.

---

## Architecture

| Layer | Detail |
|---|---|
| Base URL | `https://adore.software/` |
| Theme | Hugo Blox Builder (`blox-bootstrap/v5`) |
| Config | Split config in `config/_default/` |
| Content | `content/` — Markdown + frontmatter |
| Data | `data/signatories.yaml` (signatory list), `data/page_sharer.toml` |
| Shortcodes | `layouts/shortcodes/contact.html`, `signatories-list.html` |
| Deployment | Netlify (see `netlify.toml`) |

---

## Content Inventory

### Pages — ported ✓

| WP URL | Hugo file |
|---|---|
| `/` | `content/_index.md` |
| `/about/` | `content/about/index.md` |
| `/declaration/` | `content/declaration/index.md` |
| `/signatories/` | `content/signatories/index.md` |
| `/toolkit/` | `content/toolkit/index.md` |
| `/news/` | `content/news/_index.md` |
| `/contact/` | `content/contact/index.md` |
| `/get-involved/` | `content/get-involved/index.md` |
| `/privacy-policy/` | `content/privacy-policy/index.md` |
| `/about/faq/` | `content/faq/index.md` ⚠ URL changed to `/faq/` |

### Pages — missing (GitHub issues opened)

| WP URL | Hugo target | Issue |
|---|---|---|
| `/about/about-adore/` | `content/about/about-adore/index.md` | #7 |
| `/about/governance/` | `content/about/governance/index.md` | #7 |
| `/about/process/` | `content/about/process/index.md` | #7 |
| `/press/` | `content/press/index.md` | #8 |
| `/supporters/` | `content/supporters/index.md` | #8 |
| `/support/` | `content/support/index.md` | #8 |
| `/newsletter/` | `content/newsletter/index.md` | #8 |
| `/sign/` | `content/sign/index.md` | #8 |
| `/international-research-software-funders-workshop/` | `content/international-research-software-funders-workshop/index.md` | #8 |
| `/2024-international-research-software-funders-workshop/` | `content/2024-international-research-software-funders-workshop/index.md` | #8 |
| `/contact-thank-you/` | stub or redirect | #10 |
| `/thank-you-signatory/` | stub or redirect | #10 |
| `/thank-you-supporter/` | stub or redirect | #10 |

### News posts — ported ✓

| WP URL | Hugo file |
|---|---|
| `/2023/04/research-software-community-feedback/` | `content/news/2023-04-community-feedback/` |
| `/2023/07/international-research-software-funders-workshop/` | `content/news/2023-07-international-funders-workshop/` |
| `/2023/09/adore-software-is-ready-for-signing/` | `content/news/2023-09-adore-ready-for-signing/` |
| `/2023/10/investing-in-people-…/` | `content/news/2023-10-investing-in-people/` |
| `/2023/11/adore-software-signatories/` | `content/news/2023-11-adore-signatories/` |
| `/2024/01/nwo-zonmw-sign/` | `content/news/2024-01-nwo-zonmw-sign/` |
| `/2024/02/2024-international-research-software-funders-workshop/` | `content/news/2024-02-2024-funders-workshop-announcement/` |
| `/2024/02/scilifelab_co-organises_…/` | `content/news/2024-02-scilifelab-workshop/` |
| `/2024/09/the-amsterdam-declaration-is-now-open-for-all-to-sign/` | `content/news/2024-09-declaration-open-for-signing/` |
| `/2024/10/building-a-sustainable-future-for-research-software/` | `content/news/2024-10-funders-workshop/` |
| `/2024/12/dfg-signs-the-amsterdam-declaration/` | `content/news/2024-12-dfg-signs/` |

### News posts — missing (GitHub issues opened)

| WP URL | Hugo target | Issue |
|---|---|---|
| `/2023/03/rda-resa-funders-forum-gothenburg-sweden/` | `content/news/2023-03-rda-resa-gothenburg/` | #9 |
| `/2023/03/international-funders-workshop-the-future-of-research-software/` | `content/news/2023-03-international-funders-workshop/` | #9 |
| `/2023/04/the-amsterdam-declaration-…-open-for-input-from-funders/` | `content/news/2023-04-amsterdam-declaration-open-for-input/` | #9 |
| `/2023/04/listen-to-us-on-the-latest-episode-of-the-code-for-thought-podcast/` | `content/news/2023-04-code-for-thought-podcast/` | #9 |

---

## URL Redirect Mapping

Old WordPress URL patterns → new Hugo URLs. To be added to `netlify.toml` or `public/_redirects` (GitHub issue #5):

| From (WP) | To (Hugo) | Status |
|---|---|---|
| `/about/faq/` | `/faq/` | pending — see #11 |
| `/2023/04/research-software-community-feedback/` | `/news/2023-04-community-feedback/` | pending |
| `/2023/07/international-research-software-funders-workshop/` | `/news/2023-07-international-funders-workshop/` | pending |
| `/2023/09/adore-software-is-ready-for-signing/` | `/news/2023-09-adore-ready-for-signing/` | pending |
| `/2023/10/investing-in-people-anticipating-the-future-of-research-software/` | `/news/2023-10-investing-in-people/` | pending |
| `/2023/11/adore-software-signatories/` | `/news/2023-11-adore-signatories/` | pending |
| `/2024/01/nwo-zonmw-sign/` | `/news/2024-01-nwo-zonmw-sign/` | pending |
| `/2024/02/2024-international-research-software-funders-workshop/` | `/news/2024-02-2024-funders-workshop-announcement/` | pending |
| `/2024/02/scilifelab_co-organises_international_research_software_funders_workshop/` | `/news/2024-02-scilifelab-workshop/` | pending |
| `/2024/09/the-amsterdam-declaration-is-now-open-for-all-to-sign/` | `/news/2024-09-declaration-open-for-signing/` | pending |
| `/2024/10/building-a-sustainable-future-for-research-software/` | `/news/2024-10-funders-workshop/` | pending |
| `/2024/12/dfg-signs-the-amsterdam-declaration/` | `/news/2024-12-dfg-signs/` | pending |

---

## Verification Approach

1. **Gap audit** (done) — compare WP sitemap vs Hugo content directory
2. **Content accuracy** — for each ported page, fetch live WP HTML and diff key text against Hugo markdown
3. **Visual review** — run `hugo server -D` locally, open side-by-side with live site in browser
4. **Redirect check** — after deploy, curl each old WP URL and confirm 301 redirect

### Running locally

```sh
hugo server -D
```

---

## Frontmatter conventions

### Page (type: page)
```yaml
---
title: "Page Title"
date: 2024-01-01
type: page
---
```

### News post
```yaml
---
title: "Post Title"
date: 2024-01-15
categories:
  - News
tags:
  - relevant-tag
featured: true
image:
  filename: featured.jpg
  preview_only: false
---
```
