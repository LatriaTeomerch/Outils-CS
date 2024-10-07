---
theme: gaia
marp: true
_class: lead
paginate: true
---

# **TP Python Débutant**

## Générateur de nombres

---

Le but de ce TP est de creer de A à Z un petit jeu en Python pour découvrir les fonctionnalités basique du language: 
    - les modules
    - les variables
    - les fonctions
    - les boucles

---
### Plan du jeu :
- Le programme génère un nombre aléatoire entre 1 et 20.
- L'utilisateur a plusieurs tentatives pour deviner ce nombre.
- À chaque tentative, le programme indique si le nombre à deviner est plus grand ou plus petit.
- Une fonction sera utilisée pour gérer la logique principale du jeu.

---

### 1. **Importation de modules**

Nous avons besoin d'importer le module **`random`** pour générer un nombre aléatoire.

```python
import random
```

---

### 2. **Variables**

Les variables vont servir à stocker :
- Le **nombre à deviner** (généré aléatoirement).
- Le **nombre de tentatives restantes**.
- Les **propositions** de l'utilisateur.

---

### 3. **Fonctions**

Nous allons définir une fonction qui contiendra la logique principale du jeu. Cette fonction va :
- Générer un nombre aléatoire.
- Demander des propositions à l'utilisateur.
- Gérer les indices ("trop grand" ou "trop petit").
- Gérer le nombre de tentatives.

---

```python
def jeu_deviner_nombre():
    # Générer un nombre aléatoire entre 1 et 20
    nombre_a_deviner = random.randint(1, 20)
    
    # Initialiser les variables
    tentatives = 5  # L'utilisateur a 5 tentatives
    devine = False  # Cette variable sera utilisée pour savoir si l'utilisateur a trouvé

    print("Bienvenue dans le jeu de devinettes !")
    print("Je pense à un nombre entre 1 et 20. Vous avez 5 tentatives pour deviner.")

    # Boucle de jeu (tant que l'utilisateur n'a pas trouvé ou qu'il reste des tentatives)
    while tentatives > 0 and not devine:
        # Demander à l'utilisateur de deviner un nombre
        proposition = int(input("Entrez votre proposition : "))
        
        # Comparer la proposition avec le nombre à deviner
        if proposition == nombre_a_deviner:
            print(f"Félicitations ! Vous avez deviné le nombre {nombre_a_deviner} !")
            devine = True
        elif proposition < nombre_a_deviner:
            print("Trop petit !")
        else:
            print("Trop grand !")
        
        # Réduire le nombre de tentatives
        tentatives -= 1
        print(f"Il vous reste {tentatives} tentatives.\n")

    # Si l'utilisateur n'a pas deviné après toutes les tentatives
    if not devine:
        print(f"Désolé, vous avez perdu. Le nombre à deviner était {nombre_a_deviner}.")
```

---

### 4. **Boucles**

La logique principale du jeu repose sur une boucle **`while`** qui continue tant que :
- L'utilisateur n'a pas deviné le bon nombre.
- Il lui reste des tentatives.

À chaque tour de la boucle :
- L'utilisateur fait une proposition.
- Le programme compare cette proposition avec le nombre à deviner et donne des indices ("trop grand" ou "trop petit").
- Le nombre de tentatives restantes diminue.

---

### Exécution du programme :

```python
# Importer le module random
import random

# Définir la fonction du jeu
def jeu_deviner_nombre():
    nombre_a_deviner = random.randint(1, 20)
    tentatives = 5
    devine = False

    print("Bienvenue dans le jeu de devinettes !")
    print("Je pense à un nombre entre 1 et 20. Vous avez 5 tentatives pour deviner.")

    while tentatives > 0 and not devine:
        proposition = int(input("Entrez votre proposition : "))

        if proposition == nombre_a_deviner:
            print(f"Félicitations ! Vous avez deviné le nombre {nombre_a_deviner} !")
            devine = True
        elif proposition < nombre_a_deviner:
            print("Trop petit !")
        else:
            print("Trop grand !")

        tentatives -= 1
        print(f"Il vous reste {tentatives} tentatives.\n")

    if not devine:
        print(f"Désolé, vous avez perdu. Le nombre à deviner était {nombre_a_deviner}.")

# Appeler la fonction pour lancer le jeu
jeu_deviner_nombre()
```

---
### Explications du code :
1. **Importation** : On utilise `random` pour générer un nombre aléatoire entre 1 et 20.
2. **Variables** :
   - `nombre_a_deviner` stocke le nombre secret que l'utilisateur doit deviner.
   - `tentatives` garde la trace des tentatives restantes.
   - `devine` est un booléen qui devient `True` lorsque l'utilisateur a trouvé le bon nombre.
3. **Boucle `while`** : Elle continue jusqu'à ce que l'utilisateur ait deviné le nombre ou que ses tentatives soient épuisées.
4. **Fonction `jeu_deviner_nombre()`** : Cette fonction encapsule toute la logique du jeu, rendant le code réutilisable et structuré.

### Améliorations possibles :
- Ajouter un compteur de points en fonction du nombre de tentatives restantes.
- Donner la possibilité de rejouer après chaque partie.

---

### À toi de jouer !
Tu peux essayer ce code dans un environnement Python. Modifie-le, ajoute des fonctionnalités, et amuse-toi avec !