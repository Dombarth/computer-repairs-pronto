import os
import re

# List of suburb pages to update titles
suburbs = [
    ('baulkham-hills', 'Baulkham Hills'),
    ('bella-vista', 'Bella Vista'),
    ('carlingford', 'Carlingford'),
    ('cherrybrook', 'Cherrybrook'),
    ('dural', 'Dural'),
    ('glenhaven', 'Glenhaven'),
    ('glenorie', 'Glenorie'),
    ('kellyville', 'Kellyville'),
    ('kenthurst', 'Kenthurst'),
    ('north-rocks', 'North Rocks'),
    ('northmead', 'Northmead'),
    ('norwest', 'Norwest'),
    ('rouse-hill', 'Rouse Hill'),
    ('west-pennant-hills', 'West Pennant Hills'),
    ('winston-hills', 'Winston Hills'),
]

# Update titles for suburb pages
for filename, suburb_name in suburbs:
    filepath = f'hills-district/{filename}.html'
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update title tag
        old_title = f'<title>Computer Repair Help in {suburb_name} | Local Service</title>'
        new_title = f'<title>Computer Repair Help in {suburb_name}: Local Workshop Support</title>'
        content = content.replace(old_title, new_title)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Updated title: {filepath}')

# Now change "in Castle Hill" to "near Castle Hill" 
# but NOT in castle-hill.html page, and NOT in footer references to the main area
# Also keep "based in Castle Hill" but change "Workshop in Castle Hill" to "Workshop near Castle Hill"

def update_castle_hill_refs(content, is_castle_hill_page=False):
    if is_castle_hill_page:
        return content
    
    # Change "Workshop in Castle Hill" to "Workshop near Castle Hill"
    content = content.replace('Workshop in Castle Hill', 'Workshop near Castle Hill')
    
    # Change "workshop in Castle Hill" to "workshop near Castle Hill" 
    content = content.replace('workshop in Castle Hill', 'workshop near Castle Hill')
    
    # Change "based in Castle Hill" to "based near Castle Hill" only in meta descriptions
    # Actually the user wants all references to change to "near"
    content = content.replace('based in Castle Hill', 'based near Castle Hill')
    
    return content

# Process all HTML files
html_files = []
for root, dirs, files in os.walk('.'):
    # Skip hidden directories
    dirs[:] = [d for d in dirs if not d.startswith('.')]
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

for filepath in html_files:
    is_castle_hill = 'castle-hill.html' in filepath
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    content = update_castle_hill_refs(content, is_castle_hill)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Updated Castle Hill refs: {filepath}')

print('Done!')
