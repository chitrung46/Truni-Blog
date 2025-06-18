# Personal Blog

A modern, responsive blog built with Jekyll and designed for sharing knowledge about Deep Learning and Technology.

## Features

- Clean and modern design
- Responsive layout
- Blog posts with LaTeX support
- Project showcase
- CV/Resume page
- Tag-based navigation
- Pagination
- SEO optimized

## Getting Started

### Prerequisites

- Ruby (version 2.5.0 or higher)
- RubyGems
- GCC and Make

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/yourusername.github.io.git
cd yourusername.github.io
```

2. Install dependencies:
```bash
bundle install
```

3. Start the local server:
```bash
bundle exec jekyll serve
```

4. Visit `http://localhost:4000` in your browser

## Writing Posts

1. Create a new file in the `_posts` directory with the format: `YYYY-MM-DD-title.md`
2. Add the following front matter at the top of your post:

```yaml
---
layout: post
title: "Your Post Title"
date: YYYY-MM-DD
author: Your Name
tags: [Tag1, Tag2]
---
```

3. Write your content using Markdown syntax
4. For LaTeX equations, use the following syntax:
   - Inline math: `$equation$`
   - Block math: `$$equation$$`

## Customization

- Edit `_config.yml` to change site settings
- Modify `assets/css/main.css` to customize styles
- Update layouts in `_layouts` directory to change page structure

## Deployment

This site is designed to be deployed on GitHub Pages. Simply push your changes to the main branch of your repository, and GitHub Pages will automatically build and deploy your site.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 