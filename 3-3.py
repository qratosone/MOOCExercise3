import calendar
i=0
for year in xrange(1901,2001):
    for month in xrange(1,13):
            if calendar.monthcalendar(year,month)[0].index(1) == 6:
                i=i+1
print i