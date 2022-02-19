#!/bin/python3

class Sommet:
    def __init__(self, contenu=None):
        self.visite = 0
        self.contenu = contenu


class Graphe:
    def __init__(self, matrice, sommets):
        self.matrice = matrice
        self.sommets = sommets

    def liste_precedents(self, sommet):
        pass

    def liste_precedent_tous(self):
        pass

    def bellman_ford(self, sommet_debut):
        precedents = self.liste_precedents_tous()
        origin_index = self.index_sommet(sommet_debut)

        # TODO import numpy

        line_n = [INFTY for i in range(len(self.sommets))]
        line_n[origin_index] = 0
        line_n_plus = line_n  # TODO deepcopy

        # DO len(sommets)-1
        for i in range(len(self.sommets) - 1):  # On fait l'opération sur N_SOMMETS-1 lignes.
            for index_sommet in range(len(self.sommets)):  # On itére a travers chaque sommet
                for index_pre in precedents[index_sommet]:  # On itére a travers les précédents du sommet
                    if line_n_plus[index_sommet] > line_n[index_pre]:
                        line_n_plus[index_sommet] = line_n[index_pre]
            # TODO deepcopy
            line_n = line_n_plus

        for index_sommet in range(len(self.sommets)):
            for index_pre in precedents[index_sommet]:
                if liste_n[index_sommet] - liste_n[index_pre] >= self.matrice[index_pre][index_sommet]:
                    return "Belman ne s'applique pas au graphe"

        return line_n

    def index_sommet(sommet):
        retour = None
        for i in range(len(sommets)):
            if sommets[i] == sommet:
                retour = i
                break
        return retour


if __name__ == "__main__":
    g = Graphe
