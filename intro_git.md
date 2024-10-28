---
marp: true
paginate: true
math: latex 
theme: beam

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
# **Introduction à GIT**

---
# **Pourquoi utiliser Git ?**

- **Gestion des versions et de l'historique d'un projet :**
  - Git permet de suivre chaque modification d’un projet.
  - Il aide à revenir à une version précédente en cas de besoin (introduction de bug, ... ).
  
- **Collaborer efficacement :**
  - Git permet à plusieurs personnes de travailler en parallèle sur le même projet sans écraser les modifications des autres.

Pour ces raisons il est devenu **un outil incontournable** dans presque tous les projets de développement moderne.
  
---
# **Qu'est-ce que Git ?**

- **Git est un système de gestion de versions.**
  - Il enregistre toutes les modifications d’un projet, fichier par fichier.
  - Chaque version d’un projet est conservée dans une "base de données" Git.
  - Git permet de collaborer sur un projet à plusieurs de manière structurée.

---
# **Git dans la pratique**
> Imaginez que vous travaillez sur un projet durant quelques semaines puis faites un break. Deux mois plus tard, vous reprenez le projet ... Malheureusement, le code que vous avez ne fonctionne plus...

### Sans Git :
- Comment retrouver une ancienne version  du projet ? Sauvegarde (v1, v2, vXXXX) ? 
- Comment vous y prendre pour avoir de nouveau une version fonctionnelle ?

### Avec Git :
- **Revenir à une version précédente en quelques commandes.**
- **Sauvegarder des étapes importantes de votre travail (commits).**
- **Annoter des versions spécifiques du codes (tag)**


--- 
# **Git vs GitHub/GitLab/Bitbucket**

### **Git : Le logiciel**
- **Outil de gestion de versions décentralisé.**
- Fonctionne **localement** sur votre ordinateur.
- Vous permet de suivre l'historique de vos modifications, de gérer des branches, et de collaborer à plusieurs.

### **GitHub / GitLab / Bitbucket : Les plateformes**
- **Services en ligne** qui hébergent des dépôts Git à distance.
- Facilitent le partage de code et la collaboration sur des projets via une interface.
- Proposent des fonctionnalités supplémentaires (**Issues**, **Merge Requests / Pull Requests**,  **Intégration continue (CI/CD)** )

---
# **Première étape : Configuration globale**


Cette configuration sera valable pour tous vos projets git.
Elle pourra être changé par la suite 

1. Identifier qui fait les modifications 
```
git config --global user.name "Votre Nom" 
git config --global user.email "votre.email@example.com"
```
2. Passer le proxy Météo-France (permet de communiquer avec le remote)
```
git config --global --unset https.proxy
git config --global --unset http.proxy 
```

---
# **Seconde étape : Création/Clonage d'un projet**

## A. Connecter vous à [git.meteo.fr](git.meteo.fr) (via vos identifiant LDAP)
> login : chabotv 
> password : NeJamaisDonnerSonPassword
## B. Aller sur le dépot
<span style="color:red;"> On fait cloner le dépot avec le cours ?
 Ou on leur fait créer un projet sur git.meteo.fr (dans lequel ils mettront chacun leurs TP) ? Ou un par groupe (comme ça on a directement les interactions) ? 
 Ou on leur fait cloner le projet avec le cours et on leur fait mettre un nouveau remote qui sera leur répo à eux  ? </span>
Comme ça ils auront tous le cours et pourront récupérer les slides au fur et à mesure ?

---
# Clonage d'un projet

On leur crée le dépot par projet (au préalable).Le HandsOn va consister à cloner le répo puis chaque élève est responsable d'ajouter une partie des slides du cours sur le dépot.
On aura donc : 
  - Un peu de linux (cp ...)
  - clone/log/status/add/commit/push/pull
  - Un premier push qui se passe bien pour une partie 
  - Un (voir plusieurs) pull à faire pour les autres 

On introduit ensuite le concept de branche et d'issues (et 4 tâches indépendantes)
  + Readme (description du projet)
  + Quelques commandes utiles (un autre .md) (alias env, path des données)
  + Ajout d'un fichier .gitignore
  + Correction du DM Xarray ? 

---
# Création un nouveau projet 

<div class="same_columns">
<div>

Aller sur créer un nouveau proje(par ex nommé  `outils_cs` et créez en un dans votre espace personnel (sous `enm/eleves/ienm_2024-2027/votre_nom`). 

Une fois le projet créer, mettez vous dans le répertoire souhaité (sur votre poste de travail) et `cloner` ce projet 

```sh 
git clone https://git.meteo.fr/enm/eleves/
ienm_2021-2024/chabot_vincent/outils_cs.git
```

</div>
<div>

![](./figure/Project.png)
![](./figure/clone.png)

</div>
</div>



---
# **Ne pas avoir à rentrer son password à chaque communication** 

Il existe plusieurs moyens pour ne pas rentrer son password plusieurs fois : 
- Garder en cache le password `git config credential.helper 'cache --timeout=3600'
`
Ici vous n'aurez besoin de rentrer votre password que toutes les heures.
- Générer un token et l'ajouter dans la configuration du dépot (slide suivante)

---
# **Génération de token**
<div class="columns">
<div>


![width:50%](figure/TokenAn.png)
</div>
<div>

## 2. 
Copier le token généré (il ne vous sera pas redonné).
</div>
</div>

### 3. Vous pouvez ensuite l'ajouter en modifiant le fichier `.git/config`
```
[remote "origin"]
        url = https://git.meteo.fr/chabotv/MyProject.git
```
doit etre changé en 
```
[remote "origin"]
        url = https://git.meteo.fr:MyTOKEN@git.meteo.fr/chabotv/MyProject.git
```

---

# **B. Consulter l'historique du projet et première tâche**

Commencer par regarder l'historique de votre projet 
```sh 
git log
``` 


Maintenant vous allez tous modifier localement votre projet 
Pour cela : 
- Créer un dossiers `slides`
- Choisissez chacun un pdf différent et mettez le dans le dossier slides 
  
> Question : Est-ce que l'historique de votre projet a changé ? 


---
# **C. Consulter l'état du dépot** 
Nous allons maintenant consulter l'état de "l’arbre de travail" 
Pour cela faire `git status` . 

Vous deviez avoir ce type de résultat 

![](./figure/Status.png)

Cela vous renseigne que vous avez modifié le Readme.

> Est-ce que votre fichier a été modifié sur `git.meteo.fr` ? 
> Que comprenez-vous du message renvoyé par la commande ? 
---

# **D. Ajouter les modificaitions**


On va "ajouter" les modifications apporté au fichier et  associer un message de "suivi". 

``` 
git add LeNomDeMonFichier
git commit -m "Mon message décrivant les changements"
```

> Votre fichier apparaît-il sur votre dépot sur `git.meteo.fr`? 
> Consulter l'historique de votre projet (via `git log`). De même consulter l'état du dépot local (`git status`).

---
# **E. Pousser les modifications vers la plateforme**
Maintenant nous pouvons pousser les modifications sur la plateforme. 

```
git push
```

Pour le premier qui **pousse**  cela devrait bien se passer. <span style="color:red;"> Pour les autres vous devriez voir une erreur.</span> Cette dernière est liée au fait que vous êtes **en retard** sur l'état du code sur la plateforme.

Pour vous remettre à jour faire `git pull`.
>A noter que vous aurez à faire plusieurs mise à jour (ou alors, il faut que vous fassiez les `push` et `pull` dans un certain ordre)

Aller, au fur et à mesure, vérifier sur la plateforme que tout s'est bien passé. 



---
# **Travailler à plusieurs**
A plusieurs, avant de pouvoir "pousser" ses modifications sur la plateforme il faut "tirer" l'état le plus récent de la `branche` sur laquelle on travaille. 

Pour cela il faut faire 
```
git pull
```
Attention : <span style="color:red">En cas de conflit (deux utilisateurs modifiant la même partie du code), il faudra les résoudre "à la main". </span>

---

# **La notion de branche dans Git**

### Qu'est-ce qu'une branche ?
- Une **branche** est une version parallèle de votre projet.
- Elle permet de travailler sur de nouvelles fonctionnalités ou corrections de bugs **sans affecter la branche principale** (nommée `main`). Ainsi, on isole les `bugs`du au développement de la branche principale qui doit rester fonctionnelle tout au long du projet. 
- Chaque branche possède son propre historique de commits.

---
# **Pourquoi utiliser des branches ?**

1. **Développement en parallèle**
   - Vous pouvez travailler sur plusieurs aspects du projet en même temps (nouvelle fonctionnalité, tests), sans impacter le reste du code.

2. **Sécurité des modifications**
   - Les changements dans une branche n'affectent pas le code principal.
   - Permet d'expérimenter ou de corriger des bugs sans casser la version stable.

 Une fois le travail terminé, les branches peuvent être **fusionnées** (merged).

---
# **Votre première Branche**

Cette fois-ci vous allez devoir chacun 
- Créé une branche (slide suivante)
- Ajouter un (répartissez les vous) des fichier suivant dans votre branche : 
  - **Readme.md** (description du projet)
  - **Commandes.md** : Quelques commandes utiles (un autre .md) (alias env, path des données)
  - un fichier **.gitignore** (permet à git de ne pas suivre/montrer tous les fichiers)
  - Correction du DM Xarray ? 
   
---
# **Création d'une branche**


## Comment procéder 
Vous pouvez chacun créer une branche dans le projet.

Pour cela faire 
<div class="columns">
<div>

1. `git checkout -b MaBranche`

>  
2. Ajouter le fichier et un message de commit. 
3. Pousser vos modifications 
```
git push --set-upstream origin MaBranche 
```
</div>
<div>
Faite un `git status`. Que voyez-vous ?
  
<br>
</br>

Aller sur git.meteo.fr. Comment voir votre branche ?  
</div>
</div>

---
# **Notion de Merge Request (MR)** 

### Définition
- Une **Merge Request** (ou **Pull Request** sur GitHub) est une demande d'intégration de code.
- Elle permet de proposer les modifications d'une branche vers une autre (souvent vers la branche `main` ou `dev`).

---

# **Pourquoi utiliser des MergeRequest ?**

1. **Révision de code** :
   - Permet à d’autres  de **relire et commenter** le code avant qu’il ne soit intégré.
   - Aide à repérer les erreurs, améliorer la qualité du code et partager des bonnes pratiques.

2. **Discussion et collaboration** :
   - Les MRs offrent un espace pour **discuter et ajuster les changements**.
   - Les équipes peuvent échanger sur des choix techniques, des suggestions, ou des améliorations.

3. **Validation des tests** :
   - Avant de fusionner, les MRs peuvent permettre de vérifier si le code passe des **tests** (si possible automatisés)
  .

---
# **Votre première MergeRequest**

Vous pouvez maintenant créer votre première Merge Request. 
<div class="same_columns">
<div>

![](figure/MR.png)
</div>
<div>

Vous pouvez ajouter un camarade responsable d'effectuer la fusion (`merge`). 

Vous pouvez aussi ajouter des camarades responsables de relire et donner leur avis sur votre proposition d'amélioration (et poser des questions si quelque chose ne leur semble pas clair). 
</div>
</div>

---
# **Ajout de commentaires des relecteurs et Merge** 


---
# **La notion de tag** 
Lorsque vous allez développer votre projet, vous allez toujours "vouloir" ajouter de nouvelles fonctionnalités, ... 

Au bout d'un moment, le nombre de commit fait va être très important (plusieurs milliers) et il va être très difficile de savoir à quel moment vous aviez une version fonctionnelle (et avec quels fonctionnalités), quand vous avez supprimez (ou casser) une fonctionnalité.

Pour avoir un "historique" plus exploitable vous pouvez utiliser des tags. Cela constituera les versions du code vers lesquelles vous pourrez vous tourner pour avoir l'état du code comme il était `avec cette fonctionnalité`. 

Vous pouvez ajouter des tags par ligne de commande ou sur l'interface web.  

> Créez un nouveau tag (par ex v_0.0.0). 

--- 
# **La notion d'issues** 


---
# **Comment bien décrire un bug**

### Informations à inclure :
- **Titre clair** : Soyez précis 
- **Description détaillée** : Expliquez le problème rencontré de manière claire.
- **Étapes pour reproduire le bug** :
  1. Indiquez les étapes précises.
  2. Fournissez le code, si applicable.
- **Résultat attendu** : Décrivez ce que vous pensiez que le programme ferait.
- **Résultat obtenu** : Ce qui s'est réellement passé, incluant tout message d’erreur.
- **Version et environnement** : Version du code , Version de python et des librairies, Système d'exploitation (Ubuntu 20.04, Windows 98) ... 

---

On peut maintenant vouloir visualiser les différences introduites par nos modifications locales. 
Cela peut se faire via 
``` git diff```

---
# **Takeaway**  



