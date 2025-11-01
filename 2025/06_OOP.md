---
marp: true
---


# **La Programmation Orientée Objet**

---
# **Un peu de contexte**

In the realm of scientific software development, many programmers lack a strong background in computer science. This particular niche emphasizes expertise in areas such as physical modeling, numerical methods, applied mathematics, and high-performance optimization. As a result, most practitioners in this community tend to stick to the familiar procedural programming approach. However, when faced with the concept of "objects" in object-oriented programming, newcomers often encounter questions like whether they should use objects, if they offer advantages over procedural approaches, how to implement them effectively, and what potential pitfalls to watch out for. Unfortunately, the answer to these questions is often ambiguous and depends on the specific situation. 

---
## **Object vs procedural programming**

Petit schema avec le procedural en ligne et les objets dans une piscine.

---
Lors du précédent TP nous avons définis plusieurs fonction pour venir lire, filtrer et interpréter les données d'un fichier CSV relatif à un réseau de stations météo.

*read_station_data()* -> lecture du fichier d'entrée et selection d'une station via son ID
*print_station_info()* -> afficher des informations relatives à cette station
*select_period()* -> sélectionner une plage temporelle sur les données de la station.
*extrema()* -> calculer pour une variable donnée la premiere heure de ses extrema.
*aggregation()* -> calculer pour une variable donnée la moyenne sur chaque heure de la journée.
*visualize()* -> visualiser des données/résultats via un graphique.

---
Références pour les fonctions:

```python
def read_station_data(id_number):
    file_path = '/home/newton/ienm2021/chabotv/COURS_CS/data/station_2018.csv' 
    df =  pd.read_csv(file_path,parse_dates=[4])
    # Verification que l'id existe 
    if id_number not in df["number_sta"].unique(): 
        print(f"La station demandée {id_number} n'existe pas.")
        print(f"Les possibilitées sont {df["number_sta"].unique()}")
        raise ValueError("Station {id_number} does not exist!")
    # Lecture et filtrage 
    return df[df["number_sta"] == id_number]

def print_station_info(df:pd.DataFrame):
    print(f" Information pour la station {id_number}")
    print(f" Latitude de la station : {data["lat"].unique()}")
    print(f" Longitude de la station : {data["lon"].unique()}")
    print(f" Hauteur de la station : {data["height_sta"].unique()}")

def select_period(df, start_period, end_period, hour=None): 
    # On reprend l'exemple de la slide précédente
    cdt = (df.date > start_period)*(df.date < end_period)
    # Mise a jour de la condition pour rajouter la selection de l'heure
    if hour is not None: # Attention `if hour:` ne fonctionne pas avec 0.  
        cdt = cdt * (df.date.dt.hour == hour)
    df_period = df[cdt]
    return df_period 

def extrema(df:pd.DataFrame, variable:str):
    """
    Regarde pour une variable donnée la première heure pour 
    laquelle le maximum/minimum a été atteint. 
    """
    maxi = df[variable].max()
    mini = df[variable].min()
    # Filtre pour ne garder que les elements correspondants au maximum
    max_date =  df[df[variable] == maxi]
    # au minimum 
    min_date =   df[df[variable] == mini]
    heure_max = max_date["date"].dt.strftime("%H").values[0]
    heure_min = min_date["date"].dt.strftime("%H").values[0]
    return (heure_max, heure_min )
def aggregation(df:pd.DataFrame,variable:str, methode:str="mean"):
    # Création d'une liste pour mettre la donnée aggrégée 
    result = []
    for hour in range(0,24): 
        cdt = df.date.dt.hour == hour 
        df_selected = df[cdt]
        if methode == "mean": 
            result.append(df_selected[variable].mean())
        elif methode == "min": 
            result.append(df_selected[variable].min())
        elif methode == "max": 
            result.append(df_selected[variable].max())
        else:
            raise ValueError("Aggregation method not known")
    return result 

def visualize(x_value,y_value,axis_labels=['X','Y']):
    """Plot the y vs x values on a graph with the possibility of specified axis labels
    """
    plt.plot(x_value,y_value)
    plt.xlabel(axis_labels[0])
    plt.ylabel(axis_labels[1])
    plt.show()
```

---
Mon script principale d'appel à ces différentes fonctions pourrais ressembler au suivant:

```python
# Script d'appel pour la station 73010
station_id = 73010
df_station_73010 = read_station_data(73010)
print_station_info(df_station_73010)
start_period = dt.datetime(2018,10,1)
end_period = dt.datetime(2018,10,15)
df_station_73010_oct = select_period(df_station_73010, start_period, end_period) 
h_temp_max,h_temp_min = extrema (df_station_73010_oct,"t")
mean_temp = aggregation(df_station_73010_oct,"t", methode = "mean")
visualize(range(len(mean_temp)),mean_temp,axis_labels=['Heure de la journée','Temperature Moyenne'])
```
- Que se passe-t-il si je veux changer la plage temporelle ?
- Et si je veux selectionner une autre stations ?
- Les deux ?

---

Il est bien sur possible de dupliquer ce block de code pour chaque station et changer les lignes correspondantes pour varier la période sélectionnée. Il est aussi tout à fait possible de faire de ce block une fonction que l'on peut appeler, cependant elle posséderas un nombre conséquents d'arguments et il s'agit de quelques choses qu'il faut essayer d'éviter, pour des raisons de maintenances et de comprehension du code. 

Imaginons que nous voulions travailler sur une stations météo donnée sur 3 differentes plages de temps.
L'API idéal pourrait être quelques choses comme cela:

```python
Station_73 = StationMeteo(73010)
Period_1 = Station_73.select_period(start1,end1)
Period_2 = Station_73.select_period(start2,end2)
Period_3 = Station_73.select_period(start3,end3)
```

```python
Station_73 = StationMeteo(73010)
Station_73.set_period(start1, end1)
h_max,h_min = Station_73.extrema("t")
mean_t = Station_73.aggregat('t',methode='mean)
````

---