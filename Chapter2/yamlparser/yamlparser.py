import yaml
from pprint import pprint

def yamlparser():
    with open('playbook.yaml','r') as yamlfile:
        ansibleplaybook = yaml.safe_load(yamlfile)
        pprint(ansibleplaybook)

if __name__ =='__main__':
    yamlparser()