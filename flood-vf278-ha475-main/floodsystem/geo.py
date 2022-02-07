# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa

# Import haversine library
from haversine import haversine, Unit

# Function for distance
def stations_by_distance(stations, p):
    distance_list=[]
    for x in stations:
        distance=haversine(x.coord,p)
        add = (x.name,distance)
        distance_list.append(add)
    return sorted_by_key(distance_list,1)

# Function returns stations within an area of radius r
def stations_within_radius(stations, centre, r):
    distances = stations_by_distance(stations,centre)
    return_list = []
    for x in distances:
        if x[1]>r:
            break
        else:
            return_list.append(x[0])
        return_list.sort()
    return return_list

# Function return a river names set for a list of station objects
def rivers_with_station(stations):
    rivers = []
    for x in stations:
        rivers.append(x.river)
    rivers = set(rivers)
    return rivers

# Function returns dictionary with rivers as keys and lists stations for each river
def stations_by_river(stations):
    rivers = rivers_with_station(stations)
    dic_rivers = {}
    for x in rivers:
        list_rivers = []
        for y in stations:
            if x == y.river:
                list_rivers.append(y.name)
        dic_rivers[x]=list_rivers
    return dic_rivers

# Function returns tuples of Rivers with greatest number of stations
def rivers_by_station_number(stations, N):
    dic_rivers = stations_by_river(stations)
    dic_number_stations = {}
    for x in dic_rivers:
        dic_number_stations[x]=len(dic_rivers[x])
    sorted_lst = sorted(dic_number_stations.items(), key = lambda kv: kv[1])
    rivers_greater = sorted_lst[len(sorted_lst)+1-N:len(sorted_lst)+1]
    return rivers_greater