"""Configuration module for Collibra MCP.

This module centralizes all Collibra configuration variables including
the base URL and authentication credentials.
"""

import os

# Collibra API base URL
COLLIBRA_BASE_URL = '<YOUR COLLIBRA URL>'

# Authentication credentials from environment variables
USERNAME = os.getenv('COLLIBRA_ADMIN_USN')
PASSWORD = os.getenv('COLLIBRA_ADMIN_PW')

