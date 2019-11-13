# You are given the following information, but you may prefer to do some research for yourself.
#
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
weekday = 0
days = []
for year in range(1900, 2000):
    days.append([])
    year_length = 366
    if year % 4 == 0 and year % 100 != 0 or year % 100 == 0 and year % 400 == 0:
        year_length = 367
    for day in range(year_length):
        days[year - 1900].append(weekday)
        if weekday == 6:
            weekday = 0
        else:
            weekday += 1
months = []
for year in range(100):
    step = 31
    month = 0
    day = 0
    while day < 366:
        if month == 3 or month == 5 or month == 8 or month == 10:
            months += [days[year][day]]
            step = 30
        elif month == 1:
            months += [days[year][day]]
            step = 29
        else:
            months += [days[year][day]]
            step = 31
        month += 1
        day += step
sundays = 0
for day in months:
    if day == 6:
        sundays += 1
print(sundays)
