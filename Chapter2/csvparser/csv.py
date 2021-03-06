import csv
file_path = '/Users/navaneethreddy/Documents/Code/Python-for-DevOps/cars.csv'

with open(file_path, newline='') as csv_file:
    off_reader = csv.reader(csv_file , delimiter=',')
    for _ in range(10):
        print(next(off_reader))