from floodsystem.geo import stations_by_river
from floodsystem.station import MonitoringStation
from floodsystem.geo import rivers_with_station
from floodsystem.geo import rivers_by_station_number
from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius
s_id = "test-s-id"
m_id = "test-m-id"
label = "some station"
coord = (52.2053, 0.1217)
trange = (-2.3, 3.4445)
river = "River X"
town = "My Town"
station1 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
s_id1 = "test-s-id"
m_id1 = "test-m-id"
label1 = "another station"
coord1 = (-2.0, 4.0)
trange1 = (-2.3, 3.4445)
river1 = "River Y"
town1 = "My Town"
station2 = MonitoringStation(s_id1, m_id1, label1, coord1, trange1, river1, town1)
s = []
s.append(station1)
s.append(station2)


def test_stations_by_river():
    a = stations_by_river(s)
    assert a == {river: [label], river1: [label1]}


def test_rivers_with_station():
    list_river = rivers_with_station(s)
    assert len(list_river) == 2


def test_rivers_by_station_number():
    river_list2 = rivers_by_station_number(s, 2)
    river_list1 = rivers_by_station_number(s, 1)
    assert len(river_list2) == 2
    assert len(river_list1) == 1
    assert river_list2 == [(river, 1), (river1, 1)]


def test_stations_by_distance():
    p = (52.2053, 0.1218)
    closest = stations_by_distance(s, p)[:1]
    furthest = stations_by_distance(s, p)[-1:]
    assert len(closest) == 1
    assert len(furthest) == 1


def test_stations_within_radius():
    centre = (52.2053, 0.1218)
    r = 10
    assert(len(stations_within_radius(s, centre, r))) == 1
    r = 5
    assert(len(stations_within_radius(s, centre, r))) == 1
