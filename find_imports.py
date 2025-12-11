import sys
import importlib.util

# Try different possible locations
locations = [
    "langchain.agents",
    "langchain_core.agents",
    "langchain_classic.agents",
    "langchain.agents.tool_calling_agent",
]

for loc in locations:
    try:
        module = __import__(loc, fromlist=['create_tool_calling_agent'])
        if hasattr(module, 'create_tool_calling_agent'):
            print(f"✓ FOUND in: {loc}")
            print(f"  Function: {module.create_tool_calling_agent}")
        else:
            print(f"✗ Module exists but no create_tool_calling_agent: {loc}")
            print(f"  Available: {[x for x in dir(module) if not x.startswith('_')][:10]}")
    except Exception as e:
        print(f"✗ Cannot import {loc}: {e}")

# Also check AgentExecutor
print("\n--- Checking AgentExecutor ---")
for loc in locations:
    try:
        module = __import__(loc, fromlist=['AgentExecutor'])
        if hasattr(module, 'AgentExecutor'):
            print(f"✓ AgentExecutor FOUND in: {loc}")
    except:
        pass
