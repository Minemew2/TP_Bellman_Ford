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
                    
        if self.post_condidtion(tableau[len(self.sommets)-2]) == True :
            return tableau[len(self.sommets)-2]
    def liste_precedent_bouchon(self, sommet):
        if sommet == self.sommets[0]:
            return []

    def liste_precedent(self, Sommet):
            l =[]
            index_sommet =self.index_sommet(Sommet)
            for sommet in self.sommets:
                if self.matrice[self.index_sommet(sommet)][index_sommet] != 0:
                    l.append(self.index_sommet(sommet))
            return l

    def liste_precedent_tous(self):
        list_prec_tous = []
        for Sommet in self.sommets:
            list_prec_tous.append(self.liste_precedent(Sommet))
        return list_prec_tous

    def index_sommet(self,sommet):
        index = 0
        for sommets in self.sommets:
            if sommets == sommet:
                 return index
            else:
                index+=1
    

    def post_condidtion(self,liste_bellman):
        for sommet in self.sommets[1:]:
            index_sommet = self.index_sommet(sommet)
            l = self.liste_precedent(sommet)
            for antecedant in l:
                chemin = self.matrice[antecedant][index_sommet]
                if liste_bellman[index_sommet]>chemin+liste_bellman[antecedant]:
                    return False
        return True
                   

if __name__ == "__main__":
    g = Graphe()
    print(g.bellman_ford(g.sommets[0]))
