import os

'''Lists the current directory'''
os.listdir('.')

'''This is rename the file'''
os.rename('csv.py', 'csv_parser.py')

'''Changing the permissions of a file'''
os.chmod('csv.py', 0o777)

'''This will create a directory'''
os.mkdir('terraform')

'''This will create the directories recursively'''
os.makedirs('/tmp/terraform/statefiles/')

'''Removes the specified file'''
os.remove('csv.py')

'''Removes the Whole directory'''
os.removedirs('/tmp/terraform/statefiles/')

os.rmdir('/tmp/terraform/statefiles/')

'''Provides the stats on the directory'''
os.stat('csvparser')


