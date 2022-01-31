import numpy as np


class Sommet:
    def __init__(self, contenu):
        self.contenu = contenu
        self.visite = 0

    def __repr__(self):
        return self.contenu


class Graphe:
    def __init__(self):
        self.sommets = [Sommet("a"), Sommet("b"), Sommet("c"), Sommet("d"), Sommet("e")]
        self.matrice = [[0, 15, 4, 0, 0],
                        [0, 0, 0, 0, 5],
                        [0, 0, 0, 2, 11],
                        [0, 0, 0, 0, 3],
                        [0, 0, 0, 0, 0]]

    def bellman_ford(self, debut):
        # tableau = []
        # for x in range(len(self.sommets)-1):
            # tableau.append([y for y in range(len(self.sommets))])
        tableau = [[0,np.inf,np.inf,np.inf],
                   [],
                   [],
                   []]



if __name__ == "__main__":
    g = Graphe()
    a = Sommet("a")
    print(g.bellman_ford(a))
