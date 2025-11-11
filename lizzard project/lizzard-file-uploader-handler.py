import boto3
import json
import uuid
from datetime import datetime

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('lizzard-metadata')

BUCKET_NAME = 'lizzard-upload-demo'

def lambda_handler(event, context):
    try:
        file_name = f"{uuid.uuid4()}.txt"
        file_content = "This is a test file from Lambda."

        s3.put_object(Bucket=BUCKET_NAME, Key=file_name, Body=file_content)

        table.put_item(Item={
            'file_id': str(uuid.uuid4()),
            'file_name': file_name,
            'uploaded_at': datetime.utcnow().isoformat()
        })

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'File uploaded successfully', 'file_name': file_name})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
