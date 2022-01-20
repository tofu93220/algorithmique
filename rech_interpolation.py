def tri_dichotomique(T, x):
    n = len(T) # taille du tableau
    lo = 0 # indice gauche
    hi = n - 1 # indice droite
    k = -1 # on retourne ca si l'élément recherché n'est pas dans le tableau
    pos = lo + (x - T[lo]) * (hi - lo) / (T[hi] - T[lo])

    if pos == x:
        return pos
    else:
        return k


cl = [4, 12, 33, 5, 78, 15, 17, 24, 35, 51]
res = tri_dichotomique(cl, 15)

print(res)