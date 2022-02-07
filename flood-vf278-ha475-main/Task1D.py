from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

# Build list of stations

stations = build_station_list()

# Get river set
rivers = list(rivers_with_station(stations))
rivers.sort()
print(str(len(rivers)) + ' stations')

# Print first ten
d = '['
for i in range(9):
    d += "'{}', ".format(rivers[i])
d += "'{}' ]".format(rivers[9])

print('First 10 -   ' + d)

# Print stations in alphabetical order for following rivers

dic_rivers = stations_by_river(stations)
dic_rivers['River Cam'].sort()
print(dic_rivers['River Cam'])
dic_rivers['River Aire'].sort()
print(dic_rivers['River Aire'])
dic_rivers['River Thames'].sort()
print(dic_rivers['River Thames'])
