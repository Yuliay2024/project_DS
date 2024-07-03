import datetime


def delta(date1, date2):
    d1 = datetime.date(date1)
    d2 = datetime.date(date2)
    date_diff = d1 - d2
    print(abs(date_diff.days))
        
    
    
from datetime import date


def delta():
    d1 = date(year, month, day)
    d2 = date(year, month, day)
    date_diff = d1 - d2
    print(abs(date_diff))