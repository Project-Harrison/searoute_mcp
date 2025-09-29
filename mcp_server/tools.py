from mcp.server.fastmcp import FastMCP
import searoute as sr
from geopy.distance import geodesic

# Initialize FastMCP instance
mcp = FastMCP("route-server")

@mcp.tool(description="Compute shortest oceangoing route distance in nautical miles.")
def compute_distance(start_lon: float, start_lat: float, end_lon: float, end_lat: float) -> float:
    route = sr.searoute([start_lon, start_lat], [end_lon, end_lat], units="nm")
    return route["properties"]["length"]

@mcp.tool(description="Compute shortest oceangoing route with distance and waypoints between two coordinates.")
def compute_route(start_lon: float, start_lat: float, end_lon: float, end_lat: float) -> dict:
    route = sr.searoute([start_lon, start_lat], [end_lon, end_lat], units="nm")
    return {
        "distance_nm": route["properties"]["length"],
        "geometry": route["geometry"]
    }

@mcp.tool(description="Compute geodesic great-circle distance in nautical miles (ignores route, this is shortest distance on a sphere).")
def compute_geodesic(start_lon: float, start_lat: float, end_lon: float, end_lat: float) -> float:
    km = geodesic((start_lat, start_lon), (end_lat, end_lon)).km
    return km * 0.539957
