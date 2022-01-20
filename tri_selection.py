
def tri_selection(liste):
    cliste = list(liste)
    n = len(cliste) 


    for i in range(n):
        # on commence par séléctionner le premier élément de la liste qu'on stocke dans la variable rg_min
        rg_min = i
        # on recherche dans le reste de la liste l'élément qui va etre le plus petit 
        # qu'on compare avec le premier élément de la liste
        for j in range(i+1, n):
            if cliste[j] < cliste[rg_min]:
                # on enregistre l'indice de position du plus élément du reste de la liste
                rg_min = j

        # lorsqu'on a répérer la valeur la plus petite
        if rg_min != i:
            # on procède à une permutation
            cliste[i], cliste[rg_min] = cliste[rg_min], cliste[i]
   
    return cliste
		

# comp = n(n-1)/2
liste = [4,10,8,19,6,35]
print('Liste initiale: ' ,liste)
print('Liste trié: ' ,tri_selection(liste))

