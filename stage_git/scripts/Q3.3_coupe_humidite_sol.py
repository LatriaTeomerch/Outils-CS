import pylab as py
import numpy as np
import netCDF4
from netCDF4 import Dataset
import matplotlib.pyplot as plt

z_grnd_prof=[0.01,0.02,0.05,0.1,0.2,0.5,1.0,1.2,1.5,1.8]
z_grnd_prof=[0.01,0.04,0.1,0.2,0.4,0.6,0.8,1.0,1.5,2.0,3.0,5.0,8.0,12.0]
z_grnd_prof=[0.01,0.04,0.1,0.2,0.4,0.6,0.8,1.0,1.5,2.0]#,3.0,5.0,8.0,12.0]
var='WG'
unit='(m3/m3)'
nbl=len(z_grnd_prof)

def lec_champ(chemin,var):
  dataset=Dataset(chemin)
  Z=np.zeros((nbl,nbt))
  for i in range(nbl):
    Z[i,:]=moy_j(dataset.variables[var+str(i+1)][:,0,0])
  return Z

def moy_j(x):
  y=np.arange(len(x)/24.)
  for i in range(len(y)):
    y[i]=np.nanmean(x[i*24:(i+1)*24])
  return y


chemin='../data/ISBA_PROGNOSTIC.OUT_veg2.nc'
dataset=Dataset(chemin)
nbt=int(dataset.variables[var+str(1)].shape[0]/24.)
x=np.arange(int(nbt))
y=[-x for x in z_grnd_prof]
X,Y=np.meshgrid(x,y)

fig=py.figure()
py.subplot(3,1,1)
py.title(var+' '+unit)
chemin='../data/ISBA_PROGNOSTIC.OUT_veg1.nc'
Z1=lec_champ(chemin,var)
C=plt.contourf(X, Y, Z1, cmap=plt.cm.get_cmap('Blues'),vmin=0.12)
plt.colorbar(label='WG [m^3/m^3]')
py.title('veg1')
py.ylabel('profondeur du sol [m]')

py.subplot(3,1,2)
chemin='../data/ISBA_PROGNOSTIC.OUT_veg2.nc'
Z2=lec_champ(chemin,var)
C=plt.contourf(X, Y, Z2, cmap=plt.cm.get_cmap('Blues'),vmin=0.12)
plt.colorbar(label='WG [m^3/m^3]')
py.title('veg2')
py.ylabel('profondeur du sol [m]')
py.subplot(3,1,3)
Z3=Z1-Z2

leveldiff = [-0.0275,-0.025,-0.0225,-0.0175,-0.015,-0.0125,-0.01,-0.0075,-0.005,-0.0025,0,0.0025,0.005,0.0075,0.01,0.0125,0.015,0.0175,0.02,0.0225,0.025,0.0275]
plt.contourf(X, Y, Z3,leveldiff, cmap='PuOr')

py.colorbar(label='WG [m^3/m^3]')
py.title('veg1 - veg2')
py.ylabel('profondeur du sol [m]')
py.xlabel('Temps (jours)')


py.show()

