#!/usr/bin/env python3
"""
Fix mobile submenu to include the 6 new services in all HTML files.
This version properly preserves the Services toggle link.
"""

import os
import re

def get_new_services_links(prefix):
    """Generate the new services links with the appropriate path prefix."""
    links = [
        ('laptop-repairs.html', 'Laptop Repairs'),
        ('mac-repairs.html', 'Mac Repairs'),
        ('pc-repairs.html', 'PC Repairs'),
        ('screen-repairs.html', 'Screen Repairs'),
        ('data-recovery.html', 'Data Recovery'),
        ('virus-removal.html', 'Virus Removal'),
        ('electronics-repair.html', 'Electronics Repair'),
        ('board-level-repair.html', 'Board Level Repair'),
        ('charging-port-repair.html', 'Charging Port Repair'),
        ('audio-repair.html', 'Audio Repair'),
        ('monitor-repair.html', 'Monitor Repair'),
        ('console-repair.html', 'Console Repair'),
        ('upgrades.html', 'Computer Upgrades'),
        ('index.html', 'View All Services'),
    ]
    
    result = []
    for href, text in links:
        result.append(f'                            <a href="{prefix}{href}">{text}</a>')
    return '\n'.join(result)

def get_directory_type(filepath):
    """Determine which path prefix to use based on file location."""
    filepath = filepath.replace('\\', '/')
    if '/services/laptop-repairs/' in filepath or '/services/mac-repairs/' in filepath:
        return '../'  # Two levels deep
    elif filepath.startswith('services/'):
        return ''  # One level deep, no prefix needed
    elif filepath.startswith('hills-district/'):
        return '../services/'  # Need to go up and into services
    else:
        return 'services/'  # Root level, need to go into services

def fix_mobile_submenu(filepath):
    """Fix the mobile services submenu in a single file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if this file has a mobile submenu that needs updating
        # Pattern to find the Services mobile submenu - match everything from toggle to closing div
        pattern = r'(<a href="#" class="submenu-toggle">Services <span>\+</span></a>\s*<div class="mobile-submenu">)(.*?)(</div>)'
        
        match = re.search(pattern, content, re.DOTALL)
        if not match:
            # Try alternate pattern without toggle
            alt_pattern = r'(<li>\s*<div class="mobile-submenu">)(.*?)(</div>\s*</li>)'
            alt_match = re.search(alt_pattern, content, re.DOTALL)
            if alt_match and 'laptop-repairs' in alt_match.group(2):
                # This is a broken submenu from previous script run
                prefix = get_directory_type(filepath)
                new_links = get_new_services_links(prefix)
                new_submenu = f'''<li>
                        <a href="#" class="submenu-toggle">Services <span>+</span></a>
                        <div class="mobile-submenu">
{new_links}
                        </div>
                    </li>'''
                content = content.replace(alt_match.group(0), new_submenu)
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"  Fixed broken submenu in: {filepath}")
                return True
            else:
                print(f"  No Services mobile submenu found in {filepath}")
                return False
        
        # Check if it already has the new services
        if 'electronics-repair' in match.group(2):
            print(f"  Already has new services in {filepath}")
            return False
        
        # Get the appropriate path prefix
        prefix = get_directory_type(filepath)
        new_links = get_new_services_links(prefix)
        
        # Replace the old submenu content with the new one
        old_submenu = match.group(2)
        new_submenu_content = f'''
{new_links}
                        '''
        
        content = content.replace(match.group(0), match.group(1) + new_submenu_content + match.group(3))
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"  Updated: {filepath}")
        return True
    
    except Exception as e:
        print(f"  Error processing {filepath}: {e}")
        return False

def main():
    """Main function to process all HTML files."""
    updated_count = 0
    
    # Process root HTML files
    print("\nProcessing root HTML files...")
    for filename in os.listdir('.'):
        if filename.endswith('.html'):
            if fix_mobile_submenu(filename):
                updated_count += 1
    
    # Process services directory
    print("\nProcessing services directory...")
    if os.path.exists('services'):
        for filename in os.listdir('services'):
            if filename.endswith('.html'):
                filepath = f'services/{filename}'
                if fix_mobile_submenu(filepath):
                    updated_count += 1
    
    # Process services/laptop-repairs directory
    print("\nProcessing services/laptop-repairs directory...")
    if os.path.exists('services/laptop-repairs'):
        for filename in os.listdir('services/laptop-repairs'):
            if filename.endswith('.html'):
                filepath = f'services/laptop-repairs/{filename}'
                if fix_mobile_submenu(filepath):
                    updated_count += 1
    
    # Process services/mac-repairs directory
    print("\nProcessing services/mac-repairs directory...")
    if os.path.exists('services/mac-repairs'):
        for filename in os.listdir('services/mac-repairs'):
            if filename.endswith('.html'):
                filepath = f'services/mac-repairs/{filename}'
                if fix_mobile_submenu(filepath):
                    updated_count += 1
    
    # Process hills-district directory
    print("\nProcessing hills-district directory...")
    if os.path.exists('hills-district'):
        for filename in os.listdir('hills-district'):
            if filename.endswith('.html'):
                filepath = f'hills-district/{filename}'
                if fix_mobile_submenu(filepath):
                    updated_count += 1
    
    print(f"\nTotal files updated: {updated_count}")

if __name__ == '__main__':
    main()
