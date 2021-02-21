#!/usr/bin/python3

import pandas
import datetime
import os
import logging
import boto3
from botocore.exceptions import ClientError

path=os.getcwd()
workdir="/Users/navaneethreddy/Documents/Code/"

def get_current_directory():
    try:
        print("This the current directory of code :" + path + ".")
    except:
        print("Not able to get the current working directory")

def change_directory():
    try:
        print("Changing to working directory :" + os.chdir(workdir) +".")
    except:
        print("Not able to change to working directory defined")

def describe_aws_account(region,profile):
    try:
        s3 = boto3.resource('s3')
        print("Boto3 Session is initiated")
        buckets = s3.list_buckets()
        print("These are the buckets Present in Account :")
        for bucket in buckets:
            print(f'{bucket["Name"]}')
    except:
        print("No S3 Buckets were found")

def positioning(first,second):
    """This method will print the positional arguments"""
    print(f"This is the first argument:{first}")
    print(f"This is the second argument:{second}")


def create_bucket(bucket_name,region=None):
    try:
        if region is None:
            s3_client=boto3.client('s3')
            s3.client.create_bucket(Bucket=bucket_name)
        else:
            s3_client=boto3.client('s3',region_name=region)
            location={'LocationConstraint':region}
            s3_client.create_bucket(Bucket=bucket_name,CreateBucketConfiguration=location)

    except ClientError as e:
        logging.error(e)
        return False
    return True

if __name__ == "__main__":
    change_directory()
    get_current_directory()
    positioning(1,35)
    describe_aws_account("us-east-1","default")
    create_bucket("my-custom-cloud-bucket","us-east-1")