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

    def creer_tableau_bellman(self, debut, sommets):
        tableau = [[0, np.inf, np.inf, np.inf, np.inf],
                   [0, np.inf, np.inf, np.inf, np.inf],
                   [0, np.inf, np.inf, np.inf, np.inf],
                   [0, np.inf, np.inf, np.inf, np.inf]]
        return tableau

    def bellman_ford(self, debut, sommets):
            # tableau = []
            # for x in range(len(self.sommets)-1):
            # tableau.append([y for y in range(len(self.sommets))])
            tableau = self.creer_tableau_bellman(debut, sommets)
            st = self.sommets[1]
            tableau[1][1] = tableau[0][self.index_sommets(self.liste_precedent(st)[0])] + self.matrice[
                self.index_sommets(self.liste_precedent(st)[0])][1]

    def liste_precedent(self, Sommet):

            index_sommet = -1

            index_prec = -1
            list_prec = []
            for i in self.sommets:
                index_sommet += 1
                if i == Sommet:
                    for x in range(0, len(self.sommets)):
                        index_prec += 1
                        if self.matrice[x][index_sommet] > 0:
                            list_prec.append(index_prec)
            return list_prec

    def liste_precedent_tous(self):
        list_prec_tous = []
        for Sommet in self.sommets:
            index_sommet = -1
            index_prec = -1
            list_prec = []
            for i in self.sommets:
                index_sommet += 1
                if i == Sommet:
                    for x in range(0, len(self.sommets)):
                        index_prec += 1
                        if self.matrice[x][index_sommet] > 0:
                            list_prec.append(index_prec)
                        if x == len(self.sommets) - 1:
                            list_prec_tous.append(list_prec)
        return list_prec_tous

    def index_sommets(self, sommet):
        if sommet == self.sommets[0]:
            return 0
        elif sommet == self.sommets[1]:
            return 1
        elif sommet == self.sommets[2]:
            return 2
        elif sommet == self.sommets[3]:
            return 3
        elif sommet == self.sommets[4]:
            return 4


if __name__ == "__main__":
    g = Graphe()
    a = Sommet("a")
    print(g.bellman_ford(a))
