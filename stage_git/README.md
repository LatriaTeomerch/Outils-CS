# Stage_git

On va suivre le topo présent sur cette page confluence. 
http://confluence.meteo.fr/display/FTAP/1.+Tuto+Git+et+Gitlab    


Le but de ce TP est de : 
- Comprendre un peu le fonctionnement de git,  
- Tester l'ajout d'un fichier, 
- Comprendre et expérimenter le principe de branche,
- Voir comment fonctionne une merge request, 
- Voir comment utiliser les issues. 



# 1. Récupération du dépot 

## a. Se connecter sur git.meteo.fr 
## b. Créer un token (et l'enregistrer)

Un token est une chaine de caractère confidentielle associée à votre compte GitLab. 
Lorsque vous clonerez le dépôt de travail localement, il faudra passer le token afin de vous identifier auprès de GitLab (une seule fois).


Pour créer un token, il vous faut aller dans **Settings** (dans l'icône déroulante en haut à droite) > **Access Tokens**.
Là il vous suffit de donner un nom à votre token (par exemple "super_token"), de cocher la case api et de cliquer sur Create personal access token. 
Votre token apparait. 
Copiez le et gardez le précieusement, il ne vous sera plus donné ultérieurement. 
Vous pouvez ensuite retourner à la page du dépôt.


## c. Cloner le dépot
Sur la page du dépôt, cliquez sur le bouton Clone (en haut à droite) et copiez le lien Clone with HTTP. 
Dans l'exemple le lien est https://git.meteo.fr/chabotv/stage_git.git

Il faut ajouter le token de la manière suivante : 
https://git.meteo.fr:MySuperTokenGenerated@git.meteo.fr/chabotv/stage_git.git

Ouvrez un terminal localement (ou sur la machine sur laquelle je souhaite travailler) et placez vous dans votre dossier de travail.
Il vous suffit alors de taper la commande clone 
```
git clone https://git.meteo.fr:MySuperTokenGenerated@git.meteo.fr/chabotv/stage_git.git
```

A noter que si on a oublié de mettre son token lors du clonage du dépot, on peut le faire par la suite en allant modifier le fichier **.git/config**.
A noter aussi qu'il peut être bien de changer les droits de lecture et d'écriture du fichier .git/config (afin que personne n'ai accès à votre token).  

Ce dépot ayant déjà servi pour un stage on va préciser la branche de départ : 

```
git clone --branch v0.0.1 https://git.meteo.fr:MySuperTokenGenerated@git.meteo.fr/chabotv/stage_git.git
```


# 2. Récupération des données 
To get the data you can run the script present in **scripts/utils** named *data_getter.py*.
However, before doing that, you need to create (or change) the `.netrc` file in your home directory (*~*). 

Please add in it
```
default login YOURLOGIN password YOURPASSWORD
```
If you created `.netrc` you should also do a chmod : 
```bash
chmod 600 .netrc 
```

This script will get the data tar and untar them : 
```bash
python scripts/utils/data_getter.py  
```
The data will be loaded from hendrix. 


# 3. Ajouter un fichier au dépot git 

Procédure à prendre dans la page confluence. 

## Exercice
L'auteur du script *Q1.1_fractions_vegtype.py* a malheureusement oublié de dire quel était chaque type de végétation. 
Cependant, il a prévu de pouvoir modifier via un fichier de configuration l'affichage des plots réaliser (via l'argument -f).

Les possibilités pour les types de végétations sont fractions : 
- de sol nu, 
- de cultures, 
- de conifères boréaux persistants, 
- de prairies, 
- de prairies boréales,
- d’arbustes,
- d’arbres tempérés décidus, 
- de conifères tempérés persistants.

## Tache 
1. lancer le programme via `python Q1.1_fractions_vegtype.py` 
2. Aller dans le dossier `conf` 
3. Copier et renomer le fichier *Q1.1.json* (en ajoutant par exemple votre prénom)
4. Modifier ce fichier en nommant chaque type de végétation 
5. Relancer le script via `python Q1.1_fractions_vegtype.py --file conf/mon_fichier.json`
5. [Git] Regarder l'etat de votre repertoire (faire un `git status`)
6. [Git] Ajouter ce fichier (via `git add MySuperFile`)
7. [Git] Faire un commit (via git commit -m "Mon super message qui dit que je suis fier de moi"). Aller voir si le fichier est sur le serveur. 
8. [Git] Envoyer les changements sur le serveur (via git push). Aller voir si le fichier est sur le serveur. 
       **Warning** Pour le premier contributeur cela devrait bien se passer. Pour les autres, il faudra récupérer les contributions des autres avant. 
9. [Git] Récupérer les contributions des autres participants (via git pull)


## Bonus 
Afficher l'ensemble des réponses en utilisant `wcloud.py`. (Installation pip install --user wordcloud)

**NB** 
Sur sxgmap3 j'ai du mettre à jour pillow pour faire marcher le nuage de mots. 

```sh 
pip install --upgrade pillow
```

*Introduire un filtre pour prendre en compte que les réponses à la question Q1_1.* 


# 4. Protection de la branche master 
## Pourquoi ? 

## Comment changer le droit de ses branches 
Aller dans  *setting/repository/Protected branches*.
Changer qui a le droit de pousser et de faire des merge. 

## Test si bien effectif
Chacun modifie son fichier, rajouter ses modifications, commit et essaye de pousser.

Résultat attendu : 
```bash
remote: GitLab: You are not allowed to push code to protected branches on this project.To https://git.meteo.fr:supertoken@git.meteo.fr/chabotv/stage_git.git
 ! [remote rejected] main -> main (pre-receive hook declined)
error: failed to push some refs to 'https://git.meteo.fr:supertoken@git.meteo.fr/chabotv/stage_git.git'
```

## Revenir en arrière sur ce commit 

```
git reset --soft HEAD^
```


# 5. Création et utilisation de branche. Petit passage par les issues. 
Procédure dans la page confluence. 



## Exercice 
On va cette fois ci modifier le comportement de **Q2.1_Q2.2_bilan_radiatif.py**. 
Ici quelques lourdeurs et erreurs semblent s'être glissées dans le code (qu'il va falloir corriger). 
On souhaiterais aussi avoir quelques nouvelles fonctionnalités dans notre bout de code. 


### Taches à effectuer
1. Retrouver qui est qui (SW_Down, SW_Up, LW_Down, LW_UP, TS) et changer la variable 'titre'
2. Changer les variables utilisées pour le calcul de l'emissivité en conséquence (ou au moins les vérifier) 

3. Lire des arguments dans la ligne de commande pour : 
    - changer de surface (surface1/surface2)
    - Faire ou non le plot (actuellement géré par **l_plot_fig**) 

4. Calculer un coefficient d'albédo moyen sur l'ensemble de la période (et non sur une unique occurence)

5. Calculer une émissivité moyenne sur l'ensemble de la période

Bonus : 
6. Refactorisation : Faire une fonction à partir de l'affichage d'un plot en utilisant xarray (prenant en entrée le dataset ds et la liste des variables à afficher (var)).  
7. Fonctionnement : 
        Faire qu'on puisse lancer le script d'un endroit au choix. 
        Actuellement si on lance le script du répertoire au dessus, il plante (car ne trouve pas les données).  

**But du jeu :** 
Chacun prend une tâche, crée une branche et résoud la tache en local dans sa branche. 
Ensuite on va essayer de fusionner tout cela. 

### Etapes 
1 . Creer votre branche 
```bash 
git checkout -b MON_NOM_DE_BRANCHE
```
Existe-t-elle sur le répo distant ? 

2. Modifier le code pour votre tâche
3. Pousser votre branche 

```bash 
git push --set-upstream origin MON_NOM_DE_BRANCHE
```

### Merge request 
On va maintenant passer à l'étape de controle. 












