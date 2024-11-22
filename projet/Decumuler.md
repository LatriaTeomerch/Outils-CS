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
# **Décumul (avec xarray)**
---

Lorsqu'on a accès aux fichiers de sortie d'AROME/ARPEGE, la pluie (et d'autres variables) sont des variables **cumulées** depuis le début de la prévision. 

Or bien souvent, on est intéressé par visualiser des cumuls sur une certaine durée. 

Bien qu'il existe plein d'options (employant **xarray**), il n'est pas si simple de décumuler. 

---
## **Effectuer un décumul**

```python 
# On va faire un exemple 1D (plus simple à comprendre)
# On commence par selectionner la variable et l'espace
da = ds["tirf"].isel(latitude=slice(800,1200)).isel(longitude=slice(400,600))
# On selectionne ensuite que quelques pas de temps 
da = da.isel(time=slice(0,5))
# On effectue la moyenne spatiale
ds_a = da.mean(["latitude","longitude"])
# On affiche la moyenne spatiale 
print(f"Original {ds_a.values}")
# On va créé un nouveau DataArray en "shiftant" les valeurs d'un pas de temps. 
# Cela décale les valeurs mais pas "l'heure". 
ds_b = ds_a.shift({"time":-1})
print(f"Apres le shift : {ds_b.values}")
# On fait la différence avec le dataArray d'origine et  
# et on "shift" les valeurs dans l'autre sens 
diff = (ds_b-ds_a).shift({"time":1})
print(f"La difference : {diff.values}")
# On met à l'instant [0] la valeur qu'il y avait originellement. 
diff[0]=ds_a[0]
print(f"La différence reremplie : {diff.values}")
print(f"La somme sur la periode {diff.sum().values}")

```


---
# **Résultat du script de décumul**

```sh 
Original [0.09512891 0.18112381 0.24899292 0.34132582 0.44724205]
Apres le shift : [0.18112381 0.24899292 0.34132582 0.44724205        nan]
La difference reshiftée : [       nan 0.0859949  0.06786911 0.0923329  0.10591623]
La différence reremplie : [0.09512891 0.0859949  0.06786911 0.0923329  0.10591623]
La somme sur la periode 0.44724205136299133
```

On observe bien que la somme des valeurs décumulées sur la période est égale à la valeur originelle. 
