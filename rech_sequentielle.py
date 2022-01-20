# Version 1
def tri_seq(T, x):
    n = len(T)
    trouve = False
    k = -1
    for i in range(0, n):
        # si l'élément recherché est égale dans le tableau
        if T[i] == x:
            trouve = True
            # on enreistre la valeur trouvée
            k = i
        else: # si on trouve rien, on renvoit -1
            trouve = False
    
    # on renvoit cette valeur
    return k

tab = [6, 4, 7, 9, 1]
test = tri_seq(tab, 5)

print("L'indexe de l'élément recherché: " , test)    

'''
# Version 2
def tri_seq(T, x):
    i = 0
    n = len(T)
    while (i < n) and (T[i] != x):
        i = i+1
        if i < n:
            return i
        
    return -1

tab = [6, 4, 7, 9, 1]
test = tri_seq(tab, 3)

print(test)
'''