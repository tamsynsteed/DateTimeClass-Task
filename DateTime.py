#import the datetime module from pythins library

from datetime import date
d = date(2013, 8, 22)
print(d.year)
print(d.month)
print(d.day)
print(d.strftime("%y %m %d"))
