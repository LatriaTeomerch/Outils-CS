#!/usr/bin/env python
# -*- coding: utf-8 -*-
#import pylab as py
import  matplotlib.pyplot as py
import numpy as np
import netCDF4
from netCDF4 import Dataset
import matplotlib.pyplot as plt
import datetime

#-----------------------------------
# choix des variables
#------------------------------------
var='LEG_ISBA'  #'LETR_ISBA'  #'LETR_ISBA'  #'LER_ISBA' # LETR_ISBA  LEG_ISBA
unit ='W/m2'
#-------------------------------------

#parametres
deb = 1 #les données sont horaires
fin = 8760 #les données sont horaires

dataset1 = Dataset('../data/ISBA_DIAGNOSTICS.OUT_veg1.nc')
dataset2 = Dataset('../data/ISBA_DIAGNOSTICS.OUT_veg2.nc')

time=dataset1.variables['time']

dtime    = netCDF4.num2date(time[deb:fin],time.units, only_use_cftime_datetimes=False, only_use_python_datetimes=True)
time_dim = time.shape[0] -1
times =[]
for j in range(0,time.shape[0]-1):
     date = datetime.datetime(dtime[j].year,dtime[j].month,dtime[j].day,dtime[j].hour)
     times.append(date)

print(dtime)
variable1=dataset1.variables[var][deb:fin,0,0]
variable2=dataset2.variables[var][deb:fin,0,0]

py.figure()
py.grid()
py.plot(times,variable1,linewidth=1,label='surface 1')
py.ylabel(var+' '+unit)
py.plot(times,variable2,linewidth=1,label='surface 2')
py.ylabel(var+' '+unit)
py.xlabel('temps (jours)')
py.title(var)
py.legend()
py.show()
