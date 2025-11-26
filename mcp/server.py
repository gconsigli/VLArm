# This script is used to initialize MCP commands for the robot, so Ollama models with tools can control it locally.
# This MCP is built on top fo the Phosphobot API for controlling the SO-101.

from typing import str
import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("vlarm")

API_BASE_URL = "http://localhost/" # For a locally-hosted instance of the Phosphobot API.
ROBOT_ID = 0 # Configured to the actual robot.
TIMEOUT = 20.0 # Number of seconds to wait for a response from the Phosphobot API.


# Headers used for each API request.
headers = {
    "User-Agent": "vlarm/1.0",
    "Accept": "application/json",
}

# MCP command to move the robot to its initial position.
# Function: Essential to call this before any other movement commands.
async def initialize_bot() -> str:
    async with httpx.AsyncClient(base_url=API_BASE_URL, headers=headers) as client:
        try:
            response = await client.get(f"/move/init?robot_id={ROBOT_ID}", headers=headers, timeout=20.0)
            response.raise_for_status()
            return "Success: Robot initialized to its initial position."
        except Exception:
            return "Error: Unable to initialize the robot to its initial position."

# MCP command to move the robot to its absolute position, ran after initialization.
async def move_to_absolute() -> str:
    params = {
        "x": 0,
        "y": 0,
        "z": 0,
        "rx": 0,
        "ry": 0,
        "rz": 0,
        "open": 0,
        "max_trials": 10,
        "position_tolerance": 0.03,
        "orientation_tolerance": 0.2
    }
    async with httpx.AsyncClient(base_url=API_BASE_URL, headers=headers) as client:
        try:
            response = await client.get(f"/move/absolute?robot_id={ROBOT_ID}", headers=headers, params=params, timeout=TIMEOUT)
            response.raise_for_status()
            return "Success: Robot moved to absolute position."
        except Exception:
            return "Error: Unable to move the robot to absolute position."
    

# MCP command that makes the SO-101 open and close its gripper.
# Function: Test command to verify robot responsiveness.
async def say_hello() -> str:
    async with httpx.AsyncClient(base_url=API_BASE_URL, headers=headers) as client:
        try:
            response = await client.get(f"/move/hello?robot_id={ROBOT_ID}", headers=headers, timeout=TIMEOUT)
            response.raise_for_status()
            return "Success: Robot said hello."
        except Exception:
            return "Error: Unable to say hello."

# MCP command to control the SO-101's arm.
# Function: Allows for more custom movement of the robot (outside of base commands defined below).
# Note: The base controls below are for basic movements, like opening/closing the gripper and making the robotic arm go up/down/left/right to a certain extent.
async def fine_tuned_control(x: int, y: int, z: int, rx: int, ry: int, rz: int, open: int, source: str, timestamp: int, direction_x: int, direction_y: int) -> str:
    params = {
        "x": x,
        "y": y,
        "z": z,
        "rx": rx,
        "ry": ry,
        "rz": rz,
        "open": open,
        "source": source,
        "timestamp": timestamp,
        "direction_x": direction_x,
        "direction_y": direction_y
    }
    async with httpx.AsyncClient(base_url=API_BASE_URL, headers=headers) as client:
        try:
            response = await client.get(f"/move/teleop?robot_id={ROBOT_ID}", headers=headers, params=params, timeout=TIMEOUT)
            response.raise_for_status()
            return "Success: Moved arm as specified."
        except Exception:
            return "Error: Unable to move arm."
        
# MCP command to open the gripper.
async def open_gripper() -> str:
    params = {
        "open": 1
    }
    async with httpx.AsyncClient(base_url=API_BASE_URL, headers=headers) as client:
        try:
            response = await client.get(f"/move/teleop?robot_id={ROBOT_ID}", headers=headers, params=params, timeout=TIMEOUT)
            response.raise_for_status()
            return "Success: Gripper opened."
        except Exception:
            return "Error: Unable to open gripper."
        
# MCP command to open the gripper.
async def close_gripper() -> str:
    params = {
        "open": 0
    }
    async with httpx.AsyncClient(base_url=API_BASE_URL, headers=headers) as client:
        try:
            response = await client.get(f"/move/teleop?robot_id={ROBOT_ID}", headers=headers, params=params, timeout=TIMEOUT)
            response.raise_for_status()
            return "Success: Gripper closed."
        except Exception:
            return "Error: Unable to close gripper."

# MCP command to move the arm up by 20 units.
async def move_arm_up() -> str:
    params = {
        "z": 20
    }
    async with httpx.AsyncClient(base_url=API_BASE_URL, headers=headers) as client:
        try:
            response = await client.get(f"/move/teleop?robot_id={ROBOT_ID}", headers=headers, params=params, timeout=TIMEOUT)
            response.raise_for_status()
            return "Success: Arm moved up."
        except Exception:
            return "Error: Unable to move arm up."

# MCP command to move the arm down by 20 units.
async def move_arm_down() -> str:
    params = {
        "z": -20
    }
    async with httpx.AsyncClient(base_url=API_BASE_URL, headers=headers) as client:
        try:
            response = await client.get(f"/move/teleop?robot_id={ROBOT_ID}", headers=headers, params=params, timeout=TIMEOUT)
            response.raise_for_status()
            return "Success: Arm moved down."
        except Exception:
            return "Error: Unable to move arm down."

# MCP command to move the arm left by 20 units.
async def move_arm_left() -> str:
    params = {
        "y": -20
    }
    async with httpx.AsyncClient(base_url=API_BASE_URL, headers=headers) as client:
        try:
            response = await client.get(f"/move/teleop?robot_id={ROBOT_ID}", headers=headers, params=params, timeout=TIMEOUT)
            response.raise_for_status()
            return "Success: Arm moved left."
        except Exception:
            return "Error: Unable to move arm left."

# MCP command to move the arm right by 20 units.
async def move_arm_right() -> str:
    params = {
        "y": 20
    }
    async with httpx.AsyncClient(base_url=API_BASE_URL, headers=headers) as client:
        try:
            response = await client.get(f"/move/teleop?robot_id={ROBOT_ID}", headers=headers, params=params, timeout=TIMEOUT)
            response.raise_for_status()
            return "Success: Arm moved right."
        except Exception:
            return "Error: Unable to move arm right."
        
async def gravity_compensation_on() -> str:
    async with httpx.AsyncClient(base_url=API_BASE_URL, headers=headers) as client:
        try:
            response = await client.get(f"/gravity/start?robot_id={ROBOT_ID}", headers=headers, timeout=TIMEOUT)
            response.raise_for_status()
            return "Success: Gravity compensation enabled."
        except Exception:
            return "Error: Unable to enable gravity compensation."

async def gravity_compensation_off() -> str:
    async with httpx.AsyncClient(base_url=API_BASE_URL, headers=headers) as client:
        try:
            response = await client.get(f"/gravity/stop?robot_id={ROBOT_ID}", headers=headers, timeout=TIMEOUT)
            response.raise_for_status()
            return "Success: Gravity compensation disabled."
        except Exception:
            return "Error: Unable to disable gravity compensation."

# Save MCP commands.

mcp.command("initialize_bot", initialize_bot, "**NECESSARY STARTING COMMAND** Initialize the robot to its initial position. Necessary before starting any series of actions and before running move_to_absolute.")
mcp.command("move_to_absolute", move_to_absolute, "**NECESSARY STARTING COMMAND** Move the robot to its absolute position. Should be called after initialize_bot.")
mcp.command("say_hello", say_hello, "Make the robot move its gripper to say hello. Useful as a testing command.")
mcp.command("fine_tuned_control", fine_tuned_control, "Move the robot's arm with fine-tuned control using specified parameters.")
mcp.command("open_gripper", open_gripper, "Open the robot's gripper.")
mcp.command("close_gripper", close_gripper, "Close the robot's gripper.")
mcp.command("move_arm_up", move_arm_up, "Move the robot's arm up by 20 units.")
mcp.command("move_arm_down", move_arm_down, "Move the robot's arm down by 20 units.")
mcp.command("move_arm_left", move_arm_left, "Move the robot's arm left by 20 units.")
mcp.command("move_arm_right", move_arm_right, "Move the robot's arm right by 20 units.")
mcp.command("gravity_compensation_on", gravity_compensation_on, "Enable gravity compensation for the robot's arm.")
mcp.command("gravity_compensation_off", gravity_compensation_off, "Disable gravity compensation for the robot's arm.")

def main():
    mcp.run(transport='stdio')

if __name__ == "__main__":
    main()