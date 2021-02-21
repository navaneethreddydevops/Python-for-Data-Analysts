import json
import ast
from pprint import pprint


def readjsonfromfile():
    '''This Method will parsed the JSON in pretty format'''
    with open('policy.json', 'r') as iam_policy:
        policy = json.dumps(json.load(iam_policy))
        pprint(policy)


def writejsontofile():
    '''This Method will write the parsed the JSON to a file'''
    with open('policy-write.json', 'w') as iam_policy:
        policy = json.dump(policy,iam_policy)

if __name__ == '__main__':
    readjsonfromfile()
    writejsontofile()
