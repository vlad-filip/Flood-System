from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

# Build list of stations
stations = build_station_list()

# Number of stations
N = 9

print(rivers_by_station_number(stations, N))
