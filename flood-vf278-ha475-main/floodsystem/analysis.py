import matplotlib.dates as plt
import numpy as np

def polyfit(dates, levels, p):
    x=[]
    x = plt.date2num(dates)
    p_coef = np.polyfit(x-x[0]*np.ones(len(x)), levels, p)
    poly = np.poly1d(p_coef)

    return (poly, plt.date2num(dates[0]))