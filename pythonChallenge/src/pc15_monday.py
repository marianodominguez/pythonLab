import calendar

year = 1906

while year<2000:
    day = calendar.weekday(year, 1, 26)
    if day is 0:
        print calendar.month(year, 1)
    year +=10

