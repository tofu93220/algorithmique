def qsort(l):
    # Quick-Sort : Algorithme du tri rapide
    if l == []: 
        return []

    pivot = l[0] 
    g = []
    d = []
    for x in l[1:]: 
        if x < pivot:
            g.append(x) 
        else:
            d.append(x)
            
    return qsort(g)+[l[0]]+qsort(d)
    
liste = [10, 14, 65, 23, 19, 60, 5, 9, 29, 35, 1] # Exemple de liste initiale
liste_tri = qsort(liste) # Liste triée 
print('liste initiale : ',liste)
print('liste triee    : ',liste_tri)