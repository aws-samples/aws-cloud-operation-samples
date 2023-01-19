import json
import boto3
from datetime import datetime

ec2_client = boto3.client('ec2')
cloudwatch_client = boto3.client('cloudwatch')

def lambda_handler(event, context):
    date_today = datetime.utcnow().date()

    response = ec2_client.describe_reserved_instances(Filters=[{'Name':'state','Values': ['active']}])

    expiring_soon_ri = []
    for i in response['ReservedInstances']:
        print('Reserved Instance Id: ', i['ReservedInstancesId'])
        print('End Date: ', i['End'].date())
        ri_days_remaining = i['End'].date() - date_today
        ri_days_remaining = ri_days_remaining.days

        print('Days Remaining: ', ri_days_remaining)
        cloudwatch_client.put_metric_data(
            Namespace = 'AWS/ReservedInstances',
            MetricData = [
                {
                    'MetricName': 'RIExpireCountdown',
                    'Dimensions': [
                        {
                            'Name': 'Reserved Instance Id',
                            'Value': str(i['ReservedInstancesId'])
                        },
                    ],
                    'Value': ri_days_remaining,
                    'Unit': 'Count'
                },
            ],
        )

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }