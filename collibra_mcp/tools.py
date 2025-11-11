"""MCP server tools implementation."""

import requests
from pprint import pformat
import os
import base64

from collibra_mcp.config import COLLIBRA_BASE_URL, USERNAME, PASSWORD
from collibra_mcp.helper_functions import mcp_get_request

def get_collibra_assets(domain_id):
    """
    Retrieves assets from Collibra.
    
    Args:
        domain_id: The domain ID to filter assets by.
    
    Returns:
        A list of Collibra assets or an error message.
    """
    api_url = f'{COLLIBRA_BASE_URL}/assets?domainId={domain_id}'
    return mcp_get_request(api_url)
"""     try:
        # Make GET request with basic authentication
        response = requests.get(
            api_url,
            auth=(USERNAME, PASSWORD),
            headers={'Content-Type': 'application/json'}
        )
        
        # Check if request was successful
        if response.status_code == 200:
            return response.json()
        else:
            return {
                "error": f"Failed to retrieve Collibra assets. Status code: {response.status_code}",
                "status_code": response.status_code,
                "response": response.text
            }
    except Exception as e:
        return {"error": f"Error retrieving Collibra assets: {str(e)}"} """

def get_community_id(community_name):
    """
    Retrieves the community ID from Collibra by name.
    
    Args:
        community_name: The name of the community to search for.
    """
    api_url = f'{COLLIBRA_BASE_URL}/communities?name={community_name}'
    response = requests.get(api_url, auth=(USERNAME, PASSWORD))
    try:
        if response.status_code == 200:
            return response.json()['id']
        else:
            return {
                "error": f"Failed to retrieve community ID. Status code: {response.status_code}",
                "status_code": response.status_code,
                "response": response.text
            }
    except Exception as e:
        return {"error": f"Error retrieving community ID: {str(e)}"}

def get_collibra_domains(domain_name):
    """
    Retrieves domains from Collibra by name.
    
    Args:
        domain_name: The domain name to search for.
    
    Returns:
        A list of Collibra domains or an error message.
    """
    api_url = f'{COLLIBRA_BASE_URL}/domains?name={domain_name}'
    
    try:
        # Make GET request with basic authentication
        response = requests.get(
            api_url,
            auth=(USERNAME, PASSWORD),
            headers={'Content-Type': 'application/json'}
        )
        
        # Check if request was successful
        if response.status_code == 200:
            data = response.json()
            if data.get('results') and len(data['results']) > 0:
                return data['results'][0]['id']
            else:
                return {"error": f"Domain '{domain_name}' not found"}
        else:
            return {
                "error": f"Failed to retrieve Collibra domains. Status code: {response.status_code}",
                "status_code": response.status_code,
                "response": response.text
            }
    except Exception as e:
        return {"error": f"Error retrieving Collibra domains: {str(e)}"}

def add_collibra_domain(domain_name, community_id, type_id):
    api_url = COLLIBRA_BASE_URL + "/domains"

    payload = {
        "name": domain_name,
        "communityId": community_id,
        "typeId": type_id
    }

    try:
        response = requests.post(api_url, json=payload, auth=(USERNAME, PASSWORD))
        if response.status_code == 200 or response.status_code == 201:
            return response.json()
        else:
            return {
                "error": f"Failed to add Collibra domain. Status code: {response.status_code}",
                "status_code": response.status_code,
                "response": response.text
            }
    except Exception as e:
        return {"error": f"Error adding Collibra domain: {str(e)}"}

def get_asset_attributes(assetId, typeIds):
    api_url = f'{COLLIBRA_BASE_URL}/attributes?assetId={assetId}&typeIds={typeIds}&page=0&size=100'
    try:
        response = requests.get(api_url, auth=(USERNAME, PASSWORD))
        if response.status_code == 200:
            return response.json()
        else:
            return {
                "error": f"Failed to retrieve asset attributes. Status code: {response.status_code}",
                "status_code": response.status_code,
                "response": response.text
            }
    except Exception as e:
        return {"error": f"Error retrieving asset attributes: {str(e)}"}

def add_collibra_asset(asset_name, asset_type, domain_id, owner_id=None):

    api_url = COLLIBRA_BASE_URL + "/assets"
    payload = {
        "name": asset_name,
        "typeId": asset_type,
        "domainId": domain_id
    }
    
    # Add owner if provided
    if owner_id:
        payload["ownerId"] = owner_id
    
    print(payload)

    try:
        response = requests.post(api_url, json=payload, auth=(USERNAME, PASSWORD))
        if response.status_code == 200 or response.status_code == 201:
            return response.json()
        else:
            return {
                "error": f"Failed to add Collibra asset. Status code: {response.status_code}",
                "status_code": response.status_code,
                "response": response.text
            }
    except Exception as e:
        return {"error": f"Error adding Collibra asset: {str(e)}"}

def add_collibra_community(community_name):
    """
    Creates a new community in Collibra.
    
    Args:
        community_name: The name of the community to create.
    
    Returns:
        The created community or an error message.
    """
    api_url = f'{COLLIBRA_BASE_URL}/communities'
    payload = {
        "name": community_name
    }
    
    try:
        response = requests.post(api_url, json=payload, auth=(USERNAME, PASSWORD))
        if response.status_code == 200 or response.status_code == 201:
            return response.json()
        else:
            return {
                "error": f"Failed to add Collibra community. Status code: {response.status_code}",
                "status_code": response.status_code,
                "response": response.text
            }
    except Exception as e:
        return {"error": f"Error adding Collibra community: {str(e)}"}

def get_domain_type_id(domain_type_name):
    """
    Retrieves the domain type ID from Collibra by name.
    
    Args:
        domain_name: The name of the domain type to search for.
    """
    api_url = f'{COLLIBRA_BASE_URL}/domainTypes?name={domain_type_name}'
    try:
        response = requests.get(api_url, auth=(USERNAME, PASSWORD))
        if response.status_code == 200:
            data = response.json()
            if data and 'results' in data and len(data['results']) > 0:
                return data['results'][0]['id']
            return {"error": f"Domain type '{domain_type_name}' not found"}
        else:
            return {
                "error": f"Failed to retrieve domain type ID. Status code: {response.status_code}",
                "status_code": response.status_code,
                "response": response.text
            }
    except Exception as e:
        return {"error": f"Error retrieving domain type ID: {str(e)}"}

def get_asset_type_id(asset_type_name):
    """
    Retrieves the asset type ID from Collibra by name.
    
    Args:
        asset_type_name: The name of the asset type to search for.
    """
    api_url = f'{COLLIBRA_BASE_URL}/assetTypes?name={asset_type_name}&nameMatchMode=EXACT'
    try:
        response = requests.get(api_url, auth=(USERNAME, PASSWORD))
        if response.status_code == 200:
            data = response.json()
            if data and 'results' in data and len(data['results']) > 0:
                return data['results'][0]['id']
            return {"error": f"Asset type '{asset_type_name}' not found"}
        else:
            return {
                "error": f"Failed to retrieve asset type ID. Status code: {response.status_code}",
                "status_code": response.status_code,
                "response": response.text
            }
    except Exception as e:
        return {"error": f"Error retrieving asset type ID: {str(e)}"}

def get_user_id(username):
    """
    Retrieves the user ID from Collibra by username.
    
    Args:
        username: The username to search for.
    
    Returns:
        The user ID or an error message.
    """
    api_url = f'{COLLIBRA_BASE_URL}/users?name={username}'
    try:
        response = requests.get(api_url, auth=(USERNAME, PASSWORD))
        if response.status_code == 200:
            data = response.json()
            if data and 'results' in data and len(data['results']) > 0:
                return data['results'][0]['id']
            return {"error": f"User '{username}' not found"}
        else:
            return {
                "error": f"Failed to retrieve user ID. Status code: {response.status_code}",
                "status_code": response.status_code,
                "response": response.text
            }
    except Exception as e:
        return {"error": f"Error retrieving user ID: {str(e)}"}

def get_role_id(role_name):
    api_url = f'{COLLIBRA_BASE_URL}/roles?name={role_name}'
    try:
        response = requests.get(api_url, auth=(USERNAME, PASSWORD))
        if response.status_code == 200:
            data = response.json()
            if data and 'results' in data and len(data['results']) > 0:
                return data['results'][0]['id']
            return {"error": f"Role '{role_name}' not found"}
        else:
            return {
                "error": f"Failed to retrieve role ID. Status code: {response.status_code}",
                "status_code": response.status_code,
                "response": response.text
            }
    except Exception as e:
        return {"error": f"Error retrieving role ID: {str(e)}"}

def assign_steward(resource_id, owner_id, role_id, resource_type):
    """
    Assigns a Data Steward to a resource (asset, domain, or community).
    
    Args:
        resource_id: The ID of the resource. An Asset, Community or Domain.
        owner_id: The ID of the user the responsibility is created for.
        role_id: The ID of the role to assign.
        resource_type: The type of resource (allowed values: Asset, Domain, Community). 
    
    Returns:
        Success message or error.
    """
    # use the responsibilities endpoint
    api_url = f'{COLLIBRA_BASE_URL}/responsibilities'
    
    # Collibra expects TitleCase resource types
    
    payload = {
        "ownerId": owner_id,
        "roleId": role_id,
        "resourceId": resource_id,
        "resourceType": resource_type.title()
    }
    
    try:
        response = requests.post(api_url, json=payload, auth=(USERNAME, PASSWORD))
        if response.status_code == 200 or response.status_code == 201:
            return {"success": f"Successfully assigned steward to {resource_type} {resource_id}"}
        else:
            return {
                "error": f"Failed to assign steward. Status code: {response.status_code}",
                "status_code": response.status_code,
                "payload_sent": payload,
                "response": response.text
            }
    except Exception as e:
        return {"error": f"Error assigning steward: {str(e)}"}

def get_asset_types(asset_type_public_id):
    api_url = f'{COLLIBRA_BASE_URL}/assetTypes/publicId/{asset_type_public_id}'
    try:
        response = requests.get(api_url, auth=(USERNAME, PASSWORD))
        if response.status_code == 200:
            return response.json()
        else:
            return {
                "error": f"Failed to retrieve asset types. Status code: {response.status_code}",
                "status_code": response.status_code,
                "response": response.text
            }
    except Exception as e:
        return {"error": f"Error retrieving asset types: {str(e)}"}

def get_relations(sourceAssetId, targetAssetId):
    api_url = f'{COLLIBRA_BASE_URL}/relations?sourceAssetId={sourceAssetId}&targetAssetId={targetAssetId}'
    try:
        response = requests.get(api_url, auth=(USERNAME, PASSWORD))
        if response.status_code == 200:
            return response.json()
        else:
            return {
                "error": f"Failed to retrieve relation types. Status code: {response.status_code}",
                "status_code": response.status_code,
                "response": response.text
            }
    except Exception as e:
        return {"error": f"Error retrieving relations: {str(e)}"}

def get_relation_types(relationTypeId):
    api_url = f'{COLLIBRA_BASE_URL}/relationTypes/publicId/{relationTypeId}'
    
    try:
        response = requests.get(api_url, auth=(USERNAME, PASSWORD))
        if response.status_code == 200:
            return response.json()
        else:
            return {
                "error": f"Failed to retrieve relationship types. Status code: {response.status_code}",
                "status_code": response.status_code,
                "response": response.text
            }
    except Exception as e:
        return {"error": f"Error retrieving relationship types: {str(e)}"}