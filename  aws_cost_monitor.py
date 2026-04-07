import boto3
import json
import datetime

def get_aws_costs():
    try:
        # connect to AWS Cost Explorer
        client = boto3.client("ce", region_name="us-east-1")
        
        # set date range — last 30 days
        end_date   = datetime.date.today()
        start_date = end_date - datetime.timedelta(days=30)
        
        # call AWS Cost Explorer API
        response = client.get_cost_and_usage(
            TimePeriod={
                "Start": str(start_date),
                "End":   str(end_date)
            },
            Granularity="MONTHLY",
            Metrics=["UnblendedCost"],
            GroupBy=[
                {
                    "Type": "DIMENSION",
                    "Key":  "SERVICE"
                }
            ]
        )
        return response

    except Exception as e:
        print(f"Error connecting to AWS: {e}")
        return None


def process_costs(response):
    if response is None:
        print("No data received")
        return None

    report = {
        "generated_on": str(datetime.date.today()),
        "services": [],
        "total": 0.0
    }

    # loop through each service
    results = response["ResultsByTime"][0]["Groups"]
    for item in results:
        service_name = item["Keys"][0]
        cost = float(item["Metrics"]["UnblendedCost"]["Amount"])

        # only include services that actually cost something
        if cost > 0:
            report["services"].append({
                "service": service_name,
                "cost":    round(cost, 2)
            })
            report["total"] += cost

    report["total"] = round(report["total"], 2)
    return report


def save_report(report):
    if report is None:
        return

    try:
        with open("cost_report.json", "w") as f:
            json.dump(report, f, indent=4)
        print("Report saved to cost_report.json")
    except Exception as e:
        print(f"Error saving report: {e}")