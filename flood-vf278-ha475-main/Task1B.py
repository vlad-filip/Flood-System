from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

# Build list of stations
stations = build_station_list()

# Cambridge coordinates
p = (52.2053, 0.1218)

# Use stations_by_distance function to print closest stations
distance_stations = stations_by_distance(stations, p)
print(distance_stations[:10])

# Print 10 furthest away
print(distance_stations[-10:])
