from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level
s_id0 = "test-s-id0"
m_id0 = "test-m-id0"
label0 = "some station"
coord0 = (-2.0, 4.0)
trange0 = (-2.3, -3.4445)
river0 = "River 0"
town0 = "My Town"
s0 = MonitoringStation(s_id0, m_id0, label0, coord0, trange0, river0, town0)
# Create a station
s_id1 = "test-s-id"
m_id1 = "test-m-id"
label1 = "some station"
coord1 = (-2.0, 4.0)
trange1 = (2.3, 4.4445)
river1 = "River 1"
town1 = "My Town"
s1 = MonitoringStation(s_id1, m_id1, label1, coord1, trange1, river1, town1)
list_river = [s0, s1]

latest_level = 5
s0.latest_level = latest_level
s1.latest_level = latest_level
tol = 0.1
staions_over_threshold = stations_level_over_threshold(list_river, tol)
highest_rel_level = stations_highest_rel_level(list_river, 1)


def test_stations_level_over_threshold():
    assert len(staions_over_threshold) == 1


def test_stations_highest_rel_level():
    assert len(highest_rel_level) == 1
    assert highest_rel_level[0] == s1