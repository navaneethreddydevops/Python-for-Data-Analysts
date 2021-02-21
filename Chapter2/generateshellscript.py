#!/usr/bin/env python
import sys

text = '''
#!/bin/bash
export STAGE=PROD
export ACCOUNT=6444334663463

getcredentials(){
    rm -rf ~/.aws/credentials
    aws sts assume-role arn:aws:iam::123456789012:role/Developer
}

gets3data(){
    aws s3 ls --output table
}

getec22data(){
    aws ec2 list-instances --output table
}
'''
with open('generatedscript.sh', 'w') as shellscript:
    shellscript.write(text)
