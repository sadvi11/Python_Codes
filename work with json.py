import json
import datetime

# Simulated AWS cost data (later: replace with boto3)
aws_costs = {
    "date": str(datetime.date.today()),
    "services": [
        {"name": "EC2", "cost": 42.80},
        {"name": "S3", "cost": 8.20}
    ]
}

# Save to JSON file
with open("cost_report.json", "w") as f:
    json.dump(aws_costs, f, indent=4)
    print("Report saved!")

# Read it back and show total
with open("cost_report.json", "r") as f:
    report = json.load(f)

total = sum(s["cost"] for s in report["services"])
print(f"Total for {report['date']}: ${total:.2f}")
