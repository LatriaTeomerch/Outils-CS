#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pylab as py
import numpy as np
import netCDF4
from netCDF4 import Dataset
import matplotlib.pyplot as plt
import datetime

var='H' #'H'  #'VAR1'
nom_variable=''
unit ='W/m2'

#parametres
deb = 0 #les données sont horaires
fin = 8760 #les données sont horaires

dataset1 = Dataset('../data/SURF_ATM_DIAGNOSTICS.OUT_surface1.nc')
dataset2 = Dataset('../data/SURF_ATM_DIAGNOSTICS.OUT_surface2.nc')
time=dataset1.variables['time']
dtime    = netCDF4.num2date(time[deb:fin],time.units, only_use_cftime_datetimes=False, only_use_python_datetimes=True)
time_dim = time[deb:fin].shape[0]
times =[]
for i in range(0,time_dim):
     date = datetime.datetime(dtime[i].year,dtime[i].month,dtime[i].day,dtime[i].hour)
     times.append(date)

variable1=dataset1.variables[var][deb:fin,0,0]
variable2=dataset2.variables[var][deb:fin,0,0]

print(variable1.shape,variable2.shape)

py.figure()
py.grid()
py.plot(times,variable1,linewidth=1,label='surface 1')
py.ylabel(nom_variable+' '+unit)
py.plot(times,variable2,linewidth=1,label='surface 2')
py.ylabel(var+' '+unit)
py.xlabel('temps (jours)')
py.legend()
py.show()
