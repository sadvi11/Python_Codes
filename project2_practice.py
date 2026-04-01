COST_THRESHOLD = 5.0
SNS_TOPIC_ARN = "arn:aws:sns:ca-central-1:..."
# These are your AWS project settings
COST_THRESHOLD = 5.0
MY_NAME = "Sadhvi"
MY_REGION = "ca-central-1"
IS_ALERT_ACTIVE = True

print("Cost limit is:", COST_THRESHOLD)
print("My name is:", MY_NAME)
print("My AWS region is:", MY_REGION)
print("Alert active?", IS_ALERT_ACTIVE)

def get_aws_cost():
def send_alert(cost):
def lambda_handler(event, context):
    # Machine 1 — checks cost
def get_aws_cost():
    cost = 4.50
    return cost

# Machine 2 — sends alert
def send_alert(cost):
    print(f"ALERT! Your AWS bill is ${cost}")

# Machine 3 — boss function runs everything
def lambda_handler():
    print("Checking AWS costs...")
    
    cost = get_aws_cost()
    print(f"Total cost: ${cost}")
    
    if cost > 5.0:
        send_alert(cost)
    else:
        print("Cost is fine! No alert needed.")

# Start here
lambda_handler()