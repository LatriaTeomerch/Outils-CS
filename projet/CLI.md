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
# **Utilisation de Argparse**
---
# **Argparse : Un outil pour créer une interface en ligne de commande (CLI)**

- **`argparse`** est un module standard de Python.
- Il permet de **gérer les arguments de la ligne de commande** dans vos scripts.
- Il va générer automatiquement un message d'aide, 
- **Objectif** : Rendre vos scripts interactifs et flexibles.

---
# **Example (nommé ex_arpgarse.py)**

```python 
from argparse import ArgumentParser

def main(arg_a, arg_b):
    print(f"arg_a is {arg_a}")
    print(f"arg_b is {arg_b}")

if __name__ =="__main__":
    # Crée le parser 
    parser = ArgumentParser("Ma super Interface")
    # Ajoute un argument obligatoire de type entier 
    parser.add_argument("-r","--region",type=int,
                        help="Département d'analyse",required=True) 
    # Ajoute un argument optionnel de type str. 
    # Si cet argument est présent il doit être dans la liste de choix
    parser.add_argument("--variable", type=str, 
                        help="Quelle variable voulez vous analyser?",
                        choices=["RR3","Pmer"])
   
    args = parser.parse_args()
    main(args.variable, args.region)
```

---
# **Utilisation de l'aide**
```sh 
python3 ex_argparse.py -h
usage: Ma super Interface [-h] -r REGION [--variable {RR3,Pmer}]

options:
  -h, --help            show this help message and exit
  -r REGION, --region REGION
                        Département d'analyse
  --variable {RR3,Pmer}
                        Quelle variable voulez vous analyser?
```
L'aide est elle claire ?

---
# **Test sans arguments**
```sh 
python3 ex_argparse.py
```

Que se passe-t-il à votre avis ? 

---
# **Test sans arguments**
```sh 
python3 ex_argparse.py

usage: Ma super Interface [-h] -r REGION [--variable {RR3,Pmer}]
Ma super Interface: error: the following arguments are required: -r/--region
```

Comme on a spécifié un argument obligatoire, s'il n'est pas présent une erreur est levée. 

---
# **Test avec arguments**

```sh 
python3 ex_argparse.py -r 31

arg_a is None
arg_b is 31
```
Cette fois-ci on a bien spécifié la région (avec un `int`). 
L'appel à la fonction `main` est donc réalisé. L'argument `variable` n'étant pas récupéré en CLI et n'ayant pas de valeur par défaut, il est mis à `None`.