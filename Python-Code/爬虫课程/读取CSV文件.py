import csv

with open('data.csv','r') as file:
    reader = csv.reader(file)
    list1 = list(reader)
    print(list1)