#!/usr/bin/env python3
"""
Script to update navigation across all HTML files in the website.
"""
import os
import re

# Navigation templates for different directory levels
def get_nav_template(prefix):
    """Generate navigation HTML based on relative path prefix"""
    return f'''        <nav class="nav">
            <div class="container">
                <div class="nav-inner">
                    <button class="nav-toggle" id="menuToggle">☰ Menu</button>
                    <ul class="nav-menu">
                        <li><a href="{prefix}index.html">Home</a></li>
                        <li class="has-dropdown">
                            <a href="{prefix}services/index.html">Services</a>
                            <ul class="dropdown">
                                <li><a href="{prefix}services/laptop-repairs.html">Laptop Repairs</a></li>
                                <li><a href="{prefix}services/mac-repairs.html">Mac Repairs</a></li>
                                <li><a href="{prefix}services/pc-repairs.html">PC Repairs</a></li>
                                <li><a href="{prefix}services/screen-repairs.html">Screen Repairs</a></li>
                                <li><a href="{prefix}services/data-recovery.html">Data Recovery</a></li>
                                <li><a href="{prefix}services/virus-removal.html">Virus Removal</a></li>
                                <li><a href="{prefix}services/upgrades.html">Computer Upgrades</a></li>
                                <li><a href="{prefix}services/index.html">View All Services</a></li>
                            </ul>
                        </li>
                        <li class="has-dropdown">
                            <a href="{prefix}services/laptop-repairs.html">Laptop Brands</a>
                            <ul class="dropdown">
                                <li><a href="{prefix}services/laptop-repairs/dell.html">Dell Laptop Repairs</a></li>
                                <li><a href="{prefix}services/laptop-repairs/hp.html">HP Laptop Repairs</a></li>
                                <li><a href="{prefix}services/laptop-repairs/lenovo.html">Lenovo Laptop Repairs</a></li>
                                <li><a href="{prefix}services/laptop-repairs/asus.html">Asus Laptop Repairs</a></li>
                                <li><a href="{prefix}services/laptop-repairs/acer.html">Acer Laptop Repairs</a></li>
                            </ul>
                        </li>
                        <li class="has-dropdown">
                            <a href="{prefix}services/mac-repairs.html">Mac Models</a>
                            <ul class="dropdown">
                                <li><a href="{prefix}services/mac-repairs/macbook-air.html">MacBook Air Repairs</a></li>
                                <li><a href="{prefix}services/mac-repairs/macbook-pro.html">MacBook Pro Repairs</a></li>
                                <li><a href="{prefix}services/mac-repairs/imac.html">iMac Repairs</a></li>
                                <li><a href="{prefix}services/mac-repairs.html">All Mac Repairs</a></li>
                            </ul>
                        </li>
                        <li><a href="{prefix}hills-district/index.html">Hills District</a></li>
                        <li><a href="{prefix}contact.html">Contact</a></li>
                    </ul>
                </div>
            </div>
        </nav>
        <!-- Mobile Menu -->
        <div id="mobileMenu" class="mobile-menu">
            <div class="mobile-menu-header">
                <img src="{prefix}assets/images/pronto-logo.svg" alt="Computer Repairs Pronto" class="logo-img">
                <button class="mobile-menu-close" id="menuClose">×</button>
            </div>
            <div class="mobile-menu-content">
                <ul>
                    <li><a href="{prefix}index.html">Home</a></li>
                    <li>
                        <a href="#" class="submenu-toggle">Services <span>+</span></a>
                        <div class="mobile-submenu">
                            <a href="{prefix}services/laptop-repairs.html">Laptop Repairs</a>
                            <a href="{prefix}services/mac-repairs.html">Mac Repairs</a>
                            <a href="{prefix}services/pc-repairs.html">PC Repairs</a>
                            <a href="{prefix}services/screen-repairs.html">Screen Repairs</a>
                            <a href="{prefix}services/data-recovery.html">Data Recovery</a>
                            <a href="{prefix}services/virus-removal.html">Virus Removal</a>
                            <a href="{prefix}services/upgrades.html">Computer Upgrades</a>
                            <a href="{prefix}services/index.html">View All Services</a>
                        </div>
                    </li>
                    <li>
                        <a href="#" class="submenu-toggle">Laptop Brands <span>+</span></a>
                        <div class="mobile-submenu">
                            <a href="{prefix}services/laptop-repairs/dell.html">Dell Repairs</a>
                            <a href="{prefix}services/laptop-repairs/hp.html">HP Repairs</a>
                            <a href="{prefix}services/laptop-repairs/lenovo.html">Lenovo Repairs</a>
                            <a href="{prefix}services/laptop-repairs/asus.html">Asus Repairs</a>
                            <a href="{prefix}services/laptop-repairs/acer.html">Acer Repairs</a>
                        </div>
                    </li>
                    <li>
                        <a href="#" class="submenu-toggle">Mac Models <span>+</span></a>
                        <div class="mobile-submenu">
                            <a href="{prefix}services/mac-repairs/macbook-air.html">MacBook Air Repairs</a>
                            <a href="{prefix}services/mac-repairs/macbook-pro.html">MacBook Pro Repairs</a>
                            <a href="{prefix}services/mac-repairs/imac.html">iMac Repairs</a>
                            <a href="{prefix}services/mac-repairs.html">All Mac Repairs</a>
                        </div>
                    </li>
                    <li><a href="{prefix}hills-district/index.html">Hills District</a></li>
                    <li><a href="{prefix}about.html">About</a></li>
                    <li><a href="{prefix}contact.html">Contact</a></li>
                </ul>
            </div>
            <div class="mobile-menu-cta">
                <a href="tel:0400454859">📞 Call 0400 454 859</a>
            </div>
        </div>
        <script>
        document.getElementById('menuToggle').addEventListener('click', function() {{
            document.getElementById('mobileMenu').classList.add('active');
        }});
        document.getElementById('menuClose').addEventListener('click', function() {{
            document.getElementById('mobileMenu').classList.remove('active');
        }});
        document.querySelectorAll('.submenu-toggle').forEach(function(toggle) {{
            toggle.addEventListener('click', function(e) {{
                e.preventDefault();
                var submenu = this.nextElementSibling;
                var span = this.querySelector('span');
                submenu.classList.toggle('active');
                span.textContent = submenu.classList.contains('active') ? '−' : '+';
            }});
        }});
        </script>
    </header>'''

def get_prefix_from_path(filepath):
    """Determine the relative path prefix based on file location"""
    # Count directory depth
    parts = filepath.replace('\\', '/').split('/')
    depth = len([p for p in parts if p and p != '.']) - 1  # -1 for the filename
    
    if depth == 0:
        return ""
    elif depth == 1:
        return "../"
    else:
        return "../" * depth

def update_file(filepath):
    """Update navigation in a single file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if file already has the new navigation
        if 'id="menuToggle"' in content and 'id="mobileMenu"' in content:
            print(f"Skipping {filepath} - already updated")
            return False
        
        # Check if file has old navigation
        if 'onclick="document.querySelector' not in content:
            print(f"Skipping {filepath} - no old navigation found")
            return False
        
        prefix = get_prefix_from_path(filepath)
        new_nav = get_nav_template(prefix)
        
        # Pattern to match old navigation (handles both formatted and minified versions)
        old_nav_pattern = r'<nav class="nav">.*?</nav>\s*</header>'
        
        # Replace old nav with new nav
        new_content = re.sub(old_nav_pattern, new_nav, content, flags=re.DOTALL)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filepath}")
            return True
        else:
            print(f"No changes made to {filepath}")
            return False
            
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def main():
    """Main function to update all HTML files"""
    base_dir = '.'
    updated_count = 0
    
    # Files to update
    files_to_check = []
    
    # Walk through directories
    for root, dirs, files in os.walk(base_dir):
        # Skip hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                files_to_check.append(filepath)
    
    print(f"Found {len(files_to_check)} HTML files to check")
    
    for filepath in files_to_check:
        if update_file(filepath):
            updated_count += 1
    
    print(f"\nUpdated {updated_count} files")

if __name__ == '__main__':
    main()
