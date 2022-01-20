def tri_insertion(liste):
    cliste = list(liste)
    n = len(cliste)  

    for i in range(n):
        el = cliste[i] # enregistre la valeur du premier el de la liste

        j = i # enregistre l'indice du premier element de la liste 

        # tant que indice premier est supérieur à 0 et taille tableau < valeur prem el
        # on compare l'élément pivot avec celui de gauche
        while (j > 0) and (cliste[j-1] > el): 
            # on enregistre la valeur de l'élément pivot
            cliste[j] = cliste[j-1]

            j = j - 1

        cliste[j] = el

    return cliste

liste = [6, 56, 6, 45, 9, 12]
print('Liste initiale: ' ,liste)

print('Liste triée: ' ,tri_insertion(liste))