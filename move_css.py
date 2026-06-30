import re

def extract_and_append_css(html_file, css_file):
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    style_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
    if style_match:
        css_block = style_match.group(1)
        
        # Append to styles.css
        with open(css_file, 'a', encoding='utf-8') as f:
            f.write('\n\n/* ── CSS from ' + html_file + ' ── */\n')
            f.write(css_block)
            
        # Remove from html file
        new_content = re.sub(r'<style>.*?</style>\n*', '', content, flags=re.DOTALL)
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"Successfully moved CSS from {html_file} to {css_file}")
    else:
        print(f"No <style> tag found in {html_file}")

extract_and_append_css('index.html', 'styles.css')
extract_and_append_css('fundamentals.html', 'styles.css')
