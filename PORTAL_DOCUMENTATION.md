# AI for All: Complete Portal Documentation & Concepts Guide

This document serves as the master reference file for everything that has been built for the "AI for All" interactive learning portal, including the technical architecture and a detailed breakdown of all the AI concepts covered across the 22 HTML modules.

---

## 1. Technical Architecture & UI/UX

We built a production-grade, highly optimized static web application without relying on heavy frontend frameworks (no React, no Node.js dependencies).

*   **Core Stack:** Vanilla HTML5, CSS3, and JavaScript (`script.js`).
*   **Design System:** Modern "Glassmorphism" UI with deep CSS variables. Features animated text gradients, 3D card pop effects on hover, frosted glass top navigation (`backdrop-filter: blur`), and dynamic drop shadows.
*   **High-Definition Graphics:** Integrated AI-generated conceptual art (`hero-bg.png`, `concept1.png`, `concept2.png`) with smooth scale-on-hover CSS transitions.
*   **Dynamic Visualizations:** Integrated **Mermaid.js** for rendering sequence diagrams, flowcharts, and an interactive clickable Knowledge Map directly in the browser.
*   **Icons:** Used standard Ionicons for a clean, consistent vector aesthetic across the sidebar and bento cards.
*   **CI/CD Pipeline:** Configured a GitHub Actions workflow (`deploy-pages.yml`) to automatically build and deploy the repository to GitHub Pages on every push to the `main` branch.
*   **Cache Management:** Implemented query string versioning (e.g., `styles.css?v=3`) to bust aggressive browser caches and ensure instantaneous UI updates.

---

## 2. The 22 Educational Modules & Covered Concepts

The portal is divided into structured learning paths, guiding a user from fundamental LLM theory all the way to advanced production operations (LLMOps) and Agentic Architectures.

### Module 1: Home Overview (`index.html`)
The landing page directory. Features the main animated hero banner, project statistics, and the completely restructured bento-grid navigation layout linking to all sub-modules.

### Module 2: Career Roadmap (`roadmap.html`)
A structured guide for Cloud, DevOps, and Software Engineers transitioning into AI.
*   **Level 1 Skills:** Python, API Integrations, Prompt Engineering, Basic RAG.
*   **Level 2 Skills:** Agentic Frameworks (LangGraph), MCP, Evaluation Pipelines (RAGAS).

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

### Phase 3 Expansion (Advanced Engineering)

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
*Generated automatically as a comprehensive manifest of the AI for All project (v3.0).*
