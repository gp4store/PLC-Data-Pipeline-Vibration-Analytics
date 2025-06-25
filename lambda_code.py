import json
import boto3
import urllib.parse
from datetime import datetime

def lambda_handler(event, context):
    athena = boto3.client('athena')
    
    # Parse S3 event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
    
    # Extract partition info from key: plc-logs/year=2025/month=06/day=24/file.csv
    parts = key.split('/')
    year = parts[1].split('=')[1]
    month = parts[2].split('=')[1]
    day = parts[3].split('=')[1]
    
    # Build partition location
    partition_location = f"s3://{bucket}/plc-logs/year={year}/month={month}/day={day}/"
    
    # Add partition query
    query = f"""
    ALTER TABLE daily_logs 
    ADD IF NOT EXISTS PARTITION (year='{year}', month='{month}', day='{day}')
    LOCATION '{partition_location}'
    """
    
    # Execute query
    response = athena.start_query_execution(
        QueryString=query,
        QueryExecutionContext={'Database': 'plc_analytics'},
        ResultConfiguration={'OutputLocation': 's3://athena-query-results-plc-analytics-db/'}
    )
    
    return {'statusCode': 200, 'body': json.dumps('Partition added successfully')}