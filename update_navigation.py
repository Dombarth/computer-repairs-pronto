#!/usr/bin/env python3
"""
Script to update navigation menus and footer links across all HTML files
to include the 6 new service pages.
"""

import os
import re
from pathlib import Path

# New service pages to add
NEW_SERVICES = [
    ('electronics-repair.html', 'Electronics Repair'),
    ('board-level-repair.html', 'Board Level Repair'),
    ('charging-port-repair.html', 'Charging Port Repair'),
    ('audio-repair.html', 'Audio Repair'),
    ('monitor-repair.html', 'Monitor Repair'),
    ('console-repair.html', 'Console Repair'),
]

def update_services_nav(content, prefix=''):
    """Update the Services dropdown navigation with new services."""
    # Find the Services dropdown - after virus-removal and before upgrades
    if prefix:
        pattern = rf'(<li><a href="{re.escape(prefix)}virus-removal\.html">Virus Removal</a></li>\s*\n\s*<li><a href="{re.escape(prefix)}upgrades\.html">Computer Upgrades</a></li>)'
    else:
        pattern = r'(<li><a href="virus-removal\.html">Virus Removal</a></li>\s*\n\s*<li><a href="upgrades\.html">Computer Upgrades</a></li>)'
    
    new_items = '\n'.join([f'                                <li><a href="{prefix}{href}">{text}</a></li>' 
                          for href, text in NEW_SERVICES])
    
    if prefix:
        replacement = f'''<li><a href="{prefix}virus-removal.html">Virus Removal</a></li>
{new_items}
                                <li><a href="{prefix}upgrades.html">Computer Upgrades</a></li>'''
    else:
        replacement = f'''<li><a href="virus-removal.html">Virus Removal</a></li>
{new_items}
                                <li><a href="upgrades.html">Computer Upgrades</a></li>'''
    
    return re.sub(pattern, replacement, content)

def update_mobile_nav(content, prefix=''):
    """Update the mobile navigation submenu with new services."""
    if prefix:
        pattern = rf'(<a href="{re.escape(prefix)}virus-removal\.html">Virus Removal</a>\s*\n\s*<a href="{re.escape(prefix)}index\.html">View All Services</a>)'
    else:
        pattern = r'(<a href="virus-removal\.html">Virus Removal</a>\s*\n\s*<a href="index\.html">View All Services</a>)'
    
    new_items = '\n'.join([f'                            <a href="{prefix}{href}">{text}</a>' 
                          for href, text in NEW_SERVICES])
    
    if prefix:
        replacement = f'''<a href="{prefix}virus-removal.html">Virus Removal</a>
{new_items}
                            <a href="{prefix}index.html">View All Services</a>'''
    else:
        replacement = f'''<a href="virus-removal.html">Virus Removal</a>
{new_items}
                            <a href="index.html">View All Services</a>'''
    
    return re.sub(pattern, replacement, content)

def update_footer(content, prefix=''):
    """Update the footer Services section with new services."""
    # Find the footer Services section - after Virus Removal
    if prefix:
        pattern = rf'(<li><a href="{re.escape(prefix)}virus-removal\.html">Virus Removal</a></li></ul></div><div class="footer-nav"><h4>Areas</h4>)'
    else:
        pattern = r'(<li><a href="virus-removal\.html">Virus Removal</a></li></ul></div><div class="footer-nav"><h4>Areas</h4>)'
    
    new_items = '\n'.join([f'<li><a href="{prefix}{href}">{text}</a></li>' 
                          for href, text in NEW_SERVICES])
    
    if prefix:
        replacement = f'''<li><a href="{prefix}virus-removal.html">Virus Removal</a></li>
{new_items}</ul></div><div class="footer-nav"><h4>Areas</h4>'''
    else:
        replacement = f'''<li><a href="virus-removal.html">Virus Removal</a></li>
{new_items}</ul></div><div class="footer-nav"><h4>Areas</h4>'''
    
    return re.sub(pattern, replacement, content)

def update_internal_links(content, filename):
    """Add internal links section to the new service pages."""
    # Only add to the new service pages
    if filename not in [s[0] for s in NEW_SERVICES]:
        return content
    
    # Find the contact-box section and add related services before it
    pattern = r'(<div class="contact-box">)'
    
    # Determine related services based on current page
    related_services = []
    for href, text in NEW_SERVICES:
        if href != filename:
            related_services.append(f'<li><a href="{href}">{text}</a></li>')
    
    # Add some existing services too
    existing_services = [
        ('laptop-repairs.html', 'Laptop Repairs'),
        ('mac-repairs.html', 'Mac Repairs'),
        ('screen-repairs.html', 'Screen Repairs'),
    ]
    for href, text in existing_services[:2]:
        related_services.append(f'<li><a href="{href}">{text}</a></li>')
    
    related_html = '\n                    '.join(related_services[:4])
    
    internal_links = f'''<h2>Related Services</h2>
                <ul class="service-list">
                    {related_html}
                </ul>

                \\g<1>'''
    
    return re.sub(pattern, internal_links, content)

def get_prefix(filepath):
    """Determine the URL prefix based on file location."""
    filepath = filepath.replace('\\', '/')
    
    if '/services/laptop-repairs/' in filepath:
        return '../'
    elif '/services/mac-repairs/' in filepath:
        return '../'
    elif '/services/' in filepath:
        return ''
    elif '/hills-district/' in filepath:
        return '../services/'
    else:
        return 'services/'

def process_file(filepath):
    """Process a single HTML file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    filename = os.path.basename(filepath)
    
    # Determine the prefix based on file location
    prefix = get_prefix(filepath)
    
    # Update desktop navigation
    content = update_services_nav(content, prefix)
    
    # Update mobile navigation
    content = update_mobile_nav(content, prefix)
    
    # Update footer
    content = update_footer(content, prefix)
    
    # Add internal links to new service pages
    if '/services/' in filepath.replace('\\', '/') and '/laptop-repairs/' not in filepath.replace('\\', '/') and '/mac-repairs/' not in filepath.replace('\\', '/'):
        content = update_internal_links(content, filename)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    """Main function to process all HTML files."""
    # Get all HTML files in the project
    html_files = []
    for root, dirs, files in os.walk('.'):
        # Skip node_modules and other non-essential directories
        if 'node_modules' in root or '.git' in root:
            continue
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    
    updated = 0
    for filepath in html_files:
        if process_file(filepath):
            print(f"Updated: {filepath}")
            updated += 1
    
    print(f"\nTotal files updated: {updated}")

if __name__ == '__main__':
    main()
