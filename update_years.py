import os
import re

# Walk through all HTML files
for root, dirs, files in os.walk('.'):
    # Skip hidden directories
    dirs[:] = [d for d in dirs if not d.startswith('.')]
    
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original = content
            
            # Replace "over nineteen years" with "over twenty years"
            content = content.replace('over nineteen years', 'over twenty years')
            
            # Replace "nearly twenty years" with "over twenty years"
            content = content.replace('nearly twenty years', 'over twenty years')
            
            if content != original:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f'Updated: {filepath}')

print('Done!')
