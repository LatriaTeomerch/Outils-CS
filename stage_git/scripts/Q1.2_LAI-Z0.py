# -*-coding:Latin-1 -*
import pylab as py
from netCDF4 import Dataset as netcdf_dataset
import numpy as np
import matplotlib.pyplot as plt

dataset = netcdf_dataset('../data/PREP_Q1.nc')

#-------------------------------------
# choisir une variable
#--------------------------------------
#var='LAIP1'    # LAI: Leaf area index
var='Z0VEGP1'  # Z0: roughness

#---------------------------------------
variable=dataset.variables[var][:,:]
lat = dataset.variables['REG_LAT'][:,0]
lon = dataset.variables['REG_LON'][0,:]
plt.contourf(lon, lat, variable)
plt.title(var)
plt.colorbar()
plt.show()
