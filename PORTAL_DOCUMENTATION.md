# AI for All: Complete Portal Documentation & Concepts Guide
**Version 4.0 — All 22 modules live across 3 phases**

This document serves as the master reference file for everything built in the "AI for All" interactive learning portal, including the technical architecture and a detailed breakdown of all AI concepts covered across the 22 HTML modules.

---

## 1. Technical Architecture & UI/UX

We built a production-grade, highly optimized static web application without relying on heavy frontend frameworks (no React, no Node.js dependencies).

*   **Core Stack:** Vanilla HTML5, CSS3, and JavaScript (`script.js`). No React, no Node.js dependencies.
*   **Design System:** Modern "Glassmorphism" UI with deep CSS variables. Features animated text gradients, 3D card pop effects on hover, frosted glass top navigation (`backdrop-filter: blur`), and dynamic drop shadows.
*   **High-Definition Graphics:** Integrated AI-generated conceptual art (`hero-bg.png`, `concept1.png`, `concept2.png`) with smooth scale-on-hover CSS transitions.
*   **Dynamic Visualizations:** Integrated **Mermaid.js** for rendering sequence diagrams, flowcharts, and an interactive clickable Knowledge Map directly in the browser. Custom HTML/CSS flowcharts on pages where Mermaid is not needed.
*   **Navigation:** Full 6-section sidebar consistent across all 22 pages — Getting Started, Core Modules, Production Ops, Advanced Engineering, Deep Operations, Resources. Active state auto-detected via `script.js` using `window.location.pathname`.
*   **Landing Page (v4.0):** Features a "15 Things First" priority learning path strip, Level 1 & Level 2 buzzword chips with tab switching, a Tools Ecosystem grid (8 categories), and all 22 modules surfaced across 4 bento-grid sections with phase badges.
*   **Roadmap Page (v4.0):** Redesigned with hero banner, career path cards, visual role specialisation flowchart, role comparison table with salary/demand data, an 8-step animated journey timeline, and skill mastery bar charts.
*   **Icons:** Used standard Ionicons for a clean, consistent vector aesthetic across the sidebar and bento cards.
*   **CI/CD Pipeline:** Configured a GitHub Actions workflow (`deploy-pages.yml`) to automatically build and deploy the repository to GitHub Pages on every push to the `main` branch.
*   **Cache Management:** Implemented query string versioning (`styles.css?v=4`) to bust aggressive browser caches and ensure instantaneous UI updates.

---

## 2. The 22 Educational Modules & Covered Concepts

The portal is divided into structured learning paths, guiding a user from fundamental LLM theory all the way to advanced production operations (LLMOps) and Agentic Architectures.

### Module 1: Home Overview (`index.html`)
The landing page. v4.0 redesign features: updated hero stats (22 modules, 80+ concepts, 3 phases), a "15 Things First" priority learning path strip, tabbed Level 1/Level 2 buzzword chip clouds, a Tools Ecosystem grid across 8 categories (Chat Assistants, Coding Tools, Agent Frameworks, Workflow, RAG/Search, Local AI, Evaluation, Observability), and all 22 modules surfaced in 4 bento-grid sections with Phase 1/Phase 3 phase badges. Live search filters the sidebar. Portal progress bar shows 22/22 modules live.

### Module 2: Career Roadmap (`roadmap.html`)
A structured visual guide for Cloud, DevOps, and Software Engineers transitioning into AI. v4.0 redesign includes: animated hero banner with salary/demand stats, 3 career path cards (DevOps→AI Platform, SWE→AI Engineer, Security→AI Security), custom HTML flowchart for role specialisation, a role comparison table with salary ranges and demand indicators, an 8-step journey timeline with glowing numbered dots and skill chips, and a skills mastery bar chart section.
*   **Level 1 Skills:** Python, API Integrations, Prompt Engineering, Basic RAG.
*   **Level 2 Skills:** Agentic Frameworks (LangGraph), MCP, Evaluation Pipelines (RAGAS).
*   **Level 3 Skills:** LLMOps, AI Security, Open Source Tools & FinOps.

### Module 3: AI & LLM Fundamentals (`fundamentals.html`)
The absolute basics of how Generative AI actually works under the hood.
*   **Mechanics:** Tokens, Context Windows, Temperature.

### Module 4: Claude & Prompt Engineering (`claude.html`)
Deep dive into Anthropic's Claude, Agentic IDEs, and prompt structuring (CoT, XML Tags).

### Module 5: RAG & Vector Search (`rag.html`)
Retrieval-Augmented Generation basics, Embeddings, Chunking strategies, and Vector Databases (Pinecone).

### Module 6: Agentic AI Systems (`agents.html`)
The transition from passive chatbots to active autonomous agents using the ReAct loop and Tool Calling.

### Module 7: Model Context Protocol (`mcp.html`)
The standard for connecting AI models to external data securely (the "USB-C for AI").

### Module 8: LLMOps & Observability (`llmops.html`)
Operating LLMs in production environments. Telemetry, latency, and tools like LangSmith.

### Module 9: AI Security & Risk Management (`security.html`)
The OWASP LLM Top 10, basic Prompt Injection, and Model Poisoning.

### Module 10: AI Evaluation (`evals.html`)
How to mathematically prove AI accuracy with RAGAS, Faithfulness, and Answer Relevance.

### Module 11: OS Tools & FinOps (`tools.html`)
Managing the cost of AI using local LLMs (Ollama) and open weights.

### Module 12: Glossary (`glossary.html`)
A searchable, A-Z dictionary of all the buzzwords mentioned above.

---

### Phase 3 — Advanced Engineering (All modules live)

### Module 13: LangGraph Deep Dive (`langgraph.html`)
Build highly controllable, stateful, multi-actor applications with LLMs using graphs.
*   **Concepts:** StateGraphs, Conditional Routing, Checkpointing, and Time Travel.

### Module 14: Agent Engineering (`agent-engineering.html`)
Designing intelligent systems with complex memory systems.
*   **Concepts:** Semantic vs Episodic Memory, Plan & Execute loops, Reflection architectures.

### Module 15: AI Architecture Patterns (`architecture-patterns.html`)
The definitive visual guide to the 7 core design patterns used in modern AI engineering. Includes Basic Chatbot, RAG, Single Agent, MCP, Multi-Agent, Human-in-the-loop, and Gateways.

### Module 16: Infrastructure & Model Serving (`infrastructure.html`)
The hardware and software required to serve open-source LLMs efficiently.
*   **Concepts:** vLLM, KServe, Quantization, Distillation, GPU scheduling.

### Module 17: Multi-Agent Systems (`multi-agent.html`)
Orchestrating teams of specialized AI agents.
*   **Concepts:** Supervisor vs Worker roles, Hierarchical teams, Agent Mesh (A2A).

### Module 18: GraphRAG & Knowledge Graphs (`graphrag.html`)
Overcoming the limitations of Vector RAG by understanding entity relationships and global context.

### Module 19: Advanced AI Observability (`observability-advanced.html`)
Tracing multi-step agent executions and managing token usage across distributed systems using OpenTelemetry.

### Module 20: AI Gateways (`ai-gateway.html`)
Standardizing API access, model routing, and cost control across multiple LLM providers (e.g., LiteLLM, Portkey).

### Module 21: Advanced AI Security (`advanced-security.html`)
Protecting agentic systems from sophisticated attacks.
*   **Threats:** Jailbreaking, Data Exfiltration, Sandboxing vulnerabilities.

### Module 22: AI Relationship Map (`knowledge-map.html`)
An interactive, fully clickable visual Mermaid graph mapping out how every single concept (from Tokens to RAG to Agents to Ops) ties together into one cohesive ecosystem.

---

## 3. Navigation Architecture (v4.0)

All 22 HTML pages share a canonical 6-section sidebar. Active state is auto-detected via `script.js` using `window.location.pathname`. No manual `active` class needed in markup.

| Section | Pages |
|---|---|
| Getting Started | Home Overview, Career Roadmap |
| Core Modules | Fundamentals, Claude, RAG, Agents, MCP |
| Production Ops | LLMOps, Evals, Security, Tools |
| Advanced Engineering | LangGraph, Agent Engineering, Architecture Patterns, Infrastructure, Multi-Agent, GraphRAG |
| Deep Operations | Advanced Observability, AI Gateways, Advanced Security, Knowledge Map |
| Resources | Glossary |

---
*Updated for AI for All project v4.0 — all 22 modules live, sidebar unified across all pages.*
