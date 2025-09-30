# Integration Examples

## Claude Desktop (Anthropic)

Use Claude to compute a maritime route with a prompt:

> "Using the MCP server at `https://mcp.projectharrison.org/route`, get the distance in nautical miles between New York (40.7128, -74.0060) and Rotterdam (51.9244, 4.4777). Return the polyline and estimated distance."

Claude should POST a JSON body and parse the response.

---

## MCP Inspector (CLI)

You can query `searoute_mcp` locally:

```bash
curl -X POST http://localhost:8000/route \
  -H "Content-Type: application/json" \
  -d '{"source": [40.7128, -74.0060], "destination": [51.9244, 4.4777]}'
