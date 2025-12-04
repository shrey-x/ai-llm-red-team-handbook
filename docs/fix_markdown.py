#!/usr/bin/env python3
"""
Markdown Fixer Script
Fixes common markdown linting issues in the AI LLM Red Team Handbook
"""

import re
import sys

def fix_markdown(content):
    """Apply all markdown fixes"""
    lines = content.split('\n')
    fixed_lines = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Fix MD009: Remove trailing spaces (except intentional line breaks)
        if line.endswith(' ') and not line.endswith('  '):
            line = line.rstrip()
        
        # Fix MD036: Convert bold headings to proper headings
        # Pattern: Line starts with ** and ends with ** (bold used as heading)
        if re.match(r'^\*\*[^*]+\*\*\s*:?\s*$', line):
            # Check if previous line is empty (good indicator it's a heading)
            if i > 0 and (not fixed_lines or fixed_lines[-1].strip() == ''):
                # Remove the ** and convert to heading
                heading_text = line.strip('*').strip().rstrip(':')
                # Use ### for subsection headings
                line = f'### {heading_text}'
        
        # Fix MD040: Add language to code blocks without language specifier
        if line.strip() == '```' and i + 1 < len(lines):
            # Check what kind of content follows
            next_line = lines[i + 1] if i + 1 < len(lines) else ''
            
            # Determine language based on content
            if next_line.strip().startswith(('def ', 'class ', 'import ', 'from ', 'print(', 'for ', 'if ', 'return')):
                line = '```python'
            elif next_line.strip().startswith(('const ', 'let ', 'var ', 'function ', 'class ', '=>')):
                line = '```javascript'
            elif next_line.strip().startswith(('$', '#', 'cd ', 'ls ', 'mkdir ', 'rm ', 'cat ', 'echo ')):
                line = '```bash'
            elif next_line.strip().startswith(('{', '[')):
                line = '```json'
            elif 'GET ' in next_line or 'POST ' in next_line or 'HTTP' in next_line:
                line = '```http'
            elif re.match(r'^[\w\-]+:', next_line) or 'Subject:' in next_line:
                line = '```text'
            else:
                # Default to text for unknown
                line = '```text'
        
        # Fix MD034: Wrap bare URLs in angle brackets
        # Match URLs not already in markdown links or angle brackets
        if 'http' in line and not re.search(r'\[.*\]\(http', line) and not re.search(r'<http', line):
            # Find bare URLs
            line = re.sub(r'(?<![<\(])https?://[^\s)>]+(?![>\)])', r'<\g<0>>', line)
        
        fixed_lines.append(line)
        i += 1
    
    # Fix MD031 and MD032: Add blank lines around code blocks and lists
    final_lines = []
    i = 0
    while i < len(fixed_lines):
        line = fixed_lines[i]
        
        # Check if this is a code block start
        if line.strip().startswith('```'):
            # Add blank line before if previous line isn't blank
            if final_lines and final_lines[-1].strip() != '':
                final_lines.append('')
            final_lines.append(line)
            i += 1
            # Copy content until closing ```
            while i < len(fixed_lines) and not fixed_lines[i].strip().startswith('```'):
                final_lines.append(fixed_lines[i])
                i += 1
            # Add closing ```
            if i < len(fixed_lines):
                final_lines.append(fixed_lines[i])
                i += 1
            # Add blank line after if next line isn't blank
            if i < len(fixed_lines) and fixed_lines[i].strip() != '':
                final_lines.append('')
            continue
        
        # Check if this is a list item
        if re.match(r'^(\s*[-*+]\s|^\s*\d+\.)', line):
            # If this is first list item, add blank before
            if final_lines and final_lines[-1].strip() != '' and not re.match(r'^(\s*[-*+]\s|^\s*\d+\.)', final_lines[-1]):
                final_lines.append('')
            
            # Add list items
            final_lines.append(line)
            i += 1
            
            # Continue adding list items
            while i < len(fixed_lines) and (re.match(r'^(\s*[-*+]\s|^\s*\d+\.)', fixed_lines[i]) or fixed_lines[i].strip() == ''):
                final_lines.append(fixed_lines[i])
                i += 1
            
            # Add blank line after if next line isn't blank and isn't already a heading or hr
            if i < len(fixed_lines) and fixed_lines[i].strip() != '' and not fixed_lines[i].startswith('#') and not fixed_lines[i].startswith('---'):
                final_lines.append('')
            continue
        
        final_lines.append(line)
        i += 1
    
    return '\n'.join(final_lines)


def main():
    input_file = 'AI LLM Red Team Hand book.md'
    backup_file = 'AI LLM Red Team Hand book.md.backup'
    
    print(f"Reading {input_file}...")
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f"Creating backup at {backup_file}...")
    with open(backup_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Applying markdown fixes...")
    fixed_content = fix_markdown(content)
    
    print(f"Writing fixed content to {input_file}...")
    with open(input_file, 'w', encoding='utf-8') as f:
        f.write(fixed_content)
    
    print("✓ Markdown fixes applied successfully!")
    print(f"  - Backup saved to: {backup_file}")
    print(f"  - Fixed file: {input_file}")
    print("\nFixes applied:")
    print("  1. ✓ Converted bold text to proper headings (MD036)")
    print("  2. ✓ Added blank lines around lists (MD032)")
    print("  3. ✓ Added blank lines around code blocks (MD031)")
    print("  4. ✓ Added language specifiers to code blocks (MD040)")
    print("  5. ✓ Wrapped bare URLs (MD034)")
    print("  6. ✓ Removed trailing spaces (MD009)")


if __name__ == '__main__':
    main()
