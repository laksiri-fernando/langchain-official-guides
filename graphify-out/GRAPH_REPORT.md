# Graph Report - .  (2026-06-24)

## Corpus Check
- Corpus is ~9,715 words - fits in a single context window. You may not need a graph.

## Summary
- 60 nodes · 57 edges · 14 communities (8 shown, 6 thin omitted)
- Extraction: 95% EXTRACTED · 5% INFERRED · 0% AMBIGUOUS · INFERRED: 3 edges (avg confidence: 0.85)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Core Pipeline|Core Pipeline]]
- [[_COMMUNITY_OpenCode Configuration|OpenCode Configuration]]
- [[_COMMUNITY_Graphify Features|Graphify Features]]
- [[_COMMUNITY_Extraction Spec|Extraction Spec]]
- [[_COMMUNITY_Query & MCP|Query & MCP]]
- [[_COMMUNITY_GitHub & Merge|GitHub & Merge]]
- [[_COMMUNITY_Update Mechanics|Update Mechanics]]
- [[_COMMUNITY_FalkorDB Export|FalkorDB Export]]
- [[_COMMUNITY_GraphML Export|GraphML Export]]
- [[_COMMUNITY_Neo4j Export|Neo4j Export]]
- [[_COMMUNITY_SVG Export|SVG Export]]
- [[_COMMUNITY_Token Benchmark|Token Benchmark]]
- [[_COMMUNITY_Cluster Only|Cluster Only]]

## God Nodes (most connected - your core abstractions)
1. `Full Build Pipeline` - 16 edges
2. `Graphify System` - 9 edges
3. `Subagent Extraction Prompt Template` - 6 edges
4. `docs-langchain` - 5 edges
5. `BFS Graph Traversal` - 5 edges
6. `Save Result Feedback Loop` - 4 edges
7. `AST Structural Extraction` - 3 edges
8. `Semantic LLM Extraction` - 3 edges
9. `Watch Mode for Auto-Rebuild` - 3 edges
10. `GitHub Clone` - 3 edges

## Surprising Connections (you probably didn't know these)
- `MCP Server` --conceptually_related_to--> `BFS Graph Traversal`  [INFERRED]
  skills/graphify/references/exports.md → skills/graphify/references/query.md
- `Full Build Pipeline` --references--> `URL Ingestion`  [EXTRACTED]
  skills/graphify/SKILL.md → skills/graphify/references/add-watch.md
- `Full Build Pipeline` --references--> `Wiki Export`  [EXTRACTED]
  skills/graphify/SKILL.md → skills/graphify/references/exports.md
- `Full Build Pipeline` --references--> `GitHub Clone`  [EXTRACTED]
  skills/graphify/SKILL.md → skills/graphify/references/github-and-merge.md
- `Full Build Pipeline` --references--> `CLAUDE.md Integration`  [EXTRACTED]
  skills/graphify/SKILL.md → skills/graphify/references/hooks.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Build Pipeline Phases** — graphify_skill_corpus_detection, graphify_skill_ast_extraction, graphify_skill_semantic_extraction, graphify_skill_community_detection, graphify_skill_community_labeling, graphify_skill_graph_outputs [EXTRACTED 1.00]
- **Graph Query and Exploration Operations** — references_query_bfs_traversal, references_query_dfs_traversal, references_query_query_expansion, references_query_shortest_path, references_query_node_explanation, references_query_save_result [EXTRACTED 1.00]
- **Graph Export Capabilities** — references_exports_wiki_export, references_exports_neo4j_export, references_exports_falkordb_export, references_exports_svg_export, references_exports_graphml_export, references_exports_mcp_server, references_exports_token_benchmark [EXTRACTED 1.00]

## Communities (14 total, 6 thin omitted)

### Community 0 - "Core Pipeline"
Cohesion: 0.17
Nodes (15): AST Structural Extraction, Full Build Pipeline, Community Detection and Clustering, Community Labeling, Corpus File Detection, Graph Output Generation, Semantic LLM Extraction, Debounce Mechanism (+7 more)

### Community 1 - "OpenCode Configuration"
Cohesion: 0.22
Nodes (8): enabled, transport, type, url, mcp, docs-langchain, plugin, $schema

### Community 2 - "Graphify Features"
Cohesion: 0.25
Nodes (8): Cumulative Cost Tracker, Subagent Dispatch for Semantic Extraction, Extraction Cache, God Nodes Analysis, Graph Query Interface, Graphify System, Python Interpreter Resolution, Obsidian Vault Export

### Community 3 - "Extraction Spec"
Cohesion: 0.29
Nodes (7): Honesty Rules and Audit Trail, Confidence Score Rubric, Deep Mode Extraction, Hyperedge Definition, Node ID Format Rules, Source File Path Rule, Subagent Extraction Prompt Template

### Community 4 - "Query & MCP"
Cohesion: 0.33
Nodes (7): MCP Server, BFS Graph Traversal, DFS Graph Traversal, Node Explanation, Query Vocabulary Expansion, Save Result Feedback Loop, Shortest Path Finding

### Community 5 - "GitHub & Merge"
Cohesion: 0.67
Nodes (3): Cross-Repo Graph Merge, GitHub Clone, Multi-Subfolder Merge

### Community 6 - "Update Mechanics"
Cohesion: 0.67
Nodes (3): Build Merge Function, Code-Only Change Detection, Incremental Update

## Knowledge Gaps
- **36 isolated node(s):** `$schema`, `plugin`, `type`, `transport`, `url` (+31 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **6 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Full Build Pipeline` connect `Core Pipeline` to `Graphify Features`, `Query & MCP`, `GitHub & Merge`, `Update Mechanics`?**
  _High betweenness centrality (0.424) - this node is a cross-community bridge._
- **Why does `Graphify System` connect `Graphify Features` to `Core Pipeline`, `Extraction Spec`?**
  _High betweenness centrality (0.179) - this node is a cross-community bridge._
- **Why does `BFS Graph Traversal` connect `Query & MCP` to `Core Pipeline`?**
  _High betweenness centrality (0.132) - this node is a cross-community bridge._
- **What connects `$schema`, `plugin`, `type` to the rest of the system?**
  _38 weakly-connected nodes found - possible documentation gaps or missing edges._