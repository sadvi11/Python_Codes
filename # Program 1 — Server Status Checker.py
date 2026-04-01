# Program 1 — Server Status Checker
# Cloud engineers use this to monitor if servers are alive
# Real world: runs every minute on AWS Lambda

import urllib.request

def check_server(url):
    """
    Check if a server is up or down
    GET  → ping the server
    PROCESS → did it respond?
    OUTPUT → up or down message
    """
    try:
        # Try to connect to the server
        urllib.request.urlopen(url, timeout=5)
        return "UP"
    except:
        return "DOWN"

# List of servers to check
# In real AWS projects this list comes from a config file
servers = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.amazon.com"
]

# Check each server one by one
print("Checking servers...")
print("-" * 40)

for server in servers:
    status = check_server(server)
    print(f"Server: {server}")
    print(f"Status: {status}")
    print("-" * 40)