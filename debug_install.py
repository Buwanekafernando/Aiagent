import sys
import langchain
import langchain.agents

print(f"Python executable: {sys.executable}")
print(f"LangChain version: {langchain.__version__}")
print(f"LangChain file: {langchain.__file__}")
print(f"LangChain agents file: {langchain.agents.__file__}")
try:
    from langchain.agents import create_tool_calling_agent
    print("SUCCESS: create_tool_calling_agent imported")
except ImportError as e:
    print(f"FAILURE: {e}")

print("Dir of langchain.agents:")
print(dir(langchain.agents))
