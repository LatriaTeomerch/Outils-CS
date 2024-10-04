import numpy as np
import matplotlib.pyplot as plt

print("Hello World")

names_list = ["Paul", "Vincent", "Thibault"]

nb_names = len(names_list)

for name in names_list:
    if name == "Paul":
        print("Paul is here")
    else:
        print("Paul is not here")


def present(name: str, name_list: list):
    """_summary_

    Args:
        name (_type_): _description_
        name_list (_type_): _description_
    """
    for name in names_list:
        if name == "Paul":
            print(f"{name} is here")
        else:
            print(f"{name} is not here")
