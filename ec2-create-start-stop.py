import os
import boto3

AMI = os.environ['AMI']
INSTANCE_TYPE = os.environ['INSTANCE_TYPE']
KEY_NAME = os.environ['KEY_NAME']
SUBNET_ID = os.environ['SUBNET_ID']


ec2 = boto3.resource('ec2')

def lambda_handler(event, context):
    
    
    if event["action"] == "create":
        
        instance = ec2.create_instances(
        ImageId=AMI,
        InstanceType=INSTANCE_TYPE,
        KeyName=KEY_NAME,
        SubnetId=SUBNET_ID,
        MaxCount=1,
        MinCount=1
    )
    client = boto3.client('ec2')
    Myec2=client.describe_instances()
    for pythonins in Myec2['Reservations']:
        for printout in pythonins['Instances']:
            print(printout['InstanceId'])
            insta_id=printout['InstanceId']
    
    if event["action"] == "stop":
        ec2.instances.filter(InstanceIds = [insta_id]).stop()

    if event["action"] == "start":
        ec2.instances.filter(InstanceIds = [insta_id]).start()
       
    

     