import logging
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from collibra_mcp import tools

# Configure logging
logging.basicConfig(
    level=logging.WARNING,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

mcp = FastMCP("collibra-mcp")


@mcp.tool()
def get_collibra_assets(
    domain_id: Annotated[str, "The domain ID to filter Collibra assets by"]
) -> str:
    """
    Retrieves assets from Collibra for a given domain.
    
    Args:
        domain_id: The domain ID to filter assets by.
    
    Returns:
        A list of Collibra assets or an error message.
    """
    logger.info(f"Retrieving Collibra assets for domain {domain_id}")
    result = tools.get_collibra_assets(domain_id)
    logger.info(f"Successfully retrieved Collibra assets")
    return str(result)

@mcp.tool()
def get_collibra_domains(
    domain_name: Annotated[str, "The domain name to search for in Collibra"]
) -> str:
    """
    Retrieves domains from Collibra by name.
    
    Args:
        domain_name: The domain name to search for.
    
    Returns:
        A list of Collibra domains or an error message.
    """
    logger.info(f"Retrieving Collibra domains for name {domain_name}")
    result = tools.get_collibra_domains(domain_name)
    logger.info(f"Successfully retrieved Collibra domains")
    return str(result)

@mcp.tool()
def add_collibra_domain(
    domain_name: Annotated[str, "The name of the domain to add"],
    community_id: Annotated[str, "The community ID to add the domain to"],
    type_id: Annotated[str, "The type ID of the domain to add"]
) -> str:
    """
    Adds a new domain to Collibra.
    """
    logger.info(f"Adding Collibra domain {domain_name} to community {community_id} with type {type_id}")
    result = tools.add_collibra_domain(domain_name, community_id, type_id)
    logger.info(f"Successfully added Collibra domain")
    return str(result)

@mcp.tool()
def add_collibra_asset(
    asset_name: Annotated[str, "The name of the asset to add"],
    asset_type: Annotated[str, "The type of the asset to add"],
    domain_id: Annotated[str, "The domain ID to add the asset to"],
    owner_id: Annotated[str, "Optional: The owner ID to assign to the asset"] = None
) -> str:
    """
    Adds a new asset to Collibra.
    """
    logger.info(f"Adding Collibra asset {asset_name} to domain {domain_id} with type {asset_type}")
    result = tools.add_collibra_asset(asset_name, asset_type, domain_id, owner_id)
    logger.info(f"Successfully added Collibra asset")
    return str(result)

@mcp.tool()
def get_community_id(
    community_name: Annotated[str, "The name of the community to search for"]
) -> str:
    """
    Retrieves the community ID from Collibra by name.
    """
    logger.info(f"Retrieving community ID for {community_name}")
    result = tools.get_community_id(community_name)
    logger.info(f"Successfully retrieved community ID")
    return str(result)

@mcp.tool()
def add_collibra_community(
    community_name: Annotated[str, "The name of the community to create"]
) -> str:
    """
    Creates a new community in Collibra.
    """
    logger.info(f"Creating Collibra community {community_name}")
    result = tools.add_collibra_community(community_name)
    logger.info(f"Successfully created Collibra community")
    return str(result)

@mcp.tool()
def get_domain_type_id(
    domain_name: Annotated[str, "The name of the domain type to search for"]
) -> str:
    """
    Retrieves the domain type ID from Collibra by name.
    """
    logger.info(f"Retrieving domain type ID for {domain_name}")
    result = tools.get_domain_type_id(domain_name)
    logger.info(f"Successfully retrieved domain type ID")
    return str(result)

@mcp.tool()
def get_asset_type_id(
    asset_type_name: Annotated[str, "The name of the asset type to search for"]
) -> str:
    """
    Retrieves the asset type ID from Collibra by name.
    """
    logger.info(f"Retrieving asset type ID for {asset_type_name}")
    result = tools.get_asset_type_id(asset_type_name)
    logger.info(f"Successfully retrieved asset type ID")
    return str(result)

@mcp.tool()
def get_user_id(
    username: Annotated[str, "The username to search for"]
) -> str:
    """
    Retrieves the user ID from Collibra by username.
    """
    logger.info(f"Retrieving user ID for {username}")
    result = tools.get_user_id(username)
    logger.info(f"Successfully retrieved user ID")
    return str(result)

@mcp.tool()
def assign_steward(
    asset_id: Annotated[str, "The ID of the asset to assign a steward to"],
    steward_user_id: Annotated[str, "The ID of the user to assign as steward"],
    role_id: Annotated[str, "The ID of the role to assign as steward"],
    resource_type: Annotated[str, "The type of the resource to assign a steward to"]
) -> str:
    """
    Assigns a Data Steward to an asset.
    """
    logger.info(f"Assigning steward {steward_user_id} to asset {asset_id}")
    result = tools.assign_steward(asset_id, steward_user_id, role_id, resource_type)
    logger.info(f"Successfully assigned steward")
    return str(result)

@mcp.tool()
def get_role_id(
    role_name: Annotated[str, "The name of the role to search for"]
) -> str:
    """
    Retrieves the role ID from Collibra by name.
    """
    logger.info(f"Retrieving role ID for {role_name}")
    result = tools.get_role_id(role_name)
    logger.info(f"Successfully retrieved role ID")
    return str(result)

@mcp.tool()
def get_asset_types():
    """
    Retrieves all asset types from Collibra.
    """
    logger.info(f"Retrieving all asset types")
    result = tools.get_asset_types()
    logger.info(f"Successfully retrieved all asset types")
    return str(result)


@mcp.tool()
def get_relations(sourceAssetId, targetAssetId):
    """
    Retrieves all relations from Collibra.
    """
    logger.info(f"Retrieving all relations")
    result = tools.get_relations(sourceAssetId, targetAssetId)
    logger.info(f"Successfully retrieved all relations")
    return str(result)

@mcp.tool()
def get_relation_types():
    """
    Retrieves all relation types from Collibra.
    """
    logger.info(f"Retrieving all relation types")
    result = tools.get_relation_types()
    logger.info(f"Successfully retrieved all relation types")
    return str(result)

@mcp.tool()
def get_relation_type_id(relation_type_name):
    """
    Retrieves the relation type ID from Collibra by name.
    """
    logger.info(f"Retrieving relation type ID for {relation_type_name}")
    result = tools.get_relation_type_id(relation_type_name)
    logger.info(f"Successfully retrieved relation type ID")
    return str(result)
    
def run_server():
    """Run the MCP server."""
    logger.info("Starting Collibra MCP server...")
    try:
        # Use stdio transport for better integration with Cascade
        mcp.run(transport="stdio")
    except Exception as e:
        logger.error(f"Error running server: {e}")
    finally:
        logger.info("Server shutdown complete")

if __name__ == "__main__":
    run_server()