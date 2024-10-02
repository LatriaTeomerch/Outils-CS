#import pylab as py
from netCDF4 import Dataset as netcdf_dataset
import numpy as np
import matplotlib.pyplot as plt
#from cartopy import config
#import cartopy.crs as ccrs


dataset = netcdf_dataset('../data/PGD_Q0.nc')
var=['FRAC_NATURE','FRAC_TOWN','FRAC_SEA','FRAC_WATER']

levels = [0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1]


for i in range(4):
    plt.subplot(2,2,i+1)
    variable=dataset.variables[var[i]][:,:]
    lat = dataset.variables['REG_LAT'][:,0]
    lon = dataset.variables['REG_LON'][0,:]
    plt.contourf(lon, lat, variable,levels)
    plt.title(var[i])
    plt.colorbar()
    
plt.show()
