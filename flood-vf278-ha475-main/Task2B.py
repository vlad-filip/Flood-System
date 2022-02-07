from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

# Build list of stations
stations = build_station_list()

# Update latest level data for all stations
update_water_levels(stations)

# Return stations with levels over 0.8 tol
stations_tol = stations_level_over_threshold(stations,0.8)
for x in stations_tol:
    print('{}   '.format(x[0].name)+'{}'.format(x[1]))