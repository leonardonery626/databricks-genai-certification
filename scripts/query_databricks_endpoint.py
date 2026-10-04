"""
Query a Databricks serving endpoint from your own laptop.

Setup (once, in a terminal on your computer):
    pip install -U openai databricks-sdk

Set two environment variables (PowerShell example):
    $env:DATABRICKS_HOST  = "https://<your-workspace>.cloud.databricks.com"
    $env:DATABRICKS_TOKEN = "dapi..."          # Settings > Developer > Access tokens

Run:
    python query_databricks_endpoint.py                       # list endpoints
    python query_databricks_endpoint.py <endpoint-name>       # chat with one
"""
import os
import sys

from openai import OpenAI

HOST = os.environ["DATABRICKS_HOST"].rstrip("/")
TOKEN = os.environ["DATABRICKS_TOKEN"]

# Databricks serving endpoints speak the OpenAI protocol.
# base_url = workspace host + /serving-endpoints ; model = ENDPOINT NAME.
client = OpenAI(api_key=TOKEN, base_url=f"{HOST}/serving-endpoints")


def list_endpoints():
    from databricks.sdk import WorkspaceClient  # reads the same env vars
    w = WorkspaceClient()
    for ep in w.serving_endpoints.list():
        print(ep.name)


def ask(endpoint: str, question: str):
    msgs = [{"role": "user", "content": question}]
    # Agent endpoints (Knowledge Assistant, ResponsesAgent) use the Responses API: `input=`
    try:
        r = client.responses.create(model=endpoint, input=msgs)
        print(r.output_text)
        return
    except Exception as e:
        print(f"[responses API failed: {e.__class__.__name__}] trying chat completions...")
    # Foundation-model / legacy chat endpoints use Chat Completions: `messages=`
    r = client.chat.completions.create(model=endpoint, messages=msgs, max_tokens=256)
    print(r.choices[0].message.content)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        list_endpoints()
    else:
        ask(sys.argv[1], " ".join(sys.argv[2:]) or "What can you tell me about these documents?")
