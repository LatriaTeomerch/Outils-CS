# -*-coding:Latin-1 -*
import pylab as py
from netCDF4 import Dataset as netcdf_dataset
import numpy as np
import matplotlib.pyplot as plt
import datetime
import json
import argparse 


dataset = netcdf_dataset('../data/PREP_Q1.nc')
var=['VEGTYPE1','VEGTYPE4','VEGTYPE5','VEGTYPE7','VEGTYPE10','VEGTYPE15','VEGTYPE18','VEGTYPE19',]
dict_correspondance = {
    'VEGTYPE1':'Toto1',
    'VEGTYPE4':'VEGTYPE4',
    'VEGTYPE5':'VEGTYPE5',
    'VEGTYPE7':'VEGTYPE7',
    'VEGTYPE10':'VEGTYPE10',
    'VEGTYPE15':'VEGTYPE15',
    'VEGTYPE18':'VEGTYPE18',
    'VEGTYPE19':'VEGTYPE19'
}

# Lecture du fichier avec les réponses. 
parser = argparse.ArgumentParser(description="Reponse")
parser.add_argument("--file","-f", type=str,dest="json", help="Chemin du fichier json a considerer")
args = parser.parse_args()
if args.json is not None:
    with open(args.json) as f: 
        dict_correspondance = json.load(f)
    suptitle = args.json

levels = [0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1]

for i in range(8):
    plt.subplot(3,3,i+1)
    variable=dataset.variables[var[i]][:,:]
    lat = dataset.variables['REG_LAT'][:,0]
    lon = dataset.variables['REG_LON'][0,:]
    plt.contourf(lon, lat, variable,levels,cmap='rainbow')
    plt.title(dict_correspondance[var[i]])
    plt.colorbar()
    if args.json is not None:
        plt.suptitle(args.json)
    
plt.show()
