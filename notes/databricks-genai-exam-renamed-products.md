# Databricks Generative AI Engineer Associate — Renamed Product Tracker

Verified against docs.databricks.com and mirrors (Microsoft Learn / Google Cloud docs) as of **September 2026**.
Exam guide version referenced: **March 18, 2026**.

> Re-check this list two weeks before your exam date — Databricks renaming has been frequent in 2026.

---

## Confirmed renames

### 1. Vector Search → Databricks AI Search
- **Old name(s):** Vector Search / Databricks Vector Search / Mosaic AI Vector Search
- **Current name:** **Databricks AI Search**
- **What it does:** Built-in search solution that finds embeddings most similar to a query; powers retrieval for RAG systems, recommenders, and image/video recognition.
- **Exam relevance:** Section 4 objectives on "Mosaic AI Vector Search," creating/querying a Vector Search index, and configuring vector search all map to this product.
- **Source:** docs.databricks.com/aws/en/ai-search/create-ai-search

### 2. Agent Bricks "Multiagent Supervisor" → Supervisor Agent
- **Old name(s):** Multiagent Supervisor / Multi-Agent Supervisor (exact term used in the exam guide, Section 1)
- **Current name:** **Supervisor Agent** (an Agent Bricks capability)
- **What it does:** Coordinates Genie Agents, agent endpoints, Unity Catalog functions, MCP servers, and custom agents to complete complex, multi-domain tasks, with built-in access controls.
- **Exam relevance:** Section 1 — "Determine how and when to use Agent Bricks ... Multiagent Supervisor."
- **Source:** docs.databricks.com/aws/en/agents/agent-bricks/multi-agent-supervisor

### 3. Genie Spaces → Genie Agents
- **Old name(s):** Genie Spaces (exact term used in the exam guide, Section 3)
- **Current name:** **Genie Agents**
- **What it does:** Converts natural-language business questions into SQL against annotated Unity Catalog tables; returns the generated query, results, and visualizations.
- **Exam relevance:** Section 3 — "Enable multi-agent systems to leverage Genie Spaces or conversational API to retrieve data."
- **Source:** docs.databricks.com/aws/en/genie-agents/

---

## Rename in progress — verify before relying on it

### 4. AI Gateway → Unity AI Gateway (Beta)
- **Old name:** Mosaic AI Gateway
- **Current name (per docs, but Beta):** **Unity AI Gateway**
- **Status note:** docs.databricks.com/en/ai-gateway/ labels this feature **Beta** and separately references "the previous version of Unity AI Gateway" / "Unity AI Gateway for serving endpoints" — suggesting two overlapping surfaces exist right now (an older gateway tied to Model Serving endpoints, and a newer, broader Beta gateway).
- **Exam relevance:** Section 6 — "Use AI Gateway (Inference Tables, Usage Tables, and rate limiting) to track an LLM or agent deployed via Agent Framework."
- **Action:** Confirm current GA status and scope at docs.databricks.com/en/ai-gateway/ close to your exam date.

---

## Not clearly renamed, but flagged for confusion risk

### 5. Model Serving (still "Mosaic AI Model Serving" in docs)
- **Old name(s):** Model Serving / Databricks Model Serving
- **Current docs name:** **Mosaic AI Model Serving** — confirmed current as of March 2026 official release notes.
- **Note:** The "Mosaic AI" prefix predates the 2-year window (from the 2023 MosaicML acquisition), so this isn't a *new* rename — but the exam guide drops the "Mosaic AI" prefix entirely, so don't be thrown if official materials use the fuller name.
- **Source:** docs.databricks.com/aws/en/release-notes/product/2026/march

### 6. Mosaic AI Agent Framework vs. Agent Bricks
- **Current docs name:** Still **Mosaic AI Agent Framework** in some pages (e.g., `databricks-agents` PyPI package, June 2026 release, still described as "Mosaic AI Agent Framework SDK").
- **Confusion risk:** The exam guide references both "Agent Framework" (Section 3) and "Agent Bricks" (Section 1) as if distinct. Could not fully confirm from docs.databricks.com whether Agent Framework has been folded into Agent Bricks or remains a separate, more code-first path.
- **Action:** Verify the current relationship between these two at docs.databricks.com/generative-ai/ before treating them as interchangeable on the exam.

### 7. Databricks Feature Store (not a rename — legacy split, appears in a sample question, not the objectives)
- **Current name:** **Databricks Feature Store** for Unity Catalog–enabled workspaces.
- **Legacy name:** **Workspace Feature Store (deprecated)** for non–Unity Catalog workspaces.
- Not part of the official exam objectives list, but appears in one of the sample questions.

---

## Checked and found stable (no rename detected)
- Unity Catalog
- MLflow
- Agent Evaluation
- Foundation Model APIs

---

## How to use this file
1. Paste this table into your AI study tool at the start of every session (see the AI Prep Guide's Step 3).
2. Before your exam, re-run the verification searches against docs.databricks.com for items marked "verify" above.
3. Note the one unverified claim excluded from this list: a non-official blog post claimed a much larger June 2026 Genie rebrand (Genie One, Genie Code, Genie Ontology) tied to Databricks Assistant. This was **not** confirmed directly against docs.databricks.com and is intentionally left out — treat it as a lead to check yourself, not a fact.
