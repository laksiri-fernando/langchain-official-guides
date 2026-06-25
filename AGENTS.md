# AGENTS.md

## Repo structure

Two independent `uv`-managed Python projects under one root:

- `langchain/` — `langchain.agents.create_agent` examples (multi-provider: Google GenAI, Ollama, OpenAI, Anthropic)
- `langchain-deepagents/` — `deepagents.create_deep_agent` examples (OpenRouter, Ollama, Tavily search)

Both require Python 3.12 and have their own `pyproject.toml` + `uv.lock`.

## Developer commands

Run from inside the project subdirectory (e.g. `langchain/` or `langchain-deepagents/`):

```bash
uv sync          # install deps from uv.lock
uv run <script>  # run script in project venv
```

Example:

```bash
cd langchain && uv run python quickstart.py
```

## Environment

- Root `.env` contains `ANTHROPIC_API_KEY`
- `deepagents/quickstart.py` additionally requires `TAVILY_API_KEY` in `.env`
- `langchain-deepagents/.env` and `langchain/.env` are gitignored at the project level; a shared root `.env` is gitignored at the repo level
- Every script calls `load_dotenv()` at startup — no special env loading needed beyond having `.env` present

## Model spec convention

Models are specified as `provider:model-name` strings:

| Provider | Example |
|---|---|
| Google GenAI | `google_genai:gemini-2.5-flash-lite` |
| Ollama | `ollama:qwen3.5:4b`, `ollama:gpt-oss:20b-cloud` |
| OpenRouter | `openrouter:google/gemma-4-31b-it:free` |
| Anthropic | `anthropic:claude-sonnet-4-5` |
| OpenAI | `openai:gpt-5.5` |

## What is *not* configured

- No tests, no CI, no linting, no formatter, no type checking
- No `Makefile`, `justfile`, or task runner
- No `.editorconfig`, pre-commit hooks, or codegen
- Scripts are standalone examples, not a library package — there are no entrypoint exports, just `python some_file.py`

## graphify

This project has a knowledge graph at graphify-out/ with god nodes, community structure, and cross-file relationships.

When the user types `/graphify`, invoke the `skill` tool with `skill: "graphify"` before doing anything else.

Rules:
- For codebase questions, first run `graphify query "<question>"` when graphify-out/graph.json exists. Use `graphify path "<A>" "<B>"` for relationships and `graphify explain "<concept>"` for focused concepts. These return a scoped subgraph, usually much smaller than GRAPH_REPORT.md or raw grep output.
- Dirty graphify-out/ files are expected after hooks or incremental updates; dirty graph files are not a reason to skip graphify. Only skip graphify if the task is about stale or incorrect graph output, or the user explicitly says not to use it.
- If graphify-out/wiki/index.md exists, use it for broad navigation instead of raw source browsing.
- Read graphify-out/GRAPH_REPORT.md only for broad architecture review or when query/path/explain do not surface enough context.
- After modifying code, run `graphify update .` to keep the graph current (AST-only, no API cost).
