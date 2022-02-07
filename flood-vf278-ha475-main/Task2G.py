# Import modules
import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.datafetcher import fetch_measure_levels

# Build list of stations
stations = build_station_list()

# Update latest level data for all stations
update_water_levels(stations)

# We considered the risk of flooding to be greatest in the towns
# where the latest water level is above the high typical range
stations_tol = stations_level_over_threshold(stations,1)
stations_tol.sort(key=lambda x: x[1])

# We consider data for those stations in the past three days
dt = 3
# We initialize a dic for risk level variable describe below
dic_risk={}
for x in stations_tol:
    # We initialize a risk variable that uses integers to represent the flooding risk
    # 0 for low, 1 for moderate, 2 for high, 3 for sevre
    risk=0
    dates, levels = fetch_measure_levels(x[0].measure_id,dt=datetime.timedelta(days=dt))
    # We count how many times the level seems to be increasing compared to the previous level
    # Initialize counter for station
    n=0
    for i in range(len(levels)-1):
        if type(levels[i+1])==float and type(levels[i])==float:
            if levels[i]<levels[i+1]:
                n+=1
            # We consider the risk to be moderate if more than 30% of these comparisions increase,
            # 45% for high and 60% for sevre
        if n>0.6*len(levels):
            risk=3
        elif n>0.45*len(levels):
            risk=2
        elif n>0.3*len(levels):
            risk=1
        dic_risk[x]=risk

# Print sevre stations 
print('Sevre:')
for x in stations_tol:
    if dic_risk[x]==3:
        print(x[0].town)

# Print high stations
print('High:')
for x in stations_tol:
    if dic_risk[x]==2:
        print(x[0].town)   

# Print moderate stations
print('Moderate:')
for x in stations_tol:
    if dic_risk[x]==1:
        print(x[0].town) 

# Print low stations
print('Low:')
for x in stations_tol:
    if dic_risk[x]==0:
        print(x[0].town)