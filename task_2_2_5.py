from datetime import datetime, timedelta

date = datetime(*(map(int, input().split(" "))))
interval = timedelta(int(input()))
newDate = date + interval
print(str(newDate.year) + " " + str(newDate.month) + " " + str(newDate.day))