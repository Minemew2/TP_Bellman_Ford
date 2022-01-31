def liste_precedent(self,Sommet):
        index_sommet = -1
        index_prec = -1
        list_prec = []
        for i in self.sommets : 
            index_sommet +=1
            if i == Sommet :
                for x in range (0,len(self.sommets)):
                    index_prec+=1
                    if self.matrice[x][index_sommet] > 0:
                        list_prec.append(index_prec)
        return list_prec
