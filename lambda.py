import boto3

def lambda_handler(event, context):
    # Initialize S3 client
    s3 = boto3.client('s3')
    
    # Retrieve bucket and object key from the S3 event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    try:
        # Read the object from the source bucket
        response = s3.get_object(Bucket=bucket, Key=key)
        data = response['Body'].read().decode('utf-8')
        
        # Process the data (e.g., perform some computation or transformation)
        processed_data = data.upper()  # Example: Convert data to uppercase
        
        # Write the processed data to the destination bucket
        destination_bucket = 'processed-bucket'
        destination_key = 'processed_' + key
        s3.put_object(Bucket=destination_bucket, Key=destination_key, Body=processed_data)
        
        return {
            'statusCode': 200,
            'body': 'Data processed and stored in the destination bucket'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error processing data: {str(e)}'
        }


import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    # Log the event details
    logger.info("Received S3 event: " + json.dumps(event))
    
    # Extract bucket and object key from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    # Log information about the uploaded object
    logger.info(f"Object '{key}' uploaded to bucket '{bucket}'")
    
    # Return a successful response
    return {
        'statusCode': 200,
        'body': 'Object upload event logged successfully'
    }
