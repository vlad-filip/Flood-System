import datetime
from floodsystem.analysis import polyfit

# Dates is a list of 9 dates
dates = [datetime.datetime(2021, 3, 2, 12, 45), datetime.datetime(2021, 3, 2, 12, 30), datetime.datetime(2021, 3, 2, 12, 15), datetime.datetime(2021, 3, 2, 12, 0), datetime.datetime(2021, 3, 2, 11, 0), datetime.datetime(2021, 3, 2, 10, 45), datetime.datetime(2021, 3, 2, 10, 30), datetime.datetime(2021, 3, 2, 10, 15), datetime.datetime(2021, 3, 2, 10, 0)]

#Dates1 is a list of 10 dates
dates1 = [datetime.datetime(2021, 3, 2, 13, 0), datetime.datetime(2021, 3, 2, 12, 45), datetime.datetime(2021, 3, 2, 12, 30), datetime.datetime(2021, 3, 2, 12, 15), datetime.datetime(2021, 3, 2, 12, 0), datetime.datetime(2021, 3, 2, 11, 0), datetime.datetime(2021, 3, 2, 10, 45), datetime.datetime(2021, 3, 2, 10, 30), datetime.datetime(2021, 3, 2, 10, 15), datetime.datetime(2021, 3, 2, 10, 0)]

# Levels is a list of 9 water levels
levels = [2.926, 2.927, 2.928, 2.928, 2.93, 2.931, 2.932, 2.933, 2.933]

p = 2

def test_analysis():
    # Test that output is returned when there are equal dates and levels
    poly, d0 = polyfit(dates, levels, p)
    if len(dates) == len(levels):
        assert poly != None
        assert d0 != None
    
    # Test that output is returned when there are equal dates and levels
    poly, d0 = polyfit(dates1, levels, p)    
    if len(dates1) > len(levels):
        assert poly != None
        assert d0 != None