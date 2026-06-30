import re
import os

files_to_update = [
    ('glossary.html', 'book-outline', '#60a5fa', 'Dictionary', 'index.html'),
    ('agent-engineering.html', 'construct-outline', '#f472b6', 'Architecture Patterns', 'architecture-patterns.html'),
    ('architecture-patterns.html', 'layers-outline', '#34d399', 'Infrastructure', 'infrastructure.html'),
    ('infrastructure.html', 'server-outline', '#fbbf24', 'Multi-Agent Systems', 'multi-agent.html'),
    ('multi-agent.html', 'people-outline', '#818cf8', 'GraphRAG', 'graphrag.html'),
    ('graphrag.html', 'analytics-outline', '#2dd4bf', 'Observability', 'observability-advanced.html'),
    ('observability-advanced.html', 'eye-outline', '#f87171', 'AI Gateway', 'ai-gateway.html'),
    ('ai-gateway.html', 'swap-horizontal-outline', '#fbbf24', 'Advanced Security', 'advanced-security.html'),
    ('advanced-security.html', 'lock-closed-outline', '#f472b6', 'Knowledge Map', 'knowledge-map.html'),
    ('knowledge-map.html', 'map-outline', '#818cf8', 'Home', 'index.html')
]

qa_html = """
            <section class="animate-on-scroll" style="margin-top:40px;">
                <div class="eyebrow">Interview Prep</div>
                <h2 style="margin-top:0; border:none;">Top Interview Questions</h2>
                <div class="qa-list">
                    <div class="qa-item">
                        <div class="qa-q">Can you explain this concept in 30 seconds? <ion-icon name="add-outline" class="qa-toggle"></ion-icon></div>
                        <div class="qa-a">This is a core component of modern AI engineering designed to solve scalability, accuracy, and latency issues in production agentic systems.</div>
                    </div>
                </div>
            </section>
"""

chip_html = """
                <div class="chip-strip">
                    <span class="chip ch-p">V4.0 Optimized</span>
                    <span class="chip ch-b">Core Concept</span>
                </div>
"""

for fname, icon, color, next_title, next_link in files_to_update:
    if not os.path.exists(fname):
        continue
        
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Check if already V4 optimized
    if 'V4.0 Optimized' in content:
        print(f"Skipping {fname}, already optimized.")
        continue
        
    next_html = f"""
            <section class="animate-on-scroll" style="margin-top:40px;">
                <div class="eyebrow">Up Next</div>
                <h2 style="margin-top:0; border:none;">Continue Learning</h2>
                <div class="next-steps-grid">
                    <a href="{next_link}" class="next-card">
                        <ion-icon name="{icon}" style="color: {color};"></ion-icon>
                        <div class="next-card-text">
                            <h4>{next_title}</h4>
                            <p>Continue your journey &rarr;</p>
                        </div>
                    </a>
                </div>
            </section>
"""
    
    # 1. Inject chip strip before closing </header>
    content = re.sub(r'(</header>)', chip_html + r'\1', content, count=1)
    
    # 2. Inject QA and Next Steps before the closing </div> of content-area
    # content-area closes right before </main>
    # Search for the last </div> before </main>
    # Actually, easier to inject before </main> directly, but we need it inside content-area
    
    # Let's just find </main> and replace it with closing div (if needed) or just inject right before it if it's inside content-area.
    # Actually the structure is <div class="content-area"> ... </div> </main>
    
    content = content.replace('        </div>\n    </main>', qa_html + next_html + '        </div>\n    </main>')
    
    # 3. Add script tag at the bottom if not exists
    script_snippet = """    <script>
        document.querySelectorAll('.qa-q').forEach(q => {
            q.addEventListener('click', () => {
                const item = q.parentElement;
                item.classList.toggle('open');
            });
        });
    </script>
</body>"""
    if 'qa-q' not in content.split('</body>')[0]: # Prevent double injection
        content = content.replace('</body>', script_snippet)
        
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Injected V4 components into {fname}")

