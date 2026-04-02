import boto3
import os
import json
from botocore.exceptions import ClientError

# connect to S3
s3 = boto3.client("s3", region_name="ca-central-1")
BUCKET = "sadhvi-cloud-projects"


# ── 1. CREATE BUCKET ──────────────────────────────
def create_bucket():
    try:
        s3.create_bucket(
            Bucket=BUCKET,
            CreateBucketConfiguration={
                "LocationConstraint": "ca-central-1"
            }
        )
        print(f"Bucket '{BUCKET}' created!")
    except ClientError as e:
        print(f"Bucket error: {e}")


# ── 2. UPLOAD FILE ────────────────────────────────
def upload_file(local_file, s3_key):
    try:
        s3.upload_file(local_file, BUCKET, s3_key)
        print(f"Uploaded '{local_file}' to S3 as '{s3_key}'")
    except ClientError as e:
        print(f"Upload failed: {e}")
    except FileNotFoundError:
        print(f"Local file '{local_file}' not found")


# ── 3. LIST FILES ─────────────────────────────────
def list_files():
    try:
        response = s3.list_objects_v2(Bucket=BUCKET)
        files = response.get("Contents", [])
        if not files:
            print("Bucket is empty")
            return
        print(f"\nFiles in '{BUCKET}':")
        for f in files:
            size_kb = round(f["Size"] / 1024, 2)
            print(f"  {f['Key']:<40} {size_kb} KB")
    except ClientError as e:
        print(f"Could not list files: {e}")


# ── 4. DOWNLOAD FILE ──────────────────────────────
def download_file(s3_key, local_file):
    try:
        s3.download_file(BUCKET, s3_key, local_file)
        print(f"Downloaded '{s3_key}' → '{local_file}'")
    except ClientError as e:
        print(f"Download failed: {e}")


# ── 5. DELETE FILE ────────────────────────────────
def delete_file(s3_key):
    try:
        s3.delete_object(Bucket=BUCKET, Key=s3_key)
        print(f"Deleted '{s3_key}' from S3")
    except ClientError as e:
        print(f"Delete failed: {e}")


# ── 6. GENERATE SHAREABLE LINK ────────────────────
def get_shareable_link(s3_key, expires_in=3600):
    try:
        url = s3.generate_presigned_url(
            "get_object",
            Params={"Bucket": BUCKET, "Key": s3_key},
            ExpiresIn=expires_in
        )
        print(f"Shareable link (expires in 1 hour):\n{url}")
    except ClientError as e:
        print(f"Could not generate link: {e}")


# ── RUN ALL FUNCTIONS ─────────────────────────────
print("===== S3 File Manager =====\n")

# upload your cost report from Project 2
upload_file("cost_report.json", "reports/cost_report.json")

# list everything in bucket
list_files()

# download it back with a new name
download_file("reports/cost_report.json", "downloaded_report.json")

# generate a shareable link
get_shareable_link("reports/cost_report.json")

print("\n===== Done! =====")