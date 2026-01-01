#!/usr/bin/env python3
"""
Fix mobile menu issues across all HTML files:
1. Replace favicon.svg with proper logo (prontositelogo.png)
2. Replace × character with SVG X icon for better compatibility
"""

import os
import re

# Define the correct logo path replacements and the SVG close icon
CLOSE_SVG = '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>'

def get_logo_path(file_path):
    """Calculate the correct relative path to the logo based on file location"""
    # Count directory depth from root
    parts = file_path.replace('\\', '/').split('/')
    # Filter out '.' and count actual subdirectories
    depth = 0
    for part in parts[:-1]:  # exclude filename
        if part not in ['.', '']:
            depth += 1
    
    if depth == 0:
        # Root level files
        return 'assets/images/prontositelogo.png'
    elif depth == 1:
        # One level deep (services/, hills-district/)
        return '../assets/images/prontositelogo.png'
    elif depth == 2:
        # Two levels deep (services/laptop-repairs/, services/mac-repairs/)
        return '../../assets/images/prontositelogo.png'
    return 'assets/images/prontositelogo.png'

def fix_html_file(file_path):
    """Fix the mobile menu in a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f'Error reading {file_path}: {e}')
        return False
    
    original_content = content
    logo_path = get_logo_path(file_path)
    
    # Fix 1: Replace favicon.svg logo with proper logo path in mobile menu header
    # Handle various patterns of favicon.svg paths
    content = re.sub(
        r'<img src="[^"]*favicon\.svg" alt="Computer Repairs Pronto" class="logo-img">',
        f'<img src="{logo_path}" alt="Computer Repairs Pronto" class="logo-img">',
        content
    )
    
    # Fix 2: Replace × character with SVG icon in close button
    # The × might be encoded as various characters
    close_button_new = f'<button class="mobile-menu-close" id="menuClose" aria-label="Close menu">{CLOSE_SVG}</button>'
    
    # Match the close button with × character (various encodings)
    content = re.sub(
        r'<button class="mobile-menu-close" id="menuClose">×</button>',
        close_button_new,
        content
    )
    content = re.sub(
        r'<button class="mobile-menu-close" id="menuClose">&times;</button>',
        close_button_new,
        content
    )
    content = re.sub(
        r'<button class="mobile-menu-close" id="menuClose">&#215;</button>',
        close_button_new,
        content
    )
    content = re.sub(
        r'<button class="mobile-menu-close" id="menuClose">&#xD7;</button>',
        close_button_new,
        content
    )
    
    if content != original_content:
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'Fixed: {file_path}')
            return True
        except Exception as e:
            print(f'Error writing {file_path}: {e}')
            return False
    else:
        print(f'No changes needed: {file_path}')
        return False

def main():
    """Find and fix all HTML files"""
    fixed_count = 0
    
    for root, dirs, files in os.walk('.'):
        # Skip hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                if fix_html_file(file_path):
                    fixed_count += 1
    
    print(f'\nTotal files fixed: {fixed_count}')

if __name__ == '__main__':
    main()
