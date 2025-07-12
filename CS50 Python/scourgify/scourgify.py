import sys
import csv

from tabulate import tabulate

if len(sys.argv) < 3:
    sys.exit('Too few command-line argumwents')
if len(sys.argv) > 3:
    sys.exit('Too many command-line argumwents')

if sys.argv[1].endswith('.csv'):

    with open(sys.argv[1], newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            name = row[0].split(',')
            if name[0] == 'name':
                first = 'first'
                last = 'last'
                house = 'house'
                with open(sys.argv[2], 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([first, last, house])
            else:
                first = name[1]
                last = name[0]
                house = row[1]
                with open(sys.argv[2], 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([first.strip(), last, house])


else:
    sys.exit('Not a CSV file')
