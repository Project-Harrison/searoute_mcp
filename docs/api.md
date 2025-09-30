**📚 Docs Setup**

**1. Create `/docs/index.md`:**
Basic landing page for the docs.

```markdown
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
```

---

**2. Create `/docs/api.md`:**
Document the API endpoints.

````markdown
# API Reference

## `/route`
**Method:** POST  
**Description:** Returns a maritime route between two coordinates or port names.

**Example Request:**
```json
{
  "source": [37.7749, -122.4194],
  "destination": [35.6895, 139.6917]
}
````

**Example Response:**

```json
{
  "distance_nm": 4672.1,
  "polyline": [[...]],
  "metadata": {...}
}
```
