#''' version 1
def tri_bulle(liste):
    cliste = list(liste)
    n = len(cliste)

    for i in range(n, 2, -1): 
        for j in range(1, i-1, 1):
            if cliste[j+1] < cliste[j]:
                # echanger
                cliste[j], cliste[j+1] = cliste[j+1], cliste[j]

    return cliste

liste = [4, 56, 6, 45, 9, 12]
print('Liste initiale: ' ,liste)

print('Liste triée: ' ,tri_bulle(liste))

#'''

''' version 2
def tri_bulle(liste):
    cliste = list(liste)
    n = len(cliste)

    permutation = True
    passage = 0
    while permutation:
        permutation = False
        passage = passage + 1
        
        for i in range(0, n-passage):
            if cliste[i] > cliste[i+1]:
                permutation = True

                cliste[i], cliste[i+1] = cliste[i+1], cliste[i]

    return cliste

liste = [4, 56, 6, 45, 9, 12]
print('Liste initiale: ' ,liste)

print('Liste triée: ' ,tri_bulle(liste))

'''