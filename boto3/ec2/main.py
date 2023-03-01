import boto3

ec2_client = boto3.client('ec2', region_name='us-east-1')

response = ec2_client.describe_instances(Filters=[{'Name': 'tag:Shutdown', 'Values': ['yes']}])

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        print(f'Shutdown instance: {instance_id}..')
        ec2_client.stop_instances(InstanceIds=[instance_id])
