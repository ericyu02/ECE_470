import csv
import os

# create player class

# extract each row of each input file into player class

# add each player to array displaying important stats

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, '../res/moneypuck/moneypuck_2023-24.csv')

rows = []
with open(file_path, 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
print(header)
print(rows)

