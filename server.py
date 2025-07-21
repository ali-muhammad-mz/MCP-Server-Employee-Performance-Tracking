from mcp.server.fastmcp import FastMCP
import logging

# Create an MCP server with name ResourceManager
mcp = FastMCP("ResourceManager")

# Mock database
mock_db = {
    "E-0001": {"current": "forget_password", "completed": "3"},
    "E-0002": {"current": "add_review", "completed": "2"},
    "E-0003": {"current": "payment_by_card", "completed": "4"},
    "E-0004": {"current": "cancel_order", "completed": "1"},
}

@mcp.tool()
def get_current_feature(employee_id: str) -> str:
    """Fetch the current feature being worked on by the given employee ID"""
    employee_data = mock_db.get(employee_id)
    if employee_data:
        return employee_data.get("current", "No current feature found.")
    return "No such employee ID"

@mcp.tool()
def get_completed_features(employee_id: str) -> str:
    """Fetch the number of completed features for the given employee ID"""
    employee_data = mock_db.get(employee_id)
    if employee_data:
        return employee_data.get("completed", "No completed feature found.")
    return "No such employee ID"

@mcp.tool()
def change_current_feature(employee_id: str, new_feature: str) -> str:
    """
    Change the current feature of an employee and mark the previous one as completed.
    """
    employee_data = mock_db.get(employee_id)

    if not employee_data:
        return "Employee ID not found."

    employee_data["completed"] = str(int(employee_data["completed"]) + 1)

    # Update current feature
    employee_data["current"] = new_feature

    return (
        f"Updated {employee_id}: Current feature set to '{new_feature}'. "
        f"Total '{employee_data["completed"]}' features are completed."
    )

