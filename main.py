from tools import run_agent

if __name__ == "__main__":
    query = input("What can I help you? ")
    result = run_agent(query)
    print(result)