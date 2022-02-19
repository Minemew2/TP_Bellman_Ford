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

    def creer_tableau_bellman(self, debut):
        tableau = [[0, np.inf, np.inf, np.inf, np.inf],
                   [0, np.inf, np.inf, np.inf, np.inf],
                   [0, np.inf, np.inf, np.inf, np.inf],
                   [0, np.inf, np.inf, np.inf, np.inf]]
        return tableau

    def bellman_ford(self, debut):
            # tableau = []
            # for x in range(len(self.sommets)-1):
            # tableau.append([y for y in range(len(self.sommets))])
        precedents = self.liste_precedent_tous()
        origin_index = self.index_sommet(debut)

        # TODO import numpy

        tableau = self.creer_tableau_bellman(debut)

        for ligne in range(1,len(self.sommets)-1):
            for sommet in range(len(self.sommets)):
                if self.sommets[sommet] != debut:
                    distance_candidat = tableau[ligne-1][self.liste_precedent(self.sommets[sommet])[0]]+self.matrice[self.liste_precedent(self.sommets[sommet])[0]][sommet]
                    for candidat in range(1,len(self.liste_precedent(self.sommets[sommet]))):
                        distance_potentiel = tableau[ligne-1][self.liste_precedent(self.sommets[sommet])[candidat]]+self.matrice[self.liste_precedent(self.sommets[sommet])[candidat]][sommet]
                        if distance_potentiel < distance_candidat:
                            distance_candidat = distance_potentiel
                    tableau[ligne][sommet] = distance_candidat

        # for index_sommet in range(len(self.sommets)):
            # for index_pre in precedents[index_sommet]:
                # if line_n[index_sommet] - line_n[index_pre] >= self.matrice[index_pre][index_sommet]:
                    # return "Belman ne s'applique pas au graphe"

        return tableau[len(self.sommets)-2]
    def liste_precedent_bouchon(self, sommet):
        if sommet == self.sommets[0]:
            return []

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

    def index_sommet(self, sommet):
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
    print(g.bellman_ford(g.sommets[0]))
