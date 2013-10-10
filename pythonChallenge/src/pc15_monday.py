import calendar

year = 1006

while year<2000:
    day = calendar.weekday(year, 1, 26)
    if day is 0 and calendar.isleap(year):
        print calendar.month(year, 1)
    year +=10

