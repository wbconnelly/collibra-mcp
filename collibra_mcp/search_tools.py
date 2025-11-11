"""Search tools for Collibra MCP."""
import requests
from pprint import pformat
import os
import base64

from collibra_mcp.config import COLLIBRA_BASE_URL, USERNAME, PASSWORD

def search_collibra_assets(keyword, asset_type_id):
    """
    Searches for assets in Collibra.
    
    Args:
        keyword: The search keyword to use.
        asset_type_id: The asset type ID to filter by.
    """
    api_url = f'{COLLIBRA_BASE_URL}/search'
    payload = {
        "keywords": keyword,
        "filters": [
            {
                "field": "assetType",
                "values": [
                    asset_type_id
                ]
            }
        ],
        "sortField": "RELEVANCE",
        "sortOrder": "DESC",
        "limit": 50,
        "offset": 0,
        "product": "ALL"
    }
    response = requests.post(api_url, json=payload, auth=(USERNAME, PASSWORD))
    if response.status_code == 200:
        return response.json()
    else:
        return {
            "error": f"Failed to search Collibra assets. Status code: {response.status_code}",
            "status_code": response.status_code,
            "response": response.text
        }
