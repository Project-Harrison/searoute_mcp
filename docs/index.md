# searoute_mcp

A Maritime Routing MCP Server by Project Harrison.  
Provides geodesic routes between global ports using the MCP protocol.

## Key Features
- `/route`: Compute optimized maritime routes.
- `/version`: Check the server version.

## Usage
Submit a POST request to `/route` with two ports or coordinates.  
Returns a polyline, distance, and metadata.

See [API Reference](api.md) for full details.
