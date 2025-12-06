# AI Humanoid Robotics Book

A comprehensive, research-backed book on AI Humanoid Robotics built with Docusaurus, Spec-Kit Plus, and Claude Code.

## Overview

This book provides a practical foundation for understanding and developing AI humanoid robotics, integrating core concepts from AI (perception, control, planning, cognition) with practical aspects of robotics hardware, software development, and ethical considerations.

## Project Structure

```
.
├── docs/                    # Book chapters (MDX format)
│   ├── 00-preface.mdx
│   ├── 01-introduction.mdx
│   ├── ... (chapters 02-11)
│   └── references.md
├── specs/                   # Spec-Kit Plus specifications
│   └── 001-robotics-book/
│       ├── index.yaml
│       ├── chapters.yaml
│       ├── quality.yaml
│       └── reproducibility.yaml
├── static/                  # Static assets
│   └── img/                 # Diagrams and figures
├── src/                     # Source files
│   └── css/
│       └── custom.css       # Custom styles
├── docusaurus.config.ts     # Docusaurus configuration
├── sidebars.ts              # Sidebar configuration
└── package.json             # Dependencies and scripts
```

## Prerequisites

- **Node.js**: Version 18 or higher
- **npm**: Comes with Node.js

## Getting Started

### Installation

```bash
npm install
```

### Local Development

Start the development server:

```bash
npm start
```

The site will be available at `http://localhost:3000`.

The development server supports hot-reloading, so changes to files will automatically refresh in the browser.

### Building for Production

Build the static site:

```bash
npm run build
```

This generates a `build/` directory with static HTML files ready for deployment.

### Preview Production Build

To preview the production build locally:

```bash
npm run serve
```

This serves the `build/` directory locally.

## Contributing

### Adding Content

1. **Chapters**: Edit the corresponding `.mdx` file in the `docs/` directory
2. **Images**: Place diagrams and figures in `static/img/`
3. **References**: Add citations to `docs/references.md` in APA format

### Content Guidelines

- **Citations**: All factual claims must include inline APA citations
- **Sources**: Minimum 15 credible references, with ≥50% from peer-reviewed journals
- **Readability**: Target Flesch-Kincaid grade 10-12
- **Code Examples**: All code snippets must be runnable (MWEs - Minimal Working Examples)
- **Reproducibility**: Include environment, dependencies, commands, and expected outputs

### Quality Checks

Before submitting:

- [ ] Run `npm run build` to ensure the site builds without errors
- [ ] Verify all links work correctly
- [ ] Check that citations are properly formatted (APA style)
- [ ] Ensure code examples are runnable
- [ ] Review readability scores

## Deployment

### GitHub Pages

The site can be deployed to GitHub Pages using the `deploy` script:

```bash
npm run deploy
```

This will:
1. Build the site
2. Deploy to the `gh-pages` branch
3. Make it available at `https://<username>.github.io/<repo-name>/`

### Configuration

Update `docusaurus.config.ts` with your repository details:

```typescript
url: 'https://your-username.github.io',
baseUrl: '/your-repo-name/',
organizationName: 'your-username',
projectName: 'your-repo-name',
```

## Project Specifications

This project follows Spec-Driven Development (SDD) principles. See:

- **Specification**: `specs/001-robotics-book/spec.md`
- **Plan**: `specs/001-robotics-book/plan.md`
- **Tasks**: `specs/001-robotics-book/tasks.md`
- **Quality Standards**: `specs/001-robotics-book/quality.yaml`
- **Reproducibility**: `specs/001-robotics-book/reproducibility.yaml`

## License

[Add your license here]

## Acknowledgments

Built with:
- [Docusaurus](https://docusaurus.io/)
- [Spec-Kit Plus](https://github.com/specify/spec-kit-plus)
- [Claude Code](https://claude.ai/)

