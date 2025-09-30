# tests/test_basic.py

from mcp_server import main

def test_import_main():
    """Basic smoke test to ensure the main module imports cleanly."""
    assert main is not None
