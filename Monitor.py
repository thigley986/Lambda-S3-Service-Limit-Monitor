import boto3
import collections

service_limit = int('SERVICE_LIMIT')
warning_threshold = float('0.8')
sns_arn = 'SNS_TOPIC'

s3 = boto3.client('s3')
sns = boto3.client('sns')

def lambda_handler(event, context):
    response = s3.list_buckets()
    bucket_count =  len(response['Buckets'])
    print "There are currently %s buckets in the region." % (bucket_count)
    
    subject = "S3 Service Limits Warning"
    message = "There are currently %s S3 buckets.  The service limit is %s.  Time to request an increase of the service limit!" % (bucket_count, service_limit)
	
    if bucket_count > (service_limit * warning_threshold):
        response = sns.publish(
            TargetArn=sns_arn,
            Subject=subject,
            Message=message
        )
