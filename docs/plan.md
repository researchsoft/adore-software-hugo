# ADORE.software Hugo Site — Cleanup & Bug Fix Plan

## Context

The Hugo reimplementation of adore.software is largely functional but has outstanding content gaps, code quality issues, and design inconsistencies. This document organises remaining work into four perspectives so it can be tackled systematically. Each item should be addressed with a GitHub issue + dedicated PR so changes can be reviewed before merging.

---

## Perspective 1: Web Developer — Functionality & Infrastructure

### 1.1 Missing content pages (create 404s)

These pages exist in the WP original but are absent from Hugo. Redirects in `netlify.toml` are already configured; the destination pages are still missing.

**GitHub issue #7** — About sub-pages (copy from live WP):
- `content/about/about-adore/index.md`
- `content/about/governance/index.md`
- `content/about/process/index.md`

**GitHub issue #8** — Main pages:
- `content/press/index.md`
- `content/newsletter/index.md`
- `content/sign/index.md`
- `content/support/index.md`
- `content/international-research-software-funders-workshop/index.md`
- `content/2024-international-research-software-funders-workshop/index.md`

**GitHub issue #10** — Thank-you stubs (needed for Netlify form redirect `action=` targets):
- `content/contact-thank-you/index.md`
- `content/thank-you-signatory/index.md`
- `content/thank-you-supporter/index.md`

### 1.2 Missing news posts (GitHub issue #9)

Four 2023 posts are stubs with no body content or featured images:
- `content/news/2023-03-rda-resa-gothenburg/index.md`
- `content/news/2023-03-international-funders-workshop/index.md`
- `content/news/2023-04-amsterdam-declaration-open-for-input/index.md`
- `content/news/2023-04-code-for-thought-podcast/index.md`

Action: fetch original WP post HTML, convert to Markdown, add featured images.

### 1.3 Hardcoded internal links in content

`content/_index.md` (lines 18, 20, 25, 66, 85) uses raw `href="/get-involved/"` etc. These bypass Hugo's link validation. If URLs change they will silently 404. Replace with Hugo `relref` function calls.

### 1.4 Verify Netlify form redirect targets exist

All three forms redirect to thank-you pages:
- `layouts/shortcodes/contact.html` → `/contact-thank-you/`
- `layouts/shortcodes/sign.html` → `/thank-you-signatory/`
- `layouts/shortcodes/support-form.html` → `/thank-you-supporter/`

These stubs need a `title:` and minimal body so Netlify doesn't 404 on submission.

---

## Perspective 2: Naïve GitHub Editor — Editability & Consistency

### 2.1 Inline HTML in _index.md is hostile to non-coders

`content/_index.md` contains ~90 lines of raw `<div style="...">` HTML mixed into frontmatter sections. A non-technical editor cannot safely change CTA text, button labels, or hero copy without breaking layout.

Action: Extract hero/CTA HTML blocks into CSS classes (in `assets/scss/custom.scss`) and named shortcodes, so editors touch only plain text.

### 2.2 Frontmatter inconsistency in news posts

Only 1 of 15 news posts has a `summary:` field; the rest rely on Hugo auto-truncation. The news grid can show a truncated list item or odd prose as the excerpt.

Action: Add explicit `summary:` (1–2 sentences) to all 15 news posts. Standardise the frontmatter template in `archetypes/news.md`.

### 2.3 Create an archetype for news posts

`archetypes/default.md` likely has no news-specific template. Adding `archetypes/news.md` with the correct frontmatter skeleton lets editors duplicate it without guessing.

### 2.4 CLAUDE.md is out of date

Several pages listed as "missing" in CLAUDE.md (e.g. `/supporters/`, `/press/`, `/sign/`) now exist as stubs. Update the inventory tables to reflect current state.

---

## Perspective 3: Designer — Visual Consistency & Performance

### 3.1 Colour inconsistency — third blue (#0066cc) crept in

`assets/scss/custom.scss` (line 412) and `content/_index.md` (lines 64–68) use `#0066cc`, which is not in the brand palette (teal `rgb(1,95,94)`, yellow `#f5c200`). Every CTA and "Visit website" button should use `$brand-teal` or `$brand-yellow`.

Action: Replace all `#0066cc` instances with `$brand-teal`.

### 3.2 Move inline styles out of _index.md into SCSS

`content/_index.md` has dozens of `style="..."` attributes. Global design changes (button padding, hero font size on mobile) require editing content files rather than the stylesheet.

Priority blocks to extract:
- `.hero-flex-container` (lines 15–27)
- `.hero-cta-btn-primary` / `.hero-cta-btn-secondary`
- `.signatories-cta-section` (lines 80–88)
- `.view-all-btn` (line 66)

### 3.3 Homepage image is 4.3 MB

`static/uploads/homepage-group.jpg` weighs 4.3 MB and is served at full resolution — the single biggest Core Web Vitals risk.

Action: Re-export/compress to ≤ 300 KB (WebP preferred, JPEG fallback). Update `custom_head.html` to use `<picture>` with WebP source, or move the image into `assets/` so Hugo processes it at build time.

Other oversized images:
- `uploads/dfg_logo.jpg` — 704 KB
- `uploads/news-2024-workshop-announce.jpg` — 908 KB

### 3.4 Navbar active-link highlighting is disabled

`config/_default/params.yaml` line 41: `highlight_active_link: false`. Users cannot tell which section they are in.

Action: Set to `true`. Verify the CSS in `custom.scss` does not fight it.

### 3.5 Footer uses fragile `calc(-50vw + 50%)` full-bleed hack

`assets/scss/custom.scss` (lines 174–176) uses `width: 100vw; margin-left: calc(-50vw + 50%)`. This causes horizontal scroll on some browsers/viewports.

Action: Restructure footer to sit outside the container at the layout level in `layouts/partials/site_footer.html`, rather than fighting it in CSS.

### 3.6 Missing signatory/supporter logos

`data/signatories.yaml` has 50+ entries with `logo: ""`. `data/supporters.yaml` has all entries with empty logos. Cards show a generic placeholder icon.

Action: Collect logos (see GitHub issue #3) and place in `static/uploads/signatories/` and `static/uploads/supporters/`. Update the YAML entries.

---

## Perspective 4: Expert Coder — Code Quality & Maintainability

### 4.1 Dead code: empty partial and unused data file

- `layouts/partials/components/page_sharer.html` — 0 bytes, referenced in no template
- `data/page_sharer.toml` — 83 lines of social-sharing config, referenced nowhere

Action: Delete both files.

### 4.2 Reduce `!important` density in custom.scss

`assets/scss/custom.scss` has 13 `!important` declarations. Several indicate specificity battles with the theme. For each one, trace why it was needed; where the theme can be overridden via a more-specific selector, do so. Where it is genuinely required, add a comment explaining the constraint.

### 4.3 Logo sizing should be responsive

`assets/scss/custom.scss` (lines 153–154): `.logo-image { width: 180px !important; height: 180px !important; }` — fixed pixels block responsive scaling.

Action: Replace with `max-width: 180px; height: auto;`.

### 4.4 Navbar min-height is fixed at 130px

Line 53: `min-height: 130px`. If the menu wraps to two lines on small screens this will overflow.

Action: Remove the fixed `min-height` and test on 320 px and 375 px viewport widths.

### 4.5 Inconsistent SCSS variable usage

Brand colours are defined as `$brand-teal` and `$brand-yellow` in `custom.scss`, but many places use hardcoded `rgb(1,95,94)` or `#f5c200` literals instead.

Action: Replace all hardcoded brand colour values with SCSS variables.

### 4.6 Supporter and signatory shortcodes share CSS class names

`signatories-list.html` and `supporters-list.html` both emit `.signatory-card`, `.signatory-name`, `.signatory-logo` — for semantically different entities. SCSS changes to signatory styling accidentally affect supporter cards.

Action: Rename supporter classes to `.supporter-card`, `.supporter-name`, `.supporter-logo` in `layouts/shortcodes/supporters-list.html` and update `assets/scss/custom.scss`.

### 4.7 Form shortcodes missing `aria-required`

`sign.html`, `contact.html`, and `support-form.html` mark required fields visually with `<span class="text-danger">*</span>` but do not set `aria-required="true"` on the input elements. Screen readers will not announce required status.

Action: Add `aria-required="true"` to all required `<input>` and `<textarea>` fields.

### 4.8 Inline style on news-featured link

`layouts/shortcodes/news-featured.html` (line 32): `style="text-decoration:none;"` on the post title anchor.

Action: Remove inline style; add `.news-card-title a { text-decoration: none; }` to `custom.scss`.

---

## File Map — Critical Files to Modify

| File | Changes needed |
|------|----------------|
| `content/_index.md` | Extract inline HTML to CSS classes/shortcodes; fix hardcoded hrefs |
| `assets/scss/custom.scss` | Replace #0066cc; fix $brand-teal vars; reduce !important; rename supporter classes; fix logo sizing; remove footer hack |
| `config/_default/params.yaml` | Set `highlight_active_link: true` |
| `layouts/shortcodes/sign.html` | Add aria-required |
| `layouts/shortcodes/contact.html` | Add aria-required |
| `layouts/shortcodes/support-form.html` | Add aria-required |
| `layouts/shortcodes/supporters-list.html` | Rename CSS classes to supporter-* |
| `layouts/shortcodes/news-featured.html` | Remove inline style |
| `layouts/partials/site_footer.html` | Remove full-bleed CSS hack; make footer naturally full-width |
| `data/signatories.yaml` | Add logos, remove placeholder comment |
| `data/supporters.yaml` | Add logos |
| `CLAUDE.md` | Update content inventory to reflect current state |
| `archetypes/news.md` | Create with standard news frontmatter |
| All 15 news posts | Add `summary:` field |
| 4 stub news posts | Fill in content + add featured images |
| 8 missing content pages | Create with content from WP |
| 3 thank-you stubs | Flesh out so Netlify form redirects succeed |

## Files to Delete

- `layouts/partials/components/page_sharer.html` (empty, unused)
- `data/page_sharer.toml` (unreferenced)

---

## Verification

1. Run `hugo server -D` — zero build errors or warnings
2. Open each previously-missing page — no 404s
3. Submit each form (contact, sign, support) — confirm redirect to correct thank-you page
4. Run Lighthouse on homepage — LCP should improve after homepage image is compressed
5. Resize browser to 320 px — navbar and footer should not overflow horizontally
6. Check signatories page — "Visit website" buttons should use brand teal, not #0066cc
7. Navigate through all sections — active nav link should be highlighted
8. `grep -r '#0066cc' assets/ content/` — should return zero results
9. `grep -c '!important' assets/scss/custom.scss` — should be ≤ 5
