import csv


with open('data_csv/id.csv', newline='\n') as f:
    reader = csv.reader(f)
    for row in reader:
        print(str(row))
