---
Title: The UNIX Command Line, A Beginner's Guide
Summary: The UNIX command-line shell is hard to grasp for beginner. Here is a crash course for beginners, with a description of the basic commands.

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
# **The UNIX Command Line: A Beginner's Guide**

---
## **CLI (Command Line Interface) vs. GUI (Graphical User Interface)**


|  | CLI |GUI |
|:--:|:--:|:---|
| Utilisation intuitive | Non | Oui |
| Controle fin des actions | Oui | Généralement non |
| Utilisation de ressources supplémentaires | Non | Oui |
| Automatisation aisée | Oui | Non |

L'interpreteur de commande UNIX est dénommé "[Shell](https://en.wikipedia.org/wiki/Shell_(computing))."  Plusieurs co-existent. On utilisera ici `bash` "[Bourne-Again shell](https://en.wikipedia.org/wiki/Bash_(Unix_shell))"


---

# UNIX CLI Part 1/4: Les commandes sans danger

---

## Exploration: La commande `ls` 

La commande `ls` permet de lister le contenu d'un repertoire. On ne peut rien casser avec, n'hésitez pas à vous en servir. 

```bash
> ls
dungeon.sh 
Documents
(...)
```

---
On peut ajuster la command afin d'avoir plus d'information. 


```bash
> ls -lh
-rw-r--r--  1 chabotv assim 2,4K sept.   8  2025 dungeon.sh
drwxr-xr-x  2 chabotv assim 4,0K nov.  25  2024 Documents
``` 
- `l` : liste les fichiers dans un format long (montrant des détails comme les permissions)
- `h` : affiche le poids des fichiers dans un format humainement compréhensible 

>
> Avez vous une idée de la signification de `-rw-r--r--` ? 
>

---

### **Auto-complétion (Sans danger)**

Taper chaque lettre peut être ennuyeux et surtout source d'erreurs. La plupart des terminals permmettent d'utiliser l'auto-complétion via la touche **Tabulation** (dénotée `\t`).  
Exemple : Arriver au répertoire du cours : `/home/newton/ienm2021/chabotv/COURS_CS` 
```bash
> ls /ho\t 
newton
(...)
> ls /home/ne\t
> ls /home/newton/i\t
ienm2021
ienm2022 
(...)
> ls /home/newton/ienm2021/cha\t
> ls /home/newton/ienm2021/chabotv/COURS_CS\t
   dungeon.sh 
```

---
### **Caractère générique** 


Pour accélerer les recherches vous pouvez utilisez des cararctères génériques. 
Utilisez `*` pour n'importe quel groupe de caractères et `?` pour un seul caractère.  

```bash
> ls *.pdf  # Lists all files ending with .pdf
> ls */*.pdf  # Lists all first-level files ending with .pdf
> ls */*/*.pdf  # Lists all second-level files ending with .pdf
```

Ce que vous avez appris avec `ls` (complétion, caractère générique, options) peut être appliquées à la plupart des commandes unix. 
Pour avoir une idée des options d'une commande faites `man MA_COMMANDE`. 
Ex : `man ls` 

> Quelle est l'option permettant de trier les fichiers en commançant par les plus volumineux ? 

---

## Navigation
Pour changer de répetoire, il faut utiliser la commande `cd` (change directory). 
`pwd` (present working directory) permet de savoir où vous êtes. 


Si jamais vous souhaitez revenir dans votre répertoire personnel (home directory) vous pouvez faire un simple `cd`. 
```bash 
> cd 
> pwd 
    /home/gmap/mrpa/chabotv
```
Si vous souhaitez revenir au répertoire précédent faites `cd -`.  



---

## **Examiner des fichiers textes (`cat`, `head`, `tail`)**

Ces commandes permettent d'examiner le contenu d'un fichier texte. 
`cat` affiche l'ensemble du contenu, que celui-ci soit de l'ASCII ou du binaire. 
A titre d'exemple, vous pouvez utiliser le dictionnaire de mots  `/usr/share/dict/words` or `/usr/dict/words`.

---

```bash
> cat /usr/share/dict/words
A
a
aa
aal
aalii
aam
Aani
(...)
```

Vous pouvez utiliser les commandes `head ` ou `tail` pour voir le début ou la fin du fichier. Par défaut, cela affiche uniquement 10 lignes, mais via des options on peut adapter ce nombre de lignes. 


---

# UNIX CLI Part 2/4: Commandes de gestion de fichiers


---

## Touch a File: `touch`

La commande `touch` permet de modifier l'heure d'accès et de modification d'un fichier sans changer le fichier en lui-même. C'est sans doute la plus petite modification que l'on peut faire.  
Si le fichier n'existe pas, `touch` crée un fichier vide pour vous.


```bash
> ls -l tmp.txt
-rw-r--r-- 1 chabotv mrpa 121 Sep 19 14:31 tmp.txt
> touch tmp.txt
> ls -l tmp.txt
-rw-r--r-- 1 chabotv mrpa 121 Sep 19 14:32 tmp.txt
> touch tmp2.txt
> ls -lrt tmp*
-rw-r--r-- 1 chabotv mrpa   0 Sep 19 14:32 tmp2.txt
-rw-r--r-- 1 chabotv mrpa 121 Sep 19 14:32 tmp.txt
```

---

## Créer un repertoire : `mkdir`


```bash
> ls      # When there's nothing to report, nothing happens
> mkdir TEST
> ls 
TEST
> mkdir TEST
mkdir: TEST: File exists
> cd TEST
> ls
```
---

## Copier un fichier/repertoire: `cp`

La commande `cp`  permet de dupliquer des fichiers. On peut utiliser l'option `-i` pour des raisons de sécurités : cela demandera confirmation avant d'écraser le fichier. 



```bash
> ls tmp*
tmp.txt		tmp2.txt
> cp tmp.txt tmp_copy.txt
> ls tmp*
tmp.txt		tmp2.txt	tmp_copy.txt
> cp tmp2.txt tmp_copy.txt
> ls tmp*
tmp.txt		tmp2.txt	tmp_copy.txt
> cp -i tmp.txt tmp_copy.txt
overwrite tmp_copy.txt? (y/n [n]) y
tmp.txt		tmp2.txt	tmp_copy.txt
```

---

Si vous avez besoin de copier un répertoire entier, il faut explicitement mettre l'option `-r` : 


```bash
> mkdir TMP  # Create a dummy void folder 
> cp TMP TMP3 
cp: TMP is a directory (not copied).
> cp -r TMP TMP3 
> ls TMP3
test1.txt
```
---

## **Déplacer ou renomer des Fichiers/Répertoires: `mv`**


La commande `mv` permet de déplacer des fichiers et des dossiers.  

```bash
> mkdir TMP  # Create a dummy void folder 
> mkdir TMP2 # Create another dummy folder 
> touch TMP/test1.txt # Create a dummy file
> mv TMP/test1.txt TMP2/test_02.txt
> tree
.
├── TMP
└── TMP2
    └── test_02.txt

3 directories, 1 file
```
---

## **Supprimer des fichiers : `rm`**

Une des commandes les plus puissantes et dangereuse : `rm`.  
Dans sa forme la plus simple on supprime un fichier :  
```bash
> tree
.
├── TMP
└── TMP2
    └── test2.txt

3 directories, 1 file
> rm TMP2/test2.txt
> tree
.
├── TMP
└── TMP2

3 directories, 0 files
```

---
## **Le cas spécifique de `rm -rf *`**   

Par déaut  `rm`, ne supprime pas les répertoires mais seulement les fichiers. 
Il faut utiliser l'option `-r` (recursive) pour supprimer un répertoire entier + contenu. 

```bash
> rm -r TMP2
```

`rm -rf *`
L'option `-f` signifie qu'on force la commande à s'exécuter. `-rf` permet donc de supprimer l'ensemble des éléments en dessous du point cible, en enlevant l'ensemble des barrières qu'il pourrait exister.
Le caractère générique `*` signifiant "tout ce qu'il y a dans ce dossier".  
Par conséquent les conséquences d'un mauvais usage de cette commande peuvent être important.



---

# UNIX CLI Part 3/4: Edition de fichiers & Script UNIX



---

## Editeur de texte 

Lorsque vous opérez en local, vous pouvez utilisez des éditeurs de texte graphique pour éditer vos scripts.
A titre d'example, vous pouvez utiliser `vscode` ou `gedit` pour éditer vos scripts.

```bash
> code hello.sh
```
ou 

```bash 
> gedit hello.sh 
```
---

Dans le fichier ouvert (en mode graphique) vous pouvez créer un simple script affichant "Hello, World!".
Pour cela, vous allez utiliser la commande UNIX `echo` permettant d'écrire dans le shell : 

```shell
echo "Hello, World!"
```

Une fois le fichier sauvegardé (`ctrl +s `), vérifier que le fichier est présent puis vous pouvez l'executer via 

```bash 
bash hello.sh 
```

---

# UNIX CLI part 4/4 :  Tester vos base 


In this final section, we'll put your newfound UNIX command-line skills to the test. We'll use a script called `dungeon.sh` to create a random file structure resembling a dungeon with monsters and loot. Each time you run the script, it will generate a unique dungeon for you to explore.

---

Le script `dungeon.sh` est disponible dans le dossier de votre professeur : 
```
/home/newton/ienm2021/chabotv/COURS_CS
```
---

## Now, let's embark on your UNIX adventure! **Here is your quest**:

1. Create a folder `Cours_CS` and a subfolder `Test_unix`  and move inside it
1. Copy the file `dungeon.sh` from your teacher repository (`
/home/newton/ienm2021/chabotv/COURS_CS
`) 
1. Try to execute the script 
1. If needed, change the access right to the file (via `chmod` command) so the file can be executed. 
1. Count how many `goblins` files there are in the dungeon
1. Find all the `prince` and `princess` occurrences in the files
1. Delete the dungeon - without wiping  out the script `dungeon.sh`!
1. restart with a new dungeon.


---
# **Quelques compléments**

Il est possible (et même encouragé) de créer des alias pour des courtes commandes récurrentes. 
Pour ce faire, il faut éditer le fichier `~/.bashrc` en ajoutant l'alias souhaité. 

Ex : On peut par exemple ajouter le repertoire dans lequel les supports de cours seront disponible. 
```bash 
alias cdprof='cd /home/newton/ienm2021/chabotv/COURS_CS'
```





