#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pylab as py
import numpy as np
import netCDF4
from netCDF4 import Dataset
import matplotlib.pyplot as plt
import datetime
import os 
#----------------------
# Task 3. Lire le fichier de surface et le fait qu'on va plotter les figures en ligne de commande
#--------------------
# choix du fichier par l'utilisateur 
#---------------------
fic = 'surface1'
fic = 'surface2'
#---------------------

#----------------------------------------------------------
print(' Q_2.1: trouver le nom des variables et les unités')

var          = ['VAR1','VAR2','VAR3','VAR4','VAR5'] 
unit         = ['','','','',''] # Changer ici l'unité
#-----------------------
# Task 1 : Changer le titre après avoir trouver qui est qui. 
#-------
title        = ['a','b','c','d','e'] # Changer ici le titre 
#----------------------------------------------------------

#parametres
deb = 0 #les données sont horaires
fin = 8760 #les données sont horaires

# Tache 7. 
# Faire en sorte qu'on trouve les données si on lance le script d'ailleurs que depuis le dossier script. 
# Idée : utiliser les informations sur  __file__
#        print('File name :    ', os.path.basename(__file__))
#        print('Directory Name:     ', os.path.dirname(__file__)) 
#        print("Absolute path : ", os.path.abspath(__file__)) 

dataset = Dataset('../data/SURF_ATM_DIAGNOSTICS.OUT_'+fic+'.nc')
time     = dataset.variables['time']
dtime    = netCDF4.num2date(time[deb:fin],time.units, only_use_cftime_datetimes=False, only_use_python_datetimes=True)
time_dim = time[deb:fin].shape[0]
times =[]

for j in range(0,time.shape[0]):
     date = datetime.datetime(dtime[j].year,dtime[j].month,dtime[j].day,dtime[j].hour)
     times.append(date)
dim_nvar    = len(var)
time_period = fin - deb
variable    = np.zeros((dim_nvar,time_period), float)


l_plot_fig=True
if l_plot_fig:
  py.figure()
  for i in range(len(var)):
    plt.subplot(2,3,i+1)
    py.grid()
    py.plot(times,dataset.variables[var[i]][deb:fin,0,0])
    py.title(title[i])
    py.ylabel(var[i]+' ('+unit[i]+')')
    py.xlabel('temps (jours)',fontsize=8)
    plt.tick_params(labelsize=8)
  py.show()

print('---------------')
print('               ')
print('Q_2.2 : calcul de l albedo, émissivité au  pas de temps = 4020')

VAR1 = dataset.variables[var[0]][4020,0,0]
VAR2 = dataset.variables[var[1]][4020,0,0]
VAR3 = dataset.variables[var[2]][4020,0,0]
VAR4 = dataset.variables[var[3]][4020,0,0]
VAR5 = dataset.variables[var[4]][4020,0,0]

sigma = 5.670374 * 10**(-8) # W.m ^2 K^-1

# calcuer albedo et emissivité à partir. 
# Tache 2. Mettre chaque variable a sa place
SW_up   = VAR1
SW_down = VAR2
LW_up   = VAR4
LW_down = VAR3
Ts      = VAR5

albedo     = SW_up / SW_down
emis       = (LW_up - LW_down) / (sigma*Ts**4 - LW_down )

print('albedo: ', albedo)
print('emis: ', emis)


# Tache 4 .Calcul d'un albedo moyen 
# Prendre la moyenne sur toute la periode des champs 


# Tache 5. Calcul d'une emissivité moyenne 
# Calcul d'une emissivité à chaque pas de temps et prendre la moyenne. 


# Tache 6. 
#  Transformer ce bout de code en fonction (prenant en entrée le dataset ds et une liste de variable du dataset à afficher.)
l_plot_fig_xr = False
if l_plot_fig_xr:
  import xarray as xr 
  # Ouverture du fichier 
  ds = xr.open_dataset('../data/SURF_ATM_DIAGNOSTICS.OUT_'+fic+'.nc')
  # Calcul de la disposition des images
  nrow = int(np.sqrt(len(var)))
  ncol = int(np.ceil(len(var)/nrow)) 
  fig, ax = plt.subplots(nrow,ncol)
  for i in range(len(var)):
    row = i//ncol 
    col = i%ncol 
    ds[var[i]].isel(lat=0).isel(lon=0).plot(ax=ax[row,col])
  # Affichage de l'image
  plt.show()