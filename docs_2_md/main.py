#!/usr/bin/env python3
import os
import re
import sys
import time
import datetime
import argparse
import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import html2text

class DocumentationScraper:
    def __init__(self, url, output_dir="./output"):
        self.start_url = url
        self.base_url = f"{urlparse(url).scheme}://{urlparse(url).netloc}"
        self.domain = urlparse(url).netloc
        self.visited_urls = set()
        self.output_dir = output_dir
        self.html_converter = html2text.HTML2Text()
        self.html_converter.ignore_links = False
        self.html_converter.body_width = 0  # No wrapping
        self.html_converter.ignore_images = False
        self.html_converter.wrap_links = False
        self.html_converter.unicode_snob = True
        self.html_converter.default_image_alt = "image"

    def get_page_content(self, url):
        """Fetch the content of a page"""
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.text
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return None

    def is_same_domain(self, url):
        """Check if URL belongs to the same domain"""
        parsed_url = urlparse(url)
        return parsed_url.netloc == self.domain or not parsed_url.netloc

    def is_documentation_link(self, url):
        """Determine if a link is likely part of the documentation"""
        parsed_url = urlparse(url)
        path = parsed_url.path.lower()
        
        # Skip asset files, anchors, etc.
        skip_extensions = ['.css', '.js', '.png', '.jpg', '.jpeg', '.gif', '.svg', 
                          '.ico', '.woff', '.ttf', '.eot', '.pdf', '.zip']
        
        if any(path.endswith(ext) for ext in skip_extensions):
            return False
            
        # Skip URLs with query parameters or fragments only
        if not path and (parsed_url.query or parsed_url.fragment):
            return False
            
        return True

    def normalize_url(self, url, base_url):
        """Convert relative URLs to absolute URLs"""
        if not url:
            return None
            
        # Handle anchor links
        if url.startswith('#'):
            return None
            
        # Convert relative URLs to absolute
        absolute_url = urljoin(base_url, url)
        
        # Remove fragments from URLs
        absolute_url = absolute_url.split('#')[0]
        
        return absolute_url

    def extract_links(self, html, base_url):
        """Extract all links from a page"""
        soup = BeautifulSoup(html, 'html.parser')
        links = []
        
        for a_tag in soup.find_all('a', href=True):
            url = self.normalize_url(a_tag['href'], base_url)
            if url and self.is_same_domain(url) and self.is_documentation_link(url):
                links.append(url)
                
        return list(set(links))  # Remove duplicates

    def extract_title(self, html):
        """Extract title from page"""
        soup = BeautifulSoup(html, 'html.parser')
        title_tag = soup.find('title')
        if title_tag:
            return title_tag.text.strip()
        h1_tag = soup.find('h1')
        if h1_tag:
            return h1_tag.text.strip()
        return "Untitled"

    def extract_main_content(self, html):
        """Extract main content from page"""
        soup = BeautifulSoup(html, 'html.parser')
        
        # Try to find main content container
        main_content = None
        
        # Common content containers
        content_selectors = [
            'main', 'article', '.content', '.main-content', '#content', 
            '.documentation', '.docs-content', '.markdown-body', '.post-content',
            '.article-content', '.doc-content'
        ]
        
        for selector in content_selectors:
            if selector.startswith('#'):
                element = soup.find(id=selector[1:])
            elif selector.startswith('.'):
                element = soup.find(class_=selector[1:])
            else:
                element = soup.find(selector)
                
            if element:
                main_content = element
                break
        
        # If no content container found, use body
        if not main_content:
            main_content = soup.find('body')
            
        # If somehow still no content found, use the whole document
        if not main_content:
            main_content = soup
            
        return str(main_content)

    def html_to_markdown(self, html):
        """Convert HTML to Markdown"""
        return self.html_converter.handle(html)

    def clean_filename(self, text):
        """Convert text to safe filename"""
        # Replace non-alphanumeric characters with underscores
        safe_name = re.sub(r'[^a-zA-Z0-9]', '_', text)
        # Remove multiple consecutive underscores
        safe_name = re.sub(r'_+', '_', safe_name)
        # Truncate if too long
        if len(safe_name) > 100:
            safe_name = safe_name[:100]
        return safe_name.lower()

    def save_markdown(self, title, content, url):
        """Save content as Markdown file"""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
            
        filename = self.clean_filename(title) + '.md'
        filepath = os.path.join(self.output_dir, filename)
        
        # Add metadata
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        metadata = f"---\n"
        metadata += f"title: {title}\n"
        metadata += f"source: {url}\n"
        metadata += f"captured: {timestamp}\n"
        metadata += f"---\n\n"
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(metadata + content)
            
        return filepath

    def scrape_page(self, url):
        """Scrape a single page"""
        if url in self.visited_urls:
            return []
            
        self.visited_urls.add(url)
        print(f"Scraping: {url}")
        
        html = self.get_page_content(url)
        if not html:
            return []
            
        # Extract page title
        title = self.extract_title(html)
        
        # Extract main content
        main_content_html = self.extract_main_content(html)
        
        # Convert HTML to Markdown
        markdown_content = self.html_to_markdown(main_content_html)
        
        # Save to file
        saved_path = self.save_markdown(title, markdown_content, url)
        print(f"Saved to: {saved_path}")
        
        # Extract links for further scraping
        return self.extract_links(html, url)

    def scrape(self, max_pages=100):
        """Scrape documentation starting from start URL"""
        to_visit = [self.start_url]
        page_count = 0
        
        while to_visit and page_count < max_pages:
            current_url = to_visit.pop(0)
            new_links = self.scrape_page(current_url)
            
            # Add new links to visit queue
            for link in new_links:
                if link not in self.visited_urls and link not in to_visit:
                    to_visit.append(link)
            
            page_count += 1
            # Small delay to be nice to servers
            time.sleep(0.5)
            
        print(f"Completed scraping {page_count} pages.")
        print(f"Output directory: {os.path.abspath(self.output_dir)}")


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description="Convert online documentation to Markdown for offline reading")
    parser.add_argument("url", help="URL of the documentation to scrape")
    parser.add_argument("--output-dir", default="./output", help="Directory to save markdown files")
    parser.add_argument("--max-pages", type=int, default=50, help="Maximum number of pages to scrape")
    
    args = parser.parse_args()
    
    if not args.url.startswith(('http://', 'https://')):
        print("Error: URL must start with http:// or https://")
        return 1

    print(f"Starting to scrape documentation from: {args.url}")
    print(f"Output directory: {args.output_dir}")
    print(f"Maximum pages: {args.max_pages}")
    
    try:
        scraper = DocumentationScraper(args.url, args.output_dir)
        scraper.scrape(max_pages=args.max_pages)
        print("Documentation conversion completed successfully!")
        return 0
        
    except Exception as e:
        print(f"Error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main()) 