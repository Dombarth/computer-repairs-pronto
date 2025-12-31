import os

# Walk through all HTML files and Python files
for root, dirs, files in os.walk('.'):
    # Skip hidden directories
    dirs[:] = [d for d in dirs if not d.startswith('.')]
    
    for file in files:
        if file.endswith('.html') or file.endswith('.py'):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original = content
                
                # Replace pronto-logo.svg with prontositelogo.png
                content = content.replace('pronto-logo.svg', 'prontositelogo.png')
                
                # Also replace pronto-logo.png with prontositelogo.png (if any)
                content = content.replace('pronto-logo.png', 'prontositelogo.png')
                
                if content != original:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f'Updated: {filepath}')
            except Exception as e:
                print(f'Error with {filepath}: {e}')

print('Done!')
