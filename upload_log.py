import boto3
from datetime import datetime

s3 = boto3.client('s3')
today = datetime.now()

# Create partitioned S3 key
s3_key = f"plc-logs/year={today.year}/month={today.month:02d}/day={today.day:02d}/plc-data-{today.strftime('%Y%m%d')}.csv"

# Upload your daily log file
s3.upload_file(
    'local-plc-log.csv',  # your local file
    'vibration-daily-readings-project',    # your S3 bucket
    s3_key
)