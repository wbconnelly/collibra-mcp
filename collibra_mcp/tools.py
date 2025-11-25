"""MCP server tools implementation."""

from collibra_mcp.config import COLLIBRA_BASE_URL
from collibra_mcp.helper_functions import (
    mcp_get_request,
    mcp_post_request,
    mcp_patch_request
    )

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

def get_community_id(community_name):
    """
    Retrieves the community ID from Collibra by name.
    
    Args:
        community_name: The name of the community to search for.
    """
    api_url = f'{COLLIBRA_BASE_URL}/communities?name={community_name}'
    response_json = mcp_get_request(api_url)

    if isinstance(response_json, dict) and response_json.get("error"):
        return response_json

    try:
        return response_json['id']
    except (TypeError, KeyError):
        return {"error": f"Community '{community_name}' not found"}

def get_collibra_domains(domain_name):
    """
    Retrieves domains from Collibra by name.
    
    Args:
        domain_name: The domain name to search for.
    
    Returns:
        A list of Collibra domains or an error message.
    """
    api_url = f'{COLLIBRA_BASE_URL}/domains?name={domain_name}'
    
    response_json = mcp_get_request(api_url)

    if isinstance(response_json, dict) and response_json.get("error"):
        return response_json

    if isinstance(response_json, dict) and response_json.get('results'):
        return response_json['results'][0]['id']
    return {"error": f"Domain '{domain_name}' not found"}

def add_collibra_domain(domain_name, community_id, type_id):
    api_url = COLLIBRA_BASE_URL + "/domains"

    payload = {
        "name": domain_name,
        "communityId": community_id,
        "typeId": type_id
    }

    return mcp_post_request(api_url, payload)

def get_asset_attributes(assetId, typeIds):
    api_url = f'{COLLIBRA_BASE_URL}/attributes?assetId={assetId}&typeIds={typeIds}&page=0&size=100'
    return mcp_get_request(api_url)

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

    return mcp_post_request(api_url, payload)

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
    
    return mcp_post_request(api_url, payload)

def get_domain_type_id(domain_type_name):
    """
    Retrieves the domain type ID from Collibra by name.
    
    Args:
        domain_name: The name of the domain type to search for.
    """
    api_url = f'{COLLIBRA_BASE_URL}/domainTypes?name={domain_type_name}'
    response_json = mcp_get_request(api_url)

    if isinstance(response_json, dict) and response_json.get("error"):
        return response_json

    if isinstance(response_json, dict) and response_json.get('results'):
        return response_json['results'][0]['id']
    return {"error": f"Domain type '{domain_type_name}' not found"}

def get_asset_type_id(asset_type_name):
    """
    Retrieves the asset type ID from Collibra by name.
    
    Args:
        asset_type_name: The name of the asset type to search for.
    """
    api_url = f'{COLLIBRA_BASE_URL}/assetTypes?name={asset_type_name}&nameMatchMode=EXACT'
    response_json = mcp_get_request(api_url)

    if isinstance(response_json, dict) and response_json.get("error"):
        return response_json

    if isinstance(response_json, dict) and response_json.get('results'):
        return response_json['results'][0]['id']
    return {"error": f"Asset type '{asset_type_name}' not found"}

def get_user_id(username):
    """
    Retrieves the user ID from Collibra by username.
    
    Args:
        username: The username to search for.
    
    Returns:
        The user ID or an error message.
    """
    api_url = f'{COLLIBRA_BASE_URL}/users?name={username}'
    response_json = mcp_get_request(api_url)

    if isinstance(response_json, dict) and response_json.get("error"):
        return response_json

    if isinstance(response_json, dict) and response_json.get('results'):
        return response_json['results'][0]['id']
    return {"error": f"User '{username}' not found"}

def get_role_id(role_name):
    api_url = f'{COLLIBRA_BASE_URL}/roles?name={role_name}'
    response_json = mcp_get_request(api_url)

    if isinstance(response_json, dict) and response_json.get("error"):
        return response_json

    if isinstance(response_json, dict) and response_json.get('results'):
        return response_json['results'][0]['id']
    return {"error": f"Role '{role_name}' not found"}

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
    
    response_json = mcp_post_request(api_url, payload)

    if isinstance(response_json, dict) and response_json.get("error"):
        # ensure payload is present for diagnostics
        response_json.setdefault("payload_sent", payload)
        return response_json

    return {"success": f"Successfully assigned steward to {resource_type} {resource_id}"}

def get_asset_types(asset_type_public_id):
    api_url = f'{COLLIBRA_BASE_URL}/assetTypes/publicId/{asset_type_public_id}'
    return mcp_get_request(api_url)

def get_relations(sourceAssetId, targetAssetId):
    api_url = f'{COLLIBRA_BASE_URL}/relations?sourceAssetId={sourceAssetId}&targetAssetId={targetAssetId}'
    return mcp_get_request(api_url)

def get_relation_types(relationTypeId):
    api_url = f'{COLLIBRA_BASE_URL}/relationTypes/publicId/{relationTypeId}'
    
    return mcp_get_request(api_url)
    
def add_attribute(assetId, attributeTypeId, value):
    api_url = f'{COLLIBRA_BASE_URL}/attributes'
    payload = {
        "assetId": assetId,
        "attributeTypeId": attributeTypeId,
        "value": value
    }
    return mcp_post_request(api_url, payload)

def get_attribute_id(attribute_name):
    api_url = f'{COLLIBRA_BASE_URL}/attributes?name={attribute_name}'
    return mcp_get_request(api_url)

def get_attributes(assetId, typeId):
    api_url = f'{COLLIBRA_BASE_URL}/attributes?assetId={assetId}&typeIds={typeId}&page=0&size=100'
    return mcp_get_request(api_url)

def change_attribute(attributeId, value):
    api_url = f'{COLLIBRA_BASE_URL}/attributes/{attributeId}'
    payload = {
    "id": attributeId,
    "value": value
    }
    return mcp_patch_request(api_url, payload)