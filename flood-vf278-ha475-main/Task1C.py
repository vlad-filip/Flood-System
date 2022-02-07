from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

# Build list of stations
stations = build_station_list()

# Cambridge coordinates
p = (52.2053, 0.1218)

# Use function to print stations within a radius of r = 10 km
r = 10
print(stations_within_radius(stations, p, r))
