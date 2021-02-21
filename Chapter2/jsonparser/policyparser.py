import json
import ast
from pprint import pprint


def readjsonpretty():
    '''This Method will parsed the JSON in pretty format'''
    with open('policy.json', 'r') as iam_policy:
        policy = json.dumps(json.load(iam_policy))
        pprint(policy)


if __name__ == '__main__':
    readjsonpretty()
