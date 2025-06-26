import json
import boto3
import urllib.parse
from datetime import datetime

def lambda_handler(event, context):
    athena = boto3.client('athena')
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
    parts = key.split('/')
    year = parts[1].split('=')[1]
    month = parts[2].split('=')[1]
    day = parts[3].split('=')[1]
    
    partition_location = f"s3://{bucket}/plc-logs/year={year}/month={month}/day={day}/"
    
    query = f"""
    ALTER TABLE daily_logs 
    ADD IF NOT EXISTS PARTITION (year='{year}', month='{month}', day='{day}')
    LOCATION '{partition_location}'
    """
    
    response = athena.start_query_execution(
        QueryString=query,
        QueryExecutionContext={'Database': 'your-database-name'},
        ResultConfiguration={'OutputLocation': 's3://your-output-query-bucket/'}
    )
    
    return {'statusCode': 200, 'body': json.dumps('Partition added successfully')}