import sys
import csv

from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit('Too few command-line argumwents')
if len(sys.argv) > 2:
    sys.exit('Too many command-line argumwents')

if sys.argv[1].endswith('.csv'):
    pizza_list = []
    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        for row in reader:
            pizza_list.append(row)
        print(tabulate(pizza_list, headers='firstrow', tablefmt="grid"))


else:
    sys.exit('Not a CSV file')
