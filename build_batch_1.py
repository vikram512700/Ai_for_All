import re

# Extract Layout Components from index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

sidebar_match = re.search(r'(<aside class="sidebar" id="sidebar">.*?</aside>)', index_html, re.DOTALL)
sidebar = sidebar_match.group(1) if sidebar_match else ""

topbar = """        <header class="topbar">
            <button class="icon-btn mobile-toggle" id="mobile-toggle"><ion-icon name="menu-outline"></ion-icon></button>
            <div class="search-bar">
                <ion-icon name="search-outline"></ion-icon>
                <input type="text" id="search-input" placeholder="Search modules, concepts, tools...">
            </div>
            <div class="topbar-actions">
                <button class="icon-btn" id="theme-toggle" title="Toggle theme"><ion-icon name="moon-outline"></ion-icon></button>
            </div>
        </header>"""

scripts = """    <script src="script.js"></script>
    <script>
        // Q&A Accordion Logic
        document.querySelectorAll('.qa-q').forEach(q => {
            q.addEventListener('click', () => {
                const item = q.parentElement;
                item.classList.toggle('open');
            });
        });
    </script>
</body>
</html>"""

def build_page(filename, title, module_num, heading, gradient_text, desc, chips, content_sections, next_steps, qa_items):
    
    chip_html = '<div class="chip-strip">\n'
    for c in chips:
        chip_html += f'    <span class="chip {c[1]}">{c[0]}</span>\n'
    chip_html += '</div>\n'
    
    qa_html = '<div class="qa-list">\n'
    for qa in qa_items:
        qa_html += f"""    <div class="qa-item">
        <div class="qa-q">{qa[0]} <ion-icon name="add-outline" class="qa-toggle"></ion-icon></div>
        <div class="qa-a">{qa[1]}</div>
    </div>\n"""
    qa_html += '</div>\n'
    
    next_html = '<div class="next-steps-grid">\n'
    for nx in next_steps:
        next_html += f"""    <a href="{nx[3]}" class="next-card">
        <ion-icon name="{nx[0]}" style="color: {nx[1]};"></ion-icon>
        <div class="next-card-text">
            <h4>{nx[2]}</h4>
            <p>Continue your journey &rarr;</p>
        </div>
    </a>\n"""
    next_html += '</div>\n'
    
    html = f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | AI for All</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Fira+Code:wght@400;500&display=swap" rel="stylesheet">
    <script type="module" src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.esm.js"></script>
    <script nomodule src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.js"></script>
    <link rel="stylesheet" href="styles.css?v=4">
</head>
<body>
<div class="app-container">
    {sidebar}
    <div class="mobile-overlay" id="mobile-overlay"></div>
    <main class="main-content">
{topbar}
        <div class="content-area">
            <header class="page-header animate-on-scroll">
                <span class="badge">Module {module_num}</span>
                <h1>{heading} <span class="text-gradient">{gradient_text}</span></h1>
                <p class="page-description">{desc}</p>
                {chip_html}
            </header>
            
{content_sections}

            <section class="animate-on-scroll" style="margin-top:40px;">
                <div class="eyebrow">Interview Prep</div>
                <h2 style="margin-top:0; border:none;">Top Interview Questions</h2>
                {qa_html}
            </section>
            
            <section class="animate-on-scroll" style="margin-top:40px;">
                <div class="eyebrow">Up Next</div>
                <h2 style="margin-top:0; border:none;">Continue Learning</h2>
                {next_html}
            </section>
        </div>
    </main>
</div>
{scripts}
"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Generated {filename}")

# ==============================================================================
# 1. Claude.html
# ==============================================================================
claude_content = """
            <section class="animate-on-scroll">
                <div class="eyebrow">The Best Coding LLM</div>
                <h2 style="margin-top:0;">Claude 3.5 Sonnet vs The Rest</h2>
                <div class="info-box">
                    <ion-icon name="information-circle-outline"></ion-icon>
                    <p>As of late 2025, Claude 3.5 Sonnet remains the undisputed champion of coding tasks, architecture design, and complex multi-file refactoring, beating GPT-4o in almost all SWE-bench evaluations.</p>
                </div>
                
                <div class="bento-grid">
                    <div class="bento-card">
                        <div class="card-icon amber"><ion-icon name="sparkles-outline"></ion-icon></div>
                        <h3>Claude Web (Chat)</h3>
                        <p>The standard web interface. Great for asking questions and pasting code snippets. Uses Artifacts to render UI code instantly.</p>
                    </div>
                    <div class="bento-card">
                        <div class="card-icon blue"><ion-icon name="terminal-outline"></ion-icon></div>
                        <h3>Claude Code (CLI)</h3>
                        <p>An agentic command-line tool. You run <code>claude</code> in your terminal, and it can read files, write files, run tests, and fix errors autonomously.</p>
                    </div>
                </div>
            </section>

            <section class="animate-on-scroll" style="margin-top:40px;">
                <h2>Prompt Engineering Mastery</h2>
                <p>Claude responds best to structured, specific prompts using XML tags.</p>
                
                <div class="temp-grid">
                    <div class="temp-card">
                        <h4>XML Tags</h4>
                        <p>Use <code>&lt;context&gt;</code> and <code>&lt;instructions&gt;</code> to separate data from commands. Claude is heavily trained on XML.</p>
                    </div>
                    <div class="temp-card">
                        <h4>Few-Shot Prompting</h4>
                        <p>Don't just tell it what to do; give it 2-3 examples of the exact output format you expect.</p>
                    </div>
                    <div class="temp-card">
                        <h4>Chain of Thought (CoT)</h4>
                        <p>Force Claude to think before acting by asking it to write its thought process inside <code>&lt;thinking&gt;</code> tags.</p>
                    </div>
                </div>
                
                <div class="key-box">
                    <ion-icon name="key-outline"></ion-icon>
                    <p><strong>Pro Tip:</strong> When using Claude Code, create a <code>SKILL.md</code> file in your directory. Claude will automatically read it to learn your project's specific style guidelines and architectural rules.</p>
                </div>
            </section>
"""

build_page(
    'claude.html', 
    'Claude & Prompt Engineering', 
    '4', 
    'Claude & Prompt', 
    'Engineering', 
    'Master Anthropic\'s Claude, Agentic IDEs, and advanced prompt structuring techniques like CoT and XML tagging.',
    [('Claude 3.5 Sonnet', 'ch-a'), ('Claude Code', 'ch-b'), ('XML Tags', 'ch-p'), ('Chain-of-Thought', 'ch-g'), ('SKILL.md', 'ch-r')],
    claude_content,
    [('search-outline', '#34d399', 'RAG & Vector Search', 'rag.html'), ('hardware-chip-outline', '#f472b6', 'Agentic AI', 'agents.html')],
    [
        ("Why does Claude prefer XML tags?", "Anthropic explicitly fine-tuned Claude to recognize and parse XML tags (like <document> or <instructions>). It helps the model distinguish between your instructions and the raw data it needs to process."),
        ("What is the difference between Claude Chat and Claude Code?", "Claude Chat is a passive web UI. Claude Code is an agentic CLI tool installed via npm that runs in your terminal, has read/write access to your local file system, and can execute bash commands autonomously."),
        ("How does Chain-of-Thought (CoT) improve accuracy?", "LLMs predict the next token. If an LLM outputs an answer immediately, it has 1 token of 'thought'. If you force it to write out its step-by-step reasoning first, it uses hundreds of tokens to 'think', leading to drastically higher accuracy on logic puzzles or complex coding tasks.")
    ]
)

# ==============================================================================
# 2. RAG.html
# ==============================================================================
rag_content = """
            <section class="animate-on-scroll">
                <div class="eyebrow">The Knowledge Problem</div>
                <h2 style="margin-top:0;">Why We Need RAG</h2>
                <div class="info-box">
                    <ion-icon name="information-circle-outline"></ion-icon>
                    <p>LLMs are frozen in time after training and only know public internet data. RAG (Retrieval-Augmented Generation) is how you let an LLM read your private enterprise PDFs, databases, and Confluence pages <strong>without</strong> retraining the model.</p>
                </div>
                
                <div class="bento-grid">
                    <div class="bento-card">
                        <div class="card-icon purple"><ion-icon name="document-text-outline"></ion-icon></div>
                        <h3>1. Chunking</h3>
                        <p>You can't fit a 1,000-page PDF in a prompt. You must split the document into small "chunks" (e.g., 500 words each).</p>
                    </div>
                    <div class="bento-card">
                        <div class="card-icon green"><ion-icon name="code-working-outline"></ion-icon></div>
                        <h3>2. Embeddings</h3>
                        <p>Convert each chunk into a mathematical Vector (an array of 1536 numbers) representing its semantic meaning.</p>
                    </div>
                    <div class="bento-card">
                        <div class="card-icon blue"><ion-icon name="server-outline"></ion-icon></div>
                        <h3>3. Vector Database</h3>
                        <p>Store these vectors in a specialized DB like Pinecone, Qdrant, or Azure AI Search.</p>
                    </div>
                    <div class="bento-card">
                        <div class="card-icon amber"><ion-icon name="search-outline"></ion-icon></div>
                        <h3>4. Semantic Search</h3>
                        <p>When a user asks a question, convert it to a vector, find the 5 closest chunks using Cosine Similarity, and send them to the LLM.</p>
                    </div>
                </div>
            </section>

            <section class="animate-on-scroll" style="margin-top:40px;">
                <h2>Advanced RAG Architectures</h2>
                
                <div class="embedding-visual">
                    <div class="emb-word-row">
                        <div class="emb-word" style="background: rgba(129,140,248,0.1); color: #818cf8; border-color: rgba(129,140,248,0.3);">Hybrid Search</div>
                        <div class="emb-arrow">&rarr;</div>
                        <div class="emb-vector" style="color: var(--text-primary);">Vector Search (Meaning) + BM25 (Keyword Match)</div>
                    </div>
                    <div class="emb-word-row">
                        <div class="emb-word" style="background: rgba(52,211,153,0.1); color: #34d399; border-color: rgba(52,211,153,0.3);">Cross-Encoder Re-ranking</div>
                        <div class="emb-arrow">&rarr;</div>
                        <div class="emb-vector" style="color: var(--text-primary);">Using a second LLM to re-score and perfectly sort the top 10 search results.</div>
                    </div>
                    <div class="emb-word-row">
                        <div class="emb-word" style="background: rgba(251,191,36,0.1); color: #fbbf24; border-color: rgba(251,191,36,0.3);">Query Expansion</div>
                        <div class="emb-arrow">&rarr;</div>
                        <div class="emb-vector" style="color: var(--text-primary);">Having the LLM rewrite the user's bad prompt into 3 better prompts before searching.</div>
                    </div>
                </div>
                
                <div class="warn-box">
                    <ion-icon name="warning-outline"></ion-icon>
                    <p><strong>Lost in the Middle:</strong> Research shows LLMs ignore information placed in the middle of a massive context window. Always put the most relevant RAG chunks at the very beginning or very end of the prompt.</p>
                </div>
            </section>
"""

build_page(
    'rag.html', 
    'RAG & Vector Search', 
    '5', 
    'RAG & <span class="text-gradient">Vector Search</span>', 
    '', 
    'Connect LLMs to your private enterprise data using Vector Databases, embeddings, and hybrid search.',
    [('Embeddings', 'ch-p'), ('Vector DB', 'ch-g'), ('Cosine Similarity', 'ch-a'), ('Hybrid Search', 'ch-b')],
    rag_content,
    [('hardware-chip-outline', '#f472b6', 'Agentic AI', 'agents.html'), ('analytics-outline', '#2dd4bf', 'GraphRAG', 'graphrag.html')],
    [
        ("Why use a Vector Database instead of a regular SQL database?", "SQL databases perform exact keyword matches (e.g., searching 'Dog' will not return 'Puppy'). Vector Databases perform semantic search by comparing the mathematical distance between concepts in multi-dimensional space, meaning 'Dog' and 'Puppy' will be matched instantly."),
        ("What is Hybrid Search?", "Hybrid Search combines traditional BM25 keyword search (great for exact names, acronyms, or IDs) with Vector Search (great for concepts and intent). The scores are fused together using Reciprocal Rank Fusion (RRF) for the best possible results."),
        ("What is Chunking, and why is it hard?", "Chunking is splitting a large document into smaller pieces for the LLM to read. It's hard because if you split arbitrarily (e.g., every 500 words), you might cut a sentence or paragraph in half, destroying the semantic meaning of that chunk.")
    ]
)

# ==============================================================================
# 3. Agents.html
# ==============================================================================
agents_content = """
            <section class="animate-on-scroll">
                <div class="eyebrow">Beyond Chatbots</div>
                <h2 style="margin-top:0;">What makes an AI "Agentic"?</h2>
                <div class="info-box">
                    <ion-icon name="information-circle-outline"></ion-icon>
                    <p>A standard LLM just talks. An <strong>Agent</strong> is an LLM that has been given a loop (to think iteratively) and Tools (to take actions in the real world, like running code or searching the web).</p>
                </div>
                
                <div class="transformer-flow">
                    <div class="tf-step">
                        <div class="tf-box tf-1"><h4>1. Goal</h4><p>User says: "Research Apple's stock and write a report."</p></div>
                    </div>
                    <div class="tf-arrow"></div>
                    <div class="tf-step">
                        <div class="tf-box tf-2"><h4>2. Plan</h4><p>Agent breaks goal into steps: 1. Search Web, 2. Scrape Data, 3. Write.</p></div>
                    </div>
                    <div class="tf-arrow"></div>
                    <div class="tf-step">
                        <div class="tf-box tf-3"><h4>3. Tool Execution</h4><p>Agent outputs JSON calling the `web_search` tool API.</p></div>
                    </div>
                    <div class="tf-arrow"></div>
                    <div class="tf-step">
                        <div class="tf-box tf-4"><h4>4. Observation</h4><p>Tool returns data. Agent reflects: "Is this enough data?"</p></div>
                    </div>
                    <div class="tf-arrow"></div>
                    <div class="tf-step">
                        <div class="tf-box tf-5"><h4>5. Output</h4><p>Agent finalizes the report and breaks out of the loop.</p></div>
                    </div>
                </div>
            </section>

            <section class="animate-on-scroll" style="margin-top:40px;">
                <h2>Core Agent Concepts</h2>
                
                <div class="bento-grid">
                    <div class="bento-card">
                        <div class="card-icon amber"><ion-icon name="build-outline"></ion-icon></div>
                        <h3>Function Calling</h3>
                        <p>The native ability of modern LLMs (GPT-4o, Claude 3.5) to output structured JSON matching a specific tool schema, rather than outputting conversational text.</p>
                    </div>
                    <div class="bento-card">
                        <div class="card-icon pink"><ion-icon name="sync-outline"></ion-icon></div>
                        <h3>The ReAct Loop</h3>
                        <p><strong>Re</strong>ason + <strong>Act</strong>. The agent writes down its thought ("I need to search for X"), takes the action, observes the result, and loops until the goal is met.</p>
                    </div>
                    <div class="bento-card">
                        <div class="card-icon blue"><ion-icon name="git-network-outline"></ion-icon></div>
                        <h3>Agent Orchestration</h3>
                        <p>Using frameworks like LangGraph or CrewAI to string multiple agents together, handle state management, and prevent infinite loops.</p>
                    </div>
                </div>
            </section>
"""

build_page(
    'agents.html', 
    'Agentic AI Systems', 
    '6', 
    'Agentic <span class="text-gradient">AI Systems</span>', 
    '', 
    'Build autonomous agents that plan, use tools, reflect, and solve complex multi-step problems.',
    [('ReAct Loop', 'ch-p'), ('Tool Calling', 'ch-g'), ('Function Calling', 'ch-a'), ('LangGraph', 'ch-b')],
    agents_content,
    [('git-network-outline', '#60a5fa', 'Model Context Protocol', 'mcp.html'), ('git-branch-outline', '#818cf8', 'LangGraph Deep Dive', 'langgraph.html')],
    [
        ("What is the difference between Function Calling and Tool Calling?", "They are often used interchangeably, but technically: Function Calling is the LLM's ability to output a JSON object matching a function signature. Tool Calling is the broader agentic framework where the application actually executes that function and feeds the result back to the LLM."),
        ("What happens if an Agent gets stuck in an infinite loop?", "This is a common failure mode where an agent calls a tool, gets an error, and repeatedly tries the exact same bad tool call forever. Frameworks like LangGraph fix this by enforcing a `max_steps` limit (e.g., abort after 10 loops)."),
        ("What is ReAct?", "ReAct stands for Reason + Act. It is a prompting paradigm where you force the LLM to write a 'Thought:' before taking an 'Action:'. This dramatically improves the agent's decision-making process compared to just acting blindly.")
    ]
)

# ==============================================================================
# 4. MCP.html
# ==============================================================================
mcp_content = """
            <section class="animate-on-scroll">
                <div class="eyebrow">The USB-C of AI</div>
                <h2 style="margin-top:0;">Model Context Protocol (MCP)</h2>
                <div class="info-box">
                    <ion-icon name="information-circle-outline"></ion-icon>
                    <p>Created by Anthropic, MCP is an open standard that standardizes how AI applications connect to external data sources. Before MCP, you had to write custom tool-calling code for every API (Slack, GitHub, Postgres). Now, you just plug in an MCP Server.</p>
                </div>
                
                <div class="bento-grid">
                    <div class="bento-card">
                        <div class="card-icon blue"><ion-icon name="laptop-outline"></ion-icon></div>
                        <h3>MCP Client (The AI)</h3>
                        <p>The AI application (like Claude Desktop, Cursor, or an Agent). It maintains a 1:1 connection with the server and asks for tools/data.</p>
                    </div>
                    <div class="bento-card">
                        <div class="card-icon green"><ion-icon name="server-outline"></ion-icon></div>
                        <h3>MCP Server (The Data)</h3>
                        <p>A lightweight program running locally or remotely. It exposes Resources (files), Tools (actions), and Prompts to the Client over a secure STDIO or SSE connection.</p>
                    </div>
                </div>
            </section>

            <section class="animate-on-scroll" style="margin-top:40px;">
                <h2>What does an MCP Server expose?</h2>
                <div class="temp-grid">
                    <div class="temp-card">
                        <h4>Resources</h4>
                        <p>File-like data that the AI can read. Example: Log files, database schemas, or internal API documentation.</p>
                    </div>
                    <div class="temp-card">
                        <h4>Tools</h4>
                        <p>Executable functions the AI can call. Example: <code>execute_sql_query</code>, <code>create_github_issue</code>, <code>fetch_weather</code>.</p>
                    </div>
                    <div class="temp-card">
                        <h4>Prompts</h4>
                        <p>Pre-written prompt templates that users can easily trigger. Example: "Review this pull request based on our company guidelines."</p>
                    </div>
                </div>
                
                <div class="key-box">
                    <ion-icon name="key-outline"></ion-icon>
                    <p><strong>Security First:</strong> MCP Servers are fully controlled by the host. The LLM provider (OpenAI/Anthropic) NEVER gets direct access to your database. The LLM simply asks the local MCP Client to run a tool, and the local Client talks to the local Server.</p>
                </div>
            </section>
"""

build_page(
    'mcp.html', 
    'Model Context Protocol', 
    '7', 
    'Model Context <span class="text-gradient">Protocol</span>', 
    '', 
    'Standardize how your AI models securely access external tools, APIs, and enterprise data sources.',
    [('MCP Client', 'ch-b'), ('MCP Server', 'ch-g'), ('Anthropic Standard', 'ch-r'), ('STDIO', 'ch-a')],
    mcp_content,
    [('construct-outline', '#f472b6', 'Agent Engineering', 'agent-engineering.html'), ('pulse-outline', '#fbbf24', 'LLMOps & Observability', 'llmops.html')],
    [
        ("Why was MCP created?", "Prior to MCP, every AI tool (Cursor, GitHub Copilot, ChatGPT) had to build custom, proprietary integrations for every service (Slack, Jira, Postgres). MCP provides a universal, open-source standard. If you build an MCP Server for your database, EVERY AI client can instantly use it."),
        ("How does the MCP Client communicate with the Server?", "Locally, it uses STDIO (Standard Input/Output) by spawning a subprocess. Over a network, it uses SSE (Server-Sent Events) over HTTP."),
        ("Can an MCP Server execute dangerous code?", "Only if you program it to! The MCP Server dictates exactly what tools are exposed. You can restrict an MCP PostgreSQL server to only allow `SELECT` queries, ensuring the AI can never drop a table.")
    ]
)

# ==============================================================================
# 5. LangGraph.html
# ==============================================================================
langgraph_content = """
            <section class="animate-on-scroll">
                <div class="eyebrow">Advanced Agent Orchestration</div>
                <h2 style="margin-top:0;">Why LangGraph?</h2>
                <div class="info-box">
                    <ion-icon name="information-circle-outline"></ion-icon>
                    <p>Standard agents (like basic ReAct agents) are unpredictable and hard to control in production. <strong>LangGraph</strong> solves this by treating agents as State Machines (Graphs). You define exactly which paths the agent is allowed to take.</p>
                </div>
                
                <div class="bento-grid">
                    <div class="bento-card">
                        <div class="card-icon purple"><ion-icon name="git-commit-outline"></ion-icon></div>
                        <h3>Nodes & Edges</h3>
                        <p><strong>Nodes</strong> are Python functions (e.g., 'Call LLM', 'Run Tool'). <strong>Edges</strong> connect the nodes and control the flow of execution.</p>
                    </div>
                    <div class="bento-card">
                        <div class="card-icon blue"><ion-icon name="shuffle-outline"></ion-icon></div>
                        <h3>Conditional Edges</h3>
                        <p>The magic of LangGraph. After a node runs, a conditional edge acts as an 'if/else' router. <em>If tool output is bad &rarr; loop back to LLM. If good &rarr; go to End.</em></p>
                    </div>
                </div>
            </section>

            <section class="animate-on-scroll" style="margin-top:40px;">
                <h2>The Power of State & Time Travel</h2>
                
                <div class="temp-grid">
                    <div class="temp-card">
                        <h4>Global State</h4>
                        <p>Every node receives and updates a global <code>State</code> object (usually a Pydantic model). This ensures all agents share the exact same memory and context.</p>
                    </div>
                    <div class="temp-card">
                        <h4>Checkpointers</h4>
                        <p>LangGraph saves the State to a database (Postgres, SQLite) after every single node execution. This provides flawless memory persistence across sessions.</p>
                    </div>
                    <div class="temp-card">
                        <h4>Time Travel & HITL</h4>
                        <p>Because every state is saved, you can pause the graph for Human-in-the-Loop (HITL) approval, or literally 'rewind' the agent to a previous step if it made a mistake.</p>
                    </div>
                </div>
                
                <div class="warn-box">
                    <ion-icon name="warning-outline"></ion-icon>
                    <p><strong>Cyclic Graphs:</strong> Unlike traditional DAGs (Directed Acyclic Graphs) used in data engineering (like Airflow), LangGraph allows cycles (loops). This is essential for agents, which need to loop to correct their own mistakes.</p>
                </div>
            </section>
"""

build_page(
    'langgraph.html', 
    'LangGraph Deep Dive', 
    '13', 
    'LangGraph <span class="text-gradient">Deep Dive</span>', 
    '', 
    'Build highly controllable, stateful, multi-actor applications with LLMs using graphs.',
    [('StateGraphs', 'ch-p'), ('Checkpointers', 'ch-g'), ('Conditional Edges', 'ch-a'), ('Time Travel', 'ch-b'), ('HITL', 'ch-r')],
    langgraph_content,
    [('construct-outline', '#f472b6', 'Agent Engineering', 'agent-engineering.html'), ('people-outline', '#34d399', 'Multi-Agent Systems', 'multi-agent.html')],
    [
        ("Why use LangGraph instead of vanilla LangChain?", "Vanilla LangChain is great for linear pipelines (Chain A -> Chain B). But agents require non-linear logic (loops, branching, decision making). LangGraph was built specifically to handle these cyclic flows reliably."),
        ("What is Time Travel in LangGraph?", "Because LangGraph uses checkpointers to save the state after every node, you can fetch a previous state, modify it (e.g., fix a bad prompt that caused a crash), and resume the graph execution from that exact point in the past."),
        ("How does Human-in-the-Loop work?", "You can define an `interrupt_before` on a specific node (e.g., the `execute_sql` node). The graph will run, pause right before that node, and return control to the user. The user approves, and the graph resumes.")
    ]
)
