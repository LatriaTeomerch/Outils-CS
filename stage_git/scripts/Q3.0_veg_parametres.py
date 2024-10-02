#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pylab as py 
import numpy as np
import netCDF4
from netCDF4 import Dataset
import matplotlib.pyplot as plt
import datetime

#parametres
deb = 1 #les données sont horaires
fin = 8760 #les données sont horaires

dataset1 = Dataset('../data/ISBA_VEG_EVOLUTION.OUT_veg1.nc')
dataset2 = Dataset('../data/ISBA_VEG_EVOLUTION.OUT_veg2.nc')

var=['LAI','VEG','Z0VEG']
unit =['m2/m2','-','m']
time=dataset1.variables['time']
dtime    = netCDF4.num2date(time[deb:fin],time.units, only_use_cftime_datetimes=False, only_use_python_datetimes=True)
time_dim = time.shape[0] -1
times =[]
for j in range(0,time.shape[0]-1):
     date = datetime.datetime(dtime[j].year,dtime[j].month,dtime[j].day,dtime[j].hour)
     times.append(date)




py.figure()
for i in range(len(var)):
  plt.subplot(2,3,i+1)
  variable=dataset1.variables[var[i]][deb:fin,0,0]
  py.grid()
  py.plot(times,variable)
  py.title('vegetation1  '+var[i])
  py.ylabel('('+unit[i]+')')
  plt.tick_params(labelsize=8)
  #py.xlabel('temps (jours)')
for i in range(len(var)):
  plt.subplot(2,3,i+1+3)
  variable=dataset2.variables[var[i]][deb:fin,0,0]
  py.grid()
  py.plot(times,variable)
  py.title('vegetation2  '+var[i])
  py.ylabel('('+unit[i]+')')
  plt.tick_params(labelsize=8)
  #py.xlabel('temps (jours)')
py.show()

