# GET — bring in the information
cost = 8.50        # how much AWS charged
threshold = 5.0    # my limit
print(f"My AWS cost is ${cost}")
print(f"My limit is ${threshold}")
# PROCESS — make a decision
cost = 8.50
threshold = 5.0

if cost > threshold:
    print("Cost is TOO HIGH!")
else:
    print("Cost is fine!")
    # OUTPUT — do something with the result
cost = 8.50
threshold = 5.0

if cost > threshold:
    # In real project this sends an email
    print(f"ALERT SENT! Cost ${cost} exceeded limit ${threshold}")
else:
    print(f"All good! Cost ${cost} is below limit ${threshold}")
    
    # ================================
# HOW TO THINK ABOUT ANY PROGRAM
# Step 1 — GET
# Step 2 — PROCESS  
# Step 3 — OUTPUT
# ================================

# STEP 1 — GET the data
cost = 8.50
threshold = 5.0
region = "ca-central-1"

print("Checking AWS costs...")
print(f"Current cost: ${cost}")
print(f"My limit: ${threshold}")

# STEP 2 — PROCESS the data
# Ask: is cost too high?
is_too_high = cost > threshold

# STEP 3 — OUTPUT the result
if is_too_high:
    print(f"ALERT! ${cost} exceeded your limit of ${threshold}!")
    print(f"Region: {region}")
    print("Action: Check your AWS console now!")
else:
    print(f"All good! ${cost} is below your limit of ${threshold}")


#Run it. Then change `cost = 3.0` and run again.

#---

## The 3 questions to ask before writing ANY code:

#1. What data do I need?      → GET
#2. What decision do I make?  → PROCESS
#3. What do I do after?       → OUTPUT