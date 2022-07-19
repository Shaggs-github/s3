def verify_s3bucket_owner_noncompliant(event):
    import boto3
    client = boto3.client('s3')
    # Noncompliant: missing S3 bucket owner condition
    # (ExpectedSourceBucketOwner).
    client.copy_object(
        Bucket=event["bucket"],
        CopySource=f"{event['bucket']}/{event['key']}",
        Key=event["key"],
        ExpectedBucketOwner=event["owner"],
    )