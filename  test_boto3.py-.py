import boto3

# test 1 — check boto3 is installed
print("boto3 version:", boto3.__version__)

# test 2 — check your AWS credentials work
try:
    sts = boto3.client("sts", region_name="ca-central-1")
    identity = sts.get_caller_identity()
    print("Connected to AWS!")
    print(f"Account ID: {identity['Account']}")
    print(f"User: {identity['Arn']}")

except Exception as e:
    print(f"Connection failed: {e}")