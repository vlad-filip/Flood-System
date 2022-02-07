from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

# Build list of stations
stations = build_station_list()

# Update latest level data for all stations
update_water_levels(stations)

# Initialise number of stations
N = 10
stations_highest = stations_highest_rel_level(stations,N)

#Print the N stations
for x in stations_highest:
    print('{}  '.format(x[0].name)+'{}'.format(x[1]))
