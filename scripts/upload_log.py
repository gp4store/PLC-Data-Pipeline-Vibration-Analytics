import boto3
from datetime import datetime
import os

s3 = boto3.client('s3')
today = datetime.now()
s3_key = f"plc-logs/year={today.year}/month={today.month:02d}/day={today.day:02d}/plc-data-{today.strftime('%Y%m%d')}.csv"

try:

    s3.upload_file(
        'the-file-name-your-plc-creates',
        'your-s3-bucket-name',
        s3_key
    )
    

    if os.path.exists('the-file-name-your-plc-creates'):
        os.remove('the-file-name-your-plc-creates')
    
    print("File uploaded to S3 successfully!")
    
except Exception as e:
    print(f"Upload failed: {e}")