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
        <div style="display: flex; align-items: center; gap: 3rem; flex-wrap: wrap;">
          <div style="flex: 1; min-width: 280px;">
            <h1 style="color: white; font-size: 2.8rem; font-weight: bold; margin-bottom: 1.5rem; line-height: 1.2;">Research software is a critical part of research</h1>
            <p style="color: white; font-size: 1.25rem; line-height: 1.6; margin-bottom: 2.5rem;">The <a href="declaration/" style="color: white; text-decoration: underline;">Amsterdam Declaration on Funding Research Software Sustainability</a> is setting the future international agenda and comprehensively changing the way funders deal with research software.</p>
            <div style="display: flex; gap: 16px; flex-wrap: wrap;">
              <a href="/get-involved/" style="background-color: #f5c200; color: rgb(1, 95, 94); padding: 14px 28px; border-radius: 6px; text-decoration: none; font-size: 1.1rem; font-weight: bold; text-transform: uppercase; letter-spacing: 0.04em;">GET INVOLVED</a>
              <a href="/declaration/" style="background-color: white; color: rgb(1, 95, 94); padding: 14px 28px; border-radius: 6px; text-decoration: none; font-size: 1.1rem; font-weight: bold;">Read the Declaration</a>
            </div>
          </div>
          <div style="flex: 1; min-width: 280px;">
            <img src="/uploads/homepage-group.jpg" alt="Group discussing around a table" style="width: 100%; height: auto; border-radius: 8px; display: block;" />
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

        <div style="text-align: center; margin-top: 30px;">
          <a href="/signatories/" target="_self" 
            style="background-color: rgb(1, 95, 94); color: white; padding: 12px 25px; border-radius: 6px; text-decoration: none; display: inline-block; font-weight: bold;">
            View All Signatories
          </a>
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
        <div style="text-align: center;">
          <img src="/uploads/adore-logo-symbol.svg" alt="ADORE logo" style="width: 80px; height: 80px; display: block; margin: 0 auto 1.5rem;" />
          <h3 style="color: rgb(1, 95, 94);">Would you like to be involved in the adoption of the Declaration?</h3>
          <p style="font-size: 1.2rem; margin: 20px 0; color: rgb(1, 95, 94);">Become a Signatory!</p>
          <a href="/get-involved/" target="_self"
            style="background-color: #f5c200; color: rgb(1, 95, 94); padding: 15px 40px; border-radius: 0; text-decoration: none; display: inline-block; font-weight: 700; letter-spacing: 0.05em; text-transform: uppercase; margin: 20px 0;">
            GET INVOLVED
          </a>
        </div>
    design:
      spacing:
        padding: ["4rem", "2rem"]
      background:
        color: '#c5d0de'

---
