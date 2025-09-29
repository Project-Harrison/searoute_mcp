from mcp_server import tools

def test_compute_distance():
    result = tools.compute_distance(-118.25, 34.05, -157.86, 21.31)
    assert 2000 < result < 3000

def test_compute_route():
    result = tools.compute_route(-118.25, 34.05, -157.86, 21.31)
    assert "distance_nm" in result
    assert "geometry" in result
    assert result["distance_nm"] > 2000

def test_compute_geodesic():
    result = tools.compute_geodesic(-118.25, 34.05, -157.86, 21.31)
    assert 2000 < result < 3000
