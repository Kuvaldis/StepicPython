import csv
from datetime import datetime
from collections import defaultdict
import operator

with open('Crimes.csv', 'r') as crimes_file:
    crimes_file.readline()
    crimes_csv = csv.reader(crimes_file)
    by_type = defaultdict(int)
    for crime in crimes_csv:
        crime_date = datetime.strptime(crime[2], '%m/%d/%Y %I:%M:%S %p')
        if crime_date.year == 2015:
            by_type[crime[5]] += 1
    print(max(by_type.items(), key=operator.itemgetter(1)))