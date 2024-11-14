Les éoliennes ont un rendement dépendant de la vitesse du vent (en m/s). Lorsqu'il n'y a pas de vent, les éoliennes ne produisent pas. 
Lorsque le vent est trop important, les éoliennes ne produisent pas non plus. 


Pour représenter cette dépendance on peut utiliser une suite d'interolation linéaire (entre deux vitesses de vent).

Le tableau suivant présente les interpolations linéaires utilisées ainsi que les bornes de validité des interoilations linéaires. 

La courbe de rendement éolien est, pour une vitesse de vent donnée par : 
$$
f(x) = a x  + b
$$

Ci-dessous vous trouverez un tableau correspondant à une éolienne. 

|Debut (en m/s)|Fin (en m/s) | a | b |
|---|-------|---|--|
0   |2,5  | 0  | 0 | 
2.5 |3  | 0,023| -0,058|
3   |3,5| 0,057 |-0,160|
3,5 | 4 | 0,060 | -0,170|
4   |4,5| 0,083 | -0,262|
4,5 | 5 |0,091 | -0,298|
5   |5,5| 0,108 | -0,383|
5,5 | 6 | 0,127 | -0,488|
6   | 6,5| 0,154 | -0,650|
6,5 |7   |0,197 | -0,929|
7   |7,5 | 0,223 | -1,111|
7,5 |8   | 0,224 | -1,119|
8   |8,5 |0,208 | -0,991|
8,5 | 9 | 0,220 | -1,093|
9   | 9,5 | 0,132 | -0,301|
9,5 | 10 | 0,065 | 0,336|
10  |10,5 | 0,025 | 0,736|
10,5| 11 | 0,002  |0,978|
11  | 11,5 | 0,001 | 0,989|
11,5| 20 | 0,000 | 1,000|
20  | 20,5 |-2,000 | 41,000|
20,5| +∞ |0 |0|