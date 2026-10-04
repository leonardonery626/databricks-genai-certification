# Databricks Certified Generative AI Engineer Associate — Study Repo

Personal prep material for the **Databricks Certified Generative AI Engineer Associate** exam (exam guide version: March 18, 2026). Goal: pass within 3 months.

## Layout

| Path | What it is |
|---|---|
| `context/official/` | Official Databricks PDFs: the exam guide (Mar 2026) and the "AI Prep Guide: Any Databricks Certification" |
| `context/study-tutor-prompt.md` | The prompt used to prime an AI tutor every session |
| `notes/databricks-genai-exam-renamed-products.md` | Tracker mapping exam-guide product names to current Databricks names (verified Sept 2026) |
| `scripts/query_databricks_endpoint.py` | Query a Databricks Model Serving / agent endpoint from a laptop via the OpenAI-compatible API |

## Running the script

```powershell
pip install -U openai databricks-sdk
$env:DATABRICKS_HOST  = "https://<your-workspace>.cloud.databricks.com"
$env:DATABRICKS_TOKEN = "dapi..."   # never commit this
python scripts/query_databricks_endpoint.py                 # list endpoints
python scripts/query_databricks_endpoint.py <endpoint-name> "your question"
```

Credentials are read from environment variables only; `.env` and `.databrickscfg` are git-ignored.

## Sources

- Exam guide and prep guide © Databricks, downloaded from the certification page on databricks.com — always check there for the current version two weeks before the exam.
- Product facts: [docs.databricks.com](https://docs.databricks.com) and [Databricks Academy](https://academy.databricks.com).
