from mcp_server import tools

def test_compute_distance():
    result = tools.compute_distance(34.05, -118.25, 21.31, -157.86)  # LA → Honolulu
    assert result > 0

def test_compute_route():
    result = tools.compute_route(34.05, -118.25, 21.31, -157.86)  # LA → Honolulu
    assert "distance_nm" in result
    assert result["distance_nm"] > 0

def test_compute_geodesic():
    result = tools.compute_geodesic(34.05, -118.25, 21.31, -157.86)  # LA → Honolulu
    assert result > 0
