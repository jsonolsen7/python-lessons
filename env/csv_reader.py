import os
import csv
import pandas as pd

# read each line of file
with open('csv_reader.txt', encoding="utf-8") as text_reader:
    line_num = 1
    while True:
        line = text_reader.readline()
        if not line:
            break
        print(line_num, len(line.split()))
        line_num += 1

# read csv
rows = []
with open('unitedStates.csv', newline="") as unitedStates:
    csvreader = csv.reader(unitedStates)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
    print(rows)

# add new column with pandas
new_header = "Capital"
my_df = pd.read_csv('unitedStates.csv')
new_column = ["Sacramento", "Dallas", "Miami", "New York", "Quaker", "Chicaco", "Cinncinati", "Peaches", "Georgetown", "Detroit"]
my_df[new_header] = new_column

my_df.to_csv('unitedStates2.csv', index = False)