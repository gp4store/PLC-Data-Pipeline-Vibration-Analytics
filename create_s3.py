import boto3
import logging
from botocore.exceptions import ClientError

def create_s3_bucket(bucket_name):
    """
    Create an S3 bucket
    
    :param bucket_name: Bucket to create
    :return: True if bucket was created, else False
    """
    try:
        s3_client = boto3.client('s3')
        s3_client.create_bucket(Bucket=bucket_name)
        
        logging.info(f"Bucket '{bucket_name}' created successfully")
        return True
        
    except ClientError as e:
        error_code = e.response['Error']['Code']
        if error_code == 'BucketAlreadyExists':
            logging.error(f"Bucket '{bucket_name}' already exists")
        elif error_code == 'BucketAlreadyOwnedByYou':
            logging.warning(f"Bucket '{bucket_name}' already owned by you")
            return True
        else:
            logging.error(f"Error creating bucket: {e}")
        return False

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    
    bucket_name = 'vibration-daily-readings-log-project'
    
    if create_s3_bucket(bucket_name):
        print(f"Successfully created bucket: {bucket_name}")
    else:
        print(f"Failed to create bucket: {bucket_name}")