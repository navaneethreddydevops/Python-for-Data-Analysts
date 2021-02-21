import yaml
from pprint import pprint


def yamlreadfromfile():
    ''' This method will read the yaml file and print it in formatted way'''
    with open('playbook.yaml', 'r') as yamlfile:
        ansibleplaybook = yaml.safe_load(yamlfile)
        pprint(ansibleplaybook)


def yamlwritetofile():
    ''' This method will write the yaml to a file and print it in formatted way'''
    with open('playbook-write.yaml', 'w') as yamlfile:
        ansibleplaybook = yaml.safe_load(yamlfile)
        pprint(ansibleplaybook)


if __name__ == '__main__':
    yamlreadfromfile()
    yamlwritetofile()
