# AI for All: Complete Portal Documentation & Concepts Guide

This document serves as the master reference file for everything that has been built for the "AI for All" interactive learning portal, including the technical architecture and a detailed breakdown of all the AI concepts covered across the 11 HTML modules.

---

## 1. Technical Architecture & UI/UX

We built a production-grade, highly optimized static web application without relying on heavy frontend frameworks (no React, no Node.js dependencies).

*   **Core Stack:** Vanilla HTML5, CSS3, and JavaScript (`script.js`).
*   **Design System:** Modern "Glassmorphism" UI with deep CSS variables. Features animated text gradients, 3D card pop effects on hover, frosted glass top navigation (`backdrop-filter: blur`), and dynamic drop shadows.
*   **High-Definition Graphics:** Integrated AI-generated conceptual art (`hero-bg.png`, `concept1.png`, `concept2.png`) with smooth scale-on-hover CSS transitions.
*   **Dynamic Visualizations:** Integrated **Mermaid.js** for rendering sequence diagrams and flowcharts directly in the browser (used for RAG flows and Prompt Injection examples).
*   **Icons:** Used standard Ionicons for a clean, consistent vector aesthetic across the sidebar and bento cards.
*   **CI/CD Pipeline:** Configured a GitHub Actions workflow (`deploy-pages.yml`) to automatically build and deploy the repository to GitHub Pages on every push to the `main` branch.
*   **Cache Management:** Implemented query string versioning (e.g., `styles.css?v=3`) to bust aggressive browser caches and ensure instantaneous UI updates.

---

## 2. The 11 Educational Modules & Covered Concepts

The portal is divided into structured learning paths, guiding a user from fundamental LLM theory all the way to advanced production operations (LLMOps). Here is a detailed breakdown of what is taught in each module:

### Module 1: Home Overview (`index.html`)
The landing page directory. Features the main animated hero banner, project statistics, and the bento-grid navigation layout linking to all sub-modules.

### Module 2: Career Roadmap (`roadmap.html`)
A structured guide for Cloud, DevOps, and Software Engineers transitioning into AI.
*   **Concepts:** The difference between AI Platform Engineers and AI Engineers.
*   **Level 1 Skills:** Python, API Integrations, Prompt Engineering, Basic RAG.
*   **Level 2 Skills:** Agentic Frameworks (LangGraph), MCP, Evaluation Pipelines (RAGAS).

### Module 3: AI & LLM Fundamentals (`fundamentals.html`)
The absolute basics of how Generative AI actually works under the hood.
*   **Concepts:** Large Language Models (LLMs), Transformers, Attention Mechanisms.
*   **Mechanics:** Tokens (how words are split), Context Windows, Temperature (controlling creativity vs. determinism).

### Module 4: Claude & Prompt Engineering (`claude.html`)
Deep dive into Anthropic's Claude, Agentic IDEs, and prompt structuring.
*   **Concepts:** The difference between Claude (Chat) and Claude Code (Agentic CLI).
*   **Prompting:** Chain-of-Thought (CoT), Few-Shot Prompting, XML Tag structuring.
*   **Customization:** How to write `SKILL.md` (custom agent skills) and `AGENTS.md` (project rules).
*   **Integration:** How to connect Claude's API to LangGraph and route tasks between Claude and local models (Ollama).

### Module 5: RAG & Vector Search (`rag.html`)
Retrieval-Augmented Generation: How to connect LLMs to private enterprise data.
*   **Concepts:** Embeddings (turning text into math), Vector Databases (Pinecone, Qdrant).
*   **Mechanics:** Cosine Similarity, Chunking strategies, Context Injection.
*   **Advanced:** Hybrid Search (Vector + BM25 keyword search), Cross-Encoder Re-ranking.

### Module 6: Agentic AI Systems (`agents.html`)
Moving from passive chatbots to active, autonomous problem solvers.
*   **Concepts:** The ReAct Loop (Reason + Act), Tool Calling (giving LLMs access to APIs).
*   **Frameworks:** LangGraph, CrewAI.
*   **Patterns:** Supervisor Agents, Worker Agents, Reflection, Memory management.

### Module 7: Model Context Protocol (`mcp.html`)
The new standard for connecting AI models to data sources.
*   **Concepts:** What MCP is (the "USB-C for AI"), Client/Server architecture.
*   **Implementation:** How to expose local databases or APIs to an LLM securely without writing custom tool-calling code for every model.

### Module 8: LLMOps & Observability (`llmops.html`)
Operating LLMs in production environments.
*   **Concepts:** AI Telemetry, Latency tracking, Token cost monitoring.
*   **Tools:** LangSmith, Langfuse, Arize Phoenix.

### Module 9: AI Security & Risk Management (`security.html`)
Defending AI applications from malicious actors.
*   **Concepts:** The OWASP LLM Top 10.
*   **Threats:** Prompt Injection, Indirect Prompt Injection (via RAG), Excessive Agency, Data Exfiltration, Model Poisoning.
*   **Defenses:** Nvidia NeMo Guardrails, Input/Output filtering.

### Module 10: AI Evaluation (`evals.html`)
How to mathematically prove your AI is accurate, rather than relying on "vibes".
*   **Concepts:** LLM-as-a-Judge, Golden Datasets.
*   **Metrics:** Faithfulness, Answer Relevance, Context Recall, Context Precision.
*   **Frameworks:** RAGAS, DeepEval.

### Module 11: OS Tools & FinOps (`tools.html`)
Managing the cost and privacy of AI infrastructure.
*   **Concepts:** Local AI deployment, Open Weights vs. Closed Source.
*   **Tools:** Ollama, Open WebUI, LM Studio.
*   **FinOps:** Dynamic model routing (routing easy tasks to cheap/free local models, and hard tasks to expensive API models like GPT-4).

### Module 12: Glossary (`glossary.html`)
A searchable, A-Z dictionary of all the buzzwords mentioned above.

---
*Generated automatically as a comprehensive manifest of the AI for All project.*
