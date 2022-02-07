import datetime
from floodsystem.plot import plot_water_levels
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations

# Create Station
s_id0 = "test-s-id0"
m_id0 = "test-m-id0"
label0 = "some station"
coord0 = (-2.0, 4.0)
trange0 = (-2.3, -3.4445)
river0 = "River 0"
town0 = "My Town"
s0 = MonitoringStation(s_id0, m_id0, label0, coord0, trange0, river0, town0)

# Dates is a list of 9 dates 
dates = [datetime.datetime(2021, 3, 2, 12, 45), datetime.datetime(2021, 3, 2, 12, 30), datetime.datetime(2021, 3, 2, 12, 15), datetime.datetime(2021, 3, 2, 12, 0), datetime.datetime(2021, 3, 2, 11, 0), datetime.datetime(2021, 3, 2, 10, 45), datetime.datetime(2021, 3, 2, 10, 30), datetime.datetime(2021, 3, 2, 10, 15), datetime.datetime(2021, 3, 2, 10, 0)]

#Dates1 is a list of 10 dates
dates1 = [datetime.datetime(2021, 3, 2, 13, 0), datetime.datetime(2021, 3, 2, 12, 45), datetime.datetime(2021, 3, 2, 12, 30), datetime.datetime(2021, 3, 2, 12, 15), datetime.datetime(2021, 3, 2, 12, 0), datetime.datetime(2021, 3, 2, 11, 0), datetime.datetime(2021, 3, 2, 10, 45), datetime.datetime(2021, 3, 2, 10, 30), datetime.datetime(2021, 3, 2, 10, 15), datetime.datetime(2021, 3, 2, 10, 0)]

# Levels is a list of 9 water levels
levels = [2.926, 2.927, 2.928, 2.928, 2.93, 2.931, 2.932, 2.933, 2.933]

p = 2

def test_plot_water_level():
    plot_water_levels(s0, dates, levels)
    assert len(dates) == len(levels)

    plot_water_levels(s0, dates1, levels)
    assert len(dates1) > len(levels)

def test_plot_water_level_with_fit():
    plot_water_level_with_fit(s0, dates, levels, p)
    assert len(dates) == len(levels)

    plot_water_level_with_fit(s0, dates1, levels, p)
    assert len(dates1) > len(levels)