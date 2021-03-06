import os

with open('/Users/navaneethreddy/Documents/Code/Python-for-DevOps/cars.csv', 'r') as source_file:
    with open('/Users/navaneethreddy/Documents/Code/Python-for-DevOps/Chapter2/csvparser/correctedfile.csv', 'w') as output_file:
        for line in source_file:
            output_file.write(line)


def file_reader(file_path):
    """
    This method will take input as a file path and reads each line of a file
    """
    with open(file_path,'r') as source_file:
        for line in source_file:
            yield line


output = file_reader('/Users/navaneethreddy/Documents/Code/Python-for-DevOps/cars.csv')
