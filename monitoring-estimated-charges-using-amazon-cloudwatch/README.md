## Setting up an Amazon CloudWatch Billing Alarm to Proactively Monitor Estimated Charges

This solution deploys an Amazon CloudWatch Billing alarm, and connects the Amazon CloudWatch Billing alarm to an Amazon SNS topic for notifications when the alarm exceeds the specified threshold.

Amazon CloudWatch is a monitoring and observability service that provides a unified view of your application’s performance, resource utilization, and performance changes.
Amazon CloudWatch is ideal for improving operational performance and resource optimization, such as creating alarms to notify you when your billing charges are exceeding a predefined threshold.

By using Amazon CloudWatch, you can better monitor your estimated AWS charges. By monitoring the estimated AWS charges for your AWS account(s), you can be alerted and proactively notified when the calculated estimated charges exceed the defined threshold, both from the AWS CloudWatch console and via SNS Notification.

## Solution Overview

<p align='center'>
	<img src='img/0_SolutionArchitecture.png' alt='Solution Architecture Diagram'/>
</p>

## Prerequisites
You need an AWS account with the IAM permissions required to access Amazon CloudWatch, Billing & Cost Management Console, and Amazon SNS.
You will also need IAM permissions to AWS CloudFormation if you plan to deploy the sample template.

## Deployment Instructions
You can deploy the solution using the template.yaml file located in the <a href="https://github.com/aws-samples/aws-cloud-operation-samples/blob/main/monitoring-estimated-charges-using-amazon-cloudwatch/src/template.yaml">src</a> folder.
