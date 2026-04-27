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
          <div class="home-hero__text">
            <h1 class="home-hero__heading">Research software is a critical part of research</h1>
            <p class="home-hero__body">The <a href="declaration/">Amsterdam Declaration on Funding Research Software Sustainability</a> is setting the future international agenda and comprehensively changing the way funders deal with research software.</p>
            <div class="home-hero__cta-group">
              <a href="/get-involved/" class="btn btn-get-involved">Get Involved</a>
              <a href="/declaration/" class="home-hero__btn home-hero__btn--secondary">Read the Declaration</a>
            </div>
          </div>
          <div class="home-hero__image-wrap">
            <img src="/uploads/homepage-group.jpg" alt="Group discussing around a table" class="home-hero__image" />
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
        The [Amsterdam Declaration on Funding Research Software Sustainability](/declaration) (ADORE.software) aim is to raise awareness of the role of funding practice in the sustainability of research software, and to improve that practice. The Declaration includes a limited number of recommendations and an accompanying [ADORE.software Toolkit](/toolkit/). For the purposes of this Declaration, research software is defined as "all forms of software that were created during the research process or for a research purpose". A fuller description is included in the accompanying [ADORE.software Toolkit](/toolkit/).
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
    design:
      spacing:
        padding: ["4rem", "2rem"]
      background:
        color: '#f5f5f5'

  - block: markdown
    content:
      title: ""
      text: |
        {{< adore-cta >}}
    design:
      spacing:
        padding: ["0", "0"]

---
