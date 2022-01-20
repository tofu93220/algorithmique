def fusion(L1, L2) :  # cette fonction permet de fusionner la liste
	L3 = []
	
	# si l'élément en indice 0 de la liste 1 est inferieur à l'élément en indice 0 de la liste 2
	# on ajoute cette élément à la liste 3 en la retirant de la liste 1 
	# sinon on ajoute cette élément à la liste 3 en la retirant de la liste 2
	while L1 and L2 :
		if L1[0]<L2[0] : 
			L3.append(L1.pop(0))
		else : 
			L3.append(L2.pop(0))
			
	# une sous-liste étant vidée
	# on colle tout le contenu de l'autre
	# en queue de L3 
	L3 = L3 + L1 + L2
	
	return L3


def trifusion(L) : # cette fonction permet de trier la liste précédemment fusionnée
	n = len(L)
	if n <= 1 : 
		return L # si la taille du tableau est inferieur ou egale a 1, on renvoie le tableau
	else : 
		return fusion( trifusion(L[:n//2]), trifusion(L[n//2 : ] ) )


app = fusion([8,65,9,7], [55,32,41,5])
print(app)

L = app
print(trifusion(L))