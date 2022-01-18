# TP_Bellman_Ford
Implémentation de l'algo de Belman Ford en python

# Classes 
## `Sommet`
Attributs:

 - Entier: `visite` = 0 
 - `contenu` = défaut None.

Méthodes :

 - `__init__(contenu=None)`

## `Graphe` 
Attributs:

 - `Sommet[]:sommets` : Liste des sommets de longeur N.
 - `int[][]:matrice` : La matrice d'adjacence du graphe, un liste de taille N*N, avec
 `matrice[a][b]` est le nombre d'ârete entre `a` et `b`.

Méhodes:

 - `liste_precedent(Sommet:sommet) -> int[]:liste_index` l'index des sommets précédents de `sommet`.
 - `liste_precedent_tous() -> int[][]:liste_index` Renvois la liste des sommets précédents de tout
 les sommets du graphe.
 - `bellman_ford(Sommet:debut) -> int[]:distances` Resois un sommet puis donne la distance la 
 plus courte de `debut` aux autre sommets.
 - `index_sommet(Sommet:sommet) -> int:index` resois un sommet et donne son index dans la liste

## `Graphe_BF`

On profitera de cette étape pour fixer les noms des structures.

Représentation du graphe : G =(S,M)   S : liste des sommets, M : matrice d’adjacences N*N où  N est le nombre de sommets.

Représentation de la structure de calcul de la méthode BF (très important) :
Tableau de dimenssion N*(N-1) ou N représente ne nombre de sommets.
Ce tableau ne contient que des flotant (réel) et inf de numpy.





Représentation d’un sommet : On fait le traitent avec l’index des sommets, et on passe
une liste d’instance de sommets.

Représentation de l’infini : inf numpy.
Représentation des précédents d’un sommet : une liste d’index precédent index ex :
[2, 4 , 5]

Représentation de l’ensemble des  précédents des sommets : Liste des 
Exemple avec graphe complet : [[2, 3, 4], [1, 3 ,4], [1, 2, 4], [1, 2, 3]]

Classes : Sommet, Graphe
