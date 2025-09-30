# searoute_mcp

<div align="center">

<strong>Maritime Routing MCP Server (Python)</strong>

</div>

<!-- omit in toc -->
## Table of Contents

- [searoute_mcp](#searoute_mcp)
  - [Overview](#overview)
  - [Installation](#installation)
  - [Quickstart](#quickstart)
  - [Core Tools](#core-tools)
  - [Running Your Server](#running-your-server)
  - [Contributing](#contributing)
  - [License](#license)

---

## Overview

**searoute_mcp** is a Model Context Protocol (MCP) server that exposes oceangoing routing tools.  
It integrates [searoute-py](https://github.com/genthalili/searoute-py) with MCP so clients like Claude Desktop can:

- Compute oceangoing route distances (nautical miles)
- Retrieve full oceangoing routes with waypoints (GeoJSON)
- Compute geodesic great-circle distances

---

## Installation

Clone the repository and install locally:

```bash
git clone https://github.com/ShippingIntel/searoute_mcp.git
cd searoute_mcp
python3 -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate      # Windows

pip install -r requirements.txt
````

Dependencies include:

* `mcp[python]>=0.1.0`
* `searoute>=1.4.3`
* `geopy>=2.4.1`

---

## Quickstart

Run the server directly:

```bash
python -m mcp_server.main
```

Install into Claude Desktop:

```bash
mcp install mcp_server/main.py
```

Test with the MCP Inspector:

```bash
mcp dev mcp_server/main.py
```

---

## Core Tools

* **`compute_distance`**
  Shortest oceangoing route distance between two coordinates.

* **`compute_route`**
  Full oceangoing route with distance and waypoints (GeoJSON).

* **`compute_geodesic`**
  Great-circle distance (nautical miles) ignoring land/water constraints.

---

## Running Your Server

Use the `FastMCP` transport options:

```bash
# stdio (local dev)
python -m mcp_server.main stdio

# Streamable HTTP (for deployment)
python -m mcp_server.main streamable-http
```

---

## Contributing

We welcome contributions! See the [contributing guide](CONTRIBUTING.md) for setup and workflow.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


