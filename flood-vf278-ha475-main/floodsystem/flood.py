# Function returns stations with risk of flooding
def stations_level_over_threshold(stations, tol):
    stations_over_tol = []
    for x in stations:
        if x.typical_range_consistent()==True and x.relative_water_level()!=None:
            if float(x.relative_water_level())>tol:
             t = (x,x.relative_water_level())
             stations_over_tol.append(t)
    return stations_over_tol

# Function returns first N sations with risk of flooding
def stations_highest_rel_level(stations, N):
    stations_ordered = []
    for x in stations:
        if x.relative_water_level()!=None:
            t = (x, x.relative_water_level())
            stations_ordered.append(t)
    stations_ordered = sorted(stations_ordered, key=lambda x: x[1])
    stations_return = []
    for i in range(N):
        stations_return.append(stations_ordered[len(stations_ordered)-1-i])
    return stations_return