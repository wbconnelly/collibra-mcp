"""Helper functions for Collibra MCP.

This module contains utility and helper functions used across the Collibra MCP package.
"""

import requests
from collibra_mcp.config import USERNAME, PASSWORD


def mcp_get_request(api_url, success_status_codes=None, **kwargs):
    """
    Template function for making GET requests to Collibra API.
    
    Args:
        api_url: The full API URL to make the request to.
        success_status_codes: List of status codes considered successful (default: [200]).
        **kwargs: Additional arguments to pass to requests.get() (e.g., headers, params).
    
    Returns:
        On success: response.json() or parsed response data
        On failure: dict with error information including status_code and response text
    """
    if success_status_codes is None:
        success_status_codes = [200, 201, 202, 204]
    
    try:
        # Automatically add authentication
        response = requests.get(
            api_url,
            auth=(USERNAME, PASSWORD),
            headers={'Content-Type': 'application/json'},
            **kwargs
        )
        
        if response.status_code in success_status_codes:
            return response.json()
        else:
            return {
                "error": f"Request failed. Status code: {response.status_code}",
                "status_code": response.status_code,
                "response": response.text
            }
    except Exception as e:
        return {"error": f"Error making GET request: {str(e)}"}


def make_post_request(api_url, payload=None, success_status_codes=None, **kwargs):
    """
    Template function for making POST requests to Collibra API.
    
    Args:
        api_url: The full API URL to make the request to.
        payload: JSON payload to send in the request body (default: None).
        success_status_codes: List of status codes considered successful (default: [200, 201]).
        **kwargs: Additional arguments to pass to requests.post() (e.g., headers).
    
    Returns:
        On success: response.json() or parsed response data
        On failure: dict with error information including status_code, payload_sent, and response text
    """
    if success_status_codes is None:
        success_status_codes = [200, 201]
    
    try:
        # Automatically add authentication
        response = requests.post(
            api_url,
            json=payload,
            auth=(USERNAME, PASSWORD),
            **kwargs
        )
        
        if response.status_code in success_status_codes:
            return response.json()
        else:
            error_response = {
                "error": f"Request failed. Status code: {response.status_code}",
                "status_code": response.status_code,
                "response": response.text
            }
            if payload:
                error_response["payload_sent"] = payload
            return error_response
    except Exception as e:
        return {"error": f"Error making POST request: {str(e)}"}


def make_put_request(api_url, payload=None, success_status_codes=None, **kwargs):
    """
    Template function for making PUT requests to Collibra API.
    
    Args:
        api_url: The full API URL to make the request to.
        payload: JSON payload to send in the request body (default: None).
        success_status_codes: List of status codes considered successful (default: [200, 201]).
        **kwargs: Additional arguments to pass to requests.put() (e.g., headers).
    
    Returns:
        On success: response.json() or parsed response data
        On failure: dict with error information including status_code, payload_sent, and response text
    """
    if success_status_codes is None:
        success_status_codes = [200, 201]
    
    try:
        # Automatically add authentication
        response = requests.put(
            api_url,
            json=payload,
            auth=(USERNAME, PASSWORD),
            **kwargs
        )
        
        if response.status_code in success_status_codes:
            return response.json()
        else:
            error_response = {
                "error": f"Request failed. Status code: {response.status_code}",
                "status_code": response.status_code,
                "response": response.text
            }
            if payload:
                error_response["payload_sent"] = payload
            return error_response
    except Exception as e:
        return {"error": f"Error making PUT request: {str(e)}"}


def make_patch_request(api_url, payload=None, success_status_codes=None, **kwargs):
    """
    Template function for making PATCH requests to Collibra API.
    
    Args:
        api_url: The full API URL to make the request to.
        payload: JSON payload to send in the request body (default: None).
        success_status_codes: List of status codes considered successful (default: [200, 201]).
        **kwargs: Additional arguments to pass to requests.patch() (e.g., headers).
    
    Returns:
        On success: response.json() or parsed response data
        On failure: dict with error information including status_code, payload_sent, and response text
    """
    if success_status_codes is None:
        success_status_codes = [200, 201]
    
    try:
        # Automatically add authentication
        response = requests.patch(
            api_url,
            json=payload,
            auth=(USERNAME, PASSWORD),
            **kwargs
        )
        
        if response.status_code in success_status_codes:
            return response.json()
        else:
            error_response = {
                "error": f"Request failed. Status code: {response.status_code}",
                "status_code": response.status_code,
                "response": response.text
            }
            if payload:
                error_response["payload_sent"] = payload
            return error_response
    except Exception as e:
        return {"error": f"Error making PATCH request: {str(e)}"}


def make_delete_request(api_url, success_status_codes=None, **kwargs):
    """
    Template function for making DELETE requests to Collibra API.
    
    Args:
        api_url: The full API URL to make the request to.
        success_status_codes: List of status codes considered successful (default: [200, 204]).
        **kwargs: Additional arguments to pass to requests.delete() (e.g., headers).
    
    Returns:
        On success: response.json() if response has content, otherwise success message
        On failure: dict with error information including status_code and response text
    """
    if success_status_codes is None:
        success_status_codes = [200, 204]
    
    try:
        # Automatically add authentication
        response = requests.delete(
            api_url,
            auth=(USERNAME, PASSWORD),
            **kwargs
        )
        
        if response.status_code in success_status_codes:
            # Some DELETE requests return empty body
            if response.text:
                return response.json()
            else:
                return {"success": f"Successfully deleted resource. Status code: {response.status_code}"}
        else:
            return {
                "error": f"Request failed. Status code: {response.status_code}",
                "status_code": response.status_code,
                "response": response.text
            }
    except Exception as e:
        return {"error": f"Error making DELETE request: {str(e)}"}

