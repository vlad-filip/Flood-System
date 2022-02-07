import matplotlib 
import matplotlib.dates
from matplotlib import pyplot as plt
from .analysis import polyfit

# Define fuction that plots the water level at a given station with respect to time
def plot_water_levels(station, dates, levels):
    plt.plot(dates, levels, color = 'm')
    plt.axhline(y=station.typical_range[0],color='r',linestyle='-')
    plt.axhline(y=station.typical_range[1],color='r',linestyle='-')
    plt.xlabel('time')
    plt.ylabel('water level')
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.tight_layout()
    plt.show()

# Define function that plots the water level data and the best-fit polynomial
def plot_water_level_with_fit(station, dates, levels, p):
    poly, d0 = polyfit(dates, levels, p)
    
    # Plot original data points and typical range value
    plt.plot(dates, levels, '.')
    plt.axhline(y=station.typical_range[0],color='r',linestyle='-')
    plt.axhline(y=station.typical_range[1],color='r',linestyle='-')
    plt.title(station.name)
    # Plot plolynomial fit 
    plt.plot(dates, poly(matplotlib.dates.date2num(dates)-d0), color='m')
    plt.show()
