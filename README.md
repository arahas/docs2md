# Docs-2-MD

A CLI tool that scrapes online documentation/tutorials and converts them to Markdown files for offline reading.

## Features

- Scrapes documentation/tutorials from a provided URL
- Follows internal links to capture the entire documentation
- Converts HTML content to Markdown format
- Saves metadata (source URL and capture timestamp)
- Preserves links and images in the output

## Installation

This project uses `uv` for package management. Make sure you have Python 3.12+ installed.

```bash
# Clone the repository
git clone https://github.com/yourusername/docs-2-md.git
cd docs-2-md

# Install dependencies
uv pip install -e .
```

## Usage

Basic usage:

```bash
docs2md https://example.com/docs
```

This will scrape the documentation from the provided URL and save the Markdown files to the `./output` directory.

### Options

- `--output-dir TEXT`: Directory to save markdown files (default: `./output`)
- `--max-pages INTEGER`: Maximum number of pages to scrape (default: 50)

### Examples

1. Scrape Python documentation:

```bash
docs2md https://docs.python.org/3/library/functions.html --max-pages 5
```

2. Scrape FastAPI tutorial:

```bash
docs2md https://fastapi.tiangolo.com/tutorial/first-steps/ --output-dir ./fastapi-docs
```

3. Scrape a GitHub README or wiki:

```bash
docs2md https://github.com/username/repo/wiki --max-pages 10
```

4. Scrape API documentation:

```bash
docs2md https://api.example.com/docs --output-dir ./api-docs
```

## How It Works

Docs-2-MD works by:

1. Starting at the provided URL
2. Downloading the HTML content
3. Converting the main content section to Markdown
4. Saving the content with metadata (source URL and timestamp)
5. Finding all internal links on the page
6. Visiting and converting those pages as well (up to the max-pages limit)

## Development

To set up the development environment:

```bash
# Create a virtual environment
uv venv

# Activate the virtual environment
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
uv pip install -e .
```
