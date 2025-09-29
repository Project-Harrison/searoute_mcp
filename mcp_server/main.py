import logging
from mcp_server.tools import mcp  # Import shared FastMCP instance

def main():
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting route-server")
    mcp.run()

if __name__ == "__main__":
    main()
