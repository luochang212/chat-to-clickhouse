#!/bin/bash

# USAGE: pip install mcp-clickhouse
# TEST: curl http://localhost:8760/health

source .env
python -m mcp_clickhouse.main
