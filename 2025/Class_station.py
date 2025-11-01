import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def read_station_data(id_number):
    file_path = "/home/newton/ienm2021/chabotv/COURS_CS/data/station_2018.csv"
    df = pd.read_csv(file_path, parse_dates=[4])
    # Verification que l'id existe
    if id_number not in df["number_sta"].unique():
        print(f"La station demandée {id_number} n'existe pas.")
        print(f"Les possibilitées sont {df["number_sta"].unique()}")
        raise ValueError("Station {id_number} does not exist!")
    # Lecture et filtrage
    return df[df["number_sta"] == id_number]


def print_station_info(df: pd.DataFrame, id_number: int):
    print(f" Information pour la station {id_number}")
    print(f" Latitude de la station : {df["lat"].unique()}")
    print(f" Longitude de la station : {df["lon"].unique()}")
    print(f" Hauteur de la station : {df["height_sta"].unique()}")


def select_period(df, start_period, end_period, hour=None):
    # On reprend l'exemple de la slide précédente
    cdt = (df.date > start_period) * (df.date < end_period)
    # Mise a jour de la condition pour rajouter la selection de l'heure
    if hour is not None:  # Attention `if hour:` ne fonctionne pas avec 0.
        cdt = cdt * (df.date.dt.hour == hour)
    df_period = df[cdt]
    return df_period


def extrema(df: pd.DataFrame, variable: str):
    """
    Regarde pour une variable donnée la première heure pour
    laquelle le maximum/minimum a été atteint.
    """
    maxi = df[variable].max()
    mini = df[variable].min()
    # Filtre pour ne garder que les elements correspondants au maximum
    max_date = df[df[variable] == maxi]
    # au minimum
    min_date = df[df[variable] == mini]
    heure_max = max_date["date"].dt.strftime("%H").values[0]
    heure_min = min_date["date"].dt.strftime("%H").values[0]
    return (heure_max, heure_min)


def aggregation(df: pd.DataFrame, variable: str, methode: str = "mean"):
    # Création d'une liste pour mettre la donnée aggrégée
    result = []
    for hour in range(0, 24):
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


def visualize(x_value, y_value, axis_labels=["X", "Y"]):
    """Plot the y vs x values on a graph with the possibility of specified axis labels"""
    plt.plot(x_value, y_value)
    plt.xlabel(axis_labels[0])
    plt.ylabel(axis_labels[1])
    plt.show()


class StationMeteo:
    def __init__(self, id_number):
        self.id = id_number
        self.df = read_station_data(self.id)
        self.df_period = self.df

    def set_period(self, start, end):
        self.df_period = select_period(self.df, start, end)

    def info(self):
        print_station_info(self.df_period, self.id)

    def extrema(self, var: str):
        return extrema(self.df_period, var)

    def aggregate(self, var, methode):
        return aggregation(self.df_period, var, methode=methode)
