---
title:
date: 2024-01-01
type: landing
layout: "default"

sections:
  - block: markdown
    content: 
      title:
      text: |
        # Research software is a critical part of research
        {style="color: white; font-size: 3rem; text-align: center; font-weight: bold; margin-bottom: 2rem;"}

        The [Amsterdam Declaration on Funding Research Software Sustainability](declaration/) is setting the future international agenda and comprehensively changing the way funders deal with research software.
        {style="color: white; font-size: 1.5rem; text-align: center; line-height: 1.6;"}
        
        <div style="text-align: center; margin-top: 40px; display: flex; gap: 20px; justify-content: center; flex-wrap: wrap;">
          <a href="/get-involved/" target="_self" 
            style="background-color: #0066cc; color: white; padding: 15px 30px; border-radius: 6px; text-decoration: none; display: inline-block; font-size: 1.2rem; font-weight: bold;">
            GET INVOLVED
          </a>
          <a href="/declaration/" target="_self" 
            style="background-color: white; color: #0066cc; padding: 15px 30px; border-radius: 6px; text-decoration: none; display: inline-block; font-size: 1.2rem; font-weight: bold;">
            Read the Declaration
          </a>
        </div>

    design:
      background:
        gradient_start: '#0066cc'
        gradient_end: '#004499'
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

  - block: collection
    id: news
    content:
      title: Latest News
      subtitle: ''
      text: ''
      count: 4
      filters:
        folders:
          - news
        author: ""
        category: ""
        tag: ""
        exclude_featured: false
        exclude_future: false
        exclude_past: false
        publication_type: ""
      offset: 0
      order: desc
      page_type: news
    design:
      view: card
      columns: '2'
      spacing:
        padding: ["4rem", "2rem"]

  - block: markdown
    content:
      title: "Signatories"
      text: |
        See the full list of [individuals and organizations](signatories/) who have signed the Amsterdam Declaration.
        
        <div style="text-align: center; margin-top: 30px;">
          <a href="/signatories/" target="_self" 
            style="background-color: #0066cc; color: white; padding: 12px 25px; border-radius: 6px; text-decoration: none; display: inline-block; font-weight: bold;">
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
      title: "#ADOREsoftware"
      text: |
        <div style="text-align: center;">
          <h3>Would you like to be involved in the adoption of the Declaration?</h3>
          <p style="font-size: 1.2rem; margin: 20px 0;">Become a Signatory!</p>
          
          <a href="/get-involved/" target="_self" 
            style="background-color: #0066cc; color: white; padding: 15px 30px; border-radius: 6px; text-decoration: none; display: inline-block; font-weight: bold; margin: 20px 0;">
            GET INVOLVED
          </a>
          
          <p style="margin-top: 30px;">
            <a href="https://twitter.com/search?q=%23AdoreSoftware&src=typed_query" target="_blank" 
              style="color: #0066cc; text-decoration: none; font-weight: bold;">
              FOLLOW US ON TWITTER
            </a>
          </p>
        </div>
    design:
      spacing:
        padding: ["4rem", "2rem"]
      background:
        gradient_start: '#0066cc'
        gradient_end: '#004499'
        text_color_light: true

  - block: markdown
    content:
      title: "Sign up to receive updates about ADORE.software"
      text: |
        <div style="text-align: center;">
          <p>Stay informed about the Amsterdam Declaration and research software funding developments.</p>
          <a href="https://dashboard.mailerlite.com/forms/778129/110635094443558050/share" target="_blank" 
            style="background-color: white; color: #0066cc; padding: 12px 25px; border-radius: 6px; text-decoration: none; display: inline-block; font-weight: bold; margin-top: 20px;">
            SUBSCRIBE TO ReSA NEWSLETTER
          </a>
        </div>
    design:
      spacing:
        padding: ["4rem", "2rem"]
---
