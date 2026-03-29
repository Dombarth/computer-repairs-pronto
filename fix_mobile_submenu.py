#!/usr/bin/env python3
"""
Fix mobile submenu to include the 6 new services in all HTML files.
"""

import os
import re

# The new mobile submenu content for services
NEW_SERVICES_SUBMENU = '''                        <div class="mobile-submenu">
                            <a href="laptop-repairs.html">Laptop Repairs</a>
                            <a href="mac-repairs.html">Mac Repairs</a>
                            <a href="pc-repairs.html">PC Repairs</a>
                            <a href="screen-repairs.html">Screen Repairs</a>
                            <a href="data-recovery.html">Data Recovery</a>
                            <a href="virus-removal.html">Virus Removal</a>
                            <a href="electronics-repair.html">Electronics Repair</a>
                            <a href="board-level-repair.html">Board Level Repair</a>
                            <a href="charging-port-repair.html">Charging Port Repair</a>
                            <a href="audio-repair.html">Audio Repair</a>
                            <a href="monitor-repair.html">Monitor Repair</a>
                            <a href="console-repair.html">Console Repair</a>
                            <a href="upgrades.html">Computer Upgrades</a>
                            <a href="index.html">View All Services</a>
                        </div>'''

# For files in root directory (index.html, about.html, etc.)
NEW_SERVICES_SUBMENU_ROOT = '''                        <div class="mobile-submenu">
                            <a href="services/laptop-repairs.html">Laptop Repairs</a>
                            <a href="services/mac-repairs.html">Mac Repairs</a>
                            <a href="services/pc-repairs.html">PC Repairs</a>
                            <a href="services/screen-repairs.html">Screen Repairs</a>
                            <a href="services/data-recovery.html">Data Recovery</a>
                            <a href="services/virus-removal.html">Virus Removal</a>
                            <a href="services/electronics-repair.html">Electronics Repair</a>
                            <a href="services/board-level-repair.html">Board Level Repair</a>
                            <a href="services/charging-port-repair.html">Charging Port Repair</a>
                            <a href="services/audio-repair.html">Audio Repair</a>
                            <a href="services/monitor-repair.html">Monitor Repair</a>
                            <a href="services/console-repair.html">Console Repair</a>
                            <a href="services/upgrades.html">Computer Upgrades</a>
                            <a href="services/index.html">View All Services</a>
                        </div>'''

# For files in hills-district directory
NEW_SERVICES_SUBMENU_HILLS = '''                        <div class="mobile-submenu">
                            <a href="../services/laptop-repairs.html">Laptop Repairs</a>
                            <a href="../services/mac-repairs.html">Mac Repairs</a>
                            <a href="../services/pc-repairs.html">PC Repairs</a>
                            <a href="../services/screen-repairs.html">Screen Repairs</a>
                            <a href="../services/data-recovery.html">Data Recovery</a>
                            <a href="../services/virus-removal.html">Virus Removal</a>
                            <a href="../services/electronics-repair.html">Electronics Repair</a>
                            <a href="../services/board-level-repair.html">Board Level Repair</a>
                            <a href="../services/charging-port-repair.html">Charging Port Repair</a>
                            <a href="../services/audio-repair.html">Audio Repair</a>
                            <a href="../services/monitor-repair.html">Monitor Repair</a>
                            <a href="../services/console-repair.html">Console Repair</a>
                            <a href="../services/upgrades.html">Computer Upgrades</a>
                            <a href="../services/index.html">View All Services</a>
                        </div>'''

# For files in services/laptop-repairs and services/mac-repairs subdirectories
NEW_SERVICES_SUBMENU_SUBDIR = '''                        <div class="mobile-submenu">
                            <a href="../laptop-repairs.html">Laptop Repairs</a>
                            <a href="../mac-repairs.html">Mac Repairs</a>
                            <a href="../pc-repairs.html">PC Repairs</a>
                            <a href="../screen-repairs.html">Screen Repairs</a>
                            <a href="../data-recovery.html">Data Recovery</a>
                            <a href="../virus-removal.html">Virus Removal</a>
                            <a href="../electronics-repair.html">Electronics Repair</a>
                            <a href="../board-level-repair.html">Board Level Repair</a>
                            <a href="../charging-port-repair.html">Charging Port Repair</a>
                            <a href="../audio-repair.html">Audio Repair</a>
                            <a href="../monitor-repair.html">Monitor Repair</a>
                            <a href="../console-repair.html">Console Repair</a>
                            <a href="../upgrades.html">Computer Upgrades</a>
                            <a href="../index.html">View All Services</a>
                        </div>'''

def get_directory_type(filepath):
    """Determine which submenu format to use based on file location."""
    filepath = filepath.replace('\\', '/')
    if '/services/laptop-repairs/' in filepath or '/services/mac-repairs/' in filepath:
        return 'subdir'
    elif filepath.startswith('services/'):
        return 'services'
    elif filepath.startswith('hills-district/'):
        return 'hills'
    else:
        return 'root'

def fix_mobile_submenu(filepath):
    """Fix the mobile services submenu in a single file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if this file has a mobile submenu that needs updating
        # Pattern to find the Services mobile submenu
        pattern = r'(<a href="#" class="submenu-toggle">Services <span>\+</span></a>\s*<div class="mobile-submenu">)(.*?)(</div>)'
        
        match = re.search(pattern, content, re.DOTALL)
        if not match:
            print(f"  No Services mobile submenu found in {filepath}")
            return False
        
        # Check if it already has the new services
        if 'electronics-repair' in match.group(2):
            print(f"  Already has new services in {filepath}")
            return False
        
        # Get the appropriate replacement
        dir_type = get_directory_type(filepath)
        if dir_type == 'root':
            new_submenu = NEW_SERVICES_SUBMENU_ROOT
        elif dir_type == 'hills':
            new_submenu = NEW_SERVICES_SUBMENU_HILLS
        elif dir_type == 'subdir':
            new_submenu = NEW_SERVICES_SUBMENU_SUBDIR
        else:  # services
            new_submenu = NEW_SERVICES_SUBMENU
        
        # Replace the old submenu with the new one
        old_full = match.group(0)
        content = content.replace(old_full, new_submenu)
        
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
