import csv

with open('database.csv', newline='') as csvfile:
    rows = csv.DictReader(csvfile)
    for row in rows:
        if row['PM'] == 'Sam Chiu':
            print(row['Name'])