import csv
import pandas as pd

with open("backend/data.csv" ,'r', encoding='cp949') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        print(row)

