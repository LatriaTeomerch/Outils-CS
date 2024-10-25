
# Outils pour le calcul scientifique 
# Exercice - A rendre pour le 12/11/2024 

## Consignes

Par groupe de 2 (au maximum) il vous est demandé de faire le TP suivant.
Vous devrez renvoyer :
- Le code utilisé pour répondre aux questions (idéalement nous devrions être capable de le faire tourner sans modifications)
- La réponse aux différentes questions.
  

Ce TP sera comptabilisé en point bonus dans la note finale de la partie informatique.

Pour mémoire les adresses mail de vos enseignants sont :
- Thibault.Marzlin@cerfacs.fr
- vincent.chabot@meteo.fr
- pouech@cerfacs.fr



## Questions 


La première série de question utilise les données du TD du 23 Octobre 2024. 
Pour rappel, le chemin du fichier contenant les données du TD est 
`/home/newton/ienm2021/chabotv/COURS_CS/data/arome_forecast_2024100900.nc`


> 1. Améliorer la fonction de l'exercice 5 de telle sorte à prendre en entrée la variable d'intérêt dans le dataset (par ex. `r2` ou `t2m`).

> 2. Combien y-a-t'il d'occurences de température négative (en °C) dans le dataset entier ? Quel pourcentage de cas cela représente-t-il ? 

>3. Calculer la moyenne glissante de la température (sur 3h) pour la zone autour de Grenoble. On moyennera aussi selon la dimension spatiale. (Indication : utiliser la fonctionnalité `rolling` de  *xarray* pour faire des moyennes glissantes).
Quelles sont les valeurs obtenues ? 
 

Le dossier `/home/newton/ienm2021/chabotv/COURS_CS/data` contient un fichier `grid_arpege.nc`. 
Ce fichier contient une unique variable `glob0125` donnant une information d'altitude sur le domaine AROME pour ARPEGE (modèle global). La résolution de l'orographie est ici de 0.125° (~12.5 km), résolution bien plus lâche que celle d'AROME (~1.3km). 

>4.a. Faire une figure montrant l'orographie des deux modèles (AROME et ARPEGE). Qu'observe-t-on ? Que pouvez vous dire de l'altitude maximum sur chacune de ces cartes ?   

>4.b Interpoler l'orographie d'ARPEGE sur celle d'AROME (vous pouvez utiliser `interp_like` de xarray). 
Quelle est le maximum de différence (en valeur absolue) entre les deux orographies ? 

>4.c Même question mais en interpolant l'orographie d'AROME sur l'orographie d'ARPEGE. 
