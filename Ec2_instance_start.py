import boto3
import json

client=boto3.client('ec2')

def lambda_handler(event, context):

        response = client.describe_instances()

        for reservation in response["Reservations"]:

            for instance in reservation["Instances"]:

                print(instance["InstanceId"] + "starting")

                id=[instance["InstanceId"]]

                client.start_instances(InstanceIds=id)

        return("Completed")
