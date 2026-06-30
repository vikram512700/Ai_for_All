import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

new_sidebar = """<aside class="sidebar" id="sidebar">
            <a href="index.html" class="logo-container" style="text-decoration:none;"><div class="logo-icon"><ion-icon name="cube-outline"></ion-icon></div><div class="logo-text">AI for All</div></a>
            
            <div class="nav-section"><div class="nav-section-title">Getting Started</div>
                <a href="index.html" class="nav-item"><ion-icon name="home-outline"></ion-icon> Home Overview</a>
                <a href="roadmap.html" class="nav-item"><ion-icon name="map-outline"></ion-icon> Career Roadmap</a>
            </div>
            
            <div class="nav-section"><div class="nav-section-title">Core Concepts</div>
                <a href="fundamentals.html" class="nav-item"><ion-icon name="bulb-outline"></ion-icon> AI Fundamentals</a>
                <a href="claude.html" class="nav-item"><ion-icon name="sparkles-outline"></ion-icon> Claude & Prompts</a>
                <a href="rag.html" class="nav-item"><ion-icon name="search-outline"></ion-icon> Vector RAG</a>
                <a href="agents.html" class="nav-item"><ion-icon name="hardware-chip-outline"></ion-icon> Agentic AI</a>
                <a href="mcp.html" class="nav-item"><ion-icon name="git-network-outline"></ion-icon> MCP</a>
            </div>
            
            <div class="nav-section"><div class="nav-section-title">Advanced Agents</div>
                <a href="langgraph.html" class="nav-item"><ion-icon name="git-commit-outline"></ion-icon> LangGraph</a>
                <a href="agent-engineering.html" class="nav-item"><ion-icon name="brain-outline"></ion-icon> Agent Engineering</a>
                <a href="multi-agent.html" class="nav-item"><ion-icon name="people-circle-outline"></ion-icon> Multi-Agent Systems</a>
            </div>
            
            <div class="nav-section"><div class="nav-section-title">Advanced Data</div>
                <a href="graphrag.html" class="nav-item"><ion-icon name="analytics-outline"></ion-icon> GraphRAG</a>
            </div>
            
            <div class="nav-section"><div class="nav-section-title">Arch & Infra</div>
                <a href="architecture-patterns.html" class="nav-item"><ion-icon name="layers-outline"></ion-icon> Architecture Patterns</a>
                <a href="infrastructure.html" class="nav-item"><ion-icon name="server-outline"></ion-icon> Infra & Serving</a>
                <a href="ai-gateway.html" class="nav-item"><ion-icon name="git-branch-outline"></ion-icon> AI Gateways</a>
            </div>
            
            <div class="nav-section"><div class="nav-section-title">Production Ops</div>
                <a href="llmops.html" class="nav-item"><ion-icon name="pulse-outline"></ion-icon> LLMOps</a>
                <a href="observability-advanced.html" class="nav-item"><ion-icon name="eye-outline"></ion-icon> Observability</a>
                <a href="evals.html" class="nav-item"><ion-icon name="bar-chart-outline"></ion-icon> AI Evaluation</a>
                <a href="security.html" class="nav-item"><ion-icon name="shield-checkmark-outline"></ion-icon> App Security</a>
                <a href="advanced-security.html" class="nav-item"><ion-icon name="skull-outline"></ion-icon> Adv Security</a>
                <a href="tools.html" class="nav-item"><ion-icon name="build-outline"></ion-icon> OS Tools & FinOps</a>
            </div>
            
            <div class="nav-section"><div class="nav-section-title">Resources</div>
                <a href="knowledge-map.html" class="nav-item"><ion-icon name="map-outline"></ion-icon> Knowledge Map</a>
                <a href="glossary.html" class="nav-item"><ion-icon name="book-outline"></ion-icon> Glossary</a>
            </div>
        </aside>"""

for file_name in html_files:
    try:
        with open(file_name, 'rb') as f:
            content = f.read().decode('utf-8', errors='ignore')
        
        # Use regex to replace the entire <aside class="sidebar" id="sidebar">...</aside> block
        new_content = re.sub(
            r'<aside class="sidebar" id="sidebar">.*?</aside>', 
            new_sidebar, 
            content, 
            flags=re.DOTALL
        )
        
        with open(file_name, 'wb') as f:
            f.write(new_content.encode('utf-8'))
            
        print(f"Updated {file_name}")
    except Exception as e:
        print(f"Failed to update {file_name}: {e}")
