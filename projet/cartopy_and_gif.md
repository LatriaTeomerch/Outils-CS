---
marp: true
paginate: true
math: latex 


style: |
  .same_columns {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }
   .columns {
    display: grid;
    grid-template-columns: 2fr 1fr; 
    gap: 1rem;
  }


 

footer: Outils pour le calcul scientifique 2024 - Introduction à git -  Vincent Chabot, Thibault Marzlin, Paul Pouech   
---



<!-- _class: title -->
# **Comment ajouter un fond de carte et faire une animtion**
---
# **Ajout de fond de carte**

En météorologie, on peut vouloir ajouter des informations géographiques sur nos cartes. 
Pour cela, une solution est de faire appel à la librairie `cartopy`. 

On montrera ici deux exemples : 
 - Un cas où l'information géographique est présent dans la bibliothèque
 - Un cas où l'information provient d'un fichier tiers (fichier de type `geojson`). 


---
# **Ajouter les frontières et la délimitation Terre/Mer** 

<div class="columns">
<div>

```python 
import xarray as xr 
import cartopy.feature as cfeature
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

fig, axis = plt.subplots(1, 1, 
      subplot_kw=dict(projection=ccrs.PlateCarree()),figsize=(10,10))
# Fonction de plot 
ds["t2m"].isel(time=0).plot(
    ax=axis,
    transform=ccrs.PlateCarree(),  # this is important! 
    #On specifie la geometrie de la carte
    cbar_kwargs={"orientation": "horizontal", "shrink": 0.7},
    robust=True,
)
axis.coastlines() # Ajout du trait de côtes

# Ajout des frontières des pays
border_10m = cfeature.NaturalEarthFeature('cultural', 
     'admin_0_countries', '10m',edgecolor='k',facecolor='none') 
axis.add_feature(border_10m,linestyle='-', alpha=1)

plt.show()
```
</div>
<div>

Exemple 
![](../figure/Cartopy.png)
</div>
</div>

---
## Le masque en tant qu'attribut 

```python 
class Loader:
   def __init__(self,mask_file)->None:  
      self.mask = xr.open_dataset(mask_file)

   def get_determinist(self, date)-> xr.Dataset: 
      ds = xr.open_dataset("arome_forecast_{date.strftime("%Y%m%d%H")}.nc")
      return ds* mask_on_grid(self.mask, "eurw1S100")

   def _get_ensemble_member(self,date, member)-> xr.Dataset: 
      file = # Le bon nom ! 
      ds = xr.open_dataset(file).expand_dims("number")
      return ds * mask_on_grid(self.mask, "eurw1S40")

   def get_ensemble(self,date)-> xr.Dataset:
      ens_list = []
      for mb in range(0,5):
          # Rajoute la dimension membre afin de pouvoir merger.
         ens_list.append(self._get_ensemble_member(date, mb)
      return xr.merge(ens_list)

    def summarize_info(self,date):
        """
        This function print the determinist and ensemblist forecast which can help to analyse the corresponding date. 
        """
```

---
# Autre option

```python 
class Loader: 
    def __init__(self, path, list_path): 
        self.path = path 
        self.ens_path = list_path

    def get_determ(self, mask_path): 
        mask = xr.open_dataset(mask_path)
        return ds * mask_on_grid(self.mask, "eurw1s100")
    
    def _get_ensemble_member(self, mask_path, member): 
        # Lecture du membre et ajout de dimension 
        # Multiplication par le bon masque 
        pass 

    def get_ensemble(self, mask_path): 
        ens_list = []
        for mb in range(0,5): 
            ens_list(self._get_ensemble_member(mask_path, mb))
        return xr.merge(ens_list)
```

---

La première option est plutôt tournée vers l'étude d'une région :  on ne peut en changer. Si on veut étudier une autre région on doit réinstancier un autre objet. Cependant on peut étudier diverses prévisions sur la même région. 

La seconde vers l'exploitation d'une prévision déterministe/ensembliste. Dans ce cas, on peut étudier la situation sur diverses régions facilement. 

---
#  Utilisation des masques 

Exemple pour masquer un dataset 
```python
import xarray as xr
import matplotlib.pyplot as plt
ds = xr.open_dataset("/home/newton/ienm2021/chabotv/COURS_CS/data/arome_forecast_2024102712.nc")
mask = xr.open_dataset("/home/newton/ienm2021/chabotv/COURS_CS/masks/Sympo/sympo_31.nc")["eurw1s100"]
mask = mask.rename({"latitude_eurw1s100":"latitude","longitude_eurw1s100":"longitude"})
ds_masked = ds*mask
```

De cet exemple on peut en tirer une fonction "masque sur une grile" 

```python
def mask_on_grid(mask:xr.Dataset, grid:str="eurw1s100")->xr.DataArray:
    """
    Get the mask for a specific grid. 
    Rename dimension as latitude and longitude. 
    """
    # 1. Selectionne dans le dataset le masque correspondant à la grille 
    # A faire 
    # 2. Renommer les coordonnées 
    my_mask = my_mask.rename({f"latitude_{grid}":"latitude",f"longitude_{grid}":"longitude"}
    return my_mask 
```