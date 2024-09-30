import os
import re
import argparse
from datetime import datetime
import frontmatter
import yaml

def clean_frontmatter(metadata):
    properties_to_remove = ['id', 'blogger_blog', 'blogger_permalink', 'author', 'layout', 'guid']
    for prop in properties_to_remove:
        metadata.pop(prop, None)
    return metadata

def process_title(metadata, content):
    title = metadata.get('title')
    if title:
        content = f"# {title}\n\n{content}"
        metadata.pop('title')
    return metadata, content

def process_markdown_file(file_path):
    filename = os.path.basename(file_path)
    if not filename.endswith('.md'):
        raise ValueError(f"File {filename} is not a Markdown file")

    filename_pattern = r'(\d{4}-\d{2}-\d{2})-(.+)\.md'
    match = re.match(filename_pattern, filename)
    if not match:
        raise ValueError(f"Filename {filename} does not match the required pattern")

    date_str, slug = match.groups()

    with open(file_path, 'r', encoding='utf-8') as file:
        post = frontmatter.load(file)

    post.metadata = clean_frontmatter(post.metadata)
    post.metadata['date'] = datetime.strptime(date_str, '%Y-%m-%d').date()
    post.metadata['slug'] = slug

    post.metadata, post.content = process_title(post.metadata, post.content)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(frontmatter.dumps(post))

    print(f"Processed: {filename}")

def collect_categories_and_tags(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        post = frontmatter.load(file)
    
    categories = set(post.metadata.get('categories', []))
    tags = set(post.metadata.get('tags', []))
    
    return categories, tags

def extract_links(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        post = frontmatter.load(file)
    
    # Regular expression to match Markdown links
    link_pattern = r'\[([^\]]+)\]\(([^\)]+)\)'
    
    links = re.findall(link_pattern, post.content)
    return links

def process_markdown_files(directory):
    all_categories = set()
    all_tags = set()
    all_links = set()

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            process_markdown_file(file_path)
            categories, tags = collect_categories_and_tags(file_path)
            links = extract_links(file_path)
            
            all_categories.update(categories)
            all_tags.update(tags)
            all_links.update(links)
        except ValueError as e:
            print(f"Skipping {filename}: {str(e)}")

    # Dump categories and tags to files
    with open('/tmp/categories', 'w', encoding='utf-8') as f:
        for category in sorted(all_categories):
            f.write(f"{category}\n")

    with open('/tmp/tags', 'w', encoding='utf-8') as f:
        for tag in sorted(all_tags):
            f.write(f"{tag}\n")

    # Dump links to a file
    with open('/tmp/links', 'w', encoding='utf-8') as f:
        for link_text, link_url in sorted(all_links):
            f.write(f"{link_text}: {link_url}\n")

    print(f"Categories written to /tmp/categories")
    print(f"Tags written to /tmp/tags")
    print(f"Links written to /tmp/links")

def main():
    parser = argparse.ArgumentParser(description="Process Markdown files in a specified directory.")
    parser.add_argument("directory", help="Path to the directory containing Markdown files")
    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        print(f"Error: {args.directory} is not a valid directory")
        return

    process_markdown_files(args.directory)

if __name__ == "__main__":
    main()
