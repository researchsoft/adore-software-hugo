# ADORE.software Hugo Website

This repository contains the Hugo static site for [adore.software](https://adore.software), the Amsterdam Declaration on Funding Research Software Sustainability.

## About ADORE.software

The Amsterdam Declaration on Funding Research Software Sustainability (ADORE.software) aims to raise awareness of the role of funding practice in the sustainability of research software, and to improve that practice.

## Structure

This is a Hugo static site based on the [Hugo Blox Builder](https://hugoblox.com/) framework (formerly Wowchemy), similar to the [Research Software Alliance website](https://researchsoft.org).

### Key Directories

- `content/` - Markdown content files for all pages and news
- `config/_default/` - Hugo configuration files
- `layouts/` - Custom Hugo templates and partials
- `static/` - Static assets (images, files)
- `assets/` - Asset processing (SCSS, JS)
- `data/themes/` - Custom theme configurations

## Local Development

### Prerequisites

- [Hugo Extended](https://gohugo.io/installation/) v0.140.0 or later
- [Go](https://go.dev/doc/install) 1.15 or later (for Hugo modules)

### Running Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/RichardLitt/adore-software-hugo.git
   cd adore-software-hugo
   ```

2. Download theme dependencies:
   ```bash
   hugo mod get
   ```

3. Start the Hugo development server:
   ```bash
   hugo server --buildDrafts
   ```

4. Open your browser to `http://localhost:1313`

### Building for Production

```bash
hugo --gc --minify
```

The generated site will be in the `public/` directory.

## Content Management

### Adding News Articles

Create a new directory under `content/news/` with an `index.md` file:

```bash
hugo new content/news/2026-04-my-article/index.md
```

Include frontmatter with title, date, authors, categories, and tags.

### Updating Pages

Edit the Markdown files in:
- `content/declaration/index.md` - The Declaration page
- `content/about/index.md` - About page
- `content/toolkit/index.md` - Toolkit page
- `content/get-involved/index.md` - Get Involved page
- `content/signatories/index.md` - Signatories list
- `content/faq/index.md` - FAQ page
- `content/contact/index.md` - Contact page

### Adding Signatories

The signatories page (`content/signatories/index.md`) can be updated to include new individuals and organizations who sign the Declaration.

## Deployment

This site is configured for deployment on Netlify or similar platforms. The Hugo build command is:

```bash
hugo --gc --minify --buildFuture
```

## Theme and Styling

The site uses Hugo Blox Builder modules:
- `blox-bootstrap/v5` - Main theme framework
- `blox-plugin-decap-cms` - CMS integration (optional)
- `blox-plugin-netlify` - Netlify-specific features

Custom styling can be added in `assets/scss/custom.scss`.

## Attribution

This website structure is based on the [Research Software Alliance website](https://github.com/researchsoft/website) and uses the Hugo Blox Builder framework.

## License

Website content is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

## Contact

For questions about the Amsterdam Declaration or this website, visit [adore.software/contact](https://adore.software/contact).

---

**Amsterdam Declaration on Research Software Sustainability**  
*Improving funding practices for sustainable research software*
