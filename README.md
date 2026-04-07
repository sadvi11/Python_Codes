# AI S3 Document Analyser

A Python automation tool that uploads documents to AWS S3, reads them back, sends them to an AI model for intelligent analysis, and saves results back to S3.

## What it does
- Uploads files to AWS S3
- Reads files back from AWS S3
- Sends content to Groq AI (LLaMA 3.3) for analysis
- AI identifies problems and cost saving recommendations
- Saves AI results back to AWS S3

## Technologies
- Python
- AWS S3 + boto3
- Groq AI API
- python-dotenv

## How to run
1. Clone the repo
2. Create .env file with your API keys
3. Run: python3 analyser.py

## Author
Sadhvi Sharma — Nokia 5G Cloud Engineer transitioning to AI + Cloud Engineering
Calgary, Canada
