def tri_dichotomique(T, x):
    n = len(T)
    g = 0
    d = n - 1
    k = -1 # on retourne ca si l'élément recherché n'est pas dans le tableau

    while g <= d:
        c = (g + d) // 2

        if T[c] < x:
            g = c + 1
        elif T[c] > x :
            d = c - 1
        else:
            return c

    return k

cl = [4, 12, 33, 5, 78, 15, 17, 24, 35, 51]
res = tri_dichotomique(cl, 5)

print(res)