Lizzard File Uploader App (S3 + Lambda + DynamoDB) build log


Region: eu-north-1

S3 bucket created
Bucket name: lizzard-upload-demo


DynamoDB table created
Table name:  lizzard-metadata


IAM roe for Lambda created
Role name: lizzard-lambda-file-uploader
Policies attached: S3 Full access, DynamoDB full access

Lambda function created and run successfully 
Function name: lizzard-file-uploader-handler
Python code in lizzard-file-uploader-handler.py

✅ End of Phase 1 Goal:

 Lambda function runs successfully

 File appears in S3

 Metadata record appears in DynamoDB




API created & integrated
API name: Lizzard-uploaderAPI
ARN: arn:aws:apigateway:eu-north-1::/apis/tffm9ykuhk
URL: https://tffm9ykuhk.execute-api.eu-north-1.amazonaws.com

POST/upload route created

Ran into an error 
curl -X POST https://tffm9ykuhk.execute-api.eu-north-1.amazonaws.com {"message":"Not Found"}%

Solution: created a stage, deployed the route. Success.

curl -X POST https://tffm9ykuhk.execute-api.eu-north-1.amazonaws.com/prod/upload

{"message": "File uploaded successfully", "file_name": "c38c54e1-ff3c-403b-a1a9-261bfaf0b7c9.txt"}% 


✅ Phase 2 Success
- API Gateway endpoint working: [https://tffm9ykuhk.execute-api.eu-north-1.amazonaws.com/prod/upload]
- Lambda triggered via HTTP POST
- File uploaded successfully to S3
- Metadata stored in DynamoDB



Index.html file created
Tested locally

✅ Phase 3 Success

- Added simple HTML page to upload files
- Can be extended to handle real file content


