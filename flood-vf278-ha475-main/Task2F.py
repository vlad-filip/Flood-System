import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level

# Build list of stations
stations = build_station_list()

# Update latest level data for all stations
update_water_levels(stations)

# Finding the 5 stations for which the water levels are gretest 
stations_highest = stations_highest_rel_level(stations, 5)

# Fetch measurement levels for those 5 stations for past 2 days
dic_dates = {}
dic_levels = {}
dt = 2
for x in stations_highest:
    dates, levels = fetch_measure_levels(x[0].measure_id,dt=datetime.timedelta(days=dt))
    dic_dates[x[0].name] = dates
    dic_levels[x[0].name] = levels

# Plot polynomial fit
for x in stations_highest:
    plot_water_level_with_fit(x[0], dic_dates[x[0].name], dic_levels[x[0].name],4)