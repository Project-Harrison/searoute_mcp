# Searoute MCP

An MCP server for maritime routing.  
It provides three tools via Model Context Protocol:

- **compute_distance** → shortest oceangoing route distance (nm).
- **compute_route** → route geometry + distance.
- **compute_geodesic** → great-circle distance (nm).

## Install

```bash
git clone https://github.com/YOUR_ORG/searoute_mcp
cd searoute_mcp
python -m venv .venv && source .venv/bin/activate
pip install -e .
