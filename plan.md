# ADORE.software Hugo Migration — Working Plan

> Last updated: 14 April 2026
> Pick up here after restarting Claude.

---

## Context

Reimplementing https://adore.software (WordPress) in Hugo in this repo.
Theme: Hugo Blox Builder (`blox-bootstrap/v5`), hosted on Netlify.
GitHub repo: https://github.com/RichardLitt/adore-software-hugo

---

## What's been done this session

### 1. Gap audit ✓
Compared WP sitemaps (`/post-sitemap.xml`, `/page-sitemap.xml`) against Hugo `content/`.

### 2. All missing content pages created ✓

| File created | Ported from |
|---|---|
| `content/about/about-adore/index.md` | https://adore.software/about/about-adore/ |
| `content/about/governance/index.md` | https://adore.software/about/governance/ |
| `content/about/process/index.md` | https://adore.software/about/process/ |
| `content/press/index.md` | https://adore.software/press/ |
| `content/newsletter/index.md` | https://adore.software/newsletter/ |
| `content/supporters/index.md` | https://adore.software/supporters/ |
| `content/support/index.md` | https://adore.software/support/ |
| `content/sign/index.md` | https://adore.software/sign/ |
| `content/international-research-software-funders-workshop/index.md` | https://adore.software/international-research-software-funders-workshop/ |
| `content/2024-international-research-software-funders-workshop/index.md` | https://adore.software/2024-international-research-software-funders-workshop/ |
| `content/contact-thank-you/index.md` | https://adore.software/contact-thank-you/ |
| `content/thank-you-signatory/index.md` | https://adore.software/thank-you-signatory/ |
| `content/thank-you-supporter/index.md` | https://adore.software/thank-you-supporter/ |
| `content/news/2023-03-rda-resa-gothenburg/index.md` | https://adore.software/2023/03/rda-resa-funders-forum-gothenburg-sweden/ |
| `content/news/2023-03-international-funders-workshop/index.md` | https://adore.software/2023/03/international-funders-workshop-the-future-of-research-software/ |
| `content/news/2023-04-amsterdam-declaration-open-for-input/index.md` | https://adore.software/2023/04/the-amsterdam-declaration-on-funding-research-software-sustainability-is-now-open-for-input-from-funders/ |
| `content/news/2023-04-code-for-thought-podcast/index.md` | https://adore.software/2023/04/listen-to-us-on-the-latest-episode-of-the-code-for-thought-podcast/ |

### 3. New data files and shortcodes created ✓
- `data/supporters.yaml` — 47 supporters (⚠ verify completeness against live site)
- `layouts/shortcodes/supporters-list.html`
- `layouts/shortcodes/sign.html` — Netlify form for signing
- `layouts/shortcodes/support-form.html` — Netlify form for support submissions

### 4. Bug fix: about bundle type ✓
`content/about/index.md` → `content/about/_index.md`
(Leaf bundle can't have children; branch bundle can.)

### 5. URL redirects added to netlify.toml ✓
16 `[[redirects]]` rules covering all old WP post URLs → new Hugo slugs, plus `/about/faq/` → `/faq/`.

### 6. CLAUDE.md updated ✓
Architecture, content inventory, frontmatter conventions documented in `CLAUDE.md`.

### 7. GitHub issues created ✓
| Issue | Title |
|---|---|
| #7 | Port missing About sub-pages from WordPress |
| #8 | Port missing standalone pages from WordPress |
| #9 | Port missing news posts from WordPress |
| #10 | Add form thank-you stub pages |
| #11 | Add URL redirects for old WordPress post URLs |

Issues #7–#11 are all **implemented** — code is done; issues can be closed.

---

## Current build status

`hugo server -D` builds cleanly: **108 pages, 0 errors**.
All 17 new pages verified returning HTTP 200.

Run locally:
```sh
hugo server -D
```

---

## What's NOT done yet — visual parity issues

These discrepancies were identified by comparing the live WP site to the Hugo output.
**None of these have GitHub issues yet** — next step is to file them and fix sequentially.

### A — Navbar logo missing (HIGH)
- **WP:** Logo image in top-left of navbar
- **Hugo:** Falls back to plain `site.Title` text — `assets/media/logo.svg` does not exist
- **Fix:** Copy `static/adore-logo-text.svg` → `assets/media/logo.svg` (the footer already uses this file)

### B — "Get Involved" CTA button hidden on homepage (HIGH)
- **WP:** "Get Involved" button visible in navbar on all pages including homepage
- **Hugo:** `layouts/partials/components/headers/navbar.html` has `{{ if not $current_page.IsHome }}` guard that hides `main_right` menu items on the homepage
- **Fix:** Remove the `IsHome` guard from the navbar template

### C — Hero CTA buttons styling (MEDIUM)
- **WP:** "GET INVOLVED" (blue filled) + "Read the Declaration" (white outline) as side-by-side buttons
- **Hugo:** Buttons present in `content/_index.md` raw HTML but need visual comparison
- **Fix:** Open http://localhost:1313 and https://adore.software side-by-side, check and tweak button CSS

### D — News grid is stacked, not 3-column (HIGH)
- **WP:** News cards in a 3-column grid
- **Hugo:** Cards stack vertically
- **Fix:** See GitHub issue #6

### E — Footer links position (MEDIUM)
- **WP:** Footer nav links centred in footer
- **Hugo:** Links appear below the footer block
- **Fix:** See GitHub issue #5

### F — `about/` nav item has no sub-menu (LOW)
- **WP:** About links to sub-pages (about-adore, governance, process, faq)
- **Hugo:** Single nav link to `/about/` only
- **Fix:** Add `parent` entries to `menus.yaml` for sub-pages, or add links inside `/about/`

### G — Day/night toggle inactive (LOW)
- **WP:** No toggle (WP doesn't have one)
- **Hugo:** `show_day_night: true` in params but `theme_night` is blank, so the moon icon never renders
- **Fix:** Set `show_day_night: false` in `config/_default/params.yaml` to clean this up

### H — Twitter / #ADOREsoftware section on homepage (LOW)
- **WP:** Blue CTA block with "FOLLOW US TWITTER" button
- **Hugo:** Present in `_index.md` — needs visual comparison

### I — Signatories section on homepage (MEDIUM)
- **WP:** Homepage shows a full signatories grid with logos
- **Hugo:** Needs visual comparison — check whether `{{< signatories-list >}}` renders on homepage

---

## Recommended next steps

1. **File GitHub issues A–I** above (or ask Claude to do it)
2. **Fix A (logo)** — quick 1-minute fix
3. **Fix B (nav CTA)** — quick template edit
4. **Fix D (news grid)** — see issue #6
5. **Fix E (footer links)** — see issue #5
6. **Visual review pass** — run `hugo server -D`, open alongside live site, check C/H/I

---

## Frontmatter conventions (reference)

### Page (`type: page`)
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

---

## How to continue with Claude

Tell Claude:
> "Read plan.md and CLAUDE.md, then file GitHub issues for items A–I and fix them in order."

Or pick a specific item:
> "Fix issue A — the missing navbar logo."

Claude can discover, file issues (`gh issue create`), implement, and verify all in one turn.
Use `GH_PAGER=cat` prefix for all `gh` commands to avoid the interactive pager.
