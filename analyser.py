import boto3
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

s3     = boto3.client("s3", region_name="ca-central-1")
ai     = Groq(api_key=os.getenv("GROQ_API_KEY"))
BUCKET = os.getenv("AWS_BUCKET_NAME")

def upload_file(local_file, s3_key):
    try:
        s3.upload_file(local_file, BUCKET, s3_key)
        print("Uploaded " + local_file + " to S3 as " + s3_key)
    except Exception as e:
        print("Upload failed: " + str(e))

def read_from_s3(s3_key):
    try:
        response = s3.get_object(Bucket=BUCKET, Key=s3_key)
        content  = response["Body"].read().decode("utf-8")
        print("Read " + s3_key + " from S3 successfully")
        return content
    except Exception as e:
        print("Read failed: " + str(e))
        return None

def analyse_with_ai(text):
    try:
        print("Sending to Groq AI for analysis...")
        response = ai.chat.completions.create(
            model    = "llama-3.3-70b-versatile",
            messages = [{
                "role":    "user",
                "content": "You are a cloud cost expert. Analyse this document and provide: 1. A 2-sentence summary 2. Top 3 problems 3. Top 3 recommendations 4. Estimated savings\n\nDocument:\n" + text
            }]
        )
        analysis = response.choices[0].message.content
        print("AI analysis complete!")
        return analysis
    except Exception as e:
        print("AI analysis failed: " + str(e))
        return None

def save_results(analysis, s3_key):
    try:
        s3.put_object(Bucket=BUCKET, Key=s3_key, Body=analysis.encode("utf-8"), ContentType="text/plain")
        print("Results saved to S3 as " + s3_key)
    except Exception as e:
        print("Save failed: " + str(e))

def main():
    print("\n===== AI S3 Document Analyser =====\n")
    upload_file("sample.txt", "documents/sample.txt")
    content = read_from_s3("documents/sample.txt")
    if content:
        analysis = analyse_with_ai(content)
        if analysis:
            save_results(analysis, "results/sample_analysis.txt")
            print("\n===== AI Analysis Results =====\n")
            print(analysis)
            print("\n===== Done! =====\n")

main()
