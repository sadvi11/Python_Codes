# Imagine you got these values from an AWS CloudWatch API response
# and need to build a human-readable alert

metric_name  = "CPUUtilization"
metric_value = 91.3
alarm_state  = "ALARM"
instance_id  = "i-0a1b2c3d4e5f"
region = "ca-central-1"

alert_message = (
    f"[{alarm_state}] {metric_name} is {metric_value:.1f}% "
    f"on instance {instance_id} in {region}. "
    f"Threshold exceeded — investigate immediately."
)

print(alert_message)

# Example 1 — Basic
name = "Sadhvi"
print(f"My name is {name}")

# Example 2 — Numbers
cost = 4.50
print(f"Your AWS bill is ${cost}")

# Example 3 — Two variables together
region = "ca-central-1"
service = "Lambda"
print(f"Service {service} is running in {region}")

# Example 4 — Math inside f-string
budget = 10.0
spent = 4.50
remaining = budget - spent
print(f"You spent ${spent} and have ${remaining} left")

# Example 5 — Clean decimal formatting
cpu = 91.333333
print(f"CPU usage is {cpu:.1f}%")
print(f"CPU usage is {cpu:.2f}%")

# Example 6 — Real Project 2 alert message
cost = 8.75
threshold = 5.0
region = "ca-central-1"
print(f"ALERT! Your AWS cost is ${cost} USD")
print(f"Your limit was ${threshold} USD")
print(f"Region: {region}")
print(f"Action needed — check your console now!")

# ============================================
# PROJECT 2 — AWS Cost Monitor
# Concept: F-strings in real CloudWatch alerts
# ============================================

# STEP 1 — Define variables
# These values normally come from AWS CloudWatch API
# We are hardcoding them here just to practice
metric_name  = "CPUUtilization"   # what AWS is measuring
metric_value =  45.3           # current value — 91.3% CPU
alarm_state  = "ok"            # AWS alarm status
instance_id  = "i-0a1b2c3d4e5f"  # which server is affected
region       = "us-east-1"     # which AWS region

# STEP 2 — Build the alert message using F-strings
# WHY F-STRINGS?
# Because we need to mix fixed text with changing variables
# Every time CPU value changes, the message updates automatically
# Without f-strings we would have to manually join strings — messy and error prone

alert_message = (
    f"[{alarm_state}] {metric_name} is {metric_value:.1f}% "
    # {alarm_state} → fills in "ALARM"
    # {metric_name} → fills in "CPUUtilization"
    # {metric_value:.1f} → fills in "91.3" (1 decimal place only)

    f"on instance {instance_id} in {region}. "
    # {instance_id} → fills in which server "i-0a1b2c3d4e5f"
    # {region} → fills in "ca-central-1"

    f"Threshold exceeded — investigate immediately."
    # fixed text — no variable needed here
)

# STEP 3 — Print the alert
# In real Project 2 this message gets sent via SNS email
# Here we just print it to test
print(alert_message)

# ============================================
# WHY I USED F-STRINGS HERE:
# 1. Clean — easy to read and understand
# 2. Dynamic — variables update the message automatically
# 3. Professional — this is how real AWS engineers write alerts
# 4. Formatting — {metric_value:.1f} shows 91.3 not 91.300000
# ============================================