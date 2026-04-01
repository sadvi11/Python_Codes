import json

# Test 1 — trigger a FileNotFoundError on purpose
try:
    with open("doesnt_exist.json", "r") as f:
        data = json.load(f)
except FileNotFoundError:
    print("Caught it! File was missing")

# Test 2 — trigger a KeyError on purpose  
costs = {"EC2": 42.80, "S3": 5.20}
try:
    print(costs["RDS"])
except KeyError:
    print("Caught it! That key doesn't exist")

# Test 3 — trigger a ZeroDivisionError on purpose
try:
    result = 100 / 0
except ZeroDivisionError:
    print("Caught it! Can't divide by zero")

print("Script finished — no crash!")