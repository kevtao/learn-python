## put to cloud
### sam
- sam build
- sam package --s3-bucket YOUR_S3_BUCKET_NAME --output-template-file packaged.yaml
- sam deploy --template-file packaged.yaml --stack-name my-serverless-stack --capabilities CAPABILITY_IAM