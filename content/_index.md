---
title:
date: 2024-01-01
type: landing
layout: "default"
design:
  css_class: is-home

sections:
  - block: markdown
    id: hero
    content: 
      title:
      text: |
        <div class="home-hero">
          <div class="home-hero-text">
            <h1 class="home-hero-heading">Research software is a critical part of research</h1>
            <p class="home-hero-body">The <a href="declaration/">Amsterdam Declaration on Funding Research Software Sustainability</a> is setting the future international agenda and comprehensively changing the way funders deal with research software.</p>
            <div class="home-hero-cta-group">
              <a href="/get-involved/" class="home-hero-btn-primary">GET INVOLVED</a>
              <a href="/declaration/" class="home-hero-btn-secondary">Read the Declaration</a>
            </div>
          </div>
          <div class="home-hero-image-wrap">
            <img src="/uploads/homepage-group.jpg" alt="Group discussing around a table" class="home-hero-image" />
          </div>
        </div>

    design:
      background:
        text_color_light: true
      spacing:
        padding: ["6rem", "2rem", "6rem", "2rem"]

  - block: markdown
    content:
      title: "Amsterdam Declaration on Funding Research Software Sustainability"
      text: |
        The **Amsterdam Declaration on Funding Research Software Sustainability** (ADORE.software) aims to raise awareness of the role of funding practice in the sustainability of research software, and to improve that practice. The Declaration includes a limited number of recommendations and an accompanying [ADORE.software Toolkit](toolkit/).
        
        For the purposes of this Declaration, research software is defined as "all forms of software that were created during the research process or for a research purpose". A fuller description is included in the accompanying ADORE.software Toolkit.
    design:
      spacing:
        padding: ["4rem", "2rem"]
      columns: '1'

  - block: markdown
    id: news
    content:
      title: News
      text: |
        {{< news-featured slug="2024-09-declaration-open-for-signing" >}}
        {{< news-grid count="3" exclude="2024-09-declaration-open-for-signing" >}}
    design:
      spacing:
        padding: ["4rem", "2rem", "4rem", "2rem"]

  - block: markdown
    content:
      title: "Signatories"
      text: |
        {{< signatories-list >}}

        <div class="home-view-all-wrap">
          <a href="/signatories/" class="home-view-all-btn">View All Signatories</a>
        </div>
    design:
      spacing:
        padding: ["4rem", "2rem"]
      background:
        color: '#f5f5f5'

  - block: markdown
    content:
      title: ""
      text: |
        <div class="home-cta-block">
          <img src="/uploads/adore-logo-symbol.svg" alt="ADORE logo" class="home-cta-logo" />
          <h3 class="home-cta-heading">Would you like to be involved in the adoption of the Declaration?</h3>
          <p class="home-cta-subhead">Become a Signatory!</p>
          <a href="/get-involved/" class="home-cta-btn">GET INVOLVED</a>
        </div>
    design:
      spacing:
        padding: ["4rem", "2rem"]
      background:
        color: '#c5d0de'

---
